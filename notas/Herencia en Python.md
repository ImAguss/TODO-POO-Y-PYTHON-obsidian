---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-03-01T22:40:00
Revision: 2026-03-02T11:36:00
---
# Herencia en Python

La herencia permite crear clases que reutilizan y extienden el comportamiento de otras clases. Una clase derivada hereda atributos y métodos de su(s) clase(s) base.

## Sintaxis básica

```python
class Derivada(Base):
    pass
```

La clase base debe estar definida en el [[NameSpaces en Python#Namespace global de un módulo|Namespace global del modulo]]. Aunque tambien puede importarse de otro módulo:

```python
from modulo import Base
class Derivada(Base):
    pass

# También válido:
class Derivada(modulo.Base):
    pass
```

## Instanciación

Crear una instancia de una clase derivada no tiene sintaxis especial:

```python
p = Perro("Fido")  # Igual que cualquier clase
```

Si la clase derivada no define `__init__`, Python sube por la jerarquía de herencia hasta encontrar uno.

### Cuidado: `__init__` sin `super()`

Si la clase derivada define `__init__` **sin llamar a `super().__init__()`**, los atributos del padre **nunca se inicializan**:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, raza):
        self.raza = raza  # No llama a super()

>>> p = Perro("labrador")
>>> p.raza
'labrador'
>>> p.nombre
AttributeError: 'Perro' object has no attribute 'nombre'
```

El MRO no "sigue buscando" - encontró `__init__` en `Perro`, lo ejecuta, y termina ahí. No hay llamada automática al padre.

## Búsqueda de atributos

Cuando accedés a `instancia.atributo`, Python busca en orden:

```
instancia.__dict__ → ClaseDerivada.__dict__ → ClaseBase.__dict__ → ... → object.__dict__ → AttributeError
```

Es búsqueda dinámica: si no está en un nivel, sube al siguiente.

## Shadowing de atributos

Definir un atributo con el mismo nombre en la clase derivada **no sobrescribe** el de la base. Ambos existen en [[NameSpaces en Python#Namespace de una clase y de sus instancias|Namespaces distintos]], ya que cada clase tiene su propio Namespace:

```python
class Animal:
    especie = "animal"

class Perro(Animal):
    especie = "canino"    # Shadowing, no override

>>> Animal.especie
'animal'
>>> Perro.especie
'canino'
```

La búsqueda encuentra primero el de `Perro` y nunca llega al de `Animal`.

## Override de métodos

Definir un método con el mismo nombre en la clase derivada **reemplaza** para esa clase y sus instancias, esto se le denomina formalmente como [[Programacion Orientada a Objetos#Polimorfismo|Polimorfismo]]:

```python
class Animal:
    def hablar(self):
        return "Sonido genérico"

class Perro(Animal):
    def hablar(self):
        return "Guau"

>>> Perro().hablar()
'Guau'
```

El método de `Animal` sigue existiendo, pero `Perro().hablar()` ejecuta la versión de `Perro`.

## Todos los métodos son virtuales

En C++, solo los métodos marcados como `virtual` pueden ser sobreescritos dinámicamente. En Python, **todos los métodos se comportan como virtuales**:

```python
class Base:
    def metodo1(self):
        print("Base.metodo1")
        self.metodo2()      # Busca en la instancia actual

    def metodo2(self):
        print("Base.metodo2")

class Derivada(Base):
    def metodo2(self):
        print("Derivada.metodo2")

>>> d = Derivada()
>>> d.metodo1()
Base.metodo1
Derivada.metodo2    # ¡Llamó a la versión de Derivada!
```

`self` siempre es la instancia actual. La búsqueda de métodos empieza desde la clase de `self`.

## `super()` para extender métodos

### Reemplazar (override total)

```python
class Perro(Animal):
    def hablar(self):
        return "Guau"    # No llama al padre
```

### Extender (override + llamada al padre)

```python
class Perro(Animal):
    def hablar(self):
        return f"{super().hablar()}... Guau"
```

Con `__init__`:

```python
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)    # Inicializa Animal
        self.raza = raza            # Agrega lo propio
