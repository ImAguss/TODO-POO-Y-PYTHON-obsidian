---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
  - estructuras
proyecto: aprendizaje-programacion
Creacion: 2026-01-28T21:44:00
Revision: 2026-02-01T16:47:00
---
# Listas Enlazadas

Las listas enlazadas son una colección ordenada de objetos. Lo que las hace diferentes a las listas tradicionales es cómo almacenan estos objetos en memoria. Mientras que las listas usan bloques de memoria contiguos para almacenar los objetos, en las listas enlazadas **enlazamos** bloques de memoria que contienen el valor y una referencia o puntero que va hacia la posición en memoria del siguiente objeto en la lista.

## Conceptos Claves

Antes de ir más profundo en qué son las listas enlazadas y cómo se usan, debemos entender cómo están estructuradas. Cada elemento de la lista enlazada se llama **nodo** y cada nodo tiene dos campos claves:

1. El contenedor de datos que almacena el valor que se guarda en el nodo
2. La referencia al siguiente nodo de la lista, donde se guarda la posición en memoria de dicho nodo.

Imágenes de ejemplo:
![[Group_12_2.0ded5fffe97a.png]]

Una lista enlazada en términos simples es una colección de nodos, donde el primer nodo es llamado la **cabeza** y se usa como punto de partida para cualquier iteración a través de la lista. El último nodo debe tener una referencia de salida que usualmente en todos los lenguajes es un puntero a una dirección nula.

![[Group_14.27f7c4c6ec02.png]]

## Aplicaciones Prácticas

Las listas enlazadas tienen una cantidad increíble de usos. Se usan para **pilas, colas, grafos, árboles**. Son muy útiles cuando se ejecutan sobre tareas complejas, como puede ser el ciclo de vida de un sistema operativo.

### Pilas y Colas

[[Pilas y Colas|Las pilas y colas]] difieren en su filosofía a la hora de insertar y eliminar sus elementos. Mientras que las colas usan FIFO (First In-First Out), las pilas usan LIFO (Last In-First Out), pero todos sus elementos pueden ser almacenados usando una lista enlazada.

**Cola:**
![[Group_6_3.67b18836f065.png]]

**Pila:**
![[Group_7_5.930e25fcf2a0.png]]

### Grafos

Los grafos sirven para mostrar las relaciones entre objetos:

![[Group_20.32afe2d011b9.png]]

Existen varias formas de implementar grafos, pero la más común es usar listas de adyacencia. En esencia es una lista enlazada donde cada vértice del grafo es guardado siguiendo sus conexiones con otros vértices:

```
Vertex   Linked List of Vertices
1        2 → 3 → None
2        4 → None
3        None
4        5 → 6 → None
5        6 → None
6        None
```

Una forma práctica sería almacenarlo en un diccionario:

```python
graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}
```

En términos de velocidad y memoria, implementar grafos usando listas de adyacencia es más eficiente en comparación con las matrices de adyacencia que usan arreglos bidimensionales. Por eso las listas enlazadas son útiles en este tipo de aplicación.

## Comparación de Rendimiento: Arreglos vs Listas Enlazadas

