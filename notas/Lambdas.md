---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-13T06:42:00
Revision: 2026-02-14T12:55:00
---
# Tabla de Contenidos

- [[#Primeros ejemplos|Primeros ejemplos]]
- [[#Funciones anónimas|Funciones anónimas]]
- [[#Funciones lambda vs funciones regulares|Funciones lambda vs funciones regulares]]
	- [[#Funciones lambda vs funciones regulares#Comparación bytecode|Comparación bytecode]]
	- [[#Funciones lambda vs funciones regulares#Seguimiento en trazas de error|Seguimiento en trazas de error]]
	- [[#Funciones lambda vs funciones regulares#Sintaxis y limitaciones|Sintaxis y limitaciones]]
	- [[#Funciones lambda vs funciones regulares#Argumentos|Argumentos]]
	- [[#Funciones lambda vs funciones regulares#Decoradores|Decoradores]]
	- [[#Funciones lambda vs funciones regulares#Cierres (closures)|Cierres (closures)]]
	- [[#Funciones lambda vs funciones regulares#Momento de evaluación (evaluación tardía)|Momento de evaluación (evaluación tardía)]]
	- [[#Funciones lambda vs funciones regulares#Testing de lambdas|Testing de lambdas]]
- [[#Abusos de las expresiones lambda|Abusos de las expresiones lambda]]
	- [[#Abusos de las expresiones lambda#Intentar lanzar una excepción directamente|Intentar lanzar una excepción directamente]]
	- [[#Abusos de las expresiones lambda#Código críptico|Código críptico]]
	- [[#Abusos de las expresiones lambda#Definir métodos de clase con lambda|Definir métodos de clase con lambda]]
- [[#Usos apropiados de las expresiones lambda|Usos apropiados de las expresiones lambda]]
	- [[#Usos apropiados de las expresiones lambda#Construcciones funcionales clásicas|Construcciones funcionales clásicas]]
	- [[#Usos apropiados de las expresiones lambda#Funciones con argumento `key`|Funciones con argumento `key`]]
	- [[#Usos apropiados de las expresiones lambda#Frameworks de UI (Tkinter, etc.)|Frameworks de UI (Tkinter, etc.)]]
	- [[#Usos apropiados de las expresiones lambda#Uso en el intérprete interactivo|Uso en el intérprete interactivo]]
	- [[#Usos apropiados de las expresiones lambda#Monkey Patching en pruebas|Monkey Patching en pruebas]]
- [[#Alternativas a lambda|Alternativas a lambda]]
- [[#¿Son las lambdas "pitónicas"?|¿Son las lambdas "pitónicas"?]]
# Lambdas en Python

Las expresiones lambda en Python (y en otros lenguajes de programación) tienen sus orígenes en el **cálculo lambda**, un modelo computacional inventado por **Alonzo Church** en la década de 1930. Church formalizó el cálculo lambda como un sistema de abstracción pura, y de ahí proviene el término "función lambda" o "abstracción lambda".

Los lenguajes funcionales (como Haskell, Lisp o Erlang) heredan directamente la filosofía del cálculo lambda, adoptando un enfoque **declarativo** que enfatiza la abstracción, la transformación de datos, la composición y la **pureza** (sin efectos secundarios). En contraste, los lenguajes **imperativos** (como Fortran, C o el propio Python) se basan en el modelo de computación de Alan Turing (máquina de Turing), que trabaja con instrucciones paso a paso, mutación de estado y control de flujo explícito.

Aunque Python no es un lenguaje puramente funcional, incorpora algunos conceptos de este paradigma, como `map()`, `filter()`, `reduce()` y las **expresiones lambda**.

## Primeros ejemplos

La **función identidad** (que devuelve el mismo argumento que recibe) se define normalmente así:

```python
def identity(x):
    return x
```

Con una expresión lambda, sería:

```python
lambda x: x
```

Una expresión lambda se compone de:
- La palabra clave `lambda`
- Una o más **variables ligadas** (parámetros)
- El **cuerpo** de la expresión

Las variables ligadas son los argumentos de la función. En cambio, las **variables libres** son aquellas que no están ligadas y se toman del ámbito circundante (constantes o variables definidas fuera).

Ejemplos más elaborados:

```python
lambda x: x + 1
```

Podemos invocarla inmediatamente pasándole argumentos:

```python
(lambda x: x + 1)(2)   # Resultado: 3
```

Esto es una **reducción** en cálculo lambda: reemplazar la variable ligada `x` por el argumento `2`:

`(lambda x: x + 1)(2) = 2 + 1 = 3`

Como toda expresión, una lambda puede asignarse a un nombre:

```python
add_one = lambda x: x + 1
add_one(2)   # 3
```

Equivalente a:

```python
def add_one(x):
    return x + 1
```

Para múltiples argumentos, se separan por comas:

```python
full_name = lambda first, last: f'Nombre completo: {first.title()} {last.title()}'
full_name('guido', 'van rossum')
# 'Nombre completo: Guido Van Rossum'
```

## Funciones anónimas

Los siguientes términos se usan indistintamente:

- Funciones anónimas
- Funciones lambda
- Expresiones lambda
- Abstracciones lambda
- Forma lambda
- Literales de función

Una **función anónima** es, literalmente, una función sin nombre. En Python se crean con `lambda`.

```python
lambda x, y: x + y
```

Esta expresión define una función que suma dos argumentos, pero no tiene nombre. En el intérprete interactivo, podemos invocarla usando el guion bajo `_` (que guarda el último resultado evaluado):

```python
>>> lambda x, y: x + y
<function <lambda> at 0x...>
>>> _(1, 2)
3
```

**Explicación**: En el intérprete interactivo, la variable especial `_` almacena automáticamente el resultado de la última expresión evaluada. En el ejemplo, la expresión lambda se evalúa y queda guardada en `_`, por lo que luego podemos llamarla como si fuera una función. Esto **solo funciona en el intérprete**, no en scripts normales. En un módulo Python, tendrías que asignar la lambda a un nombre o pasarla directamente a otra función.

**Nota**: Para más detalles sobre el uso del guion bajo en Python, consulta [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python) (en inglés).

Otro patrón, común en JavaScript, es el de **ejecución inmediata** (IIFE, *Immediately Invoked Function Expression*). En Python también es posible, aunque no es recomendado:

```python
>>> (lambda x, y: x + y)(2, 3)
5
```

Las funciones lambda son **ciudadanos de primera clase** (first-class citizens), lo que significa que pueden pasarse como argumentos a otras funciones y devolverse como resultado.

```python
>>> high_ord_func = lambda x, func: x + func(x)
>>> high_ord_func(2, lambda x: x * x)   # 2 + (2*2) = 6
6
>>> high_ord_func(2, lambda x: x + 3)    # 2 + (2+3) = 7
7
```

Python expone varias funciones de primera clase en su biblioteca estándar, como `map()`, `filter()`, `functools.reduce()` y funciones que aceptan un argumento `key` (como `sorted()`, `min()`, `max()`).

## Funciones lambda vs funciones regulares

A menudo se dice que las lambdas en Python son solo una forma más corta (y a veces críptica) de escribir una función. Aunque no son inútiles, es importante conocer sus limitaciones.

### Comparación bytecode

Usando el módulo `dis` podemos ver que el bytecode generado es prácticamente idéntico:

```python
import dis

add_lambda = lambda x, y: x + y
dis.dis(add_lambda)
```

```python
def add_func(x, y): return x + y
dis.dis(add_func)
```

La única diferencia notable es que la función lambda carece de nombre; el intérprete la identifica como `<lambda>`.

### Seguimiento en trazas de error

Al ocurrir una excepción, el nombre de la función aparece en el traceback. Con una lambda, solo veremos `<lambda>`, lo que puede dificultar la depuración.

```python
div_zero = lambda x: x / 0
div_zero(2)
# Traceback: ... in <lambda> ZeroDivisionError
```

```python
def div_zero(x): return x / 0
div_zero(2)
# Traceback: ... in div_zero ZeroDivisionError
```

### Sintaxis y limitaciones

- **Solo expresiones**: Una lambda no puede contener declaraciones (`return`, `assert`, `raise`, etc.). Si lo intentas, obtendrás un `SyntaxError`.
- **Una sola línea**: Aunque se pueden usar paréntesis o saltos de línea, el cuerpo sigue siendo una única expresión.
- **Sin anotaciones de tipo**: No soporta type hints (Python 3.5+). Las funciones normales sí.
- **IIFE**: Pueden invocarse inmediatamente, pero esto rara vez se usa fuera del intérprete.

**Ejemplo con anotaciones de tipo (correcto en función normal):**

```python
def full_name(first: str, last: str) -> str:
    return f'{first.title()} {last.title()}'
```

Cualquier error de tipo puede ser detectado por herramientas como `mypy`. En cambio, intentar algo similar con lambda produce un error de sintaxis:

```python
lambda first: str, last: str: first.title() + " " + last.title()  # SyntaxError
```

### Argumentos

Las lambdas soportan todas las formas de pasar argumentos:

- [[Funciones en Python#Argumentos posicionales|Posicionales]]: `lambda x, y: x + y`
- [[Funciones en Python#Argumentos por palabra clave (*keyword arguments*)|Con valor por defecto]]: `lambda x, y=2: x + y`
- [[Funciones en Python#2. Número variable de argumentos `*args` y `**kwargs`|Numero Variable de argumentos]]: `*args`, `**kwargs`
- [[Funciones en Python#3. Argumentos solo-posicionales y solo-nombre|Solo posicionales (Python 3.8+)]]: `lambda x, /, y: ...`
- [[Funciones en Python#3. Argumentos solo-posicionales y solo-nombre|Solo por nombre]]: `lambda x, *, y: ...`

Ejemplos:

```python
(lambda x, y, z: x + y + z)(1, 2, 3)                # 6
(lambda x, y, z=3: x + y + z)(1, 2)                 # 6
(lambda x, y, z=3: x + y + z)(1, y=2)               # 6
(lambda *args: sum(args))(1, 2, 3)                  # 6
(lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3)  # 6
(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)     # 6
```

### Decoradores

Un [[Decoradores#Decoradores en Python#Decorador|decorador]] puede aplicarse a una lambda, aunque la sintaxis es un poco diferente.

```python
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

# Aplicado a una función normal
@trace
def add_two(x):
    return x + 2
add_two(3)

# Aplicado a una lambda (hay que pasar la lambda al decorador manualmente)
print((trace(lambda x: x ** 2))(3))
```

Esto puede ser útil para depurar lambdas usadas en contextos como `map()`.

```python
list(map(trace(lambda x: x*2), range(3)))
# Salida:
# [TRACE] func: <lambda>, args: (0,), kwargs: {}
# [TRACE] func: <lambda>, args: (1,), kwargs: {}
# [TRACE] func: <lambda>, args: (2,), kwargs: {}
# [0, 2, 4]
```

### Cierres (closures)

Un [[Decoradores#Funciones internas y cierres (closures)|cierre]] es una función que recuerda el entorno en el que fue creada, incluso después de que ese entorno haya terminado. Las lambdas también pueden actuar como cierres.

```python
def outer_func(x):
    y = 4
    return lambda z: x + y + z

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
# Salida:
# closure(5) = 9
# closure(6) = 11
# closure(7) = 13
```

### Momento de evaluación (evaluación tardía)

Un comportamiento que puede resultar contraintuitivo es la **evaluación tardía** de las variables libres en una lambda. Observa la diferencia entre una función normal y una lambda en un bucle.

**Con función normal:**

```python
def wrap(n):
    def f():
        print(n)
    return f

numbers = ('one', 'two', 'three')
funcs = []
for n in numbers:
    funcs.append(wrap(n))

for f in funcs:
    f()
# one
# two
# three
```

Aquí, `n` se evalúa en el momento de crear cada función, porque la función `wrap` recibe `n` como argumento y lo "congela" en su cierre.

**Con lambda:**

```python
numbers = ('one', 'two', 'three')
funcs = []
for n in numbers:
    funcs.append(lambda: print(n))

for f in funcs:
    f()
# three
# three
# three
```

Esto sucede porque la lambda **no evalúa la variable libre `n` en el momento de su definición**, sino cuando se ejecuta. Cuando se ejecutan las lambdas (fuera del bucle), la variable `n` ya ha tomado su último valor (`'three'`). Para solucionarlo, podemos forzar la captura del valor actual asignando un argumento por defecto:

```python
funcs.append(lambda n=n: print(n))
```

De esta forma, el valor de `n` en ese momento queda ligado al parámetro `n` de la lambda.

### Testing de lambdas

Las funciones lambda pueden probarse con `unittest` y `doctest`.

**Unittest:**

```python
import unittest

addtwo = lambda x: x + 2

class LambdaTest(unittest.TestCase):
    def test_add_two(self):
        self.assertEqual(addtwo(2), 4)

    def test_add_two_point_two(self):
        self.assertEqual(addtwo(2.2), 4.2)

    def test_add_three(self):
        # Este fallará intencionadamente
        self.assertEqual(addtwo(3), 6)

if __name__ == '__main__':
    unittest.main()
```

**Doctest:** Aunque una lambda no puede tener un docstring directamente, podemos asignarle uno a `__doc__`:

```python
addtwo = lambda x: x + 2
addtwo.__doc__ = """Suma 2 a un número.
    >>> addtwo(2)
    4
    >>> addtwo(2.2)
    4.2
    >>> addtwo(3)  # Debería fallar
    6
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```

## Abusos de las expresiones lambda

Hay situaciones en las que usar una lambda empeora la legibilidad o viola las guías de estilo (PEP 8). Algunos ejemplos de malas prácticas:

### Intentar lanzar una excepción directamente

Una lambda no puede contener declaraciones como `raise`, pero podemos rodearlo con una función externa:

```python
def throw(ex): raise ex
(lambda: throw(Exception('Algo salió mal')))()
```

Pero esto es confuso; mejor usar una función normal.

### Código críptico

```python
(lambda _: list(map(lambda _: _ // 2, _)))([1,2,3,4,5,6,7,8,9,10])
# [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
```

Usar el mismo nombre `_` para distintas variables hace el código incomprensible. Aunque renombremos:

```python
(lambda some_list: list(map(lambda n: n // 2, some_list)))([1,2,3,4,5,6,7,8,9,10])
```

Sigue siendo difícil de leer. Una función normal es mucho más clara:

```python
def div_items(some_list):
    return [n // 2 for n in some_list]
```

### Definir métodos de clase con lambda

Aunque es posible, la herramienta `flake8` marcará error E731 ("do not assign a lambda expression, use a def"). Por ejemplo:

```python
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    brand = property(lambda self: getattr(self, '_brand'),
                     lambda self, value: setattr(self, '_brand', value))
    # ... etc.
```

Es mucho más legible usar decoradores `@property` y métodos normales.

## Usos apropiados de las expresiones lambda

A pesar de las críticas, hay escenarios donde las lambdas resultan prácticas y elegantes.

### Construcciones funcionales clásicas

Con `map()`, `filter()` y `reduce()`:

```python
list(map(lambda x: x.upper(), ['cat', 'dog', 'cow']))       # ['CAT', 'DOG', 'COW']
list(filter(lambda x: 'o' in x, ['cat', 'dog', 'cow']))     # ['dog', 'cow']
from functools import reduce
reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
# 'cat | dog | cow'
```

### Funciones con argumento `key`

Funciones como `sorted()`, `min()`, `max()` aceptan un parámetro `key` que puede ser una lambda:

```python
ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
sorted(ids)                                 # orden lexicográfico
sorted(ids, key=lambda x: int(x[2:]))       # orden numérico
```

### Frameworks de UI (Tkinter, etc.)

En programación de interfaces gráficas, es común asignar acciones a eventos usando lambdas:

```python
import tkinter as tk

window = tk.Tk()
button = tk.Button(
    window,
    text="Invertir",
    command=lambda: label.configure(text=label.cget("text")[::-1])
)
button.pack()
label = tk.Label(window, text="Hola")
label.pack()
window.mainloop()
```

### Uso en el intérprete interactivo

Para pruebas rápidas y experimentación, las lambdas son ideales. Se pueden usar con `timeit` para medir tiempos de ejecución de fragmentos pequeños:

```python
from timeit import timeit
timeit(lambda: ''.join(str(i) for i in range(100)), number=10000)
```

### Monkey Patching en pruebas

En pruebas unitarias, a veces necesitamos reemplazar temporalmente una función por una que devuelva valores controlados. Las lambdas son perfectas para esto:

```python
import secrets
from contextlib import contextmanager

@contextmanager
def mock_token():
    token_hex_original = secrets.token_hex
    secrets.token_hex = lambda _: 'feedfacecafebeef'
    yield
    secrets.token_hex = token_hex_original

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_token():
    with mock_token():
        assert gen_token() == 'TOKEN_feedfacecafebeef'
```

Con `pytest` es aún más elegante:

```python
import secrets

def gen_token():
    return f'TOKEN_{secrets.token_hex(8)}'

def test_gen_token(monkeypatch):
    monkeypatch.setattr('secrets.token_hex', lambda _: 'feedfacecafebeef')
    assert gen_token() == 'TOKEN_feedfacecafebeef'
```

## Alternativas a lambda

En muchos casos, las comprensiones de listas, generadores o funciones normales son más legibles.

- **`map()` con lambda** → comprensión de listas:
  ```python
  # con lambda
  list(map(lambda x: x.capitalize(), ['cat', 'dog', 'cow']))
  # con comprensión
  [x.capitalize() for x in ['cat', 'dog', 'cow']]
  ```

- **`filter()` con lambda** → comprensión con condición:
  ```python
  # con lambda
  list(filter(lambda x: x % 2 == 0, range(11)))
  # con comprensión
  [x for x in range(11) if x % 2 == 0]
  ```

- **`reduce()` con lambda** → usar funciones específicas o sum() con generador:
  ```python
  import functools
  pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
  functools.reduce(lambda acc, pair: acc + pair[0], pairs, 0)  # 6
  # mejor:
  sum(x[0] for x in pairs)  # 6
  ```

## ¿Son las lambdas "pitónicas"?

El [PEP 8](https://peps.python.org/pep-0008/) dice:

> "Utiliza siempre una declaración `def` en lugar de una sentencia de asignación que vincule una expresión lambda directamente a un identificador."

Es decir, no se recomienda asignar una lambda a un nombre (eso es para lo que sirven las funciones normales). Sin embargo, las lambdas son pitónicas cuando se usan en contextos donde realmente se necesita una función anónima y de una sola expresión, como argumento de orden superior (en `map`, `filter`, `key`, etc.). En esos casos, aportan concisión sin sacrificar legibilidad.

En resumen: **usa lambdas cuando la lógica sea trivial y la función no necesite nombre; para todo lo demás, define una función normal.**

---
__TE SIENTES DETERMINADO__