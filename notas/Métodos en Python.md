---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-17T15:18:00
Revision: 2026-02-17T16:26:00
---
# Métodos en Python

Los métodos son uno de los pilares de la programación orientada a objetos en Python. Aunque su sintaxis es muy similar a la de las funciones, es fundamental entender sus diferencias y particularidades para utilizarlos correctamente.

## ¿Qué es un método?

Un **método** es esencialmente una función que está asociada a una clase y, por ende, a los objetos (instancias) de esa clase. Los métodos residen en el [[Namespaces en Python#Namespaces en Python|namespace]] de la clase y son accedidos a través de sus instancias.

Las diferencias clave con una función normal son:

1.  **Pertenencia**: Un método pertenece a una clase y se invoca sobre un objeto (o la propia clase). Al llamarlo, Python pasa automáticamente una referencia al objeto (o clase) como primer argumento.
2.  **Acceso al contexto**: Un método puede acceder y modificar los atributos del objeto sobre el cual fue invocado, gracias a esa referencia implícita (normalmente llamada `self`).

## Sintaxis y tipos de métodos

La declaración de un método sigue la misma estructura que una [[Funciones en Python#Definiendo funciones en Python|función]], pero con la particularidad de que el primer parámetro (por convención `self`) hace referencia a la instancia actual.

### Métodos de instancia

Son los más comunes. Operan sobre una instancia concreta de la clase.

```python
class Mascota:
    def __init__(self, nombre):
        # El método __init__ es un método especial (constructor)
        self.nombre = nombre  # 'self' es la instancia que se está creando

    def saludar(self):
        # 'self' permite acceder a los atributos de la instancia
        print(f"¡Hola! Soy {self.nombre}")

mi_gato = Mascota("Bigotes")
mi_gato.saludar()  # Output: ¡Hola! Soy Bigotes
```

Aquí, `saludar` es un método de instancia. Cuando se llama como `mi_gato.saludar()`, Python convierte automáticamente la llamada a `Mascota.saludar(mi_gato)`, pasando la instancia como argumento `self`.

#### El objeto método (bound method)

Cuando accedés a un método desde una instancia, Python no te da la función directamente. Te da un **objeto método ligado** (bound method):

```python
>>> mi_gato.saludar
<bound method Mascota.saludar of <__main__.Mascota object at 0x...>>
```

Este objeto método encapsula dos cosas:

- **`m.__self__`** → la instancia ligada (`mi_gato`)
- **`m.__func__`** → la función original (`Mascota.saludar`)

Cuando llamás al método, Python arma la llamada internamente:

```python
mi_gato.saludar()    # es equivalente a:
Mascota.saludar(mi_gato)
```

El `self` se pasa automáticamente porque ya está guardado en el objeto método.

**Guardar métodos en variables**

Como el objeto método ya tiene el `self` "empaquetado", podés guardarlo y llamarlo después sin preocuparte por pasar la instancia:

```python
>>> mi_saludo = mi_gato.saludar    # Guardamos el método
>>> mi_saludo()                    # ¡Funciona sin pasar self!
'¡Hola! Soy Bigotes'

>>> mi_saludo.__self__ is mi_gato
True
>>> mi_saludo.__func__ is Mascota.saludar
True
```

Esto es útil para pasar métodos como callbacks o almacenarlos para ejecutarlos más tarde:

```python
# Pasar métodos como callbacks
acciones = [mi_gato.saludar, otro_gato.saludar]

for accion in acciones:
    accion()    # Cada uno saluda con su propio nombre
```

**¡Cuidado!** Este comportamiento de "binding" solo aplica a métodos de instancia. Los métodos de clase ligan automáticamente el `cls`, pero los métodos estáticos devuelven la función directamente (no hay nada que ligar).


### Métodos de clase

Se definen con el [[Decoradores#Decoradores en Python|decorador]] `@classmethod` y reciben la clase (`cls`) como primer argumento, en lugar de la instancia. Pueden modificar el estado de la clase, que es compartido por todas las instancias.

```python
class Contador:
    contador_global = 0

    @classmethod
    def incrementar(cls):
        cls.contador_global += 1

Contador.incrementar()
print(Contador.contador_global)  # Output: 1
```

### Métodos estáticos

Se definen con `@staticmethod`. No reciben ningún argumento automático (ni `self` ni `cls`). Se comportan como funciones normales, pero están dentro del namespace de la clase por organización.

```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Calculadora.sumar(5, 3))  # Output: 8
```

### [[Métodos mágicos en python]] (o "mágicos")

Son métodos con doble guion bajo al inicio y al final (ej. `__init__`, `__str__`, `__repr__`). Permiten definir el comportamiento de los objetos con la sintaxis nativa de Python (como la creación, representación en string, operadores, etc.).

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

p = Punto(3, 4)
print(p)  # Output: Punto(3, 4)  (gracias a __str__)
```

## Conclusión

Como has podido observar, los métodos no tienen una complejidad excesiva. Si ya sabes cómo funcionan las [[Funciones en Python#Funciones en Python|funciones en Python]], dominar los métodos es cuestión de entender su contexto: pertenecen a una clase y reciben un primer argumento especial (`self` o `cls`) que les permite interactuar con el objeto o la clase que los contiene.

Dominar los distintos tipos de métodos te permitirá escribir código más limpio, organizado y verdaderamente orientado a objetos.

---
__TE SIENTES DETERMINADO__