En la mayoría de lenguajes de programación hay diferencias claras entre las listas enlazadas y los arreglos, ya que difieren enormemente en cómo se almacenan en memoria. En Python la historia es distinta pues las listas son [[Arrays#🔍 **Arrays Dinamicos en Python**|Arreglos Dinámicos]]. Por lo que el uso de memoria entre listas Python y las listas enlazadas es bastante similar.

Como la diferencia entre el uso de memoria entre listas enlazadas y arreglos dinámicos es insignificante, lo mejor es compararlos en base a su tiempo de complejidad, que nos sirve para medir cómo rinde un algoritmo con cierta estructura de dato en uso.

### Inserción y Borrado de Elementos

En Python puedes insertar elementos usando `.insert()` o `.append()`. Para remover elementos podemos usar sus contrapartes que son `.remove()` y `.pop()`.

La mayor diferencia entre estos métodos es cómo los usas. `insert()` y `remove()` insertan o eliminan elementos en posiciones específicas de listas, mientras que `append()` y `pop()` insertan o eliminan elementos al final de la lista.

Con todo esto en mente, cuando insertamos con `append()` o `insert()` tendremos una complejidad de O(1) cuando tratamos de insertar un elemento cerca o al principio de la lista, pero a medida que crece la lista, lo hará su complejidad, llegando hasta O(n).

Las listas enlazadas, por otro lado, son mucho más predecibles cuando se trata de insertar o eliminar elementos al principio o al final de la misma, pues su complejidad siempre se mantendrá en O(1).

Por esta razón, las listas enlazadas tienen ventajas de rendimiento en cuanto a las listas normales cuando se implementan filosofías FIFO o LIFO, ya que en estas filosofías estás constantemente insertando o quitando elementos del principio o el final.

### Recuperar Elementos

Cuando se trata de recuperar elementos, aquí los arreglos o listas Python son muchísimo mejores que las listas enlazadas. Con especificar el índice podemos obtener el elemento con una complejidad de O(1), mientras que en las listas enlazadas siempre tenemos que recorrer toda la lista para llegar al elemento que necesitamos, por ello su complejidad es de O(n).

## Herramienta Pythónica: `collections.deque`

En muchos lenguajes existen incorporaciones de módulos similares a este, pero como estamos trabajando con Python lo veremos con dicho lenguaje. En Python tenemos una colección específica que contiene listas enlazadas llamadas `deque`.

`collections.deque` usa una implementación de listas enlazadas que te van a permitir acceder, insertar o eliminar elementos al principio y final de una lista con complejidad de O(1).

### ¿Cómo se usa `collections.deque`?

Existen varios métodos que vienen por defecto con el objeto `deque`. En esta nota solo veremos algunos, como agregar o eliminar elementos.

Primero, necesitas crear la lista enlazada:

```python
>>> from collections import deque
>>> deque()
deque([])
```

El ejemplo de arriba nos creará una lista enlazada vacía. Si quieres crear una, debes hacerlo a partir de un objeto iterable:

```python
>>> deque(['a','b','c'])
deque(['a', 'b', 'c'])

>>> deque('abc')
deque(['a', 'b', 'c'])

>>> deque([{'data': 'a'}, {'data': 'b'}])
deque([{'data': 'a'}, {'data': 'b'}])
```

Cuando inicializas un objeto `deque`, se le puede pasar cualquier objeto que sea iterable como argumento.

Ahora que sabes cómo crear un objeto `deque`, podemos interactuar con él añadiendo o eliminando elementos:

```python
>>> llist = deque("abcde")
>>> llist
deque(['a', 'b', 'c', 'd', 'e'])

>>> llist.append("f")
>>> llist
deque(['a', 'b', 'c', 'd', 'e', 'f'])

>>> llist.pop()
'f'

>>> llist
deque(['a', 'b', 'c', 'd', 'e'])
```

`append()` y `pop()` añaden o eliminan elementos del lado derecho de la lista. Para eliminar del lado izquierdo podemos especificarle:

```python
>>> llist.appendleft("z")
>>> llist
deque(['z', 'a', 'b', 'c', 'd', 'e'])

>>> llist.popleft()
'z'

>>> llist
deque(['a', 'b', 'c', 'd', 'e'])
```

### Cómo Implementar Pilas y Colas

#### Colas

Para las colas quieres agregar valores a la lista (`enqueue`) y cuando se requiera remover el elemento que más estuvo en la lista (`dequeue`). En esto se basa la filosofía FIFO:

```python
>>> from collections import deque
>>> queue = deque()
>>> queue
deque([])

>>> queue.append("Mary")
>>> queue.append("John")
>>> queue.append("Susan")
>>> queue
deque(['Mary', 'John', 'Susan'])
```

Ahora para eliminar siguiendo FIFO debemos eliminar los elementos que más estuvieron en la lista, los cuales serán los primeros que fueron llegando. Por ende se deberá especificar que se deban eliminar los elementos de la izquierda:

```python
>>> queue.popleft()
'Mary'

>>> queue
deque(['John', 'Susan'])

>>> queue.popleft()
'John'

>>> queue
deque(['Susan'])
```

#### Pilas

Para las pilas la idea que se aplica es la de LIFO, es decir que los elementos que se irán eliminando serán aquellos que llegaron últimos. La forma visual de ver esto es una pila de ropa: naturalmente piensas en sacar primero la ropa de arriba que la de abajo.

Para este caso siempre se deben agregar y eliminar elementos del mismo lado. Si vas a insertar por la derecha, eliminas por la derecha; si insertas por la izquierda, eliminas por la izquierda. El siguiente ejemplo se hace con la izquierda para poder visualizar de manera más gráfica una pila de la vida real:

```python
>>> from collections import deque
>>> history = deque()

>>> history.appendleft("https://realpython.com/")
>>> history.appendleft("https://realpython.com/pandas-read-write-files/")
>>> history.appendleft("https://realpython.com/python-csv/")
>>> history
deque(['https://realpython.com/python-csv/',
       'https://realpython.com/pandas-read-write-files/',
       'https://realpython.com/'])
```

## Implementando Nuestra Propia Lista Enlazada

Si bien existen herramientas como `deque` que vimos con anterioridad, estas solo sirven para probar cosas rápidas. Pero siempre que se requiera comportamientos personalizados debes estar preparado para crear tus propias listas enlazadas siguiendo la lógica que tú mismo deseas. Aparte de otras ventajas como:

- Practicar algoritmos
- Aprender sobre teoría de Estructuras de Datos

### Cómo Crear una Lista Enlazada

Lo primero es crear una clase que represente y permita manejar los elementos de la lista:

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

Aunque en este ejemplo solo se especifica la cabeza, también se pueden agregar otros parámetros que sirven para controlar el flujo o estado de la lista. También podríamos poner otro atributo para controlar cuál es el último elemento de la lista.

Como mencionamos al principio, las listas enlazadas están conformadas por nodos. En dichos nodos es donde se almacena la información, para ello se debe crear una clase aparte o dentro de la propia clase de la lista, como uno prefiera:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
```

Aparte del atributo que guarda la información, debemos tener en cuenta que también debe existir el atributo que apunte al siguiente nodo de la lista o el nodo que permita que exista un enlace entre dos nodos.

El método `__repr__` solo sirve para que cuando se imprima el objeto lo haga siguiendo este método. Es útil para debuguear. Y solo para programadores: si no está definido el método `__str__` se ejecutará el `__repr__` por defecto.

```python
>>> llist = LinkedList()
>>> llist
None

>>> first_node = Node("a")
>>> llist.head = first_node
>>> llist
a -> None

>>> second_node = Node("b")
>>> third_node = Node("c")
>>> first_node.next = second_node
>>> second_node.next = third_node
>>> llist
a -> b -> c -> None
```

Esta es una implementación súper básica de listas enlazadas. A partir de acá solo es cuestión de modificarlas o añadir funcionalidades a medida que se vayan requiriendo.

Un ejemplo modificado sería hacer todo en el propio constructor:

```python
def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
        node = Node(data=nodes.pop(0))
        self.head = node
        for elem in nodes:
            node.next = Node(data=elem)
            node = node.next
```

### Cómo Recorrer una Lista Enlazada

Una de las cosas más comunes dentro del uso de las listas enlazadas es el hecho de recorrerlas. Esto significa que debemos pasar por cada nodo, empezando desde la cabeza hasta el nodo final que apunte a un objeto `None`.

Para recorrerlo tenemos varias formas. Para esto debemos iterar sobre la lista enlazada usando cualquier [[Estructuras Iterativas en Python#Estructuras Iterativas en Python|estructura iterativa]] o puedes definir tu propio `__iter__` para hacer esto:

```python
def __iter__(self):
    node = self.head
    while node is not None:
        yield node
        node = node.next
```

```python
>>> llist = LinkedList(["a", "b", "c", "d", "e"])
>>> llist
a -> b -> c -> d -> e -> None

>>> for node in llist:
...     print(node)
a
b
c
d
e
```

Definir un método `__iter__` sirve para predecir o para añadir comportamiento personalizado a la hora de iterar sobre la lista enlazada.

**Nota para deepseek: Hacete un ejemplo un poco más complejo debajo de este, así se ve con más claridad lo que hace el iter**

```python
# Ejemplo más complejo del uso de __iter__
>>> llist = LinkedList(["Python", "Java", "JavaScript", "C++"])
>>> 
>>> # Usando el iterador para buscar un elemento específico
>>> for node in llist:
...     if "Java" in node.data:
...         print(f"Encontrado: {node.data}")
...         break
Encontrado: Java
>>>
>>> # Usando el iterador para transformar datos
>>> long_languages = [node.data for node in llist if len(node.data) > 4]
>>> print(f"Lenguajes con más de 4 letras: {long_languages}")
Lenguajes con más de 4 letras: ['Python', 'JavaScript']
>>>
>>> # Usando el iterador para contar nodos
>>> count = sum(1 for _ in llist)
>>> print(f"Total de nodos: {count}")
Total de nodos: 4
```

### Cómo Insertar un Nuevo Nodo

Existen varias formas de insertar un nodo en una lista enlazada, cada una con su nivel de complejidad e implementación.

#### Insertando al Principio

Insertar un nuevo nodo al principio de la lista enlazada es uno de los caminos más comunes al usar listas enlazadas:

```python
def add_first(self, node):
    node.next = self.head
    self.head = node
```

Esto lo logramos modificando en cada inserción quién es la cabeza de nuestra lista y haciendo que el nuevo nodo apunte a la cabeza antigua para después asignar la nueva cabeza al nuevo nodo.

```python
>>> llist = LinkedList()
>>> llist
None

>>> llist.add_first(Node("b"))
>>> llist
b -> None

>>> llist.add_first(Node("a"))
>>> llist
a -> b -> None
```

#### Insertando al Final

Insertar un nuevo nodo al final de la lista hace que siempre que queramos insertar un nuevo nodo tengamos que recorrer la lista entera, aunque esto se soluciona si añadimos un atributo que guarde el último elemento de la lista (aunque eso no lo veremos en esta nota, lo dejo para que el que lea esto lo piense):

```python
def add_last(self, node):
    if self.head is None:
        self.head = node
        return
    for current_node in self:
        pass
    current_node.next = node
```

```python
>>> llist = LinkedList(["a", "b", "c", "d"])
>>> llist
a -> b -> c -> d -> None

>>> llist.add_last(Node("e"))
>>> llist
a -> b -> c -> d -> e -> None

>>> llist.add_last(Node("f"))
>>> llist
a -> b -> c -> d -> e -> f -> None
```

Esta forma de hacerlo, aunque fea y poco práctica gracias a su elevada complejidad, solo sirve para visualizar cómo se podría implementar una inserción de este estilo. Siempre sirve modificarlo y mejorarlo como menciono más arriba.

#### Insertando entre dos nodos

Insertar entre medio de dos nodos añade otra capa de complejidad a las listas enlazadas, ya que podemos tener dos formas:

- Insertar después del nodo existente
- Insertar antes del nodo existente

En estos casos de inserción es cuando necesitamos que se especifique el nodo o posición específica donde se quiere insertar. Existen muchas formas de hacerlo. Hay una muy elegante que usa un `while`, pero ahora veremos otra posible implementación. Recuerda que siempre puedes razonarlo y mejorarlo:

**Insertar después de un nodo específico:**

```python
def add_after(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    for node in self:
        if node.data == target_node_data:
            new_node.next = node.next
            node.next = new_node
            return

    raise Exception("Node with data '%s' not found" % target_node_data)
```

```python
>>> llist = LinkedList()
>>> llist.add_after("a", Node("b"))
Exception: List is empty

>>> llist = LinkedList(["a", "b", "c", "d"])
>>> llist
a -> b -> c -> d -> None

>>> llist.add_after("c", Node("cc"))
>>> llist
a -> b -> c -> cc -> d -> None

>>> llist.add_after("f", Node("g"))
Exception: Node with data 'f' not found
```

**Insertar antes de un nodo específico:**

```python
def add_before(self, target_node_data, new_node):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        return self.add_first(new_node)

    prev_node = self.head
    for node in self:
        if node.data == target_node_data:
            prev_node.next = new_node
            new_node.next = node
            return
        prev_node = node

    raise Exception("Node with data '%s' not found" % target_node_data)
```

```python
>>> llist = LinkedList()
>>> llist.add_before("a", Node("a"))
Exception: List is empty

>>> llist = LinkedList(["b", "c"])
>>> llist
b -> c -> None

>>> llist.add_before("b", Node("a"))
>>> llist
a -> b -> c -> None

>>> llist.add_before("b", Node("aa"))
>>> llist.add_before("c", Node("bb"))
>>> llist
a -> aa -> b -> bb -> c -> None

>>> llist.add_before("n", Node("m"))
Exception: Node with data 'n' not found
```

Como se puede ver en los ejemplos, debemos ir moviéndonos a través de la lista hasta encontrar la posición o nodo específico donde queremos insertar al nuevo. Una vez ahí, ambas implementaciones difieren ya que la asignación cambia según se quiera insertar antes o después.

**Pista:** La solución elegante se puede hacer con un `while`, eso evitaría que confirmaras con un `if` si estás en el lugar correcto.

### Cómo Eliminar un Nodo

Para eliminar un nodo de una lista enlazada primero debemos buscar dicho nodo atravesando toda la lista. Aunque la solución presentada no es elegante, también sirve.

**Pista:** Una implementación más elegante se logra con `while`.

```python
def remove_node(self, target_node_data):
    if self.head is None:
        raise Exception("List is empty")

    if self.head.data == target_node_data:
        self.head = self.head.next
        return

    previous_node = self.head
    for node in self:
        if node.data == target_node_data:
            previous_node.next = node.next
            return
        previous_node = node

    raise Exception("Node with data '%s' not found" % target_node_data)
```

```python
>>> llist = LinkedList()
>>> llist.remove_node("a")
Exception: List is empty

>>> llist = LinkedList(["a", "b", "c", "d", "e"])
>>> llist
a -> b -> c -> d -> e -> None

>>> llist.remove_node("a")
>>> llist
b -> c -> d -> e -> None

>>> llist.remove_node("e")
>>> llist
b -> c -> d -> None

>>> llist.remove_node("c")
>>> llist
b -> d -> None

>>> llist.remove_node("a")
Exception: Node with data 'a' not found
```

Claramente para este tipo de casos siempre es importante verificar si lo que se va a eliminar es la cabeza de la lista, pues la asignación varía. En estos casos tendríamos una complejidad de O(1).

Lo siguiente que hay que hacer es ir siguiendo y asignando un nodoGUIA que sirva para saber dónde nos encontramos y será con el cual se harán las asignaciones una vez encontremos el nodo deseado.

## Usos Avanzados de Listas Enlazadas

### Listas Doblemente Enlazadas

Las listas doblemente enlazadas tienen la peculiaridad de tener una referencia más que las listas enlazadas normales, la cual es la referencia hacia el anterior.

![[Group_23.a9df781f6087.png]]

El único cambio en código con respecto a las listas enlazadas solamente se produce en la clase del nodo:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
```

![[Group_21.7139fd0c8abb.png]]

Como vimos anteriormente, las colecciones `deque` también poseen listas doblemente enlazadas, por lo que su complejidad a la hora de insertar y eliminar elementos es de O(1).

### Listas Enlazadas Circulares

Las listas enlazadas circulares son un tipo de lista enlazada la cual hace que el último nodo apunte a la cabeza, haciendo que la lista sea infinita en su iteración ya que no apunta a un elemento nulo. Gracias a este comportamiento es que la lista es circular. Este enfoque se suele usar para hacer colas circulares, por ejemplo, que este tipo de colas tienen una complejidad baja con respecto a otras.

![[Group_22.cee69a15dbe3.png]]

Sus aplicaciones son muchas y algunos ejemplos destacados serían:

- Manejar los turnos en un juego multijugador
- Manejar el ciclo de vida de una aplicación dentro de un Sistema Operativo
- Usar la pila de Fibonacci

Donde una de sus ventajas es que puedes atravesar toda la lista desde prácticamente cualquier nodo, no estás restringido a hacerlo desde la cabeza. Lo único que debes procurar es que no se genere un recorrido infinito, lo cual es normal, ya que no tienes un nodo que te marque un "fin", por lo que ahí dependerá de la condición que decidas implementar.

En términos de implementación son muy similares a las listas enlazadas. La única diferencia es que puedes definir el punto de partida cuando iteras la lista:

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))
```

Aunque depende del enfoque, en una implementación básica y de práctica puedes usar el punto de partida como el punto final también, así te aseguras de que se recorra toda la lista. Pero también podrías definir una condición personalizada, como recorrer X cantidad de elementos o parar si tal elemento cumple con tanto. Es un mundo de posibilidades.

```python
>>> circular_llist = CircularLinkedList()
>>> circular_llist.print_list()
None

>>> a = Node("a")
>>> b = Node("b")
>>> c = Node("c")
>>> d = Node("d")
>>> a.next = b
>>> b.next = c
>>> c.next = d
>>> d.next = a
>>> circular_llist.head = a
>>> circular_llist.print_list()
a -> b -> c -> d

>>> circular_llist.print_list(b)
b -> c -> d -> a

>>> circular_llist.print_list(d)
d -> a -> b -> c
```

---
**TE SIENTES DETERMINADO** 