---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-09T21:12:00
Revision: 2026-02-09T21:59:00
---
# Tabla de Contenidos

- [[#Funciones como objetos de primera clase|Funciones como objetos de primera clase]]
	- [[#Funciones como objetos de primera clase#Asignando funciones a variables|Asignando funciones a variables]]
	- [[#Funciones como objetos de primera clase#Definiendo funciones dentro de otras funciones|Definiendo funciones dentro de otras funciones]]
	- [[#Funciones como objetos de primera clase#Pasando funciones como argumentos|Pasando funciones como argumentos]]
	- [[#Funciones como objetos de primera clase#Funciones que retornan otras funciones|Funciones que retornan otras funciones]]
- [[#Funciones internas y cierres (closures)|Funciones internas y cierres (closures)]]
- [[#Creando un decorador|Creando un decorador]]
	- [[#Creando un decorador#Decorador básico|Decorador básico]]
	- [[#Creando un decorador#Usando la sintaxis `@`|Usando la sintaxis `@`]]
	- [[#Creando un decorador#Decoradores que aceptan argumentos|Decoradores que aceptan argumentos]]
	- [[#Creando un decorador#Uso de `*args` y `**kwargs` en decoradores|Uso de `*args` y `**kwargs` en decoradores]]
	- [[#Creando un decorador#Apilando múltiples decoradores|Apilando múltiples decoradores]]
- [[#Preservando metadatos con `functools.wraps`|Preservando metadatos con `functools.wraps`]]
- [[#Decoradores basados en clases|Decoradores basados en clases]]
	- [[#Decoradores basados en clases#Decorador de clase básico|Decorador de clase básico]]
	- [[#Decoradores basados en clases#Ventajas de los decoradores basados en clases:|Ventajas de los decoradores basados en clases:]]
- [[#Casos de uso reales de decoradores|Casos de uso reales de decoradores]]
	- [[#Casos de uso reales de decoradores#1. Almacenamiento en caché con `@lru_cache`|1. Almacenamiento en caché con `@lru_cache`]]
	- [[#Casos de uso reales de decoradores#2. Medición del tiempo de ejecución|2. Medición del tiempo de ejecución]]
	- [[#Casos de uso reales de decoradores#3. Logging|3. Logging]]
	- [[#Casos de uso reales de decoradores#4. Validación de entrada|4. Validación de entrada]]
- [[#Resumen|Resumen]]
# Decoradores en Python

Los decoradores son una característica poderosa y elegante en Python que nos permite modificar o extender el comportamiento de una función o método **sin cambiar su código original**.

Un decorador es un patrón de diseño en Python que permite al usuario añadir nueva funcionalidad a un objeto existente sin modificar su estructura. Tradicionalmente se colocan antes de la definición de la función que se quiere decorar, usando la sintaxis `@decorator_name`.

**Puntos clave:**
- Modifican o extienden el comportamiento de una función sin alterar su implementación original.
- Usan `@decorator_name` para una aplicación limpia y legible.
- `functools.wraps` es esencial para preservar los metadatos de la función decorada.
- Los decoradores basados en clases permiten comportamientos con estado (*stateful*) entre llamadas.
- Casos de uso comunes incluyen: `@lru_cache` para almacenamiento en caché, logging, autenticación y validación de entrada.

## Funciones como objetos de primera clase

En Python, las funciones son **objetos de primera clase**, lo que significa que soportan operaciones como:
- Ser pasadas como argumentos a otras funciones
- Ser retornadas desde otras funciones
- Ser asignadas a variables
- Ser definidas dentro de otras funciones

Esta propiedad es crucial para entender cómo funcionan los decoradores.

### Asignando funciones a variables

```python
def plus_one(number):
    return number + 1

add_one = plus_one  # Asignar la función a otra variable
print(add_one(5))   # Output: 6
```

### Definiendo funciones dentro de otras funciones

```python
def plus_one(number):
    def add_one(number):
        return number + 1
    
    result = add_one(number)
    return result

print(plus_one(4))  # Output: 5
```

### Pasando funciones como argumentos

```python
def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

print(function_call(plus_one))  # Output: 6
```

### Funciones que retornan otras funciones

```python
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello = hello_function()
print(hello())  # Output: 'Hi'
```

## Funciones internas y cierres (closures)

Un **cierre** (*closure*) en Python es una función que "recuerda" el entorno en el cual fue creada, incluso después de que ese entorno ya no esté activo. Esto significa que una función anidada puede acceder a variables de su función envolvente y continuar usándolas.

Los cierres son esenciales para entender los decoradores, ya que permiten a las funciones wrapper acceder y modificar el estado de la función decorada.

**Ejemplo de cierre:**

```python
def outer_function(message):
    def inner_function():
        print(f"Mensaje del cierre: {message}")
    return inner_function

closure_function = outer_function("¡Hola, cierres!")
closure_function()  # Output: Mensaje del cierre: ¡Hola, cierres!
```

En este ejemplo, `inner_function` es un cierre porque accede a `message`, una variable de `outer_function`. Incluso después de que `outer_function` termine su ejecución, `inner_function` mantiene acceso a `message`.

## Creando un decorador

### Decorador básico

Vamos a crear un decorador que convierta el resultado de una función a mayúsculas:

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def say_hi():
    return 'hello there'

# Aplicando el decorador manualmente
decorate = uppercase_decorator(say_hi)
print(decorate())  # Output: 'HELLO THERE'
```

### Usando la sintaxis `@`

Python ofrece una sintaxis más limpia para aplicar decoradores:

```python
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())  # Output: 'HELLO THERE'
```

### Decoradores que aceptan argumentos

¿Qué pasa si queremos que el decorador mismo acepte argumentos? Necesitamos crear un decorador que devuelva otro decorador:

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
    def decorator(func):
        def wrapper(function_arg1, function_arg2, function_arg3):
            print(f"El wrapper puede acceder a todas las variables:")
            print(f"  - Del creador del decorador: {decorator_arg1}, {decorator_arg2}, {decorator_arg3}")
            print(f"  - De la llamada a la función: {function_arg1}, {function_arg2}, {function_arg3}")
            return func(function_arg1, function_arg2, function_arg3)
        return wrapper
    return decorator

pandas = "Pandas"
@decorator_maker_with_arguments(pandas, "Numpy", "Scikit-learn")
def decorated_function_with_arguments(function_arg1, function_arg2, function_arg3):
    print(f"Esta es la función decorada y solo conoce sus argumentos: {function_arg1}, {function_arg2}, {function_arg3}")

decorated_function_with_arguments(pandas, "Science", "Tools")
```

### Uso de `*args` y `**kwargs` en decoradores

Para hacer decoradores que funcionen con cualquier función, independientemente de sus argumentos, usamos [[Funciones en Python#2. Número variable de argumentos `*args` y `**kwargs`|`*args` y `**kwargs`]]:

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print(f'Los argumentos posicionales son: {args}')
        print(f'Los argumentos de palabra clave son: {kwargs}')
        return function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1, 2, 3)
# Output:
# Los argumentos posicionales son: (1, 2, 3)
# Los argumentos de palabra clave son: {}
# 1 2 3

@a_decorator_passing_arbitrary_arguments  
def function_with_keyword_arguments(**kwargs):
    print(f"Esto ha mostrado argumentos de palabra clave: {kwargs}")

function_with_keyword_arguments(first_name="Derrick", last_name="Mwiti")
# Output:
# Los argumentos posicionales son: ()
# Los argumentos de palabra clave son: {'first_name': 'Derrick', 'last_name': 'Mwiti'}
# Esto ha mostrado argumentos de palabra clave: {'first_name': 'Derrick', 'last_name': 'Mwiti'}
```

### Apilando múltiples decoradores

Puedes aplicar varios decoradores a una misma función, pero **el orden importa**:

```python
import functools

def split_string(function):
    @functools.wraps(function)
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())  # Output: ['HELLO', 'THERE']
```

En este caso, los decoradores se aplican de **abajo hacia arriba**:
1. Primero se aplica `@uppercase_decorator` (convierte a mayúsculas)
2. Luego se aplica `@split_string` (divide el string)

Si invertimos el orden, obtendríamos un error porque las listas no tienen el método `upper()`.

## Preservando metadatos con `functools.wraps`

Cuando decoras una función, **pierdes sus metadatos** (nombre, documentación, etc.):

```python
@uppercase_decorator
def say_hi():
    "Esta función dice hola"
    return 'hello there'

print(say_hi.__name__)  # Output: 'wrapper'
print(say_hi.__doc__)   # Output: None (o la documentación del wrapper)
```

Para solucionar esto, Python proporciona `functools.wraps`:

```python
import functools

def uppercase_decorator(func):
    @functools.wraps(func)  # ¡Esto preserva los metadatos!
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_decorator
def say_hi():
    "Esta función dice hola"
    return 'hello there'

print(say_hi.__name__)  # Output: 'say_hi'
print(say_hi.__doc__)   # Output: 'Esta función dice hola'
```

**Siempre** usa `@functools.wraps` cuando escribas decoradores para mantener la trazabilidad y facilitar la depuración.

## Decoradores basados en clases

Además de las funciones, Python permite crear decoradores usando clases, lo que proporciona mayor flexibilidad y mantenibilidad, especialmente para casos de uso complejos.

### Decorador de clase básico

```python
class UppercaseDecorator:
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result.upper()

@UppercaseDecorator
def greet():
    return "hello there"

print(greet())  # Output: HELLO THERE
```

**Cómo funciona:**
1. `__init__` inicializa el decorador con la función a decorar
2. `__call__` se invoca cuando se llama a la función decorada, permitiendo modificar su comportamiento

### Ventajas de los decoradores basados en clases:

1. **Decoradores con estado**: Pueden mantener estado usando variables de instancia
2. **Mayor legibilidad**: Para decoradores complejos, el [[Funciones en Python#2. Encapsulación|encapsulamiento]] en una clase puede hacer el código más organizado

**Ejemplo de decorador con estado:**

```python
class CallCounter:
    def __init__(self, function):
        self.function = function
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Función {self.function.__name__} ha sido llamada {self.count} veces.")
        return self.function(*args, **kwargs)

@CallCounter
def say_hello():
    print("¡Hola!")

say_hello()
say_hello()
# Output:
# Función say_hello ha sido llamada 1 veces.
# ¡Hola!
# Función say_hello ha sido llamada 2 veces.
# ¡Hola!
```

## Casos de uso reales de decoradores

### 1. Almacenamiento en caché con `@lru_cache`

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(50))  # Las llamadas posteriores con el mismo argumento son mucho más rápidas
```

### 2. Medición del tiempo de ejecución

```python
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.4f} segundos")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return "Listo"

print(slow_function())
```

### 3. Logging

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__} con args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} retornó: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(5, 3))
```

### 4. Validación de entrada

```python
def validate_non_negative(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError("Los argumentos no pueden ser negativos")
        return func(*args, **kwargs)
    return wrapper

@validate_non_negative
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 3))  # OK
# print(calculate_area(-5, 3))  # ValueError: Los argumentos no pueden ser negativos
```

## Resumen

Los decoradores en Python **alteran dinámicamente** la funcionalidad de una función, método o clase sin necesidad de usar subclases o cambiar el código fuente de la función decorada. Su uso asegura que tu código siga el principio **DRY** (Don't Repeat Yourself - No te repitas).

**Usos comunes de decoradores:**
- **Autorización** en frameworks como Flask y Django
- **Logging** para rastrear llamadas a funciones
- **Medición de tiempo de ejecución** para optimización
- **Sincronización** en programación concurrente
- **Validación de entrada** para funciones
- **Mecanismos de reintento** para operaciones de red
- **Almacenamiento en caché** para funciones costosas

Los decoradores son una herramienta poderosa que, una vez dominada, puede hacer que tu código sea más limpio, más modular y más fácil de mantener.

---
__TE SIENTES DETERMINADO__