---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-06T15:36:00
Revision: 2026-02-16T10:26:00
---
# Variables y Tipos de Datos en Python

## Entendiendo las Variables

En Python, las variables son nombres asociados con objetos o valores almacenados en la memoria de la computadora. Un valor puede estar asociado a una variable, lo que nos permite referirnos a dicho valor usando un nombre descriptivo y reutilizarlo cuantas veces queramos.

Para usar variables en el código, primero debemos aprender a crearlas.

Si se desea profundizar en como la memoria maneja las variables y tipos de datos: [[Como Python maneja la memoria]]

### Creando Variables

La forma fundamental de crear variables en Python es asignando un valor usando el operador de asignación `=` con la siguiente sintaxis:
```python
nombre_variable = valor
```

En esta sintaxis:
- **Izquierda:** [[Sintaxis Basica Python#Identificadores|Nombre de la variable]]
- **Centro:** Operador de asignación `=`
- **Derecha:** Valor a asignar

Este valor puede ser cualquier objeto de Python: strings, números, listas, diccionarios u objetos personalizados.

**Ejemplos:**
```python
>>> palabra = "Python"
>>> numero = 42
>>> coeficiente = 2.87
>>> frutas = ["manzana", "mango", "uva"]
>>> ordinales = {1: "primero", 2: "segundo", 3: "tercero"}
>>> class MiClasePersonalizada: pass
>>> instancia = MiClasePersonalizada()
```

En este código, las primeras asignaciones utilizan tipos de datos incorporados en Python, mientras que la última es una instancia de una clase personalizada.

### Estableciendo y Cambiando Tipos de Datos

Además del valor de las variables, es importante considerar el **tipo de dato** que tiene el valor asignado. Python es un lenguaje **dinámicamente tipado**, lo que significa que:

1. No es necesario especificar el tipo de dato al crear una variable
2. Python infiere automáticamente el tipo basándose en el valor asignado
3. El tipo de una variable puede cambiar durante la ejecución del programa

**Ejemplos de inferencia de tipos:**
```python
>>> nombre = "Juan Pérez"
>>> edad = 19
>>> materias = ["Matemáticas", "Inglés", "Física", "Química"]

>>> type(nombre)      # <class 'str'>
>>> type(edad)        # <class 'int'>
>>> type(materias)    # <class 'list'>
```

Python interpreta que "Juan Pérez" es un string, 19 es un entero, y la lista de materias es una lista.

**Cambio dinámico de tipo:**
```python
>>> edad = "19"  # Ahora es un string, no un entero
>>> type(edad)   # <class 'str'>

>>> materias = {"Matemáticas", "Inglés", "Física", "Química"}
>>> type(materias)  # <class 'set'>
```

**Nota:** Aunque Python permite el tipado dinámico, es considerada buena práctica usar **type hints** (sugerencias de tipo) para mejorar la claridad y prevenir errores, especialmente en proyectos grandes.

## Trabajando con Variables en Python

Las variables son bloques fundamentales en programación que nos permiten almacenar y manipular datos.

### Expresiones y Variables

Una **expresión** en Python es una sentencia que puede ser evaluada para producir un valor. Las variables nos permiten reutilizar valores en expresiones:

**Sin variables (repetitivo):**
```python
>>> 2 * 3.1416 * 10
62.832
>>> 2 * 3.1416 * 20
125.664
```

**Con variables (reutilizable):**
```python
>>> pi = 3.1416
>>> radio = 10
>>> 2 * pi * radio  # 62.832

>>> radio = 20
>>> 2 * pi * radio  # 125.664
```

### Objeto Contador

Un contador es una variable entera que lleva la cuenta de ocurrencias. Generalmente se inicializa en 0 y se incrementa con cada aparición:

```python
>>> contador_strings = 0
>>> elementos = ("Alice", 30, "Programmer", None, True, "Departamento C")

>>> for item in elementos:
...     if isinstance(item, str):
...         contador_strings += 1

>>> contador_strings  # 3
```

### Acumuladores

Los acumuladores son variables que almacenan la suma sucesiva de valores:

```python
>>> numeros = [1, 2, 3, 4]
>>> total = 0

>>> for numero in numeros:
...     total += numero

>>> total  # 10
```

**Nota:** Python tiene funciones incorporadas como `sum()` que simplifican estas operaciones: `sum([1, 2, 3, 4])` devuelve `10`.

### Variables Temporales (Swapping)

Las variables temporales se usan para intercambiar valores entre variables:

```python
>>> a = 5
>>> b = 10

>>> temp = a  # Guardar valor de 'a' temporalmente
>>> a = b     # Asignar valor de 'b' a 'a'
>>> b = temp  # Asignar valor temporal a 'b'

>>> a  # 10
>>> b  # 5
```

**Mejor forma en Python (sin variable temporal):**
```python
>>> a, b = b, a  # Intercambio directo
```

### Banderas Booleanas (Flags)

Son variables que almacenan valores `True` o `False` para controlar el flujo del programa:

```python
>>> alternar = True

>>> for _ in range(4):
...     if alternar:
...         print(f"✅ Alternar es {alternar}")
...         print("Hacer algo...")
...     else:
...         print(f"❌ Alternar es {alternar}")
...         print("Hacer otra cosa...")
...     alternar = not alternar  # Negar el valor
```

Las banderas también pueden ser dinámicas:
```python
>>> edad = 20
>>> es_adulto = edad > 18  # True
>>> es_adolescente = 13 <= edad <= 17  # False
```

### Variables de Bucle (Loop Variables)

Son variables que toman valores diferentes en cada iteración de un bucle:

**Bucle simple:**
```python
>>> colores = ["rojo", "naranja", "amarillo", "verde", "azul", "índigo", "violeta"]

>>> for color in colores:
...     print(color)
```

**Bucle con índice usando `enumerate()`:**
```python
>>> for indice, color in enumerate(colores):
...     print(f"Índice {indice}: {color}")
```

**Bucle while con variable de control:**
```python
>>> contador = 5
>>> while contador > 0:
...     print(contador)
...     contador -= 1  # Decrementar
```

### Variables de Almacenamiento de Datos

Son variables que contienen estructuras de datos complejas como listas, tuplas o diccionarios:

```python
>>> contactos = [
...     ("Linda", "111-2222-3333", "linda@ejemplo.com"),
...     ("José", "111-2222-3333", "jose@ejemplo.com"),
...     ("Laura", "111-2222-3333", "laura@ejemplo.com"),
... ]
```

Acceso estructurado a los datos:
```python
# Acceso a toda la tupla
>>> for contacto in contactos:
...     print(contacto)

# Desempaquetado de tuplas
>>> for nombre, telefono, email in contactos:
...     print(f"{nombre}: {telefono}")
```

## Convenciones para Nombrar Variables

Los nombres de variables deben ser descriptivos y mejorar la legibilidad del código.

### Reglas Básicas

1. **Caracteres permitidos:** Letras (A-Z, a-z), dígitos (0-9), y guiones bajos (`_`)
2. **Primer carácter:** No puede ser un dígito
3. **Sensibilidad a mayúsculas:** Python distingue entre mayúsculas y minúsculas (`edad ≠ Edad ≠ EDAD`)
4. **No usar palabras reservadas:** No se pueden usar como `if`, `for`, `class`, etc.

**Nombres válidos:**
```python
>>> nombre = "Bob"
>>> año_nacimiento = 1970
>>> es_adulto = True
>>> _variable_privada = "secreto"
```

**Nombres inválidos:**
```python
>>> 1099_archivado = False  # Error: comienza con dígito
>>> nombre-apellido = "Juan"  # Error: usa guion en lugar de guion bajo
>>> class = "Matemáticas"  # Error: palabra reservada
```

**Soporte Unicode (caracteres especiales):**
```python
>>> α = 45  # Alfa
>>> β = 90  # Beta
>>> π = 3.141592653589793  # Pi
```

Aunque técnicamente válidos, estos caracteres especiales se usan principalmente en contextos matemáticos o científicos específicos.

### Mejores Prácticas

1. **Nombres descriptivos:** Evitar nombres genéricos como `x`, `temp`, `data`
   ```python
   # Mal
   >>> t = 25
   
   # Bien
   >>> temperatura = 25
   >>> temperatura_actual = 25
   ```

2. **Evitar abreviaciones oscuras:**
   ```python
   # Mal (no claro)
   >>> doc = "Freud"
   
   # Bien
   >>> doctor = "Freud"
   >>> médico = "Freud"
   
   # Aceptable (abreviación conocida)
   >>> msg = "Hola, Pythonista!"
   >>> cmd = "python -m pip list"
   ```

3. **Separación de palabras múltiples:**
   ```python
   # Snake case (recomendado en Python)
   >>> numero_de_graduados = 200
   >>> usuario_autenticado = True
   
   # Camel case (común en otros lenguajes)
   >>> numeroDeGraduados = 200  # No recomendado en Python
   
   # Pascal case (para nombres de clases)
   >>> NumeroDeGraduados = 200  # Solo para clases
   ```

4. **Nombres para colecciones (plurales):**
   ```python
   >>> frutas = ["manzana", "banana", "cereza"]
   >>> estudiantes = ["Ana", "Carlos", "Beatriz"]
   
   >>> colores = {
   ...     "Rojo": (255, 0, 0),
   ...     "Verde": (0, 255, 0),
   ... }
   ```

5. **Adjetivos para clasificación:**
   ```python
   >>> temperatura_inicial = 25
   >>> archivo_actual = "personal_marketing.csv"
   >>> siguiente_punto = (2, 4)
   >>> es_autenticado = True
   >>> tiene_permiso = False
   ```

### Variables Públicas y No Públicas

- **Públicas:** Nombres normales (`temperatura`, `contador`)
- **No públicas (privadas):** Comienzan con un guion bajo (`_variable_interna`)
- **Fuertemente privadas:** Comienzan con dos guiones bajos (`__variable_oculta`)

**Ejemplo de variable no pública:**
```python
# modulo.py
_timeout = 30

def obtener_timeout():
    return _timeout

def establecer_timeout(segundos):
    global _timeout
    _timeout = segundos
```

El guion bajo indica que `_timeout` es para uso interno del módulo, aunque técnicamente sigue siendo accesible desde fuera.

### Nombres a Evitar

1. **Palabras clave (keywords):**
   ```python
   >>> import keyword
   >>> keyword.kwlist  # Lista de todas las palabras clave
   ```

2. **Usar palabras clave con guion bajo (evitar si es posible):**
   ```python
   # Funciona, pero no es ideal
   >>> class_ = "Negocios"
   
   # Mejor alternativa
   >>> clase_pasajero = "Negocios"
   ```

3. **Nombres de funciones incorporadas (built-ins):**
   ```python
   # ¡PELIGROSO! Sobreescribe la función list()
   >>> list = [1, 2, 3, 4]
   
   # Ahora esto falla
   >>> list(range(10))  # TypeError: 'list' object is not callable
   ```

**Para verificar nombres incorporados:**
```python
>>> import builtins
>>> dir(builtins)  # Lista de todos los nombres incorporados
```

## Conceptos Avanzados sobre Variables

### Las Variables son Referencias a Objetos

En Python, las variables **no almacenan objetos directamente**, sino **referencias** (punteros) a objetos en memoria.

```python
>>> n = 300  # Python crea un objeto entero 300, y 'n' apunta a él
>>> id(n)    # Dirección de memoria del objeto (4399012816)
```

**Diagrama conceptual:**
```
n ────→ [Objeto int: 300]
```

**Asignación múltiple a un mismo objeto:**
```python
>>> m = n  # 'm' ahora apunta al MISMO objeto que 'n'
>>> id(n) == id(m)  # True (misma dirección de memoria)
```

**Diagrama:**
```
n ────┐
      │
      └→ [Objeto int: 300]
      │
m ────┘
```

**Cambio de referencia:**
```python
>>> m = 400  # 'm' ahora apunta a un NUEVO objeto
>>> n = "foo"  # 'n' ahora apunta a un objeto string
```

**Diagrama:**
```
n ────→ [Objeto str: "foo"]
m ────→ [Objeto int: 400]
```

### Tipado Dinámico vs. Sugerencias de Tipo

**Tipado dinámico (comportamiento por defecto):**
```python
>>> valor = "Un string"  # Tipo: str
>>> valor.upper()  # Funciona: 'UN STRING'

>>> valor = 23.5  # Cambia a tipo: float
>>> valor.upper()  # Error: AttributeError
```

**Sugerencias de tipo (type hints - opcional pero recomendado):**
```python
# Sintaxis básica
>>> variable: tipo = valor

# Ejemplos
>>> lenguaje: str = "Python"
>>> numero: int = 42
>>> coeficiente: float = 2.87
```

**Sugerencias para estructuras complejas:**
```python
# Diccionario: clave str → valor str
>>> colores: dict[str, str] = {
...     "rojo": "#FF0000",
...     "verde": "#00FF00",
... }

# Diccionario: clave str → tupla de 3 ints
>>> colores_rgb: dict[str, tuple[int, int, int]] = {
...     "Rojo": (255, 0, 0),
...     "Verde": (0, 255, 0),
... }

# Lista de strings
>>> frutas: list[str] = ["manzana", "banana"]

# Lista de tuplas
>>> filas: list[tuple[str, int, str]] = [
...     ("Ana", 25, "Ingeniera"),
...     ("Luis", 30, "Médico"),
... ]
```

**Nota:** Las sugerencias de tipo solo son informativas. Python no las verifica en tiempo de ejecución por defecto (se necesitan herramientas como `mypy` para verificación estática).

## Formas Complementarias de Crear Variables

### Asignación Paralela (Mismo Valor)

```python
# Múltiples variables con el mismo valor
>>> autenticado = activo = admin = False

# Equivalente a:
>>> autenticado = False
>>> activo = False
>>> admin = False
```

### Desempaquetado de Iterables (Unpacking)

Distribuye los valores de un iterable en múltiples variables:

**Forma básica:**
```python
>>> persona = ("Jane", 25, "Desarrolladora Python")

# Forma tradicional (menos elegante)
>>> nombre = persona[0]
>>> edad = persona[1]
>>> trabajo = persona[2]

# Forma Pythonica con unpacking
>>> nombre, edad, trabajo = persona
```

**Intercambio de valores (swapping elegante):**
```python
>>> a = 5
>>> b = 10
>>> a, b = b, a  # Intercambio en una línea
```

### Asignación por Expresión (Walrus Operator `:=`)

El operador morsa (`:=`) permite asignar y usar una variable en la misma expresión:

**Ejemplo sin walrus operator:**
```python
>>> linea = input("Escribe texto: ")
>>> while linea != "stop":
...     print(linea)
...     linea = input("Escribe texto: ")
```

**Ejemplo con walrus operator (más conciso):**
```python
>>> while (linea := input("Escribe texto: ")) != "stop":
...     print(linea)
```

## Ámbito (Scope) de Variables

El ámbito define dónde una variable es visible y accesible en el código. Python sigue la regla **LEGB**:
- **L**ocal (dentro de funciones)
- **E**nclosing (funciones anidadas)
- **G**lobal (módulo)
- **B**uilt-in (incorporadas)

### Variables Globales y Locales

**Variables globales:** Definidas a nivel de módulo
```python
# Variable global
>>> valor = 42

>>> def funcion():
...     print(valor)  # Puede acceder a variables globales

>>> funcion()  # 42
```

**Variables locales:** Definidas dentro de funciones
```python
>>> def funcion():
...     entero = 42  # Variable local
...     return entero

>>> funcion()  # 42
>>> entero  # Error: NameError (no existe en ámbito global)
```

### Variables No Locales (nonlocal)

Para modificar variables de funciones exteriores desde funciones anidadas:

```python
def exterior():
    contador = 0  # Variable no local para interior()
    
    def interior():
        nonlocal contador  # Declarar como no local
        contador += 1
        return contador
    
    return interior

>>> f = exterior()
>>> f()  # 1
>>> f()  # 2
>>> f()  # 3
```

### Variables de Clase e Instancia

**Variables de clase:** Compartidas por todas las instancias
**Variables de instancia:** Únicas para cada objeto

```python
class Empleado:
    # Variable de clase
    contador = 0
    
    def __init__(self, nombre, salario):
        # Variables de instancia
        self.nombre = nombre
        self.salario = salario
        Empleado.contador += 1  # Acceder a variable de clase

>>> emp1 = Empleado("Ana", 50000)
>>> emp2 = Empleado("Luis", 60000)

>>> Empleado.contador  # 2 (acceso desde clase)
>>> emp1.contador      # 2 (acceso desde instancia)
>>> emp1.nombre        # "Ana" (único para emp1)
```

### Eliminando Variables (del)

La declaración `del` elimina referencias a variables:

```python
>>> ciudad = "Nueva York"
>>> del ciudad
>>> ciudad  # NameError: nombre 'ciudad' no está definido
```

## Tipos de Datos en Python

Un tipo de dato define:
1. Qué valores puede tomar
2. Qué operaciones se pueden realizar con él

### Clasificación Principal

1. **Numéricos**
2. **Secuencias**
3. **Conjuntos (Sets)**
4. **Diccionarios**
5. **Booleanos**

### 1. Tipos Numéricos

**Enteros (int):** Números enteros positivos o negativos
```python
>>> x = 42
>>> y = -100
>>> z = 8_675_309  # Usar _ como separador visual
>>> type(z)  # <class 'int'>
```

**Punto flotante (float):** Números decimales
```python
>>> pi = 3.14159
>>> temperatura = -5.5
>>> cientifico = 1.23e-4  # 0.000123
>>> type(pi)  # <class 'float'>
```

**Complejos (complex):** Números con parte real e imaginaria
```python
>>> complejo = 3 + 4j
>>> complejo.real  # 3.0
>>> complejo.imag  # 4.0
>>> type(complejo)  # <class 'complex'>
```

### 2. Tipos de Secuencia

**Strings (str):** Secuencias de caracteres
```python
>>> saludo = "Hola Mundo"
>>> multilinea = """Línea 1
... Línea 2"""
>>> type(saludo)  # <class 'str'>
```

**Listas (list):** Secuencias mutables
```python
>>> numeros = [1, 2, 3, 4, 5]
>>> mixto = [1, "dos", 3.0, True]
>>> numeros.append(6)  # Modificable
>>> type(numeros)  # <class 'list'>
```

**Tuplas (tuple):** Secuencias inmutables
```python
>>> coordenadas = (10, 20)
>>> rgb = (255, 0, 0)
# coordenadas[0] = 5  # Error: las tuplas son inmutables
>>> type(coordenadas)  # <class 'tuple'>
```

### 3. Conjuntos (Sets)

Colecciones no ordenadas de elementos únicos:
```python
>>> conjunto = {1, 2, 3, 4, 5}
>>> conjunto.add(6)  # Modificable
>>> conjunto.add(1)  # No se agrega (duplicado)
>>> type(conjunto)  # <class 'set'>
```

**Operaciones con conjuntos:**
```python
>>> A = {1, 2, 3}
>>> B = {3, 4, 5}

>>> A | B  # Unión: {1, 2, 3, 4, 5}
>>> A & B  # Intersección: {3}
>>> A - B  # Diferencia: {1, 2}
```

### 4. Diccionarios (dict)

Colecciones de pares clave-valor:
```python
>>> persona = {
...     "nombre": "Juan Pérez",
...     "edad": 30,
...     "ciudad": "Madrid"
... }

>>> persona["edad"]  # 30 (acceso por clave)
>>> persona["profesion"] = "Ingeniero"  # Agregar nuevo par
>>> type(persona)  # <class 'dict'>
```

### 5. Booleanos (bool)

Valores lógicos `True` o `False`:
```python
>>> es_mayor = 10 > 5  # True
>>> es_igual = 10 == 5  # False
>>> tipo(True)  # <class 'bool'>
```

**Valores que evalúan a Falso (falsy):**
- `False`
- `None`
- `0` (cualquier numérico cero)
- `""` (string vacío)
- `[]`, `()`, `{}` (colecciones vacías)

**Valores que evalúan a Verdadero (truthy):**
- Cualquier otro valor

### Verificación de Tipos

```python
>>> valor = 42
>>> isinstance(valor, int)  # True
>>> isinstance(valor, (int, float))  # True (múltiples tipos)

>>> type(valor) == int  # True (pero isinstance() es más flexible)
```

### Conversión entre Tipos

```python
>>> int(3.14)  # 3 (trunca decimales)
>>> float(42)  # 42.0
>>> str(100)   # "100"
>>> list("abc")  # ['a', 'b', 'c']
>>> tuple([1, 2, 3])  # (1, 2, 3)
>>> set([1, 2, 2, 3])  # {1, 2, 3} (elimina duplicados)
>>> bool(0)  # False
>>> bool(1)  # True
```

---
__TE SIENTES DETERMINADO__