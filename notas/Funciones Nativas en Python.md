---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-21T18:54:00
Revision: 2026-01-21T18:54:00
---
# Tabla de Contenidos

- [[#📋 Lista Completa de Funciones Incorporadas|📋 Lista Completa de Funciones Incorporadas]]
	- [[#📋 Lista Completa de Funciones Incorporadas#Funciones de Conversión y Creación de Tipos|Funciones de Conversión y Creación de Tipos]]
- [[#🔍 Funciones Clasificadas por Propósito|🔍 Funciones Clasificadas por Propósito]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Manipulación de Tipos y Conversiones**|**Manipulación de Tipos y Conversiones**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Matemáticas y Números**|**Matemáticas y Números**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Iteradores y Secuencias**|**Iteradores y Secuencias**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Strings y Caracteres**|**Strings y Caracteres**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Reflexión e Introspección**|**Reflexión e Introspección**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Entrada/Salida y Archivos**|**Entrada/Salida y Archivos**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Programación Dinámica**|**Programación Dinámica**]]
	- [[#🔍 Funciones Clasificadas por Propósito#**Programación Asíncrona** (Python 3.10+)|**Programación Asíncrona** (Python 3.10+)]]
- [[#⚠️ **Funciones Potencialmente Peligrosas**|⚠️ **Funciones Potencialmente Peligrosas**]]
	- [[#⚠️ **Funciones Potencialmente Peligrosas**#**`eval()` y `exec()` - ¡Usar con precaución!**|**`eval()` y `exec()` - ¡Usar con precaución!**]]
	- [[#⚠️ **Funciones Potencialmente Peligrosas**#**`globals()` y `locals()` - Pueden modificar entorno**|**`globals()` y `locals()` - Pueden modificar entorno**]]
- [[#🎯 **Patrones de Uso Comunes**|🎯 **Patrones de Uso Comunes**]]
	- [[#🎯 **Patrones de Uso Comunes**#**1. Validación de entrada con `isinstance()`**|**1. Validación de entrada con `isinstance()`**]]
	- [[#🎯 **Patrones de Uso Comunes**#**2. Ordenamiento personalizado con `sorted()`**|**2. Ordenamiento personalizado con `sorted()`**]]
	- [[#🎯 **Patrones de Uso Comunes**#**3. Agrupación con `zip()`**|**3. Agrupación con `zip()`**]]
	- [[#🎯 **Patrones de Uso Comunes**#**4. Filtrado con `filter()` y `map()`**|**4. Filtrado con `filter()` y `map()`**]]
- [[#📊 **Tabla de Comportamiento Especial**|📊 **Tabla de Comportamiento Especial**]]
- [[#🚀 **Mejores Prácticas**|🚀 **Mejores Prácticas**]]
# Funciones Nativas en Python

Python incluye un conjunto de **funciones incorporadas** (*built-in functions*) que están siempre disponibles sin necesidad de importar ningún módulo. Estas funciones proporcionan funcionalidades fundamentales para el lenguaje.

## 📋 Lista Completa de Funciones Incorporadas

**Si vienes desde otra nota, busca la funcion con CTRL + F**

### Funciones de Conversión y Creación de Tipos

| Función              | Descripción                                  | Sintaxis                                                                                                  | Ejemplo                                           |
| -------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **`abs()`**          | Valor absoluto de un número                  | `abs(x)`                                                                                                  | `abs(-5) → 5`                                     |
| **`aiter()`**        | Retorna un iterador asíncrono                | `aiter(async_iterable)`                                                                                   | Async: `aiter(async_gen())`                       |
| **`all()`**          | `True` si TODOS los elementos son verdaderos | `all(iterable)`                                                                                           | `all([1, 2, 3]) → True`                           |
| **`anext()`**        | Siguiente elemento de iterador asíncrono     | `anext(async_iterator[, default])`                                                                        | Async: `await anext(async_it)`                    |
| **`any()`**          | `True` si ALGÚN elemento es verdadero        | `any(iterable)`                                                                                           | `any([0, False, 5]) → True`                       |
| **`ascii()`**        | Representación ASCII de un objeto            | `ascii(object)`                                                                                           | `ascii('café') → "'caf\\xe9'"`                    |
| **`bin()`**          | Representación binaria de un entero          | `bin(x)`                                                                                                  | `bin(10) → '0b1010'`                              |
| **`bool()`**         | Convierte a valor booleano                   | `bool([x])`                                                                                               | `bool(0) → False`                                 |
| **`bytearray()`**    | Crea array de bytes mutable                  | `bytearray([source[, encoding[, errors]]])`                                                               | `bytearray(b'abc')`                               |
| **`bytes()`**        | Crea objeto bytes inmutable                  | `bytes([source[, encoding[, errors]]])`                                                                   | `bytes([65, 66, 67]) → b'ABC'`                    |
| **`callable()`**     | Verifica si objeto puede ser llamado         | `callable(object)`                                                                                        | `callable(len) → True`                            |
| **`chr()`**          | Carácter Unicode para un código              | `chr(i)`                                                                                                  | `chr(65) → 'A'`                                   |
| **`complex()`**      | Crea número complejo                         | `complex([real[, imag]])`                                                                                 | `complex(3, 4) → (3+4j)`                          |
| **`dict()`**         | Crea diccionario                             | `dict(**kwarg)` o `dict(mapping, **kwarg)`                                                                | `dict(a=1, b=2) → {'a':1, 'b':2}`                 |
| **`dir()`**          | Lista atributos del objeto                   | `dir([object])`                                                                                           | `dir(list)`                                       |
| **`divmod()`**       | Cociente y resto de división                 | `divmod(a, b)`                                                                                            | `divmod(10, 3) → (3, 1)`                          |
| **`enumerate()`**    | Enumerar elementos con índices               | `enumerate(iterable, start=0)`                                                                            | `list(enumerate(['a','b'])) → [(0,'a'),(1,'b')]`  |
| **`eval()`**         | Evalúa expresión Python                      | `eval(expression[, globals[, locals]])`                                                                   | `eval('2+2') → 4`                                 |
| **`exec()`**         | Ejecuta código Python dinámico               | `exec(object[, globals[, locals]])`                                                                       | `exec('x=5')`                                     |
| **`float()`**        | Convierte a número flotante                  | `float([x])`                                                                                              | `float('3.14') → 3.14`                            |
| **`format()`**       | Formatea valor con especificador             | `format(value[, format_spec])`                                                                            | `format(1234, ',') → '1,234'`                     |
| **`frozenset()`**    | Crea conjunto inmutable                      | `frozenset([iterable])`                                                                                   | `frozenset([1,2,3])`                              |
| **`getattr()`**      | Obtiene atributo de objeto                   | `getattr(object, name[, default])`                                                                        | `getattr(obj, 'attr', 'default')`                 |
| **`globals()`**      | Diccionario de símbolos globales             | `globals()`                                                                                               | `globals()['__name__']`                           |
| **`hasattr()`**      | Verifica si objeto tiene atributo            | `hasattr(object, name)`                                                                                   | `hasattr(obj, 'method')`                          |
| **`hash()`**         | Valor hash del objeto                        | `hash(object)`                                                                                            | `hash('texto') → -582862936`                      |
| **`help()`**         | Sistema de ayuda interactivo                 | `help([object])`                                                                                          | `help(list.append)`                               |
| **`hex()`**          | Representación hexadecimal                   | `hex(x)`                                                                                                  | `hex(255) → '0xff'`                               |
| **`id()`**           | Identidad (dirección memoria) del objeto     | `id(object)`                                                                                              | `id([]) → 140123456789`                           |
| **`input()`**        | Lee entrada del usuario                      | `input([prompt])`                                                                                         | `input("Nombre: ")`                               |
| **`int()`**          | Convierte a entero                           | `int([x[, base]])`                                                                                        | `int('101', 2) → 5`                               |
| **`isinstance()`**   | Verifica tipo/instancia                      | `isinstance(object, classinfo)`                                                                           | `isinstance(5, int) → True`                       |
| **`issubclass()`**   | Verifica herencia de clases                  | `issubclass(class, classinfo)`                                                                            | `issubclass(bool, int) → True`                    |
| **`iter()`**         | Crea iterador                                | `iter(object[, sentinel])`                                                                                | `iter([1,2,3])`                                   |
| **`len()`**          | Longitud/tamaño de objeto                    | `len(s)`                                                                                                  | `len('abc') → 3`                                  |
| **`list()`**         | Crea lista                                   | `list([iterable])`                                                                                        | `list((1,2,3)) → [1,2,3]`                         |
| **`locals()`**       | Diccionario de símbolos locales              | `locals()`                                                                                                | `x=5; locals()['x'] → 5`                          |
| **`map()`**          | Aplica función a elementos                   | `map(function, iterable, ...)`                                                                            | `list(map(str, [1,2,3])) → ['1','2','3']`         |
| **`max()`**          | Elemento máximo                              | `max(iterable, *[, key, default])` o `max(arg1, arg2, *args[, key])`                                      | `max([1,5,2]) → 5`                                |
| **`memoryview()`**   | Vista de memoria de objeto                   | `memoryview(object)`                                                                                      | `memoryview(b'abc')`                              |
| **`min()`**          | Elemento mínimo                              | `min(iterable, *[, key, default])` o `min(arg1, arg2, *args[, key])`                                      | `min([1,5,2]) → 1`                                |
| **`next()`**         | Siguiente elemento de iterador               | `next(iterator[, default])`                                                                               | `next(iter([1,2,3])) → 1`                         |
| **`object()`**       | Objeto base de todas las clases              | `object()`                                                                                                | `obj = object()`                                  |
| **`oct()`**          | Representación octal                         | `oct(x)`                                                                                                  | `oct(8) → '0o10'`                                 |
| **`open()`**         | Abre archivo                                 | `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` | `open('file.txt', 'r')`                           |
| **`ord()`**          | Código Unicode de carácter                   | `ord(c)`                                                                                                  | `ord('A') → 65`                                   |
| **`pow()`**          | Potencia/exponenciación                      | `pow(base, exp[, mod])`                                                                                   | `pow(2, 3) → 8`                                   |
| **`print()`**        | Imprime en salida estándar                   | `print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)`                                       | `print('Hola', 'Mundo', sep='-')`                 |
| **`property()`**     | Crea propiedad de clase                      | `property(fget=None, fset=None, fdel=None, doc=None)`                                                     | `@property def x(self): ...`                      |
| **`range()`**        | Secuencia de números                         | `range(stop)` o `range(start, stop[, step])`                                                              | `list(range(5)) → [0,1,2,3,4]`                    |
| **`repr()`**         | Representación oficial de objeto             | `repr(object)`                                                                                            | `repr([1,2]) → '[1, 2]'`                          |
| **`reversed()`**     | Iterador invertido                           | `reversed(seq)`                                                                                           | `list(reversed([1,2,3])) → [3,2,1]`               |
| **`round()`**        | Redondea número                              | `round(number[, ndigits])`                                                                                | `round(3.14159, 2) → 3.14`                        |
| **`set()`**          | Crea conjunto mutable                        | `set([iterable])`                                                                                         | `set([1,1,2,3]) → {1,2,3}`                        |
| **`setattr()`**      | Asigna valor a atributo                      | `setattr(object, name, value)`                                                                            | `setattr(obj, 'attr', 5)`                         |
| **`slice()`**        | Crea objeto slice                            | `slice(stop)` o `slice(start, stop[, step])`                                                              | `'python'[slice(0,4,2)] → 'pt'`                   |
| **`sorted()`**       | Lista ordenada                               | `sorted(iterable, *, key=None, reverse=False)`                                                            | `sorted([3,1,2]) → [1,2,3]`                       |
| **`staticmethod()`** | Crea método estático                         | `staticmethod(function)`                                                                                  | `@staticmethod def m(): ...`                      |
| **`str()`**          | Convierte a string                           | `str(object='')` o `str(object=b'', encoding='utf-8', errors='strict')`                                   | `str(123) → '123'`                                |
| **`sum()`**          | Suma elementos                               | `sum(iterable, /, start=0)`                                                                               | `sum([1,2,3]) → 6`                                |
| **`super()`**        | Referencia a clase padre                     | `super([type[, object-or-type]])`                                                                         | `super().__init__()`                              |
| **`tuple()`**        | Crea tupla                                   | `tuple([iterable])`                                                                                       | `tuple([1,2,3]) → (1,2,3)`                        |
| **`type()`**         | Tipo/clase de objeto                         | `type(object)` o `type(name, bases, dict, **kwds)`                                                        | `type(5) → <class 'int'>`                         |
| **`vars()`**         | `__dict__` del objeto                        | `vars([object])`                                                                                          | `vars(obj)`                                       |
| **`zip()`**          | Combina iterables                            | `zip(*iterables, strict=False)`                                                                           | `list(zip([1,2], ['a','b'])) → [(1,'a'),(2,'b')]` |
| **`__import__()`**   | Importa módulo dinámicamente                 | `__import__(name, globals=None, locals=None, fromlist=(), level=0)`                                       | `math = __import__('math')`                       |

## 🔍 Funciones Clasificadas por Propósito

### **Manipulación de Tipos y Conversiones**
```python
# Conversión básica entre tipos
str(123)           # '123'
int('456')         # 456
float('3.14')      # 3.14
bool(0)            # False
list('abc')        # ['a', 'b', 'c']
tuple([1,2,3])     # (1, 2, 3)
set([1,1,2,3])     # {1, 2, 3}
dict(a=1, b=2)     # {'a': 1, 'b': 2}
bytes([65,66,67])  # b'ABC'
```

### **Matemáticas y Números**
```python
# Operaciones matemáticas
abs(-10)           # 10
divmod(10, 3)      # (3, 1)  # cociente y resto
pow(2, 3)          # 8
pow(2, 3, 3)       # 2  # (2³ mod 3)
round(3.14159, 2)  # 3.14

# Representaciones numéricas
bin(10)            # '0b1010'
hex(255)           # '0xff'
oct(8)             # '0o10'
complex(3, 4)      # (3+4j)

# Suma y comparaciones
sum([1, 2, 3])     # 6
max([1, 5, 2])     # 5
min([1, 5, 2])     # 1
```

### **Iteradores y Secuencias**
```python
# Creación y manipulación de iterables
list(range(5))           # [0, 1, 2, 3, 4]
list(enumerate(['a','b']))  # [(0, 'a'), (1, 'b')]
list(zip([1,2], ['a','b'])) # [(1, 'a'), (2, 'b')]
list(reversed([1,2,3]))  # [3, 2, 1]
sorted([3,1,2])          # [1, 2, 3]

# Verificaciones
len([1, 2, 3])           # 3
all([True, 1, 'texto'])  # True
any([False, 0, 5])       # True

# Iteradores
it = iter([1, 2, 3])
next(it)                 # 1
next(it, 'fin')          # 2
```

### **Strings y Caracteres**
```python
# Manipulación de caracteres
ord('A')            # 65  # código Unicode
chr(65)             # 'A' # carácter del código
ascii('café')       # "'caf\\xe9'"  # representación ASCII

# Formateo
format(1234, ',')   # '1,234'  # separador de miles
format(0.25, '.2%') # '25.00%' # porcentaje
```

### **Reflexión e Introspección**
```python
# Información sobre objetos
type(5)             # <class 'int'>
isinstance(5, int)  # True
issubclass(bool, int)  # True  # bool hereda de int!
callable(len)       # True
hasattr(obj, 'method')  # True/False
getattr(obj, 'attr', 'default')  # obtiene atributo
setattr(obj, 'attr', value)      # establece atributo

# Diccionarios de símbolos
globals()           # diccionario con variables globales
locals()            # diccionario con variables locales
vars(obj)           # equivalente a obj.__dict__
dir(obj)            # lista de atributos del objeto
```

### **Entrada/Salida y Archivos**
```python
# Interacción con usuario
input("Ingresa tu nombre: ")  # lee entrada del usuario
print("Hola", "Mundo", sep="-", end="!")  # Hola-Mundo!

# Archivos
archivo = open('datos.txt', 'r', encoding='utf-8')
contenido = archivo.read()
archivo.close()

# Ayuda
help(list.append)   # documentación interactiva
```

### **Programación Dinámica**
```python
# Evaluación y ejecución dinámica
eval('2 + 2 * 3')   # 8  # ¡CUIDADO con eval()!
exec('x = 5')       # ejecuta código Python
math = __import__('math')  # importa módulo dinámicamente

# Hash e identidad
hash('texto')       # valor hash (para diccionarios)
id([1,2,3])         # identidad única del objeto
```

### **Programación Asíncrona** (Python 3.10+)
```python
import asyncio

async def ejemplo():
    async_it = aiter(async_generador())  # iterador asíncrono
    valor = await anext(async_it)        # siguiente valor asíncrono
```

## ⚠️ **Funciones Potencialmente Peligrosas**

### **`eval()` y `exec()` - ¡Usar con precaución!**
```python
# ❌ NUNCA hagas esto con entrada de usuario
codigo_usuario = input("Ingresa código: ")
eval(codigo_usuario)  # ¡Podría ejecutar código malicioso!

# ✅ Usar solo con código confiable
# o en entornos controlados
variables_seguras = {'x': 1, 'y': 2}
eval('x + y', {}, variables_seguras)  # 3
```

### **`globals()` y `locals()` - Pueden modificar entorno**
```python
# Cuidado al modificar estos diccionarios
globals()['nueva_variable'] = 10  # Crea variable global

# Mejor usar asignaciones normales
nueva_variable = 10
```

## 🎯 **Patrones de Uso Comunes**

### **1. Validación de entrada con `isinstance()`**
```python
def procesar_valor(valor):
    if isinstance(valor, (int, float)):
        return valor * 2
    elif isinstance(valor, str):
        return valor.upper()
    else:
        raise TypeError(f"Tipo no soportado: {type(valor)}")
```

### **2. Ordenamiento personalizado con `sorted()`**
```python
estudiantes = [
    {'nombre': 'Ana', 'nota': 85},
    {'nombre': 'Luis', 'nota': 92},
    {'nombre': 'Carlos', 'nota': 78}
]

# Ordenar por nota (descendente)
ordenados = sorted(estudiantes, key=lambda x: x['nota'], reverse=True)
```

### **3. Agrupación con `zip()`**
```python
nombres = ['Ana', 'Luis', 'Carlos']
edades = [25, 30, 22]

# Crear lista de tuplas (nombre, edad)
personas = list(zip(nombres, edades))
# [('Ana', 25), ('Luis', 30), ('Carlos', 22)]

# Desempaquetar
nombres2, edades2 = zip(*personas)
```

### **4. Filtrado con `filter()` y `map()`**
```python
# Filtrar números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4, 6]

# Aplicar función a todos los elementos
cuadrados = list(map(lambda x: x**2, numeros))
# [1, 4, 9, 16, 25, 36]
```

## 📊 **Tabla de Comportamiento Especial**

| Función | Comportamiento Especial | Ejemplo |
|---------|------------------------|---------|
| **`sum()`** | `start` por defecto es 0 | `sum([[1],[2]], []) → [1,2]` |
| **`round()`** | Redondeo bancario (ties to even) | `round(2.5) → 2`, `round(3.5) → 4` |
| **`any()`**/`all()` | Cortocircuito evalúa hasta resultado definitivo | `any([True, 1/0])` no causa error |
| **`sorted()`** | Stable sort (mantiene orden de iguales) | Importante para ordenar por múltiples criterios |
| **`zip()`** | Se detiene con el iterable más corto (a menos que `strict=True`) | `list(zip([1,2],[3])) → [(1,3)]` |
| **`dict()`** | Claves duplicadas mantienen último valor | `dict([('a',1),('a',2)]) → {'a':2}` |

## 🚀 **Mejores Prácticas**

1. **Prefiere `isinstance()` sobre `type()`** para verificación de tipos:
   ```python
   # ✅ Mejor
   isinstance(valor, (int, float))
   
   # ❌ Peor
   type(valor) in (int, float)
   ```

2. **Usa `sorted()` en lugar de `.sort()`** cuando necesites nueva lista:
   ```python
   # ✅ Nueva lista ordenada
   nueva = sorted(original)
   
   # ❌ Modifica la original
   original.sort()
   ```

3. **`enumerate()` es mejor que `range(len())`**:
   ```python
   # ✅ Pythonico
   for i, valor in enumerate(lista):
       print(i, valor)
   
   # ❌ Menos claro
   for i in range(len(lista)):
       print(i, lista[i])
   ```

4. **Usa `zip()` para iterar múltiples listas**:
   ```python
   # ✅ Simultáneo
   for nombre, edad in zip(nombres, edades):
       print(f"{nombre}: {edad}")
   
   # ❌ Más verboso
   for i in range(len(nombres)):
       print(f"{nombres[i]}: {edades[i]}")
   ```

5. **Evita `eval()` con entrada de usuario** - usa `ast.literal_eval()` para literales simples.

---
**TE SIENTES DETERMINADO** 
