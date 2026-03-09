---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-17T16:22:00
Revision: 2026-02-17T16:22:00
---
# Tabla de Contenidos

- [[#Métodos de Inicialización y Construcción|Métodos de Inicialización y Construcción]]
- [[#Representación de Objetos: `__str__` y `__repr__`|Representación de Objetos: `__str__` y `__repr__`]]
- [[#Sobrecarga de Operadores|Sobrecarga de Operadores]]
	- [[#Sobrecarga de Operadores#Ejemplo con `__add__` (operador `+`)|Ejemplo con `__add__` (operador `+`)]]
	- [[#Sobrecarga de Operadores#Ejemplo con `__ge__` (operador `>=`)|Ejemplo con `__ge__` (operador `>=`)]]
- [[#Tablas de Métodos Mágicos por Categoría|Tablas de Métodos Mágicos por Categoría]]
	- [[#Tablas de Métodos Mágicos por Categoría#Inicialización y destrucción|Inicialización y destrucción]]
	- [[#Tablas de Métodos Mágicos por Categoría#Operadores unarios y funciones incorporadas|Operadores unarios y funciones incorporadas]]
	- [[#Tablas de Métodos Mágicos por Categoría#Asignación aumentada (operadores `+=`, `-=`, etc.)|Asignación aumentada (operadores `+=`, `-=`, etc.)]]
	- [[#Tablas de Métodos Mágicos por Categoría#Conversión de tipos|Conversión de tipos]]
	- [[#Tablas de Métodos Mágicos por Categoría#Métodos relacionados con cadenas|Métodos relacionados con cadenas]]
	- [[#Tablas de Métodos Mágicos por Categoría#Manejo de atributos|Manejo de atributos]]
	- [[#Tablas de Métodos Mágicos por Categoría#Operadores de comparación|Operadores de comparación]]
	- [[#Tablas de Métodos Mágicos por Categoría#Operadores aritméticos y binarios|Operadores aritméticos y binarios]]
	- [[#Tablas de Métodos Mágicos por Categoría#Métodos para operaciones reflejadas (cuando el operando izquierdo no implementa la operación)|Métodos para operaciones reflejadas (cuando el operando izquierdo no implementa la operación)]]
- [[#Conclusión|Conclusión]]
# Métodos mágicos en python

Los **métodos mágicos** (también llamados **dunder methods**, por *double underscore*) son métodos especiales en Python que comienzan y terminan con doble guion bajo, como `__init__` o `__str__`. No están diseñados para ser invocados directamente por el programador, sino que se ejecutan internamente en respuesta a ciertas acciones. Por ejemplo, cuando usas el operador `+` entre dos números, Python llama automáticamente al método `__add__()` de la clase correspondiente.

Todas las clases incorporadas en Python ya definen muchos de estos métodos. Puedes ver la lista completa usando la función `dir()`:

```python
print(dir(int))
# Muestra todos los métodos (incluyendo los mágicos) de la clase int
```

Algunos de los métodos mágicos más importantes y su propósito se explican a continuación.

## Métodos de Inicialización y Construcción

| Método | Descripción |
|--------|-------------|
| `__new__(cls[, ...])` | Se llama para crear una nueva instancia de la clase. Es un método de clase que recibe la clase como primer argumento y debe devolver una nueva instancia (normalmente delegando en `object.__new__(cls)`). |
| `__init__(self[, ...])` | Inicializa una instancia recién creada. Se llama después de `__new__`. |
| `__del__(self)` | El "destructor"; se llama cuando la instancia está a punto de ser destruida (recolección de basura). |

Ejemplo de `__new__` e `__init__`:

```python
class Ejemplo:
    def __new__(cls):
        print("1. __new__() llamado")
        instancia = super().__new__(cls)
        return instancia

    def __init__(self):
        print("2. __init__() llamado")
        self.valor = 42

obj = Ejemplo()
# Salida:
# 1. __new__() llamado
# 2. __init__() llamado
```

## Representación de Objetos: `__str__` y `__repr__`

- `__str__(self)`: llamado por `str(object)` y `print(object)`. Debe devolver una representación legible para el usuario.
- `__repr__(self)`: llamado por `repr(object)`. Debe devolver una representación **inequívoca** que, idealmente, pueda usarse para reconstruir el objeto (útil para depuración).

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Punto(3, 4)
print(repr(p))   # Punto(3, 4)
print(str(p))    # (3, 4)
print(p)         # (3, 4)   (porque print usa __str__)
```

## Sobrecarga de Operadores

Puedes definir cómo se comportan los operadores con tus objetos implementando los métodos mágicos correspondientes.

### Ejemplo con `__add__` (operador `+`)

```python
class Distancia:
    def __init__(self, pies, pulgadas):
        self.pies = pies
        self.pulgadas = pulgadas

    def __add__(self, otra):
        total_pies = self.pies + otra.pies
        total_pulg = self.pulgadas + otra.pulgadas
        if total_pulg >= 12:
            total_pies += total_pulg // 12
            total_pulg %= 12
        return Distancia(total_pies, total_pulg)

    def __str__(self):
        return f"{self.pies} pies, {self.pulgadas} pulgadas"

d1 = Distancia(3, 10)
d2 = Distancia(4, 4)
print(d1 + d2)   # 8 pies, 2 pulgadas
```

### Ejemplo con `__ge__` (operador `>=`)

```python
class Distancia:
    # ... (código anterior) ...

    def __ge__(self, otra):
        total1 = self.pies * 12 + self.pulgadas
        total2 = otra.pies * 12 + otra.pulgadas
        return total1 >= total2

d1 = Distancia(2, 1)
d2 = Distancia(4, 10)
print(d1 >= d2)   # False
```

## Tablas de Métodos Mágicos por Categoría

### Inicialización y destrucción

| Método | Descripción |
|--------|-------------|
| `__new__(cls, ...)` | Creación de instancia (método de clase). |
| `__init__(self, ...)` | Inicialización de instancia. |
| `__del__(self)` | Destructor. |

### Operadores unarios y funciones incorporadas

| Método | Descripción |
|--------|-------------|
| `__pos__(self)` | `+objeto` (positivo unario). |
| `__neg__(self)` | `-objeto` (negativo unario). |
| `__abs__(self)` | Llamado por `abs()`. |
| `__invert__(self)` | `~objeto` (inversión binaria). |
| `__round__(self, n)` | Llamado por `round()`. |
| `__floor__(self)` | Llamado por `math.floor()`. |
| `__ceil__(self)` | Llamado por `math.ceil()`. |
| `__trunc__(self)` | Llamado por `math.trunc()`. |

### Asignación aumentada (operadores `+=`, `-=`, etc.)

| Método | Descripción |
|--------|-------------|
| `__iadd__(self, other)` | `a += b` |
| `__isub__(self, other)` | `a -= b` |
| `__imul__(self, other)` | `a *= b` |
| `__ifloordiv__(self, other)` | `a //= b` |
| `__itruediv__(self, other)` | `a /= b` |
| `__imod__(self, other)` | `a %= b` |
| `__ipow__(self, other)` | `a **= b` |
| `__ilshift__(self, other)` | `a <<= b` |
| `__irshift__(self, other)` | `a >>= b` |
| `__iand__(self, other)` | `a &= b` |
| `__ior__(self, other)` | `a |= b` |
| `__ixor__(self, other)` | `a ^= b` |

### Conversión de tipos

| Método | Descripción |
|--------|-------------|
| `__int__(self)` | Llamado por `int()`. |
| `__float__(self)` | Llamado por `float()`. |
| `__complex__(self)` | Llamado por `complex()`. |
| `__oct__(self)` | Llamado por `oct()` (obsoleto en Python 3). |
| `__hex__(self)` | Llamado por `hex()` (obsoleto en Python 3). |
| `__index__(self)` | Para convertir a entero en expresiones de slicing. |
| `__trunc__(self)` | Llamado por `math.trunc()`. |

### Métodos relacionados con cadenas

| Método | Descripción |
|--------|-------------|
| `__str__(self)` | Llamado por `str()` y `print()`. |
| `__repr__(self)` | Llamado por `repr()`. |
| `__format__(self, format_spec)` | Llamado por `format()` y f-strings. |
| `__hash__(self)` | Llamado por `hash()`. |
| `__bool__(self)` | Llamado por `bool()`; si no está definido, se usa `__len__()`. |
| `__dir__(self)` | Llamado por `dir()`. |
| `__sizeof__(self)` | Llamado por `sys.getsizeof()`. |

### Manejo de atributos

| Método | Descripción |
|--------|-------------|
| `__getattr__(self, name)` | Se llama cuando se accede a un atributo que no existe. |
| `__setattr__(self, name, value)` | Se llama al asignar un valor a un atributo. |
| `__delattr__(self, name)` | Se llama al eliminar un atributo (`del objeto.atributo`). |

### Operadores de comparación

| Método | Descripción |
|--------|-------------|
| `__lt__(self, other)` | `<` (menor que) |
| `__le__(self, other)` | `<=` (menor o igual) |
| `__eq__(self, other)` | `==` (igual) |
| `__ne__(self, other)` | `!=` (distinto) |
| `__gt__(self, other)` | `>` (mayor que) |
| `__ge__(self, other)` | `>=` (mayor o igual) |

### Operadores aritméticos y binarios

| Método | Descripción |
|--------|-------------|
| `__add__(self, other)` | `+` |
| `__sub__(self, other)` | `-` |
| `__mul__(self, other)` | `*` |
| `__floordiv__(self, other)` | `//` |
| `__truediv__(self, other)` | `/` |
| `__mod__(self, other)` | `%` |
| `__pow__(self, other[, modulo])` | `**` |
| `__and__(self, other)` | `&` (AND binario) |
| `__or__(self, other)` | `\|` (OR binario) |
| `__xor__(self, other)` | `^` (XOR binario) |
| `__lshift__(self, other)` | `<<` (desplazamiento izquierda) |
| `__rshift__(self, other)` | `>>` (desplazamiento derecha) |

### Métodos para operaciones reflejadas (cuando el operando izquierdo no implementa la operación)

| Método | Descripción |
|--------|-------------|
| `__radd__(self, other)` | `other + self` (si `other` no implementa `__add__`). |
| `__rsub__(self, other)` | `other - self` |
| `__rmul__(self, other)` | `other * self` |
| ... (similar para el resto de operadores) ... |

## Conclusión

Los métodos mágicos son la herramienta fundamental para personalizar el comportamiento de tus clases y hacer que trabajen de manera natural con la sintaxis y las funciones incorporadas de Python. Al implementarlos adecuadamente, tus objetos pueden:

- Ser impresos de forma legible (`__str__`, `__repr__`).
- Soportar operadores (`__add__`, `__ge__`, etc.).
- Responder a conversiones de tipo (`__int__`, `__float__`).
- Integrarse con funciones como `len()`, `abs()`, `hash()`, etc.

Dominar estos métodos te permitirá escribir código más **pitónico** y expresivo.

---
__TE SIENTES DETERMINADO__