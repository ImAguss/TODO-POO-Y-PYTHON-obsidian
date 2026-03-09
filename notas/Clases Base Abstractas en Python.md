---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
  - poo
proyecto: aprendizaje-python
Creacion: 2026-03-09T14:00:00
Revision: 2026-03-09T15:06:00
---
# Clases Base Abstractas en Python

Una [[Programacion Orientada a Objetos#Herencia|clase abstracta]] es aquella que define una **interfaz** pero no necesariamente su implementación. No puede ser instanciada directamente; su propósito es servir como plantilla para otras clases.

En lenguajes como Java o C#, las clases abstractas y las interfaces son conceptos distintos. En Python, la línea es más difusa: las **Clases Base Abstractas (ABC)** del módulo `abc` cubren ambos casos.

## ¿Por qué necesitas clases abstractas?

Sin clases abstractas, no hay forma de forzar a las subclases a implementar ciertos métodos:

```python
# Sin ABC: nada impide olvidar implementar un método
class Figura:
    def area(self):
        pass  # Esperamos que las subclases lo implementen...

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    # ¡Oops! Olvidamos implementar area()

c = Circulo(5)
c.area()  # Retorna None, no hay error hasta que lo uses
```

Con ABC, Python **impide** instanciar clases que no implementan todos los métodos abstractos.

## Crear una clase abstracta con `abc`

El módulo `abc` (Abstract Base Class) proporciona las herramientas:

```python
from abc import ABC, abstractmethod

class Figura(ABC):
    """Clase abstracta: define la interfaz común para todas las figuras."""

    @abstractmethod
    def area(self):
        """Método abstracto: las subclases DEBEN implementarlo."""
        pass

    @abstractmethod
    def perimetro(self):
        """Otro método abstracto."""
        pass

    def descripcion(self):
        """Método concreto: las subclases lo heredan tal cual."""
        return f"Soy una figura con área {self.area()} y perímetro {self.perimetro()}"
```

### Intentar instanciar la clase abstracta

```python
>>> f = Figura()
TypeError: Can't instantiate abstract class Figura with abstract methods area, perimetro
```

Python **no permite** instanciar una clase con métodos abstractos sin implementar.

### Implementar en subclases concretas

```python
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        import math
        return math.pi * self.radio ** 2

    def perimetro(self):
        import math
        return 2 * math.pi * self.radio
```

Ahora se pueden instanciar:

```python
>>> r = Rectangulo(4, 5)
>>> r.area()
20
>>> r.descripcion()
'Soy una figura con área 20 y perímetro 18'

>>> c = Circulo(3)
>>> c.area()
28.274333882308138
```

## Métodos abstractos con implementación

Un método abstracto puede tener implementación que las subclases pueden reutilizar:

```python
from abc import ABC, abstractmethod

class Cuerpo(ABC):
    """Clase abstracta para cuerpos geométricos 3D."""

    def __init__(self, altura):
        self._altura = altura

    @abstractmethod
    def superficie_base(self):
        """Las subclases deben implementar cómo calcular la base."""
        pass

    def volumen(self):
        """Método concreto que usa el método abstracto."""
        return self.superficie_base() * self._altura

class Cilindro(Cuerpo):
    def __init__(self, altura, radio):
        super().__init__(altura)
        self._radio = radio

    def superficie_base(self):
        import math
        return math.pi * self._radio ** 2

class ParalelepipedoRectangulo(Cuerpo):
    def __init__(self, altura, base, profundidad):
        super().__init__(altura)
        self._base = base
        self._profundidad = profundidad

    def superficie_base(self):
        return self._base * self._profundidad
```

```python
>>> cilindro = Cilindro(altura=10, radio=3)
>>> cilindro.volumen()
282.7433388230814

>>> pr = ParalelepipedoRectangulo(altura=10, base=4, profundidad=5)
>>> pr.volumen()
200
```

## Propiedades abstractas

También puedes declarar propiedades abstractas:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @property
    @abstractmethod
    def nombre_cientifico(self):
        pass

    @property
    @abstractmethod
    def sonido(self):
        pass

class Perro(Animal):
    @property
    def nombre_cientifico(self):
        return "Canis lupus familiaris"

    @property
    def sonido(self):
        return "Guau"

class Gato(Animal):
    @property
    def nombre_cientifico(self):
        return "Felis catus"

    @property
    def sonido(self):
        return "Miau"
```

## Clases abstractas con métodos de clase y estáticos

```python
from abc import ABC, abstractmethod

class BaseDeDatos(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def desconectar(self):
        pass

    @classmethod
    @abstractmethod
    def nombre_driver(cls):
        pass

    @staticmethod
    @abstractmethod
    def validar_conexion_string(conn_string):
        pass
```

**Orden de decoradores**: `@classmethod` y `@staticmethod` van **sobre** `@abstractmethod`, no al revés.

## Herencia de múltiples ABC

Python permite heredar de múltiples clases abstractas:

```python
from abc import ABC, abstractmethod

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Nadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Pato(Volador, Nadador):
    def volar(self):
        return "Volando con alas"

    def nadar(self):
        return "Nadando con patas"

>>> p = Pato()
>>> p.volar()
'Volando con alas'
>>> p.nadar()
'Nadando con patas'
```

## ABC vs Interfaces "puras"

En Java, una **interfaz** solo declara métodos (sin implementación) y una **clase abstracta** puede tener métodos implementados. En Python:

```python
# Estilo "interfaz pura": todos los métodos abstractos
class InterfazRepositorio(ABC):
    @abstractmethod
    def guardar(self, entidad):
        pass

    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass

# Estilo "clase abstracta": mezcla métodos abstractos y concretos
class RepositorioBase(ABC):
    def __init__(self, conexion_string):
        self._conexion_string = conexion_string

    @abstractmethod
    def _obtener_conexion(self):
        pass

    def guardar(self, entidad):
        conexion = self._obtener_conexion()
        # Implementación común usando el método abstracto
        print(f"Guardando {entidad} en {conexion}")

    def buscar(self, id):
        conexion = self._obtener_conexion()
        print(f"Buscando {id} en {conexion}")
```

## Cuándo usar ABC

| Situación | ¿ABC? |
|-----------|-------|
| Definir una interfaz común para múltiples implementaciones | ✅ Sí |
| Forzar a las subclases a implementar ciertos métodos | ✅ Sí |
| Proporcionar implementación parcial compartida | ✅ Sí |
| Simplemente compartir código entre clases | ❌ No (usar herencia simple o mixin) |
| Solo necesitas que las subclases "funcionen igual" | ❌ No (duck typing es suficiente) |

## Duck typing vs ABC

Python permite **duck typing**: "si camina como un pato y cuaca como un pato, entonces es un pato". No necesitas heredar de una clase base para que el código funcione:

```python
# Sin ABC: duck typing
class Pato:
    def hacer_sonido(self):
        print("Cuac")

class Perro:
    def hacer_sonido(self):
        print("Guau")

def hacer_sonir(animal):
    animal.hacer_sonido()  # Funciona con cualquier objeto que tenga hacer_sonido()

hacer_sonir(Pato())  # Cuac
hacer_sonir(Perro())  # Guau
```

Usa **ABC** cuando:
- Quieres documentar explícitamente la interfaz esperada
- Necesitas que Python **impida** instanciar clases incompletas
- Quieres usar `isinstance(obj, MiABC)` para verificación de tipos
- Trabajas en un equipo grande donde la claridad es crítica

## `isinstance()` con ABC

Una ventaja de ABC es que permite verificación de tipos basada en interfaz:

```python
from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def to_dict(self):
        pass

class Usuario(Serializable):
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def to_dict(self):
        return {"nombre": self.nombre, "email": self.email}

>>> u = Usuario("Juan", "juan@email.com")
>>> isinstance(u, Serializable)
True

>>> "string".to_dict()
AttributeError: 'str' object has no attribute 'to_dict'
>>> isinstance("string", Serializable)
False
```

## El registro virtual con `register()`

Un ABC puede registrar clases que **no heredan de él**, haciendo que `isinstance()` funcione:

```python
from abc import ABC

class MiInterfaz(ABC):
    pass

class ClaseIndependiente:
    pass

# Registrar virtualmente
MiInterfaz.register(ClaseIndependiente)

>>> obj = ClaseIndependiente()
>>> isinstance(obj, MiInterfaz)
True
```

Esto es útil para hacer que tipos existentes (como tipos built-in) se comporten como instancias de tu ABC.

## Resumen

| Concepto | Sintaxis |
|----------|----------|
| Clase abstracta | `class MiClase(ABC):` |
| Método abstracto | `@abstractmethod def metodo(self): pass` |
| Propiedad abstracta | `@property @abstractmethod def prop(self): pass` |
| No instanciable | `TypeError` si quedan métodos abstractos |
| Herencia parcial | Subclases que no implementan todo → también abstractas |

Las ABC en Python sirven para:
1. **Definir contratos**: forzar a las subclases a implementar métodos
2. **Documentar interfaces**: hacer explícito qué métodos se esperan
3. **Verificar tipos**: usar `isinstance()` basado en interfaz
4. **Compartir código**: implementación parcial en la clase base

---
__TE SIENTES DETERMINADO__