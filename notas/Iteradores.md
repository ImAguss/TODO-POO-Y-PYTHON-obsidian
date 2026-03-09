---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-14T13:04:00
Revision: 2026-02-14T13:35:00
---
# Tabla de Contenidos

- [[#El protocolo de iteración|El protocolo de iteración]]
- [[#Creando un iterador propio|Creando un iterador propio]]
- [[#Generadores|Generadores]]
- [[#Expresiones generadoras|Expresiones generadoras]]
- [[#Resumen|Resumen]]
# Iteradores en Python

## El protocolo de iteración

Seguramente has notado que la mayoría de los objetos contenedores en Python pueden ser recorridos con un bucle [[Estructuras Iterativas en Python#Estructura `for`|for]]:

```python
for element in [1, 2, 3]:
    print(element)

for element in (1, 2, 3):
    print(element)

for key in {'one': 1, 'two': 2}:
    print(key)

for char in "123":
    print(char)

for line in open("miarchivo.txt"):
    print(line, end='')
```

Este estilo de acceso es claro, conciso y conveniente. Detrás de escena, la sentencia `for` llama a la función `iter()` sobre el objeto contenedor. Esta función retorna un **objeto iterador** que define el método `__next__()`, el cual accede a los elementos del contenedor uno a la vez, recordando la posición en la que se encuentra. Cuando no hay más elementos, `__next__()` lanza la excepción `StopIteration`, que el bucle `for` captura para terminar.

Incluso si no usamos un bucle, podemos interactuar manualmente con el iterador:

```python
s = 'abc'
it = iter(s)          # obtiene el iterador
print(next(it))       # 'a'
print(next(it))       # 'b'
print(next(it))       # 'c'
print(next(it))       # Lanza StopIteration
```

## Creando un iterador propio

Para que una clase sea iterable, debe implementar el método `__iter__()` que devuelva un objeto con el método `__next__()`. A menudo, la propia clase implementa ambos y se retorna a sí misma en `__iter__()`.

Ejemplo: un iterador que recorre una secuencia en orden inverso.

```python
class Reverse:
    """Iterador para recorrer una secuencia hacia atrás."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)   # m, a, p, s
```

## Generadores

Los generadores son una forma sencilla y potente de crear iteradores. Se definen como una función normal, pero en lugar de `return` usan la palabra clave `yield`. Cada vez que se llama a `yield`, la función "se congela" guardando su estado, y la próxima vez que se invoque `next()` sobre el generador, reanuda su ejecución justo después del `yield`.

El ejemplo anterior puede reescribirse como un generador:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)   # f, l, o, g
```

Ventajas de los generadores:
- Son más compactos y legibles.
- Guardan automáticamente el estado de las variables locales entre llamadas.
- Se encargan de lanzar `StopIteration` cuando terminan.
- No necesitan definir métodos `__iter__()` ni `__next__()`.

Cualquier cosa que pueda hacerse con un generador puede hacerse con un iterador basado en clases, pero el código suele ser más claro con `yield`.

## Expresiones generadoras

Para casos simples, podemos crear generadores sobre la marcha usando una sintaxis similar a las [[Estructuras Iterativas en Python#Comprensión de listas (*list comprehension*)|comprensiones de listas]], pero con paréntesis en lugar de corchetes. Estas expresiones generadoras son más compactas y consumen menos memoria que las comprensiones de listas equivalentes, ya que generan los valores uno a uno sin construir toda la lista.

```python
# Suma de cuadrados
sum(i*i for i in range(10))                 # 285

# Producto punto de dos vectores
xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x, y in zip(xvec, yvec))        # 260

# Conjunto de palabras únicas en un texto (suponiendo que 'page' es una lista de líneas)
unique_words = set(word for line in page for word in line.split())

# Mejor estudiante (por GPA) usando max con una expresión generadora
valedictorian = max((student.gpa, student.name) for student in graduates)

# Crear una lista a partir de un generador
data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))   # ['f', 'l', 'o', 'g']
```

## Resumen

- **Iterador**: objeto que implementa `__iter__()` y `__next__()`.
- **Iterable**: objeto del cual se puede obtener un iterador (implementa `__iter__()` o define `__getitem__()`).
- **Generador**: función con `yield` que produce un iterador automáticamente.
- **Expresión generadora**: forma compacta de crear generadores para casos simples.

Los iteradores y generadores son fundamentales en Python para trabajar con secuencias de datos de manera eficiente y elegante, especialmente cuando se manejan grandes volúmenes de información o flujos infinitos.

---
__TE SIENTES DETERMINADO__