```

## `super()` vs llamada directa

| | `ClaseBase.metodo(self)` | `super().metodo()` |
|---|---|---|
| Herencia simple | Funciona igual | Funciona igual |
| Herencia múltiple | Puede duplicar llamadas | Sigue el MRO |
| Acoplamiento | Acoplado a la clase específica | Dinámico |

En herencia simple, ambas formas son equivalentes. En herencia múltiple, `super()` es necesario para que cada método se ejecute una sola vez en el orden correcto, pero aca es donde erradica la complejidad ya que se debe comprender el MRO para poder saber que hace super() con certeza y obtener resultados predecibles. Profundizaremos mas adelante en el MRO.

`super()` devuelve un proxy que busca la **siguiente clase en el MRO**, no necesariamente la clase padre directa.

### `super()` requiere contexto

`super()` necesita saber desde qué clase se lo está llamando. Por eso:

| Contexto | `super()` funciona |
|----------|-------------------|
| Método de instancia | ✅ Sí (usa `self`) |
| `@classmethod` | ✅ Sí (usa `cls`) |
| `@staticmethod` | ❌ No (no hay contexto) |
| Fuera de un método | ❌ No (la clase aún no existe) |

```python
class A:
    valor = 1

class B(A):
    @classmethod
    def get_valor(cls):
        return super().valor  # ✅ Funciona

    @staticmethod
    def get_valor_static():
        return super().valor  # ❌ Error: no hay contexto
```

## Funciones útiles

```python
isinstance(obj, Clase)    # True si obj es instancia de Clase o subclase
issubclass(A, B)          # True si A hereda de B
```

## Heredar de clases built-in

Podés heredar de cualquier [[Módulos Built-in de Python#Módulos Built-in de Python|Modulo nativo]] de Python: `list`, `dict`, `str`, `Exception`, etc.

```python
class MiLista(list):
    def primer_elemento(self):
        return self[0] if self else None

>>> ml = MiLista([1, 2, 3])
>>> ml.append(4)           # Hereda todos los métodos de list
>>> ml.primer_elemento()
1
```

### Excepciones personalizadas

Un uso común: crear [[Excepciones en Python#Excepciones|excepciones]] con nombre específico:

```python
class ErrorDeValidacion(Exception):
    pass

class ErrorDeAutenticacion(Exception):
    pass

try:
    # código
except ErrorDeValidacion:
    # manejar error específico
except ErrorDeAutenticacion:
    # manejar otro error
```

Esto permite jerarquías de errores propias sin reescribir lógica.


## Herencia múltiple

Python permite heredar de múltiples clases base:

```python
class A:
    def metodo(self):
        print("A")

class B:
    def metodo(self):
        print("B")

class C(A, B):    # Hereda de A y B
    pass

>>> C().metodo()
A    # ¿Por qué A y no B?
```

Cuando hay múltiples padres, ¿en qué orden Python busca métodos y atributos? Acá entra el **MRO**.

## MRO (Method Resolution Order)

El MRO es el orden en que Python busca atributos y métodos cuando hay herencia múltiple. Es una **lista precalculada** que define la precedencia de búsqueda.

### Cómo ver el MRO

```python
>>> C.mro()
[<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>]

>>> C.__mro__
(<class 'C'>, <class 'A'>, <class 'B'>, <class 'object'>)
```

Cuando buscás `C().metodo()`, Python recorre esa lista en orden: C → A → B → object. Como `A` tiene `metodo`, lo ejecuta y no sigue buscando.

### Intuición del MRO: búsqueda por niveles

El algoritmo real (C3) es complejo, pero hay una forma intuitiva de pensarlo que funciona en casi todos los casos:

**El MRO recorre la jerarquía "por niveles", de izquierda a derecha, sin repetir clases.**

1. La clase misma va primero
2. Después sus bases directas, de izquierda a derecha
3. Después las bases de las bases, respetando el orden
4. Cada clase aparece **una sola vez**
5. Las clases base siempre van **después** de sus derivadas

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

```
      A
     / \
    B   C
     \ /
      D
