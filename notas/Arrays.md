---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
  - estructuras
proyecto: aprendizaje-programacion
Creacion: 2026-01-27T22:19:00
Revision: 2026-01-28T21:44:00
---
# Tabla de Contenidos

- [[#¿Por qué usar Arreglos en Python?|¿Por qué usar Arreglos en Python?]]
- [[#¿Qué son los Arreglos en Python?|¿Qué son los Arreglos en Python?]]
- [[#¿Las listas Python son iguales que un Arreglo?|¿Las listas Python son iguales que un Arreglo?]]
- [[#Creando un Arreglo en Python|Creando un Arreglo en Python]]
- [[#Accediendo a los Elementos de un Arreglo|Accediendo a los Elementos de un Arreglo]]
- [[#Operaciones Básicas en un Arreglo|Operaciones Básicas en un Arreglo]]
	- [[#Operaciones Básicas en un Arreglo#Encontrando la Longitud de un Array|Encontrando la Longitud de un Array]]
- [[#Agregando/Cambiando elementos de un Arreglo|Agregando/Cambiando elementos de un Arreglo]]
	- [[#Agregando/Cambiando elementos de un Arreglo#`append()` - Agregar un elemento al final|`append()` - Agregar un elemento al final]]
	- [[#Agregando/Cambiando elementos de un Arreglo#`extend()` - Agregar múltiples elementos|`extend()` - Agregar múltiples elementos]]
	- [[#Agregando/Cambiando elementos de un Arreglo#`insert()` - Insertar en una posición específica|`insert()` - Insertar en una posición específica]]
- [[#Concatenación de Arreglos|Concatenación de Arreglos]]
- [[#Eliminando/Quitando elementos de un arreglo|Eliminando/Quitando elementos de un arreglo]]
	- [[#Eliminando/Quitando elementos de un arreglo#`pop()` - Eliminar por índice (retorna el valor)|`pop()` - Eliminar por índice (retorna el valor)]]
	- [[#Eliminando/Quitando elementos de un arreglo#`remove()` - Eliminar por valor (no retorna)|`remove()` - Eliminar por valor (no retorna)]]
- [[#Rebanando un Arreglo (Slicing)|Rebanando un Arreglo (Slicing)]]
- [[#Iterando sobre un Arreglo|Iterando sobre un Arreglo]]
	- [[#Iterando sobre un Arreglo#Iteración básica con `for`|Iteración básica con `for`]]
	- [[#Iterando sobre un Arreglo#Iteración con índice usando `enumerate()`|Iteración con índice usando `enumerate()`]]
- [[#Listas Enlazadas: La Otra Cara de la Moneda|Listas Enlazadas: La Otra Cara de la Moneda]]
	- [[#Listas Enlazadas: La Otra Cara de la Moneda#¿Qué son las Listas Enlazadas?|¿Qué son las Listas Enlazadas?]]
	- [[#Listas Enlazadas: La Otra Cara de la Moneda#Comparación: Arrays vs Listas Enlazadas|Comparación: Arrays vs Listas Enlazadas]]
	- [[#Listas Enlazadas: La Otra Cara de la Moneda#Implementación básica de Lista Enlazada|Implementación básica de Lista Enlazada]]
- [[#¿Cuándo usar cada uno?|¿Cuándo usar cada uno?]]
	- [[#¿Cuándo usar cada uno?#**Usa Arrays cuando:**|**Usa Arrays cuando:**]]
	- [[#¿Cuándo usar cada uno?#**Usa Listas Enlazadas cuando:**|**Usa Listas Enlazadas cuando:**]]
- [[#Arreglos NumPy: La Mejor Alternativa|Arreglos NumPy: La Mejor Alternativa]]
- [[#Ejemplo Práctico Completo|Ejemplo Práctico Completo]]
- [[#📊 **Comparación Directa**|📊 **Comparación Directa**]]
- [[#🔍 **Arrays Dinamicos en Python**|🔍 **Arrays Dinamicos en Python**]]
	- [[#🔍 **Arrays Dinamicos en Python**#**En C/C++: Arrays ESTÁTICOS (tamaño fijo)**|**En C/C++: Arrays ESTÁTICOS (tamaño fijo)**]]
	- [[#🔍 **Arrays Dinamicos en Python**#**En Python: Arrays "PSEUDO-dinámicos**|**En Python: Arrays "PSEUDO-dinámicos**]]
	- [[#🔍 **Arrays Dinamicos en Python**#🧠 **La Magia Detrás: Python vs C**|🧠 **La Magia Detrás: Python vs C**]]
		- [[#🧠 **La Magia Detrás: Python vs C**#**C/C++: "Lo que ves es lo que hay"**|**C/C++: "Lo que ves es lo que hay"**]]
		- [[#🧠 **La Magia Detrás: Python vs C**#**Python: "El ilusionista"**|**Python: "El ilusionista"**]]
	- [[#🔍 **Arrays Dinamicos en Python**#📈 **Estrategia de Crecimiento de Python**|📈 **Estrategia de Crecimiento de Python**]]
	- [[#🔍 **Arrays Dinamicos en Python**#🔧 **¿Cómo funciona realmente?**|🔧 **¿Cómo funciona realmente?**]]
		- [[#🔧 **¿Cómo funciona realmente?**#**En C puro (lo que Python NO hace):**|**En C puro (lo que Python NO hace):**]]
		- [[#🔧 **¿Cómo funciona realmente?**#**En Python (lo que SÍ hace automáticamente):**|**En Python (lo que SÍ hace automáticamente):**]]
	- [[#🔍 **Arrays Dinamicos en Python**#🎯 **Los 3 Niveles de "Arrays" en Python**|🎯 **Los 3 Niveles de "Arrays" en Python**]]
		- [[#🎯 **Los 3 Niveles de "Arrays" en Python**#**1. `array.array()` - "Semi-dinámico"**|**1. `array.array()` - "Semi-dinámico"**]]
		- [[#🎯 **Los 3 Niveles de "Arrays" en Python**#**2. `list` - "Completamente dinámico"**|**2. `list` - "Completamente dinámico"**]]
		- [[#🎯 **Los 3 Niveles de "Arrays" en Python**#**3. `numpy.array` - "Pseudo-estático"**|**3. `numpy.array` - "Pseudo-estático"**]]
- [[#Tabla de Resumen: Tipos de "Arrays" en Python|Tabla de Resumen: Tipos de "Arrays" en Python]]
# Arrays 

Los **arrays** o **arreglos** en las estructuras de datos pueden contener datos del mismo tipo. A menudo son confundidos con las listas de Python o los arreglos NumPy. Técnicamente, funcionan de formas distintas a estos dos.

## ¿Por qué usar Arreglos en Python?

Los arreglos ayudan a reducir el tamaño general del código. Por ejemplo, si tienes que guardar números enteros del 1 al 100, no querrás recordar o inventar 100 nombres de variables diferentes. Para solucionar esto, puedes guardar dichos valores en un arreglo y acceder a ellos mediante un índice:

![[Basic-Array-Structure-Arrays-In-Python-Edureka-768x346.png]]

## ¿Qué son los Arreglos en Python?

Un **arreglo** es básicamente una estructura de datos que puede almacenar más de un valor al mismo tiempo. Es una colección ordenada o una serie de elementos ordenados del **mismo tipo**.

**Ejemplo:**
```python
a = arr.array('d', [1, 2, 3])
```

Podemos recorrer la estructura mediante iteraciones y capturar sus elementos, también podemos hacerlo especificando el índice. Esto va a variar dependiendo de cómo tengas que resolver el problema.

## ¿Las listas Python son iguales que un Arreglo?

Los **arreglos Python** y las **listas** almacenan sus valores de manera similar, pero hay diferencias clave:

| Característica | Listas | Arreglos |
|----------------|---------|----------|
| **Tipos de datos** | Pueden almacenar cualquier tipo | Todos los elementos deben ser del mismo tipo |
| **Flexibilidad** | Alta flexibilidad | Menor flexibilidad |
| **Rendimiento** | Generalmente más lento | Más eficiente para operaciones numéricas |
| **Uso de memoria** | Más memoria por elemento | Menos memoria por elemento |

**Nota importante**: En Python, los arreglos del módulo `array` son de **tamaño dinámico**, a diferencia de otros lenguajes donde los arreglos son estructuras de tamaño fijo con posiciones contiguas en memoria. Esto es diferente a los arreglos tradicionales de otros lenguajes.

## Creando un Arreglo en Python

Los arreglos en Python pueden crearse importando el módulo `array`:

```python
import array as arr
```

Aunque existe este módulo, se recomienda el uso de **[arreglos NumPy](https://numpy.org/doc/stable/)**, ya que respetan más la estructura de los arreglos tradicionales y ofrecen más funcionalidades.

La función `array()` toma dos parámetros: el tipo de dato y la lista con los valores.

**Sintaxis:**
```python
a = arr.array(tipo_dato, lista_valores)
```

**Ejemplo:**
```python
a = arr.array('d', [1, 2, 3])
```

Donde el parámetro `'d'` especifica que los valores a almacenar son números de punto flotante de tamaño 8 bytes:

| Código | Tipo de dato Python | Tamaño (bytes) |
|--------|---------------------|----------------|
| `i` | int | 2 |
| `I` | int | 2 |
| `u` | unicode character | 2 |
| `h` | int | 2 |
| `H` | int | 2 |
| `l` | int | 4 |
| `L` | int | 4 |
| `f` | float | 4 |
| `d` | float | 8 |

## Accediendo a los Elementos de un Arreglo

Para acceder a los elementos de un arreglo, necesitas especificar el valor del índice que lo almacena. Los índices empiezan a contar desde 0:

```python
nombre_array[indice]
```

**Ejemplo:**
```python
a = arr.array('d', [1, 2.3, 3])
print(a[1])
```

**Salida:**
```
2.3
```

## Operaciones Básicas en un Arreglo

Hay varias operaciones que pueden hacerse dentro de los arreglos:

![[OPERATIONS-NEW.png]]

### Encontrando la Longitud de un Array

En Python podemos usar la función nativa [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|`len()`]] para saber la longitud o cantidad de elementos almacenados en un arreglo:

```python
len(nombre_array)
```

**Ejemplo:**
```python
a = arr.array('d', [1.1, 2.1, 3.1])
print(len(a))
```

**Salida:**
```
3
```

## Agregando/Cambiando elementos de un Arreglo

En Python podemos agregar valores a un arreglo usando las funciones [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|`append()`, `extend()`, `insert()`]]:

### `append()` - Agregar un elemento al final

```python
a = arr.array('d', [1.1, 2.1, 3.1])
a.append(3.4)
print(a)
```

**Salida:**
```
array('d', [1.1, 2.1, 3.1, 3.4])
```

### `extend()` - Agregar múltiples elementos

```python
a = arr.array('d', [1.1, 2.1, 3.1])
a.extend([4.5, 6.3, 6.8])
print(a)
```

**Salida:**
```
array('d', [1.1, 2.1, 3.1, 4.5, 6.3, 6.8])
```

### `insert()` - Insertar en una posición específica

Inserta un nuevo elemento en el índice especificado y mueve los elementos subsiguientes:

```python
a = arr.array('d', [1.1, 2.1, 3.1])
a.insert(2, 3.8)  # Inserta 3.8 en la posición 2
print(a)
```

**Salida:**
```
array('d', [1.1, 2.1, 3.8, 3.1])
```

**Nota**: Estos métodos aunque sean automáticos en Python, podrían programarse en otros lenguajes que no los ofrezcan o si se requiere añadir complejidad específica.

## Concatenación de Arreglos

```python
a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
b = arr.array('d', [3.7, 8.6])
c = a + b
print("Array c =", c)
```

**Salida:**
```
Array c = array('d', [1.1, 2.1, 3.1, 2.6, 7.8, 3.7, 8.6])
```

## Eliminando/Quitando elementos de un arreglo

Los elementos de un arreglo se pueden remover usando las funciones [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|`pop()`, `remove()`]].

### `pop()` - Eliminar por índice (retorna el valor)

Puede usarse sin parámetro o con un índice. Sin parámetro, elimina el último elemento. Retorna el elemento eliminado.

```python
a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])
print("Elemento eliminado (último):", a.pop())
print("Array actual:", a)
print("Elemento eliminado (índice 3):", a.pop(3))
print("Array final:", a)
```

**Salida:**
```
Elemento eliminado (último): 4.6
Array actual: array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2])
Elemento eliminado (índice 3): 3.1
Array final: array('d', [1.1, 2.2, 3.8, 3.7, 1.2])
```

### `remove()` - Eliminar por valor (no retorna)

Elimina la primera ocurrencia del valor especificado.

```python
a = arr.array('d', [1.1, 2.1, 3.1])
a.remove(1.1)
print(a)
```

**Salida:**
```
array('d', [2.1, 3.1])
```

## Rebanando un Arreglo (Slicing)

El [[Listas en Python#Indexación y *Slicing* (rebanado)|slicing]] funciona de la misma forma que en las listas:

```python
a = arr.array('d', [1.1, 2.1, 3.1, 2.6, 7.8])
print("Primeros 3 elementos:", a[0:3])
print("Del segundo al cuarto:", a[1:4])
print("Todos menos el último:", a[:-1])
```

**Salida:**
```
Primeros 3 elementos: array('d', [1.1, 2.1, 3.1])
Del segundo al cuarto: array('d', [2.1, 3.1, 2.6])
Todos menos el último: array('d', [1.1, 2.1, 3.1, 2.6])
```

## Iterando sobre un Arreglo

Para iterar sobre un arreglo se puede usar cualquier [[Estructuras Iterativas en Python#Estructuras Iterativas en Python|estructura iterativa]] según las necesidades:

### Iteración básica con `for`
```python
a = arr.array('d', [1.1, 2.2, 3.8, 3.1, 3.7, 1.2, 4.6])

print("Todos los valores:")
for x in a:
    print(x)

print("\nValores específicos (índices 1 a 3):")
for x in a[1:4]:
    print(x)
```

**Salida:**
```
Todos los valores:
1.1
2.2
3.8
3.1
3.7
1.2
4.6

Valores específicos (índices 1 a 3):
2.2
3.8
3.1
```

### Iteración con índice usando `enumerate()`
```python
a = arr.array('i', [10, 20, 30, 40, 50])

for indice, valor in enumerate(a):
    print(f"Índice {indice}: {valor}")
```

**Salida:**
```
Índice 0: 10
Índice 1: 20
Índice 2: 30
Índice 3: 40
Índice 4: 50
```

## Listas Enlazadas: La Otra Cara de la Moneda

### ¿Qué son las Listas Enlazadas?

Una **lista enlazada** es una estructura de datos lineal donde los elementos (nodos) no están almacenados en posiciones contiguas de memoria. Cada nodo contiene:
1. **Datos** (el valor almacenado)
2. **Referencia** (puntero) al siguiente nodo

```python
# Representación conceptual de un nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
```

### Comparación: Arrays vs Listas Enlazadas

| Característica | Arrays | Listas Enlazadas |
|----------------|--------|------------------|
| **Acceso aleatorio** | O(1) - Muy rápido | O(n) - Lento |
| **Inserción al inicio** | O(n) - Lento (desplaza elementos) | O(1) - Muy rápido |
| **Inserción al final** | O(1) - Rápido (amortizado) | O(n) - Lento (debes recorrer) |
| **Eliminación al inicio** | O(n) - Lento | O(1) - Rápido |
| **Uso de memoria** | Fijo/Contiguo | Disperso/Punteros |
| **Tamaño** | Fijo/Dinámico (en Python) | Siempre dinámico |

### Implementación básica de Lista Enlazada

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Uso
lista = ListaEnlazada()
lista.agregar_al_inicio(3)
lista.agregar_al_inicio(2)
lista.agregar_al_inicio(1)
lista.imprimir()  # 1 -> 2 -> 3 -> None
```

## ¿Cuándo usar cada uno?

### **Usa Arrays cuando:**
- Necesitas acceso aleatorio frecuente (por índice)
- Conoces aproximadamente el tamaño de los datos
- Realizas muchas operaciones matemáticas/numéricas
- Prefieres menos uso de memoria (contiguo)

### **Usa Listas Enlazadas cuando:**
- Realizas muchas inserciones/eliminaciones al inicio
- No sabes el tamaño de los datos de antemano
- La memoria es fragmentada
- Implementas pilas (stacks) o colas (queues)

## Arreglos NumPy: La Mejor Alternativa

Para trabajo numérico serio, **NumPy** es superior al módulo `array`:

```python
import numpy as np

# Crear array NumPy
arr_numpy = np.array([1, 2, 3, 4, 5], dtype=np.float64)

# Operaciones vectorizadas (MUCHO más eficiente)
print("Array original:", arr_numpy)
print("Array * 2:", arr_numpy * 2)  # Multiplica todos por 2
print("Array + 10:", arr_numpy + 10)  # Suma 10 a todos
print("Promedio:", arr_numpy.mean())
print("Suma total:", arr_numpy.sum())
```

## Ejemplo Práctico Completo

```python
import array as arr

# 1. Crear un array de enteros
calificaciones = arr.array('i', [85, 90, 78, 92, 88])

# 2. Acceder y modificar
print("Primera calificación:", calificaciones[0])
calificaciones[2] = 80  # Actualizar tercera calificación

# 3. Agregar nuevas calificaciones
calificaciones.append(95)
calificaciones.extend([87, 91])

# 4. Calcular promedio
promedio = sum(calificaciones) / len(calificaciones)
print(f"Promedio: {promedio:.2f}")

# 5. Encontrar máxima y mínima
print(f"Máxima: {max(calificaciones)}")
print(f"Mínima: {min(calificaciones)}")

# 6. Filtrar calificaciones aprobatorias (>70)
aprobatorias = [cal for cal in calificaciones if cal > 70]
print(f"Aprobatorias: {aprobatorias}")

# 7. Ordenar (convertir a lista para ordenar)
calificaciones_ordenadas = sorted(calificaciones)
print(f"Ordenadas: {calificaciones_ordenadas}")
```

## 📊 **Comparación Directa**

| Lenguaje   | Tipo de Array             | ¿Tamaño?                  | ¿Memoria contigua?      | ¿Dinámico?                    |
| ---------- | ------------------------- | ------------------------- | ----------------------- | ----------------------------- |
| **C/C++**  | `int arr[10]`             | **FIJO** en compilación   | **SÍ**, bloque continuo | **NO**, manual con `malloc()` |
| **Python** | `array.array('i', [...])` | **DINÁMICO** en ejecución | **SÍ**, pero gestionado | **SÍ**, automático            |

## 🔍 **Arrays Dinamicos en Python**

### **En C/C++: Arrays ESTÁTICOS (tamaño fijo)**
```c
// C - Tamaño FIJO en tiempo de COMPILACIÓN
int numeros[10];  // ¡10 posiciones PARA SIEMPRE!
numeros[11] = 42; // 💥 ERROR en tiempo de ejecución (buffer overflow)

// C - "Dinámico" pero complicado
int *numeros = malloc(10 * sizeof(int));
// Ahora tienes que gestionar TODO:
// 1. Realloc para redimensionar (complejo)
// 2. Free para liberar (si no -> memory leak)
// 3. Controlar índices manualmente
```

### **En Python: Arrays "PSEUDO-dinámicos**
```python
import array as arr

# Python - Se siente dinámico
numeros = arr.array('i', [1, 2, 3])
print(id(numeros))  # Dirección de memoria: 0x7f8a1c

# Agregamos más elementos
numeros.append(4)
numeros.append(5)
numeros.append(6)

print(id(numeros))  # ¡MISMA dirección! 0x7f8a1c
# Pero... ¿cómo cabe más en el mismo espacio?
```

### 🧠 **La Magia Detrás: Python vs C**

#### **C/C++: "Lo que ves es lo que hay"**
```c
// Visualización de memoria en C:
+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 |   |   |   |   |   |   |   |  // int arr[10];
+---+---+---+---+---+---+---+---+---+---+
  ↑
  // ¡Solo 10 cajitas! Si quieres la 11... 💥
```

#### **Python: "El ilusionista"**
```python
# Visualización de Python:
# Paso 1: Creamos un array pequeño
+---+---+---+
| 1 | 2 | 3 |  # array('i', [1, 2, 3])
+---+---+---+

# Paso 2: Python ANTICIPA y reserva MÁS espacio
+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 |   |   |   |   |   |   |   |  # Reserva extra
+---+---+---+---+---+---+---+---+---+---+

# Paso 3: Añadimos elementos (usa espacio reservado)
+---+---+---+---+---+---+---+---+---+---+
| 1 | 2 | 3 | 4 | 5 | 6 |   |   |   |   |  # append() 4, 5, 6
+---+---+---+---+---+---+---+---+---+---+

# Paso 4: Si llenamos TODO el espacio reservado...
# ¡Python crea un NUEVO array más grande y COPIA todo!
```

### 📈 **Estrategia de Crecimiento de Python**

Python usa una **estrategia de sobre-asignación** (over-allocation):

```python
# Ejemplo real del factor de crecimiento
import sys

arr = arr.array('i')

tamanos = []
for i in range(20):
    arr.append(i)
    tamanos.append(sys.getsizeof(arr))

print("Crecimiento del array:")
for i, tam in enumerate(tamanos):
    print(f"Elemento {i}: {tam} bytes")
```

**Salida típica:**
```
Elemento 0: 64 bytes
Elemento 1: 64 bytes  # Mismo tamaño
...
Elemento 4: 64 bytes  # Aún cabe
Elemento 5: 96 bytes  # ¡CRECIMIENTO! Nuevo array 50% más grande
Elemento 6: 96 bytes  # Sigue cabiendo
...
```

### 🔧 **¿Cómo funciona realmente?**

#### **En C puro (lo que Python NO hace):**
```c
// En C tendrías que hacer algo como:
int* redimensionar_array(int* viejo, int viejo_tam, int nuevo_tam) {
    int* nuevo = malloc(nuevo_tam * sizeof(int));
    for(int i = 0; i < viejo_tam; i++) {
        nuevo[i] = viejo[i];
    }
    free(viejo);  // ¡TÚ gestionas!
    return nuevo;
}
```

#### **En Python (lo que SÍ hace automáticamente):**
```python
# Simplificación del código interno de Python
class PyArray:
    def __init__(self, tipo, elementos):
        self.tipo = tipo
        self.elementos = elementos[:]  # Copia
        self.capacidad = len(elementos) * 2  # ¡Reserva extra!
    
    def append(self, valor):
        if len(self.elementos) >= self.capacidad:
            # 1. Calcula nuevo tamaño (usualmente 1.5x o 2x)
            nueva_capacidad = int(self.capacidad * 1.5)
            
            # 2. Crea nuevo array más grande
            nuevo_array = crear_array(self.tipo, nueva_capacidad)
            
            # 3. Copia los elementos viejos
            for i, elem in enumerate(self.elementos):
                nuevo_array[i] = elem
            
            # 4. Reemplaza el viejo (¡GC se encarga de limpiar!)
            self.elementos = nuevo_array
            self.capacidad = nueva_capacidad
        
        # 5. Añade el nuevo elemento
        self.elementos[len(self.elementos)] = valor
```

### 🎯 **Los 3 Niveles de "Arrays" en Python**

#### **1. `array.array()` - "Semi-dinámico"**
```python
import array as arr
a = arr.array('i', [1, 2, 3])
a.append(4)  # ✅ Dinámico (pero solo tipo homogéneo)
# Interno: Similar a listas pero optimizado para tipos simples
```

#### **2. `list` - "Completamente dinámico"**
```python
lista = [1, "hola", 3.14, True]  # ✅ Cualquier tipo
lista.append([1, 2, 3])  # ✅ Incluso otras listas
# Más flexible pero menos eficiente en memoria
```

#### **3. `numpy.array` - "Pseudo-estático"**
```python
import numpy as np
arr = np.array([1, 2, 3], dtype=np.int32)
# arr.append(4)  # ❌ NO existe append() en NumPy
arr = np.append(arr, 4)  # ✅ Pero crea COPIA nueva
# NumPy prefiere tamaño fijo por rendimiento
```

## Tabla de Resumen: Tipos de "Arrays" en Python

| Tipo | Módulo | Características | Mejor para |
|------|--------|----------------|------------|
| **Lista** | Built-in | Heterogénea, dinámica | Datos generales |
| **Array** | `array` | Homogénea, eficiente | Datos simples del mismo tipo |
| **NumPy Array** | `numpy` | Homogénea, operaciones vectorizadas | Cálculos numéricos |
| **Lista Enlazada** | Custom | Nodos enlazados, inserción rápida | Inserción/eliminación frecuente |

---

**TE SIENTES DETERMINADO** 💪
