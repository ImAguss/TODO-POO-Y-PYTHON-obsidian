---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-19T19:15:00
Revision: 2026-02-28T21:11:00
---
# Clases en Python

Las clases en Python permiten crear nuevos tipos de datos y crear nuevas instancias de dichas clases. Cada instancia de clase puede tener atributos que mantienen su estado. Entre estos atributos también están los métodos: funciones que pertenecen y son atributos de la clase.

Comparado con otros lenguajes de programación, el mecanismo de clases en Python es una mezcla entre C++ y Modula-3. Las clases en Python utilizan todas las características del [[Programacion Orientada a Objetos#Clases|paradigma orientado a objetos]]; el mecanismo de herencia permite usar como base múltiples clases, donde una clase derivada puede sobrescribir cualquier método de la clase base —esto se llama [[Programacion Orientada a Objetos#Polimorfismo|Polimorfismo]].

En la terminología de C++, los miembros de una clase son todos públicos. Sí, en Python no existe la encapsulación fuerte; profundizaremos esto más adelante. Todas las funciones miembro son virtuales.

## Cómo funcionan los nombres y los objetos

Los objetos, como sabemos, tienen individualidad —o sea, son únicos— y múltiples nombres (en múltiples scopes) pueden estar ligados a un mismo objeto. Esto se conoce como aliasing. No suele apreciarse como una característica destacada de Python, pero es la base de cómo funcionan, por ejemplo, los [[NameSpaces en Python#¿Qué es un namespace?|Namespaces]].

Como bien hemos discutido en muchas notas, los nombres solo guardan referencias a objetos, es decir, posiciones de memoria donde estos se guardan. Esto provoca efectos no controlados cuando se manipulan tipos de datos [[Listas en Python#Mutabilidad La característica clave|Mutables]], pero no tanto con los [[Tuplas en Python#Explorando la inmutabilidad|Inmutables]]. Esta forma de manejar nombres y referencias hace que pasar un objeto sea barato, ya que la implementación solo pasa un puntero. Si una función modifica el objeto pasado como argumento, el llamador verá el cambio. Esto elimina el mecanismo que se ve en C de pasar valores por referencia o por valor, aunque requiere tener especial cuidado al manejar mutables e inmutables.

## Primer vistazo a las clases

### Sintaxis de la definición de una clase

La forma más simple para definir una clase luce así:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

Como podemos ver, las definiciones de clases tienen cierto parecido con las definiciones de [[Funciones en Python#Definiendo funciones en Python|Funciones]]. Esto incluye su comportamiento con el orden de declaración: se ejecutan en tiempo de ejecución, por lo que colocarlas dentro de un `if` hace que se definan solo después de ejecutarse ese bloque.

Cuando una nueva definición de clase es creada, también se crea un nuevo namespace que guarda todos los atributos y el scope local de dicha clase.

Como bien sabemos del [[Programacion Orientada a Objetos#Clases|concepto de POO]], las clases solo sirven como moldes para crear objetos de clase, que usarán el namespace de la clase para crear y asignar los atributos siguiendo el método mágico [[Métodos mágicos en python#Métodos de Inicialización y Construcción|__init__]].

### Objetos de clase

Los objetos clase soportan dos tipos de operaciones: referencia de atributos e instanciación.

La **referencia de atributos** usa la sintaxis estándar de Python: `obj.name`. Un atributo es válido si su nombre está definido dentro de la clase donde el objeto fue creado. Python busca primero en el namespace del objeto; si no está ahí, busca en el namespace de la clase, y si tampoco, en la clase padre.

Entonces, si tenemos:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

`MyClass.i` y `MyClass.f` son referencias a atributos válidas, retornando un entero y un objeto función (NO método). Esto también soporta asignación, por lo que cambiar el valor de `MyClass.i` es totalmente válido. Los métodos mágicos también son atributos de la clase, como puede ser `__doc__`.

La **instanciación** usa la notación de función. Al escribir `x = MyClass()`, Python crea un nuevo objeto de clase y lo liga al nombre `x`. Internamente, primero se ejecuta el método `__new__` para crear la instancia, y luego `__init__` para inicializarla con valores.

Como bien dijimos, la operación de instanciación llama a `__new__` para crear la instancia, pero el método `__init__` es el que inicializa el objeto con valores por defecto. Como bien sabemos, los métodos mágicos se pueden modificar, permitiendo que el programador defina el comportamiento al momento de inicializar el objeto —aunque también se podría modificar `__new__` si se quisiera.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i
# (3.0, -4.5)
```

## Objetos de instancia

Una vez creada una instancia, ¿qué podemos hacer con ella? Los objetos de instancia entienden una sola operación: **referencias de atributos**.

Hay dos tipos de atributos válidos en una instancia:

### Atributos de datos

Los atributos de datos corresponden a las "variables de instancia" en Smalltalk o los "data members" en C++. Son valores almacenados en el objeto, específicos de esa instancia.

La característica más particular de Python es que **los atributos de datos no necesitan declararse**. Se crean dinámicamente cuando se asignan por primera vez:

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

>>> fido = Perro("Fido")
>>> fido.edad = 3           # ¡Se crea dinámicamente!
>>> fido.raza = "Labrador"
>>> fido.edad
3
```

Incluso podemos crear atributos que nunca estuvieron en `__init__`:

```python
>>> fido.trucos = ["dar la pata", "sentarse"]
>>> fido.trucos
['dar la pata', 'sentarse']
```

Y también podemos eliminarlos:

```python
>>> del fido.raza
>>> fido.raza
Traceback (most recent call last):
    ...
AttributeError: 'Perro' object has no attribute 'raza'
```

**¡Cuidado!** Esta flexibilidad es un arma de doble filo. Podés agregar atributos a cualquier instancia en cualquier momento, pero esto puede hacer que tu código sea difícil de seguir si no tenés cuidado.

### Métodos

El otro tipo de atributo de instancia es el **método**. Ya los cubrimos en profundidad en [[Métodos en Python#Métodos en Python|Métodos en Python]], así que aquí solo repasamos la idea clave:

Un método es una función que "pertenece" a un objeto. Cuando accedés a un método desde una instancia, obtenés un **objeto método ligado** (bound method) que ya tiene el `self` empaquetado:

```python
>>> fido.saludar
<bound method Perro.saludar of <__main__.Perro object at 0x...>>

>>> mi_saludo = fido.saludar    # Se puede guardar
>>> mi_saludo()                 # ¡Funciona sin pasar self!
'¡Guau! Soy Fido'
```

Para más detalle sobre el binding, los atributos `__self__` y `__func__`, y los distintos tipos de métodos, ver [[Métodos en Python#Métodos en Python|Métodos en Python]].

## Variables de clase vs variables de instancia

Hasta ahora vimos atributos definidos en `__init__` como `self.nombre = nombre`. Estos son **atributos de instancia**: cada objeto tiene su propia copia, guardada en su propio namespace. Pero también existen las **variables de clase**: atributos definidos directamente en el cuerpo de la clase, fuera de cualquier método.

```python
class Perro:
    especie = "Canis familiaris"   # Variable de clase (compartida)
    
    def __init__(self, nombre):
        self.nombre = nombre        # Variable de instancia (única)
```

Las variables de clase pertenecen al [[Namespaces en Python#Namespace de una clase y de sus instancias|namespace de la clase]] y son compartidas por todas las instancias:

```python
>>> fido = Perro("Fido")
>>> buddy = Perro("Buddy")

>>> fido.especie
'Canis familiaris'
>>> buddy.especie
'Canis familiaris'
>>> Perro.especie
'Canis familiaris'
```

Todas las instancias acceden a la misma variable porque Python **busca primero en el namespace de la instancia**, y si no encuentra, sube al namespace de la clase.

### ¿Qué pasa cuando una instancia asigna?

Acá está la clave: cuando una instancia hace una asignación, **siempre escribe en su propio namespace**, nunca en el de la clase.

```python
>>> fido.especie = "Canis lupus"
```

Esta línea NO modifica `Perro.especie`. Lo que hace es **crear un atributo nuevo** en el namespace de `fido`:

```python
>>> fido.__dict__
{'nombre': 'Fido', 'especie': 'Canis lupus'}
>>> Perro.__dict__['especie']
'Canis familiaris'                   # La clase sigue igual
>>> buddy.__dict__
{'nombre': 'Buddy'}                  # buddy no tiene 'especie'
>>> buddy.especie
'Canis familiaris'                   # buddy ve la variable de clase
```

El mecanismo de búsqueda de atributos es:

1. Python busca en `fido.__dict__` → encuentra `'especie'` → lo devuelve
2. Si no estuviera, buscaría en `Perro.__dict__`
3. Si tampoco, buscaría en las clases padre

Esto se llama **shadowing**: la instancia "tapona" la variable de clase con su propia versión, pero **sin modificar la clase ni otras instancias**.

### La instancia sigue conectada a la clase

Aunque la instancia tiene su propio namespace para escribir, **sigue conectada a la clase** para leer. Si la clase cambia un atributo que la instancia NO tiene, la instancia ve el cambio:

```python
class Perro:
    especie = "Canis familiaris"

>>> fido = Perro("Fido")
>>> fido.especie                    # No está en fido.__dict__
'Canis familiaris'                   # Lo encuentra en Perro.__dict__

>>> Perro.especie = "Canis lupus"   # Cambio la CLASE
>>> fido.especie                    # fido ve el cambio
'Canis lupus'
```

Pero si `fido` ya tiene ese atributo:

```python
>>> fido.especie = "Gato"           # Crea atributo en fido.__dict__
>>> fido.__dict__
{'nombre': 'Fido', 'especie': 'Gato'}

>>> Perro.especie = "Nuevo valor"    # Cambio la clase
>>> fido.especie                    # fido NO ve el cambio
'Gato'                               # Tiene su propio 'especie'
```

### Con mutables: el problema real

El shadowing con inmutables no rompe nada. El problema aparece cuando la variable de clase es **mutable** (lista, diccionario, etc.) y una instancia la **modifica** en lugar de asignar:

```python
class Perro:
    trucos = []                     # Variable de clase mutable
    
    def agregar_truco(self, truco):
        self.trucos.append(truco)    # Modifica, NO asigna
```

```python
>>> fido = Perro("Fido")
>>> buddy = Perro("Buddy")

>>> fido.agregar_truco("dar la pata")
>>> fido.trucos
['dar la pata']
>>> buddy.trucos                    # ¡También se modificó!
['dar la pata']
>>> Perro.trucos                    # La clase también cambió
['dar la pata']
```

¿Por qué? Porque `append` no asigna, **modifica el objeto existente**. Y ese objeto vive en el namespace de la clase, no en el de la instancia.

```python
>>> fido.__dict__
{'nombre': 'Fido'}                   # No tiene 'trucos'
>>> Perro.__dict__['trucos']
['dar la pata']                     # La lista está en la clase
```

`fido.trucos` busca en la clase, encuentra la lista, y `append` la modifica. Como todas las instancias comparten esa referencia, el cambio las afecta a todas.

**Solución:** definir mutables en `__init__` para que cada instancia tenga su propio objeto:

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = []            # Cada instancia tiene SU lista
```

### ¿Cuándo usar variables de clase?

Tienen usos legítimos:

1. **Constantes de clase** — valores inmutables compartidos:

```python
class Perro:
    especie = "Canis familiaris"
    PATAS = 4
```

2. **Contador de instancias** — llevar registro de cuántos objetos se crearon:

```python
class Perro:
    cantidad = 0
    
    def __init__(self, nombre):
        self.nombre = nombre
        Perro.cantidad += 1         # Modifica la CLASE, no la instancia
```

3. **Valores por defecto** — defaults que pueden cambiar pero tienen un valor común:

```python
class Perro:
    alimento_favorito = "carne"
    
    def __init__(self, nombre, alimento=None):
        self.nombre = nombre
        self.alimento = alimento or Perro.alimento_favorito
```

**Regla práctica:** si el atributo debe ser único por instancia, definilo en `__init__`. Si es compartido e inmutable, puede ser variable de clase. Nunca uses mutables como variables de clase a menos que sepas exactamente lo que estás haciendo.

## Convenciones en Python

Python no tiene encapsulación fuerte como otros lenguajes orientados a objetos. Todo es público por defecto. Las "reglas" son **convenciones** que la comunidad respeta, pero el lenguaje no las enforcementa.

### La "encapsulación fantasma"

Python ofrece dos convenciones para indicar visibilidad:

- **`_atributo`** (un guion bajo): "protegido" — señalamos que no debería tocarse desde afuera, pero se puede acceder sin problemas.
- **`__atributo`** (dos guiones bajos): "privado" — Python aplica *name mangling*, renombrando el atributo a `_Clase__atributo`. Se puede acceder, pero es más incómodo.

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo           # "Protegido"
        self.__secreto = "1234"       # "Privado"
    
    def mostrar(self):
        print(f"Saldo: {self._saldo}")

>>> c = Cuenta(1000)
>>> c._saldo                        # Accesible, pero "no deberías"
1000
>>> c.__secreto                     # Error aparente
Traceback (most recent call last):
    ...
AttributeError: 'Cuenta' object has no attribute '__secreto'

>>> c._Cuenta__secreto              # Pero existe, con otro nombre
'1234'
```

El *name mangling* de `__` existe principalmente para evitar colisiones de nombres en herencia, no para encapsulación real.

### `self` es solo convención

El nombre `self` no tiene significado especial para Python. Podés usar cualquier otro nombre:

```python
class Perro:
    def __init__(yo_mismo, nombre):
        yo_mismo.nombre = nombre
    
    def ladrar(el_bicho):
        return f"¡Guau! Soy {el_bicho.nombre}"

>>> p = Perro("Fido")
>>> p.ladrar()
'¡Guau! Soy Fido'
```

Funciona, pero **romper esta convención hace el código ilegible** para otros programadores Python.

### Filosofía: convenciones sobre restricciones

Python prefiere confiar en el programador. La filosofía es:

> "Somos todos adultos aquí."

El lenguaje te permite hacer casi cualquier cosa, pero la comunidad espera que respetes las convenciones. Código que las ignora funciona, pero es difícil de mantener y entender.

```python
# Funciona, pero es terrible
class X:
    def __init__(s, n):
        s._X__dato = n      # Name mangling manual
    
    def get(self):
        return self._X__dato
```

### Otros usos de convenciones

- **Constantes en MAYÚSCULAS**: `PI = 3.14159` — indica "no modificar"
- **Métodos "privados"**: `_metodo_interno()` — indica "no llamar desde afuera"
- **Dunder methods**: `__init__`, `__str__` — métodos especiales del lenguaje, no inventar propios con doble guion bajo

### `__class__` y la introspección

Cada objeto tiene `__class__`, que guarda su tipo:

```python
>>> fido.__class__
<class '__main__.Perro'>
>>> type(fido)
<class '__main__.Perro'>
>>> fido.__class__.__name__
'Perro'
```

Esto es útil para introspección y verificación de tipos en tiempo de ejecución.

---
__TE SIENTES DETERMINADO__