```

Pensando por niveles:
- Nivel 0: D
- Nivel 1: B, C (de izquierda a derecha)
- Nivel 2: A (base de B y C)

```python
>>> D.mro()
[<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>]
```

La intuición coincide: D → B → C → A → object.

### Caso con bases adicionales

¿Qué pasa si una clase tiene otra base?

```python
class A:
    pass

class B(A):
    pass

class X:
    pass

class C(X, A):    # C hereda de X y A
    pass

class D(B, C):
    pass
```

```
        A
       /|\
      / | \
     B  |  X
      \ | /
       \|/
        D
```

Por niveles: D (nivel 0) → B, C (nivel 1) → A, X (nivel 2)

Pero el MRO real es:

```python
>>> D.mro()
[<class 'D'>, <class 'B'>, <class 'C'>, <class 'X'>, <class 'A'>, <class 'object'>]
```

¿Por qué X antes que A? Porque `C(X, A)` dice "X antes que A". El MRO respeta el orden declarado en cada clase.

La intuición de "por niveles" funciona como guía, pero el MRO también considera las **restricciones de orden** que cada clase impone.

## El problema del diamante

El "diamante" ocurre cuando una clase hereda de dos clases que comparten un ancestro común:

```
      A
     / \
    B   C
     \ /
      D
```

Sin MRO correcto, `A` podría visitarse dos veces. El MRO C3 garantiza que cada clase se visita una sola vez:

```python
class A:
    def metodo(self):
        print("A")

class B(A):
    def metodo(self):
        print("B")
        super().metodo()

class C(A):
    def metodo(self):
        print("C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("D")
        super().metodo()

>>> D().metodo()
D
B
C
A
```

El MRO es `D → B → C → A → object`. Cada clase aparece una vez, y `super()` sigue ese orden.

### ¿Por qué B llama a C y no a A?

Porque `super()` no llama al "padre directo". Llama a la **siguiente clase en el MRO**.

Cuando `B.metodo()` llama a `super().metodo()`:
- El MRO es `D, B, C, A, object`
- La clase actual es `B`
- La siguiente en el MRO es `C`
- Entonces llama a `C.metodo()`

## `super()` en herencia múltiple

En herencia simple, `super()` llama al padre directo. En herencia múltiple, `super()` delega al siguiente en el MRO, formando una cadena cooperativa:

```python
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()

>>> D()
D
B
C
A
```

Una sola llamada a `super().__init__()` en `D` ejecuta **todos** los `__init__` de la jerarquía, una sola vez cada uno.

Si usaras llamadas directas (`A.__init__(self)`), `A` se llamaría dos veces (desde B y desde C). `super()` con MRO evita esa duplicación.

## Cuando el MRO falla: contradicciones

No toda jerarquía tiene un MRO válido. Si las restricciones de orden se contradicen, Python rechaza la clase:

```python
class X:
    pass

class Y:
    pass

class A(X, Y):    # A dice: X antes que Y
    pass

class B(Y, X):    # B dice: Y antes que X
    pass

class C(A, B):    # ¿X antes de Y o Y antes de X?
    pass
```

```python
TypeError: Cannot create a consistent method resolution
order (MRO) for bases X, Y
```

`A` exige que X vaya antes que Y. `B` exige que Y vaya antes que X. No hay forma de ordenarlos sin contradecir a uno. Python se niega a crear la clase.

### ¿Cuándo pasa esto?

Casi nunca en la práctica. Requiere jerarquías deliberadamente contradictorias. El error es una **protección**: Python te está diciendo "tu jerarquía tiene un problema de diseño, arréglalo".

## Resumen: MRO y herencia múltiple

| Concepto | Descripción |
|----------|-------------|
| MRO | Orden de búsqueda de atributos/métodos |
| Ver MRO | `Clase.mro()` o `Clase.__mro__` |
| Intuición | Por niveles, izquierda-derecha, sin repetir |
| `super()` | Sigue el MRO, no el padre directo |
| Diamante | MRO garantiza una sola visita por clase |
| Contradicción | `TypeError` si no hay orden válido |

---
__TE SIENTES DETERMINADO__