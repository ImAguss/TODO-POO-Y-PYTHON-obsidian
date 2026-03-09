---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-programacion
Creacion: 2026-03-05
Revision: 2026-03-03T16:54:00
---
# Tabla de Contenidos

- [[#Tipos de Datos y Memoria|Tipos de Datos y Memoria]]
	- [[#Tipos de Datos y Memoria#Tipos Inmutables|Tipos Inmutables]]
	- [[#Tipos de Datos y Memoria#Tipos Mutables|Tipos Mutables]]
	- [[#Tipos de Datos y Memoria#Tabla de Tipos|Tabla de Tipos]]
- [[#Reference Counting (Conteo de Referencias)|Reference Counting (Conteo de Referencias)]]
	- [[#Reference Counting (Conteo de Referencias)#¿Cómo funciona?|¿Cómo funciona?]]
	- [[#Reference Counting (Conteo de Referencias)#Observar el conteo de referencias|Observar el conteo de referencias]]
	- [[#Reference Counting (Conteo de Referencias)#Pasaje de Parámetros: Por Valor vs Por Referencia|Pasaje de Parámetros: Por Valor vs Por Referencia]]
	- [[#Reference Counting (Conteo de Referencias)#Limitación del Reference Counting|Limitación del Reference Counting]]
- [[#Garbage Collector Generacional|Garbage Collector Generacional]]
	- [[#Garbage Collector Generacional#¿Cómo funciona?|¿Cómo funciona?]]
	- [[#Garbage Collector Generacional#Módulo `gc`|Módulo `gc`]]
	- [[#Garbage Collector Generacional#Ejemplo: Referencias Circulares|Ejemplo: Referencias Circulares]]
- [[#El Destructor `__del__`|El Destructor `__del__`]]
	- [[#El Destructor `__del__`#Uso Básico|Uso Básico]]
	- [[#El Destructor `__del__`#El Problema con Referencias Circulares|El Problema con Referencias Circulares]]
	- [[#El Destructor `__del__`#Los objetos "uncollectable"|Los objetos "uncollectable"]]
- [[#Solución: `weakref`|Solución: `weakref`]]
	- [[#Solución: `weakref`#Uso de `weakref`|Uso de `weakref`]]
- [[#Creación de Objetos: `__new__` vs `__init__`|Creación de Objetos: `__new__` vs `__init__`]]
- [[#Resumen|Resumen]]
	- [[#Resumen#Buenas Prácticas|Buenas Prácticas]]
- [[#Ver también|Ver también]]
# Cómo Python Maneja la Memoria

Python gestiona la memoria automáticamente mediante dos mecanismos principales: **reference counting** y **garbage collector generacional**. Comprender cómo funcionan es clave para escribir código eficiente y evitar fugas de memoria.

## Tipos de Datos y Memoria

### Tipos Inmutables

Los tipos inmutables (`int`, `float`, [[Trabajando con los strings en Python#Trabajando con Strings en Python|`str`]], [[Tuplas en Python#Tuplas en Python|`tuple`]], `frozenset`, `bytes`) son los más sencillos de manejar, pero los que más castigan la memoria.

**Cuando se modifica una variable inmutable, se crea un NUEVO objeto en memoria:**

```python
mi_variable = 'uno, dos'
print(hex(id(mi_variable)))  # 0x1d258bff030

mi_variable += ' y tres'      # ¡Se crea un NUEVO objeto!
print(hex(id(mi_variable)))  # 0x1d258bff330 ← Distinta dirección
```

La dirección de memoria cambia porque el string es inmutable. El objeto original queda disponible para ser liberado por el garbage collector. Una vez deja de tener nombres ligados.

### Tipos Mutables

Los tipos mutables ([[Listas en Python#Listas en Python|`list`]], [[Diccionarios en Python#Diccionarios en Python|`dict`]], [[Sets en Python#Sets en Python|`set`]], objetos de clases) se modifican en el mismo lugar de memoria:

```python
mi_lista = [1, 2, 3, 4, 5]
print(hex(id(mi_lista)))  # 0x1adc2ba6248

mi_lista[0] = 15
mi_lista.append(6)
print(hex(id(mi_lista)))  # 0x1adc2ba6248 ← MISMA dirección
```

**Los elementos dentro de una lista son referencias:**

```python
mi_lista = [1, 2, 3]
nuevo_valor = 15
mi_lista[0] = nuevo_valor

# Ambos apuntan al MISMO objeto
print(hex(id(mi_lista[0])))   # 0x7ff83c48d5e0
print(hex(id(nuevo_valor)))   # 0x7ff83c48d5e0
```

### Tabla de Tipos

| Inmutables  | Mutables         |
| ----------- | ---------------- |
| `str`       | `list`           |
| `int`       | `dict`           |
| `float`     | `set`            |
| `bool`      | `bytearray`      |
| `tuple`     | Objetos de clase |
| `frozenset` | (por defecto)    |
| `bytes`     |                  |
| `range`     |                  |
| `None`      |                  |

---

## Reference Counting (Conteo de Referencias)

Es el mecanismo **principal** de gestión de memoria en Python. Cada objeto tiene un contador de [[NameSpaces en Python#¿Qué es un namespace?|Referencias]].

### ¿Cómo funciona?

Cada vez que una variable apunta a un objeto, el contador aumenta. Cuando la variable deja de apuntar, el contador disminuye. Cuando llega a **cero**, el objeto se libera inmediatamente.

```python
import sys

a = [1, 2, 3]    # contador = 1
b = a            # contador = 2
c = a            # contador = 3

print(sys.getrefcount(a))  # 4 (incluye la referencia de getrefcount)

del a            # contador = 2
del b            # contador = 1
del c            # contador = 0 → ¡Objeto liberado!
```

### Observar el conteo de referencias

```python
import sys

uno = 1
dos = uno
tres = uno
cuatro = 1

print(sys.getrefcount(uno))  # Alto, porque Python cachea enteros pequeños

lista = [1, 2, 3, 4, 1]
for i, elem in enumerate(lista):
    print(f"lista[{i}] = {elem}, refcount = {sys.getrefcount(elem)}")
# Los dos '1' apuntan al mismo objeto
```

### Pasaje de Parámetros: Por Valor vs Por Referencia

El comportamiento depende del tipo de dato:

**Inmutables: se comportan como pasaje por valor**
```python
def pasajePorValor(x):
    x = x + 1
    print(f"Dirección de x: {hex(id(x))}, valor: {x}")

v = 100
pasajePorValor(v)
print(f"Dirección de v: {hex(id(v))}, valor: {v}")
# v NO cambió - se creó un nuevo objeto dentro de la función
```

**Mutables: se comportan como pasaje por referencia**
```python
def pasajePorReferencia(l):
    l[0] = 100
    print(f"Dirección de l: {hex(id(l))}, valor: {l}")

lista = [1, 2, 3, 4, 5]
pasajePorReferencia(lista)
print(f"Dirección de lista: {hex(id(lista))}, valor: {lista}")
# lista SÍ cambió - es el mismo objeto
```

### Limitación del Reference Counting

**No detecta referencias circulares:**

```python
class Nodo:
    def __init__(self):
        self.siguiente = None

a = Nodo()
b = Nodo()
a.siguiente = b
b.siguiente = a  # Referencia circular

del a  # contador de a = 1 (aún referenciado por b.siguiente)
del b  # contador de b = 1 (aún referenciado por a.siguiente)
# ¡Ninguno llega a 0! → Fuga de memoria
```

---

## Garbage Collector Generacional

Para solucionar el problema de las referencias circulares, Python tiene un **segundo mecanismo**: el GC generacional.

### ¿Cómo funciona?

1. Divide los objetos en **3 generaciones** (0, 1, 2)
2. Los objetos nuevos están en generación 0
3. Si un objeto sobrevive a una recolección, "promociona" a la siguiente generación
4. La generación 0 se recolecta seguido, la 2 casi nunca
5. Esto es eficiente porque la mayoría de objetos "mueren jóvenes"

### Módulo `gc`

```python
import gc

# Forzar recolección de basura
objetos_liberados = gc.collect()
print(f"Se liberaron {objetos_liberados} objetos")

# Desactivar el GC generacional (NO recomendado)
gc.disable()

# Reactivar
gc.enable()

# Ver umbrales de recolección
print(gc.get_threshold())  # (700, 10, 10) por defecto
```

### Ejemplo: Referencias Circulares

**Sin GC generacional:**
```python
import ctypes
import gc

class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

gc.disable()  # Desactivamos GC para ver el problema

# Lista que se referencia a sí misma
lst = []
lst.append(lst)
direccion = id(lst)

del lst  # Destruimos la referencia

# El objeto aún existe en memoria
print(PyObject.from_address(direccion).refcnt)  # 1 ← ¡Aún existe!
```

**Con GC generacional:**
```python
gc.enable()
gc.collect()

# Ahora el objeto fue liberado
print(PyObject.from_address(direccion).refcnt)  # 0
```

---

## El Destructor `__del__`

El método [[Métodos mágicos en python#Métodos mágicos en python|`__del__`]] se ejecuta cuando un objeto va a ser destruido.

### Uso Básico

```python
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo {nombre} abierto")
    
    def __del__(self):
        self.archivo.close()
        print(f"Archivo {self.nombre} cerrado")

a = Archivo('test.txt')
del a  # Se ejecuta __del__ automáticamente
```

### El Problema con Referencias Circulares

**Cuando hay `__del__` y referencias circulares, el GC NO puede liberar los objetos:**

```python
class A:
    def __init__(self):
        self.ref = None
    def __del__(self):
        print("A destruido")

class B:
    def __init__(self):
        self.ref = None
    def __del__(self):
        print("B destruido")

a = A()
b = B()
a.ref = b  # A → B
b.ref = a  # B → A (ciclo)

del a
del b
# ¡NUNCA imprime "A destruido" ni "B destruido"!
# Python marca estos objetos como "uncollectable"
```

**¿Por qué?**

El GC detecta el ciclo pero no sabe en qué orden ejecutar los destructores:
- Si destruye A primero, `A.__del__()` podría acceder a `self.ref` (que es `b`) que ya fue destruido
- Si destruye B primero, pasa lo mismo con `b.ref` (que es `a`)
- Python decide: "mejor no tocarlo" → fuga de memoria

### Los objetos "uncollectable"

```python
import gc

class A:
    def __init__(self):
        self.ref = None
    def __del__(self):
        pass  # No imprimir para no confundir

a = A()
b = A()
a.ref = b
b.ref = a

del a, b
gc.collect()

print(gc.garbage)  # Lista de objetos que no se pudieron liberar
```

---

## Solución: `weakref`

Las **referencias débiles** no incrementan el contador de referencias, por lo que no crean ciclos "reales":

```python
import weakref

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
    def __del__(self):
        print(f"Nodo {self.valor} destruido")

# Con referencia normal
a = Nodo(1)
b = Nodo(2)
a.siguiente = b
b.siguiente = a  # Ciclo real → __del__ nunca se ejecuta

del a, b
# No imprime nada

# Con referencia débil
a = Nodo(1)
b = Nodo(2)
a.siguiente = b
b.siguiente = weakref.ref(a)  # Referencia débil → NO incrementa contador

del a, b
# Imprime: "Nodo 1 destruido", "Nodo 2 destruido" ✅
```

### Uso de `weakref`

```python
import weakref

class Jefe:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subordinados = []

class Empleado:
    def __init__(self, nombre, jefe):
        self.nombre = nombre
        # Referencia débil al jefe para evitar ciclos
        self.jefe = weakref.ref(jefe)

jefe = Jefe("Carlos")
emp = Empleado("Ana", jefe)

print(emp.jefe())  # <Jefe object at ...> - acceder con ()
print(emp.jefe().nombre)  # "Carlos"

del jefe
print(emp.jefe())  # None - el jefe fue destruido
```

---

## Creación de Objetos: `__new__` vs `__init__`

Cuando se crea una instancia, Python ejecuta **dos métodos**:

1. **`__new__`** (método de clase): Crea el espacio en memoria en el monticulo y devuelve la referencia
2. **`__init__`** (método de instancia): Inicializa los atributos

```python
class A:
    def __new__(cls):
        print("__new__ llamado")
        instancia = super().__new__(cls)
        print(f"Instancia creada: {hex(id(instancia))}")
        return instancia
    
    def __init__(self):
        print(f"__init__ llamado, self: {hex(id(self))}")

a = A()
# __new__ llamado
# Instancia creada: 0x...
# __init__ llamado, self: 0x... (misma dirección)
```

Normalmente no reescribimos `__new__`, pero es útil para:
- Singletons
- Subclases de tipos inmutables (int, str, tuple)
- Personalizar la creación de instancias

---

## Resumen

| Mecanismo | Función | Detecta ciclos |
|-----------|---------|----------------|
| **Reference Counting** | Principal, inmediato | ❌ No |
| **GC Generacional** | Secundario, periódico | ✅ Sí |
| **`__del__`** | Código al destruir | ⚠️ Problema con ciclos |
| **`weakref`** | Referencias que no cuentan | ✅ Evita ciclos |

### Buenas Prácticas

1. **Evita referencias circulares** cuando sea posible
2. **Usa `weakref`** cuando necesites referencias entre objetos que pueden crear ciclos
3. **No abuses de `__del__`** - es mejor usar context managers (`with`)
4. **Confía en el GC** - Python gestiona la memoria automáticamente
5. **Solo desactiva el GC** si sabes exactamente lo que estás haciendo

---

**Referencias:**
- Mark Lutz - Learning Python, Fifth Edition (Capítulos sobre memoria)
- Documentación oficial: https://docs.python.org/3/library/gc.html
- Unidad 2 - POO, UNSJ 2025
