---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-23T20:24:00
Revision: 2026-01-25T17:48:00
---
# Tabla de Contenidos

- [[#Características de los diccionarios|Características de los diccionarios]]
- [[#Creando diccionarios en Python|Creando diccionarios en Python]]
	- [[#Creando diccionarios en Python#Diccionarios literales|Diccionarios literales]]
	- [[#Creando diccionarios en Python#Usando el constructor `dict()`|Usando el constructor `dict()`]]
	- [[#Creando diccionarios en Python#Usando `.fromkeys()`|Usando `.fromkeys()`]]
- [[#Accediendo a los valores de un diccionario|Accediendo a los valores de un diccionario]]
- [[#Llenando diccionarios de manera incremental|Llenando diccionarios de manera incremental]]
	- [[#Llenando diccionarios de manera incremental#1. Asignar claves manualmente|1. Asignar claves manualmente]]
	- [[#Llenando diccionarios de manera incremental#2. Añadir claves en una estructura iterativa|2. Añadir claves en una estructura iterativa]]
	- [[#Llenando diccionarios de manera incremental#3. Construir un diccionario con comprensión|3. Construir un diccionario con comprensión]]
- [[#Explorando la clase `dict`|Explorando la clase `dict`]]
	- [[#Explorando la clase `dict`#Obtener valores individuales con `.get(clave, default=None)`|Obtener valores individuales con `.get(clave, default=None)`]]
	- [[#Explorando la clase `dict`#Recuperando todos los valores con `.values()`|Recuperando todos los valores con `.values()`]]
	- [[#Explorando la clase `dict`#Accediendo a todas las claves con `.keys()`|Accediendo a todas las claves con `.keys()`]]
	- [[#Explorando la clase `dict`#Obteniendo todos los pares clave-valor con `.items()`|Obteniendo todos los pares clave-valor con `.items()`]]
	- [[#Explorando la clase `dict`#Configurando una clave con `.setdefault(clave, default=None)`|Configurando una clave con `.setdefault(clave, default=None)`]]
	- [[#Explorando la clase `dict`#Actualizando un diccionario con `.update([otro])`|Actualizando un diccionario con `.update([otro])`]]
	- [[#Explorando la clase `dict`#Quitando claves con `.pop(clave, [,default])`|Quitando claves con `.pop(clave, [,default])`]]
	- [[#Explorando la clase `dict`#Borrando items con `.popitem()`|Borrando items con `.popitem()`]]
	- [[#Explorando la clase `dict`#Limpiando diccionarios con `.clear()`|Limpiando diccionarios con `.clear()`]]
- [[#Usando operadores con diccionarios|Usando operadores con diccionarios]]
	- [[#Usando operadores con diccionarios#Sentencias `in` y `not in`|Sentencias `in` y `not in`]]
	- [[#Usando operadores con diccionarios#Igualdad y desigualdad: `==` y `!=`|Igualdad y desigualdad: `==` y `!=`]]
	- [[#Usando operadores con diccionarios#Unión y unión aumentada ` ` y ` =`]]
- [[#Usando funciones nativas con diccionarios|Usando funciones nativas con diccionarios]]
	- [[#Usando funciones nativas con diccionarios#Chequear datos con `all()` y `any()`|Chequear datos con `all()` y `any()`]]
	- [[#Usando funciones nativas con diccionarios#Determinar el número de items con `len()`|Determinar el número de items con `len()`]]
	- [[#Usando funciones nativas con diccionarios#Encontrando valores máximos y mínimos con `min()` y `max()`|Encontrando valores máximos y mínimos con `min()` y `max()`]]
	- [[#Usando funciones nativas con diccionarios#Ordenando elementos con `sorted()`|Ordenando elementos con `sorted()`]]
	- [[#Usando funciones nativas con diccionarios#Sumando valores con `sum()`|Sumando valores con `sum()`]]
- [[#Iterando a través de los diccionarios|Iterando a través de los diccionarios]]
	- [[#Iterando a través de los diccionarios#Iterando sobre las claves|Iterando sobre las claves]]
	- [[#Iterando a través de los diccionarios#Iterando sobre los valores|Iterando sobre los valores]]
	- [[#Iterando a través de los diccionarios#Iterando sobre los pares clave-valor|Iterando sobre los pares clave-valor]]
- [[#Explorando tipos especiales de diccionarios|Explorando tipos especiales de diccionarios]]
	- [[#Explorando tipos especiales de diccionarios#`Counter` para conteos eficientes|`Counter` para conteos eficientes]]
	- [[#Explorando tipos especiales de diccionarios#`defaultdict` para valores por defecto automáticos|`defaultdict` para valores por defecto automáticos]]
- [[#Creando tipos de diccionarios personalizados|Creando tipos de diccionarios personalizados]]
- [[#📊 Resumen de métodos importantes|📊 Resumen de métodos importantes]]
# Diccionarios en Python

Los **diccionarios** en Python son una parte fundamental y útil del lenguaje. Proporcionan una colección **mutable** de pares **clave-valor** que nos permite acceder de manera ultra eficiente y modificar valores a través de sus claves correspondientes.

```python
>>> config = {
...     "color": "green",
...     "width": 42,
...     "height": 100,
...     "font": "Courier",
... }

>>> # Acceder a un valor mediante su clave
>>> config["color"]
'green'

>>> # Actualizar un valor
>>> config["font"] = "Helvetica"
>>> config
{
    'color': 'green',
    'width': 42,
    'height': 100,
    'font': 'Helvetica'
}
```

Como dijimos, los diccionarios son una parte fundamental del lenguaje. Los encuentras en conceptos clave como los **scopes** y los **namespaces**:

```python
>>> globals()
{
    '__name__': '__main__',
    '__doc__': None,
    '__package__': None,
    ...
}
```

Además, Python soporta el uso de diccionarios mediante objetos:

```python
>>> class Numero:
...     def __init__(self, valor):
...         self.valor = valor
...

>>> Numero(42).__dict__
{'valor': 42}
```

## Características de los diccionarios

- **Mutables**: Los diccionarios pueden modificar el objeto original que contiene sus valores
- **Dinámicos**: Los diccionarios pueden crecer y disminuir en cantidad según lo que se necesite
- **Eficientes**: Los diccionarios implementan la estructura de datos **Hashing**, por lo que su acceso a los elementos es extremadamente rápido
- **Ordenados**: Al igual que otras colecciones de datos, los diccionarios mantienen el orden en que se insertan los elementos (desde Python 3.6)

A pesar de estas ventajas, los diccionarios tienen algunas restricciones:

- **Hasheables**: Las claves deben poder ser hasheadas, lo que significa que **no pueden ser mutables**
- **Únicas**: Los diccionarios no permiten claves duplicadas (por el mismo motivo del hash)

## Creando diccionarios en Python

### Diccionarios literales

Puedes definir un diccionario separando claves y valores con comas, encerrados entre llaves `{}`. Para especificar que un valor pertenece a una clave, usas dos puntos `:`:

```python
{
    <clave_1>: <valor_1>,
    <clave_2>: <valor_2>,
      ...,
    <clave_N>: <valor_N>,
}
```

Las claves y valores pueden ser opcionales si buscas crear diccionarios vacíos. Solo usa llaves sin especificar contenido:

```python
>>> diccionario_vacio = {}
```

**¿Cómo sabemos que un objeto es hasheable?** Un objeto es **hasheable** cuando es **inmutable**. Esto es una condición necesaria porque Python calcula el hash basándose en el estado del objeto. Si el objeto cambia (es mutable), su hash también cambiaría, causando problemas en la estructura del diccionario.

Ejemplos de diccionarios:

```python
>>> equipos_MLB = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Boston": "Red Sox",
...     "Minnesota": "Twins",
...     "Milwaukee": "Brewers",
...     "Seattle": "Mariners",
... }
```

Incluso puedes usar tipos de datos como claves:

```python
>>> tipos = {int: 1, float: 2, bool: 3}
>>> tipos
{<class 'int'>: 1, <class 'float'>: 2, <class 'bool'>: 3}

>>> tipos[float]
2
>>> tipos[bool]
3
```

**¡Error común!** No puedes usar listas como claves (son mutables):

```python
>>> {[1, 2]: "¿Una lista como clave? Mmm..."}
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'list'
```

Si necesitas usar varios elementos como clave, puedes usar [[Tuplas en Python#Explorando la inmutabilidad|tuplas]] ya que son inmutables.

Otra restricción es que las claves deben ser **únicas**. Si una clave se repite, la segunda aparición reemplaza a la primera:

```python
>>> equipos_MLB = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Chicago": "Cubs",  # ¡Sobrescribe "White Sox"!
...     "Boston": "Red Sox",
... }

>>> equipos_MLB
{
    'Colorado': 'Rockies',
    'Chicago': 'Cubs',  # "White Sox" no está presente
    'Boston': 'Red Sox',
}
```

Aunque las claves tienen restricciones, **los valores no tienen prácticamente ninguna**. Pueden ser listas, objetos mutables, sets, enteros, strings, lo que quieras:

```python
>>> class Punto:
...     def __init__(self, x, y):
...         self.x = x
...         self.y = y
...

>>> datos = {
...     "colores": ["rojo", "verde", "azul"],
...     "plugins": {"py_code", "dev_sugar", "fasting_py"},
...     "timeout": 3,
...     "posicion": Punto(42, 21),
... }
```

### Usando el constructor `dict()`

Otra forma de crear diccionarios es con su constructor `dict()`. Sus argumentos pueden ser una serie de palabras clave, mappings o iterables clave-valor:

```python
dict()
dict(**kwargs)
dict(mapping, **kwargs)
dict(iterable, **kwargs)
```

Si llamas a `dict()` sin argumentos, obtienes un diccionario vacío:

```python
>>> dict()
{}
```

Si los argumentos son [[Sintaxis Basica Python#Identificadores|identificadores Python]] válidos, obtienes un diccionario:

```python
>>> equipos_MLB = dict(
...     Colorado="Rockies",
...     Chicago="White Sox",
...     Boston="Red Sox",
...     Minnesota="Twins",
...     Milwaukee="Brewers",
...     Seattle="Mariners",
... )
```

También puedes usar una lista de tuplas:

```python
>>> equipos_MLB = dict(
...     [
...         ("Colorado", "Rockies"),
...         ("Chicago", "White Sox"),
...         ("Boston", "Red Sox"),
...         ("Minnesota", "Twins"),
...         ("Milwaukee", "Brewers"),
...         ("Seattle", "Mariners"),
...     ]
... )
```

Incluso puedes combinar listas con [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|zip()]] para unir dos iterables:

```python
>>> lugares = ["Colorado", "Chicago", "Boston", "Minnesota", "Milwaukee", "Seattle"]
>>> equipos = ["Rockies", "White Sox", "Red Sox", "Twins", "Brewers", "Mariners"]

>>> dict(zip(lugares, equipos))
{
    'Colorado': 'Rockies',
    'Chicago': 'White Sox',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle': 'Mariners'
}
```

### Usando `.fromkeys()`

Este método nos permite crear un nuevo diccionario a partir de un iterable con valores por defecto:

```python
.fromkeys(iterable, valor=None, /)
```

```python
>>> inventario = dict.fromkeys(["manzana", "naranja", "banana", "mango"], 0)

>>> inventario
{'manzana': 0, 'naranja': 0, 'banana': 0, 'mango': 0}
```

## Accediendo a los valores de un diccionario

Una vez creado el diccionario, puedes acceder a su contenido mediante las claves. Para especificar un valor, llama al diccionario seguido de `[]` con el nombre de la clave:

```python
>>> equipos_MLB["Minnesota"]
'Twins'
>>> equipos_MLB["Colorado"]
'Rockies'
```

Si no proporcionas una clave válida, Python lanzará una excepción:

```python
>>> equipos_MLB["Indianapolis"]
Traceback (most recent call last):
    ...
KeyError: 'Indianapolis'
```

Para acceder a elementos anidados (listas, diccionarios dentro del diccionario), combina los accesos:

```python
>>> persona = {
...     "nombre": "Juan",
...     "edad": 35,
...     "hijos": ["Ralph", "Betty", "Bob"],
...     "mascotas": {"perro": "Frieda", "gato": "Sox"},
... }

>>> persona["hijos"][0]
'Ralph'
>>> persona["hijos"][2]
'Bob'

>>> persona["mascotas"]["perro"]
'Frieda'
>>> persona["mascotas"]["gato"]
'Sox'
```

## Llenando diccionarios de manera incremental

Los diccionarios son estructuras de datos **dinámicas**. Puedes añadir pares clave-valor de manera dinámica, y Python se encarga de ajustar el tamaño del diccionario.

### 1. Asignar claves manualmente

A veces necesitas crear un diccionario vacío e ir asignando valores según el flujo del programa:

```python
>>> persona = {}

>>> persona["nombre"] = "Juan"
>>> persona["apellido"] = "Pérez"
>>> persona["edad"] = 35
>>> persona["cónyuge"] = "María"
>>> persona["hijos"] = ["Ralph", "Betty", "Bob"]
>>> persona["mascotas"] = {"perro": "Frieda", "gato": "Sox"}

>>> persona
{
    'nombre': 'Juan',
    'apellido': 'Pérez',
    'edad': 35,
    'cónyuge': 'María',
    'hijos': ['Ralph', 'Betty', 'Bob'],
    'mascotas': {'perro': 'Frieda', 'gato': 'Sox'}
}
```

Si la clave ya existe, se sobrescribe el valor.

### 2. Añadir claves en una estructura iterativa

Puedes aprovechar las estructuras iterativas para añadir pares clave-valor:

```python
>>> cuadrados = {}

>>> for entero in range(1, 10):
...     cuadrados[entero] = entero**2
...

>>> cuadrados
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### 3. Construir un diccionario con comprensión

Python tiene **comprensión de diccionarios**, una herramienta concisa para crear diccionarios:

```python
>>> cuadrados = {entero: entero**2 for entero in range(1, 10)}
>>> cuadrados
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## Explorando la clase `dict`

Los diccionarios tienen varios métodos para realizar diferentes acciones como acceder a claves, valores e items, así como actualizar o eliminar valores.

### Obtener valores individuales con `.get(clave, default=None)`

El método `.get()` proporciona una manera conveniente de recuperar valores sin tener que verificar si la clave existe:

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}

>>> inventario.get("manzana")
100
>>> print(inventario.get("mango"))
None
```

Puedes personalizar el valor por defecto:

```python
>>> inventario.get("mango", 0)
0
```

### Recuperando todos los valores con `.values()`

El método `.values()` retorna una vista dinámica de los valores en el diccionario:

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}

>>> inventario.values()
dict_values([100, 80, 100])  # Los valores duplicados se incluyen
```

### Accediendo a todas las claves con `.keys()`

Similar a `.values()`, pero para claves:

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}

>>> inventario.keys()
dict_keys(['manzana', 'naranja', 'banana'])
```

### Obteniendo todos los pares clave-valor con `.items()`

Retorna tuplas (clave, valor):

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}

>>> inventario.items()
dict_items([('manzana', 100), ('naranja', 80), ('banana', 100)])
```

### Configurando una clave con `.setdefault(clave, default=None)`

Crea una clave con valor por defecto si no existe, o retorna el valor existente:

```python
>>> inventario = {"manzana": 100, "naranja": 80}

>>> inventario.setdefault("manzana")
100
>>> print(inventario.setdefault("mango"))
None
>>> inventario
{'manzana': 100, 'naranja': 80, 'mango': None}
>>> inventario.setdefault("banana", 0)
0
>>> inventario
{'manzana': 100, 'naranja': 80, 'mango': None, 'banana': 0}
```

### Actualizando un diccionario con `.update([otro])`

El método `.update()` fusiona un diccionario con otro diccionario o con un iterable de pares clave-valor:

```python
>>> config = {
...     "color": "verde",
...     "ancho": 42,
...     "alto": 100,
...     "fuente": "Courier",
... }

>>> config_usuario = {
...     "ruta": "/home",
...     "color": "rojo",  # ¡Sobrescribe "verde"!
...     "fuente": "Arial",
...     "posicion": (200, 100),
... }

>>> config.update(config_usuario)

>>> config
{
    'color': 'rojo',
    'ancho': 42,
    'alto': 100,
    'fuente': 'Arial',
    'ruta': '/home',
    'posicion': (200, 100)
}
```

### Quitando claves con `.pop(clave, [,default])`

Elimina un par clave-valor y retorna el valor:

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}

>>> inventario.pop("manzana")
100
>>> inventario
{'naranja': 80, 'banana': 100}

>>> inventario.pop("mango")
Traceback (most recent call last):
    ...
KeyError: 'mango'

>>> inventario.pop("mango", 0)  # Con valor por defecto
0
```

### Borrando items con `.popitem()`

Elimina y retorna un par clave-valor en orden LIFO (Last In, First Out):

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}

>>> inventario.popitem()
('banana', 100)
>>> inventario
{'manzana': 100, 'naranja': 80}

>>> inventario.popitem()
('naranja', 80)
>>> inventario
{'manzana': 100}

>>> inventario.popitem()
('manzana', 100)
>>> inventario
{}
```

Si el diccionario está vacío:

```python
>>> inventario.popitem()
Traceback (most recent call last):
    ...
KeyError: 'popitem(): dictionary is empty'
```

### Limpiando diccionarios con `.clear()`

Elimina todos los items de un diccionario:

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100}
>>> inventario.clear()
>>> inventario
{}
```

## Usando operadores con diccionarios

### Sentencias `in` y `not in`

Permiten verificar si una clave, valor o par está en un diccionario:

```python
>>> equipos_MLB = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Boston": "Red Sox",
... }

>>> "Chicago" in equipos_MLB
True
>>> "Indianapolis" in equipos_MLB
False
>>> "Indianapolis" not in equipos_MLB
True

# Verificar en claves explícitamente
>>> "Chicago" in equipos_MLB.keys()
True

# Verificar en valores
>>> "Rockies" in equipos_MLB.values()
True

# Verificar pares clave-valor
>>> ("Boston", "Red Sox") in equipos_MLB.items()
True
```

### Igualdad y desigualdad: `==` y `!=`

Los diccionarios son iguales si tienen los mismos pares clave-valor, **sin importar el orden**:

```python
>>> {1: 1, 2: 2, 3: 3} == {3: 3, 2: 2, 1: 1}
True

>>> {1: 1, 2: 2, 3: 3} != {3: 3, 2: 2, 1: 1}
False
```

### Unión y unión aumentada: `|` y `|=`

El operador `|` crea un nuevo diccionario combinando dos diccionarios. Los valores del diccionario de la derecha sobrescriben los del de la izquierda en caso de claves repetidas:

```python
>>> config_predeterminada = {
...     "color": "verde",
...     "ancho": 42,
...     "alto": 100,
...     "fuente": "Courier",
... }

>>> config_usuario = {
...     "ruta": "/home",
...     "color": "rojo",  # ¡Sobrescribe "verde"!
...     "fuente": "Arial",
...     "posicion": (200, 100),
... }

>>> config = config_predeterminada | config_usuario
>>> config
{
    'color': 'rojo',
    'ancho': 42,
    'alto': 100,
    'fuente': 'Arial',
    'ruta': '/home',
    'posicion': (200, 100)
}
```

El operador `|=` funciona como `+=`, actualizando el diccionario original:

```python
>>> config = {
...     "color": "verde",
...     "ancho": 42,
...     "alto": 100,
...     "fuente": "Courier",
... }

>>> config |= config_usuario  # Equivalente a: config = config | config_usuario
>>> config
{
    'color': 'rojo',
    'ancho': 42,
    'alto': 100,
    'fuente': 'Arial',
    'ruta': '/home',
    'posicion': (200, 100)
}
```

## Usando funciones nativas con diccionarios

Python tiene varias funciones nativas que funcionan con diccionarios:

| Función | Descripción |
|---------|-------------|
| `all()` | Retorna `True` si todos los elementos en un iterable son verdaderos |
| `any()` | Retorna `True` si al menos un elemento en el iterable es verdadero |
| `len()` | Retorna el número de items en el diccionario |
| `max()` | Retorna el valor más grande |
| `min()` | Retorna el valor más pequeño |
| `sorted()` | Retorna una nueva lista ordenada de los elementos |
| `sum()` | Retorna la suma de los valores |

### Chequear datos con `all()` y `any()`

Útil para verificar si todos o algunos valores son verdaderos:

```python
>>> inventario = {"manzana": 100, "naranja": 80, "banana": 100, "mango": 200}

>>> all(inventario.values())
True

>>> inventario["mango"] = 0
>>> all(inventario.values())
False
```

### Determinar el número de items con `len()`

```python
>>> equipos_MLB = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Boston": "Red Sox",
... }

>>> len(equipos_MLB)
3
```

### Encontrando valores máximos y mínimos con `min()` y `max()`

```python
>>> partes_computadora = {
...     "CPU": 299.99,
...     "Motherboard": 149.99,
...     "RAM": 89.99,
...     "GPU": 499.99,
...     "SSD": 129.99,
... }

>>> min(partes_computadora.values())
89.99
>>> max(partes_computadora.values())
499.99
```

### Ordenando elementos con `sorted()`

```python
>>> estudiantes = {
...     "Alice": 89.5,
...     "Bob": 76.0,
...     "Charlie": 92.3,
...     "Diana": 84.7,
... }

# Ordenar por valores (notas)
>>> dict(sorted(estudiantes.items(), key=lambda item: item[1]))
{
    'Bob': 76.0,
    'Diana': 84.7,
    'Alice': 89.5,
    'Charlie': 92.3
}

# Ordenar por valores en orden inverso
>>> dict(sorted(estudiantes.items(), key=lambda item: item[1], reverse=True))
{
    'Charlie': 92.3,
    'Alice': 89.5,
    'Diana': 84.7,
    'Bob': 76.0
}
```

### Sumando valores con `sum()`

```python
>>> ventas_diarias = {
...     "Lunes": 1500,
...     "Martes": 1750,
...     "Miércoles": 1600,
... }

>>> sum(ventas_diarias.values()) / len(ventas_diarias)
1616.6666666666667  # Promedio diario
```

## Iterando a través de los diccionarios

### Iterando sobre las claves

Hay dos formas equivalentes:

```python
>>> estudiantes = {
...     "Alice": 89.5,
...     "Bob": 76.0,
...     "Charlie": 92.3,
... }

# Forma 1: Directamente (por defecto itera sobre claves)
>>> for estudiante in estudiantes:
...     print(estudiante)
...
Alice
Bob
Charlie

# Forma 2: Explícitamente con .keys()
>>> for estudiante in estudiantes.keys():
...     print(estudiante)
...
Alice
Bob
Charlie
```

Para acceder a los valores mientras iteras por claves:

```python
>>> for estudiante in estudiantes:
...     print(estudiante, "->", estudiantes[estudiante])
...
Alice -> 89.5
Bob -> 76.0
Charlie -> 92.3
```

### Iterando sobre los valores

Usa `.values()`:

```python
>>> equipos_MLB = {
...     "Colorado": "Rockies",
...     "Chicago": "White Sox",
...     "Boston": "Red Sox",
... }

>>> for equipo in equipos_MLB.values():
...     print(equipo)
...
Rockies
White Sox
Red Sox
```

### Iterando sobre los pares clave-valor

Usa `.items()` para obtener ambos a la vez:

```python
>>> for lugar, equipo in equipos_MLB.items():
...     print(lugar, "->", equipo)
...
Colorado -> Rockies
Chicago -> White Sox
Boston -> Red Sox
```

## Explorando tipos especiales de diccionarios

En el módulo `collections` encontrarás tipos especializados de diccionarios:

| Clase | Descripción |
|-------|-------------|
| `OrderedDict` | Diccionario que recuerda el orden de inserción (ya menos útil desde Python 3.6) |
| `Counter` | Diccionario especializado para contar objetos eficientemente |
| `defaultdict` | Diccionario que maneja claves faltantes automáticamente |

### `Counter` para conteos eficientes

```python
>>> from collections import Counter

>>> Counter("mississippi")
Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

### `defaultdict` para valores por defecto automáticos

Útil cuando quieres agrupar valores por una clave:

```python
>>> empleados = [
...     ("Ventas", "Juan"),
...     ("Ventas", "Martín"),
...     ("Contabilidad", "Catalina"),
...     ("Marketing", "Elizabeth"),
...     ("Marketing", "Linda"),
... ]

>>> from collections import defaultdict

>>> departamentos = defaultdict(list)  # Lista vacía por defecto

>>> for departamento, empleado in empleados:
...     departamentos[departamento].append(empleado)
...

>>> departamentos
defaultdict(<class 'list'>,
    {
        'Ventas': ['Juan', 'Martín'],
        'Contabilidad': ['Catalina'],
        'Marketing': ['Elizabeth', 'Linda']
    }
)
```

## Creando tipos de diccionarios personalizados

Puedes crear diccionarios personalizados heredando de:
1. La clase nativa `dict` (puede tener problemas)
2. `collections.UserDict` (más confiable)

Ejemplo: un diccionario que se ordena automáticamente:

```python
class DiccionarioOrdenable(dict):
    def ordenar_por_claves(self, inverso=False):
        items_ordenados = sorted(
            self.items(),
            key=lambda item: item[0],
            reverse=inverso
        )
        self.clear()
        self.update(items_ordenados)

    def ordenar_por_valores(self, inverso=False):
        items_ordenados = sorted(
            self.items(),
            key=lambda item: item[1],
            reverse=inverso
        )
        self.clear()
        self.update(items_ordenados)

# Uso
>>> estudiantes = DiccionarioOrdenable(
...     {
...         "Alice": 89.5,
...         "Bob": 76.0,
...         "Charlie": 92.3,
...     }
... )

>>> id(estudiantes)  # Guarda el ID del objeto
4350960304

>>> estudiantes.ordenar_por_valores(inverso=True)
>>> estudiantes
{
    'Charlie': 92.3,
    'Alice': 89.5,
    'Bob': 76.0
}

>>> id(estudiantes)  # ¡Mismo objeto, diferente orden!
4350960304
```

## 📊 Resumen de métodos importantes

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `clear()` | Elimina todos los elementos | `d.clear()` |
| `copy()` | Retorna una copia superficial | `d2 = d.copy()` |
| `fromkeys()` | Crea diccionario con claves y valor por defecto | `dict.fromkeys(['a','b'], 0)` |
| `get()` | Retorna valor o default si no existe | `d.get('x', 0)` |
| `items()` | Vista de pares (clave, valor) | `for k,v in d.items()` |
| `keys()` | Vista de claves | `for k in d.keys()` |
| `pop()` | Elimina y retorna valor | `d.pop('x')` |
| `popitem()` | Elimina y retorna par (LIFO) | `d.popitem()` |
| `setdefault()` | Retorna valor, lo crea si no existe | `d.setdefault('x', 0)` |
| `update()` | Fusiona con otro diccionario | `d.update({'x':1})` |
| `values()` | Vista de valores | `for v in d.values()` |

---

**TE SIENTES DETERMINADO** 💪