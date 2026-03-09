---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-21T19:23:00
Revision: 2026-01-22T18:29:00
---
# Tabla de Contenidos

- [[#Características de las tuplas|Características de las tuplas]]
- [[#Construyendo tuplas en Python|Construyendo tuplas en Python]]
	- [[#Construyendo tuplas en Python#Creando tuplas literales|Creando tuplas literales]]
	- [[#Construyendo tuplas en Python#Usando `tuple()`|Usando `tuple()`]]
- [[#Accediendo a los elementos en una tupla: Indexación|Accediendo a los elementos en una tupla: Indexación]]
- [[#Obteniendo múltiples elementos desde una tupla: *Slicing*|Obteniendo múltiples elementos desde una tupla: *Slicing*]]
- [[#Explorando la inmutabilidad|Explorando la inmutabilidad]]
- [[#Empaquetado y desempaquetado de tuplas|Empaquetado y desempaquetado de tuplas]]
- [[#Retornando tuplas desde funciones|Retornando tuplas desde funciones]]
- [[#Creando copias de una tupla|Creando copias de una tupla]]
- [[#Concatenando y repitiendo tuplas|Concatenando y repitiendo tuplas]]
	- [[#Concatenando y repitiendo tuplas#Concatenando tuplas|Concatenando tuplas]]
	- [[#Concatenando y repitiendo tuplas#Repitiendo contenido de una tupla|Repitiendo contenido de una tupla]]
- [[#Invertir y ordenar tuplas|Invertir y ordenar tuplas]]
	- [[#Invertir y ordenar tuplas#Invertir tuplas con `reversed()`|Invertir tuplas con `reversed()`]]
	- [[#Invertir y ordenar tuplas#Invertir una tupla con rebanado|Invertir una tupla con rebanado]]
	- [[#Invertir y ordenar tuplas#Ordenar una tupla con `sorted()`|Ordenar una tupla con `sorted()`]]
- [[#Iterando sobre las tuplas en Python|Iterando sobre las tuplas en Python]]
	- [[#Iterando sobre las tuplas en Python#Usando un bucle|Usando un bucle]]
	- [[#Iterando sobre las tuplas en Python#Usar expresiones generadoras|Usar expresiones generadoras]]
- [[#Explorando otras características de las tuplas|Explorando otras características de las tuplas]]
	- [[#Explorando otras características de las tuplas#`.count()`|`.count()`]]
	- [[#Explorando otras características de las tuplas#`.index()`|`.index()`]]
	- [[#Explorando otras características de las tuplas#Encontrando elementos en una tupla|Encontrando elementos en una tupla]]
	- [[#Explorando otras características de las tuplas#Obteniendo la longitud de una tupla|Obteniendo la longitud de una tupla]]
	- [[#Explorando otras características de las tuplas#Comparando tuplas|Comparando tuplas]]
- [[#Errores comunes usando tuplas en Python|Errores comunes usando tuplas en Python]]
	- [[#Errores comunes usando tuplas en Python#Error 1: Tupla de un solo elemento|Error 1: Tupla de un solo elemento]]
	- [[#Errores comunes usando tuplas en Python#Error 2: Hashabilidad y objetos mutables|Error 2: Hashabilidad y objetos mutables]]
- [[#Usando alternativas a las tuplas nativas|Usando alternativas a las tuplas nativas]]
	- [[#Usando alternativas a las tuplas nativas#Tuplas con campos nombrados: `collections.namedtuple`|Tuplas con campos nombrados: `collections.namedtuple`]]
	- [[#Usando alternativas a las tuplas nativas#Tuplas con campos nombrados y sugerencias de tipo: `typing.NamedTuple`|Tuplas con campos nombrados y sugerencias de tipo: `typing.NamedTuple`]]
	- [[#Usando alternativas a las tuplas nativas#Clases de datos: `dataclasses.dataclass`|Clases de datos: `dataclasses.dataclass`]]
- [[#¿Deberías usar las tuplas?|¿Deberías usar las tuplas?]]
	- [[#¿Deberías usar las tuplas?#Ejemplos de casos de uso|Ejemplos de casos de uso]]
# Tuplas en Python

Las **tuplas** son un tipo de dato especial de Python. Son de tipo **inmutable**, lo cual es la principal diferencia con las [[Listas en Python#Mutabilidad: La característica clave|Listas]] que son mutables.

## Características de las tuplas

- **Ordenadas**: Los elementos mantienen el orden en que fueron insertados
- **Livianas**: Consumen relativamente poca memoria comparadas con otras secuencias como las listas
- **Indexables desde 0**: Permiten acceder a elementos usando índices que empiezan desde 0
- **Inmutables**: Una vez creadas, no pueden modificarse
- **Heterogéneas**: Pueden almacenar objetos de diferentes tipos
- **Anidables**: Pueden contener otras tuplas (tuplas de tuplas)
- **Iterables**: Se pueden recorrer con bucles
- **Sliceables**: Soporta operaciones de rebanado (*slicing*)
- **Combinables**: Soportan operación de concatenación
- **Hasheables**: Pueden funcionar como claves en diccionarios (si todos sus elementos son inmutables)

Las tuplas son colecciones de objetos, comúnmente llamadas contenedores, porque una sola tupla puede contener un número arbitrario de otros objetos.

## Construyendo tuplas en Python

Las tuplas, al igual que las listas, tienen elementos separados por comas, pero se encierran entre paréntesis. También existe la función `tuple()` para crearlas.

### Creando tuplas literales

Las tuplas literales son probablemente la forma más común de crearlas:

```python
item_0, item_1, ..., item_n
# o
(item_0, item_1, ..., item_n)
```

Aunque los paréntesis no son requeridos, ayudan a la legibilidad del código:

```python
>>> jane = ("Jane Doe", 25, 1.75, "Canada")
>>> point = (2, 7)
>>> pen = (2, "Solid", True)

>>> days = (
...     "Monday",
...     "Tuesday",
...     "Wednesday",
...     "Thursday",
...     "Friday",
...     "Saturday",
...     "Sunday",
... )
```

Aunque no sean requeridos, colocar paréntesis a elementos separados por comas hará que automáticamente sean tuplas:

```python
>>> empty = ()
>>> empty
()
>>> type(empty)
<class 'tuple'>

>>> "Hello, %s! You're %s years old." % ("Linda", 24)
'Hello, Linda! You're 24 years old.'

>>> "Hello, %s! You're %s years old." % "Linda", 24
Traceback (most recent call last):
    ...
TypeError: not enough arguments for format string
```

### Usando `tuple()`

La función `tuple()` es el constructor para crear objetos de tipo tupla desde un iterable (lista, diccionario, string, etc.). Si se llama sin argumentos, crea una tupla vacía:

```python
tuple([iterable])
```

```python
>>> tuple(["Jane Doe", 25, 1.75, "Canada"])
('Jane Doe', 25, 1.75, 'Canada')

>>> tuple("Pythonista")
('P', 'y', 't', 'h', 'o', 'n', 'i', 's', 't', 'a')

>>> tuple({
...     "manufacturer": "Boeing",
...     "model": "747",
...     "passengers": 416,
... }.values())
('Boeing', '747', 416)

>>> tuple()
()
```

También se pueden crear tuplas mediante expresiones generadoras:

```python
>>> tuple(x**2 for x in range(10))
(0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
```

**Nota**: Para crear una expresión generadora independiente, necesitas un par de paréntesis que la encierre. En el ejemplo anterior, los paréntesis requeridos son proporcionados por la llamada a `tuple()`.

## Accediendo a los elementos en una tupla: Indexación

Puedes extraer los elementos de una tupla accediendo mediante sus índices, exactamente igual que con las [[Listas en Python#Indexación y *Slicing* (rebanado)|Listas]]:

```python
>>> jane = ("Jane Doe", 25, 1.75, "Canada")

>>> jane[0]
'Jane Doe'
>>> jane[1]
25
>>> jane[3]
'Canada'
```

Incluso se puede usar `len()`:

```python
>>> len(jane)
4
```

Lo mismo ocurre con tuplas de tuplas:

```python
>>> employee = (
...     "John",
...     35,
...     "Python Developer",
...     ("Django", "Flask", "FastAPI", "CSS", "HTML"),
... )

>>> employee[-1][0]
'Django'

>>> employee[-1][1]
'Flask'
```

## Obteniendo múltiples elementos desde una tupla: *Slicing*

Como otras secuencias en Python, las tuplas soportan operaciones de rebanado (*slicing*):

```python
tupla[inicio:fin:paso]
```

| Parámetro | Descripción | Valor por Defecto |
|-----------|-------------|-------------------|
| `inicio` | Índice donde comienza el rebanado (incluido) | `0` |
| `fin` | Índice donde termina el rebanado (no incluido) | `len(tupla)` |
| `paso` | Cada cuántos elementos saltar | `1` |

```python
>>> days = (
...     "Monday",
...     "Tuesday",
...     "Wednesday",
...     "Thursday",
...     "Friday",
...     "Saturday",
...     "Sunday",
... )

>>> days[:5]
('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

>>> days[5:]
('Saturday', 'Sunday')
```

## Explorando la inmutabilidad

Como mencionamos, las tuplas son **inmutables**, lo que significa que una vez que creas la tupla no puedes cambiar o actualizar los elementos originales. Esta característica implica que no puedes usar índices para modificar los elementos existentes en una tupla.

```python
>>> jane = ("Jane Doe", 25, 1.75, "Canada")

>>> jane[3] = "United States"
Traceback (most recent call last):
    ...
TypeError: 'tuple' object does not support item assignment
```

Las tuplas no poseen los métodos de modificación que tienen las listas como `.append()`, `.extend()`, `.insert()`, etc.

Tampoco soportan la instrucción `del` para eliminar elementos:

```python
>>> point = (7, 14, 21)

>>> del point[2]
Traceback (most recent call last):
    ...
TypeError: 'tuple' object doesn't support item deletion
```

## Empaquetado y desempaquetado de tuplas

Cuando escribes una instrucción como `punto = x, y, z`, estás **empaquetando** valores en una tupla. El proceso inverso se llama **desempaquetado**:

```python
>>> point = (7, 14, 21)

>>> x, y, z = point
>>> x
7
>>> y
14
>>> z
21
```

**¡Cuidado!** El número de variables debe coincidir con el número de elementos:

```python
>>> point = (7, 14, 21)

>>> x, y = point
Traceback (most recent call last):
    ...
ValueError: too many values to unpack (expected 2)
```

Más ejemplos:

```python
>>> name, age, job = ("John Doe", 35, "Python Developer")
```

También se puede usar el operador `*` para hacer el desempaquetado más flexible:

```python
>>> numbers = (1, 2, 3, 4, 5)

>>> *head, last = numbers
>>> head
[1, 2, 3, 4]
>>> last
5

>>> first, *middle, last = numbers
>>> first
1
>>> middle
[2, 3, 4]
>>> last
5

>>> first, second, *tail = numbers
>>> first
1
>>> second
2
>>> tail
[3, 4, 5]

>>> first, *_ = numbers
>>> first
1
```

Un uso interesante es unir tuplas:

```python
>>> name = ("John", "Doe")
>>> contact = ("john@example.com", "55-555-5555")

>>> (*name, *contact)
('John', 'Doe', 'john@example.com', '55-555-5555')
```

## Retornando tuplas desde funciones

En algunas situaciones necesitas retornar varios valores de una función. En el `return` puedes separar los elementos por comas y se [[Funciones en Python#2. Retornando valores explícitos|retornará]] un objeto tupla:

```python
>>> def find_extremes(iterable):
...     data = tuple(iterable)
...     if len(data) == 0:
...         raise ValueError("input iterable must not be empty")
...     return min(data), max(data)
...

>>> extremes = find_extremes([3, 4, 2, 6, 7, 1, 9])
>>> extremes
(1, 9)

>>> type(extremes)
<class 'tuple'>
```

## Creando copias de una tupla

Generalmente quieres hacer copias de un objeto cuando necesitas transformar datos mientras preservas los originales sin cambiarlos. Las copias son útiles con tipos de datos mutables que son propensos a modificarse por error.

Como las tuplas son inmutables, no hay manera de mutar el objeto original, así que crear copias de una tupla es innecesario en muchos casos. Además, Python trabaja con referencias, por lo que al crear una tupla y rebanar sus elementos, los elementos contenidos dentro de la tupla (si son mutables) seguirán siendo referencias compartidas.

Para crear copias verdaderamente independientes de tuplas con elementos mutables internos, necesitarías realizar una [[Listas en Python#🔍 Copia Superficial vs. Copia Profunda: Explicación Detallada|copia profunda]].

## Concatenando y repitiendo tuplas

Al igual que las listas y los strings, las tuplas soportan la concatenación y la repetición.

### Concatenando tuplas

La concatenación consiste en unir dos tuplas usando el operador `+`:

```python
>>> personal_info = ("John", 35)
>>> professional_info = ("Computer science", ("Python", "Django", "Flask"))

>>> profile = personal_info + professional_info
>>> profile
('John', 35, 'Computer science', ('Python', 'Django', 'Flask'))
```

**¡Ojo!** Las tuplas solo pueden ser concatenadas con otras tuplas.

También existe la versión con `+=`:

```python
>>> profile = ("John", 35)
>>> id(profile)
4420700928

>>> profile += ("Computer science", ("Python", "Django", "Flask"))
>>> id(profile)
4406635200

>>> profile
('John', 35, 'Computer science', ('Python', 'Django', 'Flask'))
```

Esta forma de concatenar crea una **nueva tupla** con diferente identidad (ID).

### Repitiendo contenido de una tupla

La repetición clona el contenido de una tupla un número específico de veces usando el operador `*`:

```python
>>> numbers = (1, 2, 3)

>>> numbers * 3
(1, 2, 3, 1, 2, 3, 1, 2, 3)

>>> 4 * numbers
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
```

También tiene su variante con `*=`:

```python
>>> numbers = (1, 2, 3)
>>> id(numbers)
4407400448

>>> numbers *= 3
>>> numbers
(1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> id(numbers)
4407458624
```

Como se puede ver, esta asignación crea otro objeto con diferente ID debido a la inmutabilidad.

## Invertir y ordenar tuplas

En Python existen las funciones [[Funciones Nativas en Python#**Iteradores y Secuencias**|`reversed()`]] y [[Funciones Nativas en Python#**2. Ordenamiento personalizado con `sorted()`**|`sorted()`]] que también pueden usarse con las tuplas.

### Invertir tuplas con `reversed()`

```python
>>> days = (
...     "Monday",
...     "Tuesday",
...     "Wednesday",
...     "Thursday",
...     "Friday",
...     "Saturday",
...     "Sunday",
... )

>>> reversed(days)
<reversed object at 0x107032b90>

>>> tuple(reversed(days))
(
    'Sunday',
    'Saturday',
    'Friday',
    'Thursday',
    'Wednesday',
    'Tuesday',
    'Monday'
)
```

Cuando llamas a `reversed()` obtienes un objeto iterador que contiene los elementos en orden inverso. Por eso necesitas especificar el tipo de dato con `tuple()` para consumir el iterador y crear una tupla a partir de él.

### Invertir una tupla con rebanado

Otra forma de invertir una tupla es usando el rebanado con paso `-1`:

```python
>>> reversed_days = days[::-1]

>>> reversed_days
(
    'Sunday',
    'Saturday',
    'Friday',
    'Thursday',
    'Wednesday',
    'Tuesday',
    'Monday'
)

>>> id(days) == id(reversed_days)
False
```

### Ordenar una tupla con `sorted()`

Las tuplas, como otros tipos de datos, soportan la función `sorted()`:

```python
>>> numbers = (2, 9, 5, 1, 6)

>>> sorted(numbers)
[1, 2, 5, 6, 9]
```

Es importante notar que `sorted()` retorna una **lista** en vez de un iterador como hace `reversed()`.

Para ordenar una tupla, los elementos deben ser del mismo tipo o comparables entre sí:

```python
>>> employee = ("John Doe", 35, "Python Developer")

>>> sorted(employee)
Traceback (most recent call last):
    ...
TypeError: '<' not supported between instances of 'int' and 'str'
```

También puedes ordenar en orden inverso:

```python
>>> numbers = (2, 9, 5, 1, 6)

>>> sorted(numbers, reverse=True)
[9, 6, 5, 2, 1]
```

O usando una función `key`:

```python
>>> fruits = (("apple", 0.40), ("banana", 0.25), ("orange", 0.35))

>>> sorted(fruits, key=lambda fruit: fruit[1])
[('banana', 0.25), ('orange', 0.35), ('apple', 0.4)]
```

## Iterando sobre las tuplas en Python

### Usando un bucle

```python
>>> monthly_incomes = (
...     ("January", 5000),
...     ("February", 5500),
...     ("March", 6000),
...     ("April", 5800),
...     ("May", 6200),
...     ("June", 7000),
...     ("July", 7500),
...     ("August", 7300),
...     ("September", 6800),
...     ("October", 6500),
...     ("November", 6000),
...     ("December", 5500)
... )

>>> total_income = 0
>>> for income in monthly_incomes:
...     total_income += income[1]
...

>>> total_income
75100
```

En este caso la variable `income` tomará cada tupla en cada iteración y con el índice `[1]` se accede al segundo elemento de cada tupla.

Otra forma es desempaquetando en el bucle:

```python
>>> quarter_income = 0

>>> for index, (month, income) in enumerate(monthly_incomes, start=1):
...     print(f"{month:>10}: {income}")
...     quarter_income += income
...     if index % 3 == 0:
...         print("-" * 20)
...         print(f"{'Quarter':>10}: {quarter_income}", end="\n\n")
...         quarter_income = 0
...
   January: 5000
  February: 5500
     March: 6000
--------------------
   Quarter: 16500

     April: 5800
       May: 6200
      June: 7000
--------------------
   Quarter: 19000

      July: 7500
    August: 7300
 September: 6800
--------------------
   Quarter: 21600

   October: 6500
  November: 6000
  December: 5500
--------------------
   Quarter: 18000
```

Recuerda que `enumerate()` retorna una tupla donde el primer elemento es el índice y el segundo es el elemento del iterable.

### Usar expresiones generadoras

Esta es una forma rápida de iterar a través de las tuplas:

```python
>>> numbers = ("2", "9", "5", "1", "6")

>>> tuple([int(number) for number in numbers])
(2, 9, 5, 1, 6)
```

## Explorando otras características de las tuplas

Las tuplas son un tipo de dato bastante liviano con funciones limitadas debido a su inmutabilidad, que impide añadir, actualizar o quitar elementos. En consecuencia, solo dos métodos forman parte de su API pública: `.count()` e `.index()`.

### `.count()`

Cuenta el número de ocurrencias de un elemento en una tupla:

```python
>>> fruits = (
...     "apple",
...     "banana",
...     "orange",
...     "apple",
...     "apple",
...     "kiwi",
...     "banana"
... )

>>> fruits.count("apple")
3
>>> fruits.count("banana")
2
>>> fruits.count("mango")
0
```

### `.index()`

Encuentra la primera ocurrencia de un elemento en la tupla:

```python
>>> fruits.index("apple")
0

>>> fruits.index("mango")
Traceback (most recent call last):
    ...
ValueError: tuple.index(x): x not in tuple
```

### Encontrando elementos en una tupla

Para determinar rápidamente si un valor está presente en una tupla, puedes usar `in` o `not in`:

```python
elemento in tupla
elemento not in tupla
```

Para tuplas y listas, estos operadores usan algoritmos de búsqueda que iteran sobre los elementos de la colección, con complejidad temporal O(n).

### Obteniendo la longitud de una tupla

Se puede usar `len()` para obtener el número de elementos:

```python
>>> employee = ("John Doe", "Python Developer", "Remote", "Canada")

>>> len(employee)
4
```

### Comparando tuplas

Cuando comparas dos tuplas, Python usa **orden lexicográfico**. Compara los primeros dos elementos de cada tupla. Si son diferentes, esta diferencia determina el resultado de la comparación. Si son iguales, Python compara los siguientes dos elementos, y así sucesivamente.

```python
>>> (2, 3) == (2, 3)
True

>>> (5, 6, 7) < (7, 5, 6)
True

>>> (4, 3, 2) <= (4, 3, 2)
True
```

También puedes comparar tuplas de diferentes longitudes:

```python
>>> (5, 6, 7) < (8,)
True

>>> (5, 6, 7) < (5,)
False

>>> (5, 6, 7) == (5, 6)
False
```

Este proceso de comparación requiere que los elementos sean del mismo tipo o comparables:

```python
>>> ("Python", 42, 3.14, (1, 2)) == ("Python", 42, 3.14, (1, 2))
True

>>> ("Python", 42, 3.14, (1, 2)) == ("Python", "42", 3.14, (1, 2))
False

>>> ("Python", 42, 3.14, (1, 2)) > ("Python", "42", 3.14, (1, 2))
Traceback (most recent call last):
    ...
TypeError: '>' not supported between instances of 'int' and 'str'
```

## Errores comunes usando tuplas en Python

### Error 1: Tupla de un solo elemento

Uno de los errores más comunes al crear tuplas es olvidar la coma al crear tuplas de un solo elemento:

```python
>>> numbers = (42)  # ¡Esto es un entero, NO una tupla!

>>> numbers.index(42)
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute 'index'

>>> type(numbers)
<class 'int'>

>>> numbers = (42,)  # ¡La coma hace la diferencia!

>>> numbers.index(42)
0

>>> type(numbers)
<class 'tuple'>
```

### Error 2: Hashabilidad y objetos mutables

En Python es común escuchar que las tuplas, al ser inmutables, pueden usarse como claves de diccionarios. Aunque esto no siempre es cierto: cuando almacenas objetos **mutables** en una tupla, esa tupla no será hasheable y no funcionará como clave.

```python
>>> cities = {
...     ("Vancouver", [49.2827, -123.1207]): 631_486,  # Lista es mutable
...     ("Denver", [39.7392, -104.9903]): 716_492,
... }
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'list'
```

Los objetos mutables **NO PUEDEN SER HASHEABLES**, por lo que solo los inmutables pueden ser claves de diccionario.

## Usando alternativas a las tuplas nativas

### Tuplas con campos nombrados: `collections.namedtuple`

Una *named tuple* es una subclase de tupla que incorpora campos nombrados a su interfaz pública, permitiendo acceder a los elementos mediante notación de puntos.

```python
>>> from collections import namedtuple

>>> Person = namedtuple("Person", "name age position")

>>> person = Person("John", 35, "Python Developer")
>>> person.name
'John'
>>> person.age
35
>>> person.position
'Python Developer'

>>> person[0]  # También funciona con índices
'John'
```

Sigue siendo inmutable:

```python
>>> person.name = "John Doe"
Traceback (most recent call last):
    ...
AttributeError: can't set attribute

>>> person[0] = "John Doe"
Traceback (most recent call last):
    ...
TypeError: 'Person' object does not support item assignment
```

### Tuplas con campos nombrados y sugerencias de tipo: `typing.NamedTuple`

El módulo `typing` exporta la clase `NamedTuple` que es la versión tipada de `namedtuple`:

```python
>>> from typing import NamedTuple

>>> class Employee(NamedTuple):
...     name: str
...     age: int
...     position: str = "Python Developer"  # Valor por defecto
...

>>> import csv

>>> with open("employees.csv", mode="r") as csv_file:
...     reader = csv.reader(csv_file)
...     next(reader)  # Saltar encabezados
...     employees = []
...     for name, age, position in reader:
...         employees.append(Employee(name, int(age), position))
...
```

### Clases de datos: `dataclasses.dataclass`

Son similares a las *named tuples* pero **mutables por defecto**:

```python
>>> from dataclasses import dataclass

>>> @dataclass
... class Employee:
...     name: str
...     age: int
...     position: str = "Python Developer"
...

>>> import csv

>>> with open("employees.csv", mode="r") as csv_file:
...     reader = csv.reader(csv_file)
...     next(reader)
...     employees = []
...     for name, age, position in reader:
...         employees.append(Employee(name, int(age), position))
...

>>> fatima = employees[0]
>>> fatima.name
'Fatima'
>>> fatima.age
28

>>> fatima.name = "Fatima Rodríguez"  # ¡Mutable!
>>> fatima.name
'Fatima Rodríguez'
```

Puedes hacerlas inmutables con `frozen=True`:

```python
>>> @dataclass(frozen=True)
... class Employee:
...     name: str
...     age: int
...     position: str = "Python Developer"
...
```

## ¿Deberías usar las tuplas?

Deberías usar las tuplas cuando necesites:

- **Asegurar la integridad de los datos**: Su inmutabilidad previene modificaciones accidentales
- **Reducir consumo de memoria**: Tienen menos *overhead* que las listas
- **Mejorar rendimiento**: Son más eficientes en creación, iteración y acceso
- **Usar como claves en diccionarios**: Cuando todos sus elementos son inmutables
- **Retornar múltiples valores desde funciones**: Forma idiomática en Python

### Ejemplos de casos de uso

```python
# Coordenadas RGB
>>> color = (0, 2, 255)

# Información de un vehículo
>>> car = ("Toyota", "Camry", 2020, "Blue")

# Tuplas como claves de diccionario (todas inmutables)
>>> capital_cities = {
...    ("Ottawa", (45.4215, -75.6972)): "Canada",
...    ("Washington D.C.", (38.9072, -77.0369)): "USA",
...    ("Berlin", (52.5200, 13.4050)): "Germany",
... }
```

---
**TE SIENTES DETERMINADO** 
