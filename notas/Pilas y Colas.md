---
estado: Terminado
tags:
  - aprendizaje
  - estructuras
  - programacion
proyecto: aprendizaje-programacion
Creacion: 2026-02-06T18:57:00
Revision: 2026-02-07T07:32:00
---
# Tabla de Contenidos
- [[#Base Teórica de Pilas|Base Teórica de Pilas]]
	- [[#Base Teórica de Pilas#Especificación|Especificación]]
	- [[#Base Teórica de Pilas#Operaciones Asociadas al TAD Pila|Operaciones Asociadas al TAD Pila]]
	- [[#Base Teórica de Pilas#Ejemplo de Aplicación de una Pila|Ejemplo de Aplicación de una Pila]]
	- [[#Base Teórica de Pilas#Representaciones de una Pila|Representaciones de una Pila]]
		- [[#Representaciones de una Pila#Representación Secuencial|Representación Secuencial]]
		- [[#Representaciones de una Pila#Representación Encadenada|Representación Encadenada]]
	- [[#Base Teórica de Pilas#Implementación en Python|Implementación en Python]]
		- [[#Implementación en Python#Representación Secuencial (con tamaño máximo)|Representación Secuencial (con tamaño máximo)]]
		- [[#Implementación en Python#Representación Encadenada (con nodos)|Representación Encadenada (con nodos)]]
- [[#Base Teórica de Colas|Base Teórica de Colas]]
	- [[#Base Teórica de Colas#Especificación|Especificación]]
	- [[#Base Teórica de Colas#TAD Cola|TAD Cola]]
	- [[#Base Teórica de Colas#Simulaciones|Simulaciones]]
		- [[#Simulaciones#Ejemplo: Simulación de un Cajero Automático|Ejemplo: Simulación de un Cajero Automático]]
	- [[#Base Teórica de Colas#Representación del TAD Cola|Representación del TAD Cola]]
		- [[#Representación del TAD Cola#Representación Secuencial Lineal|Representación Secuencial Lineal]]
		- [[#Representación del TAD Cola#Representación Secuencial Circular (Recomendada)|Representación Secuencial Circular (Recomendada)]]
		- [[#Representación del TAD Cola#Representación Encadenada|Representación Encadenada]]
	- [[#Base Teórica de Colas#Implementación en Python|Implementación en Python]]
		- [[#Implementación en Python#Representación Secuencial Circular|Representación Secuencial Circular]]
		- [[#Implementación en Python#Representación Encadenada|Representación Encadenada]]
# Pilas y Colas

## Base Teórica de Pilas

Las pilas son secuencias de elementos que pueden crecer y contraerse siguiendo una política específica llamada **LIFO** (Last In, First Out), o "último en entrar, primero en salir". También se le conoce como *stack* (en inglés).

Esta estructura de datos puede utilizarse para resolver una buena cantidad de problemas que se ajusten a la filosofía LIFO.

### Especificación

Una **pila** es una secuencia de cero o más elementos de un tipo determinado que obedece la política LIFO:

**P = (a₁, a₂, ..., aₙ), n ≥ 0**

Dado que esta secuencia puede crecer y contraerse, debemos definir por cuál extremo se ingresan o retiran los elementos (por ejemplo, el extremo derecho).

**P** es una [[Funciones en Python#1. Abstracción|abstracción]] de una realidad que se rige según la política LIFO. Podemos imaginarla como una pila de bandejas, donde la última que se coloca es la primera que se retira. En este caso, cada `aᵢ` representa una bandeja particular.

Si representamos la secuencia verticalmente, con `aₙ` como el último elemento ingresado, decimos que `aₙ` es el elemento que se encuentra en el **tope** o **cima** de la pila. Por lo tanto, llamaremos **tope** al extremo por el cual se ingresan y eliminan elementos. Siempre que se respete que el mismo extremo se use para ambas operaciones, el principio LIFO se cumple.

### Operaciones Asociadas al TAD Pila

| Nombre   | Encabezado       | Función (Entrada)                                                                 | Salida                                                                                                     |
| :------- | :--------------- | :-------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| Insertar | `Insertar(P, X)` | Ingresa el elemento `X` en la pila `P`.                                           | `P = (a₁, a₂, ..., aₙ, X)`                                                                                 |
| Suprimir | `Suprimir(P, X)` | Si `P` no está vacía, elimina el elemento que fue insertado más recientemente.    | Si `n > 0`: `P = (a₁, a₂, ..., aₙ₋₁)` y `X = aₙ`. Error en caso contrario.                                |
| Recorrer | `Recorrer(P)`    | Procesa todos los elementos de `P` siguiendo la política LIFO.                    | Está sujeta al proceso que se realice sobre los elementos.                                                 |
| Crear    | `Crear(P)`       | Inicializa `P`.                                                                   | `P = ( )` (pila vacía).                                                                                    |
| Vacía    | `Vacía(P)`       | Evalúa si `P` tiene elementos.                                                    | `True` si `P` no tiene elementos, `False` en caso contrario.                                               |

Las operaciones `Crear` y `Vacía` son necesarias para inicialización y verificación (equivaldrían al `__init__` y a una verificación de longitud en Python).

### Ejemplo de Aplicación de una Pila

Se desea controlar la correspondencia de pares `[` / `]`, `{` / `}` y `(` / `)` en una expresión aritmética donde los operandos son identificados por un solo carácter.

**Solución intuitiva utilizando una pila:**

*   `P`: Pila de caracteres `[`, `{`, `(`.
*   `X`, `aux`: Variables de tipo carácter.
*   `Expresión`: La expresión a validar.

**Algoritmo en pseudocódigo:**
```
Recuperar(Expresión, X)
MIENTRAS (No fin de Expresión) y (No Error) HACER
    SI (X = "[" ó X = "{" ó X = "(") ENTONCES
        Insertar(P, X)
    FIN SI
    SI (X = "]" ó X = "}" ó X = ")") ENTONCES
        Suprimir(P, aux)
        SI (No Error) ENTONCES
            SI (X = "]" y aux ≠ "[") ó (X = "}" y aux ≠ "{") ó (X = ")" y aux ≠ "(") ENTONCES
                Error = Verdadero
            FIN SI
        FIN SI
    FIN SI
    Recuperar(Expresión, X)
FIN MIENTRAS
SI (No Vacía(P) ó Error) ENTONCES
    Mostrar "ERROR DE CORRESPONDENCIA"
SINO
    Mostrar "CORRESPONDENCIA"
FIN SI
```

**Seguimiento del algoritmo para la expresión `{[(A-B)*C]^D}`:**

| Carácter | Acción en la Pila (tope a la derecha) | Estado                          |
| :------- | :------------------------------------ | :------------------------------ |
| `{`      | Insertar `{` → `{`                    |                                 |
| `[`      | Insertar `[` → `{[`                   |                                 |
| `(`      | Insertar `(` → `{[(`                  |                                 |
| `)`      | Suprimir `(` → `{[`                   | `)` coincide con `(` → OK       |
| `]`      | Suprimir `[` → `{`                    | `]` coincide con `[` → OK       |
| `}`      | Suprimir `{` → ` ` (vacía)            | `}` coincide con `{` → OK       |
| Fin      | Pila vacía y sin errores              | **Resultado: CORRESPONDENCIA**  |

**Resultados para otras expresiones:**
*   `{([A-B)*C]^D}` → **ERROR DE CORRESPONDENCIA** (cierra `)` pero el tope es `[`).
*   `{([A-B)*C]^D` → **ERROR DE CORRESPONDENCIA** (la pila no queda vacía).
*   `{[A-B)*C]^D}` → **ERROR DE CORRESPONDENCIA** (cierra `)` pero el tope es `[`).

### Representaciones de una Pila

#### Representación Secuencial
Los elementos se almacenan en un [[Arrays#¿Qué son los Arreglos en Python?|arreglo]]. Se añade una variable (por ejemplo, `tope`) que indica el índice del último elemento insertado.

![[2026-02-06_19-20-34.png]]
*Estructura: un arreglo `items` y un entero `tope`.*

#### Representación Encadenada
Cada elemento se almacena en un nodo ([[Listas Enlazadas#Listas Enlazadas|celda de lista enlazada]]). Cada nodo contiene el dato y un enlace al siguiente elemento. Se mantiene un puntero/referencia al nodo del tope.

![[2026-02-06_19-45-47.png]]
*Estructura: un puntero `tope` que apunta al primer nodo de una lista enlazada simple.*

### Implementación en Python

#### Representación Secuencial (con tamaño máximo)
```python
class PilaSecuencial:
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.items = [None] * capacidad  # Arreglo de tamaño fijo
        self.tope = -1  # Índice del último elemento. -1 significa pila vacía.

    def vacia(self) -> bool:
        return self.tope == -1

    def llena(self) -> bool:
        return self.tope == self.capacidad - 1

    def insertar(self, x):
        """Apila un elemento (push)."""
        if self.llena():
            raise OverflowError("La pila está llena")
        self.tope += 1
        self.items[self.tope] = x
        return x

    def suprimir(self):
        """Desapila y devuelve el elemento del tope (pop)."""
        if self.vacia():
            raise IndexError("La pila está vacía")
        x = self.items[self.tope]
        self.items[self.tope] = None  # Opcional, para limpieza
        self.tope -= 1
        return x

    def recorrer(self):
        """Muestra los elementos desde el tope hasta la base."""
        if not self.vacia():
            for i in range(self.tope, -1, -1):
                print(self.items[i])
        else:
            print("Pila vacía")

    def mostrar_tope(self):
        """Devuelve el elemento en el tope sin eliminarlo (peek)."""
        if self.vacia():
            return None
        return self.items[self.tope]
```

#### Representación Encadenada (con nodos)
```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class PilaEncadenada:
    def __init__(self):
        self.tope = None  # Puntero al primer nodo (tope de la pila)
        self.cantidad = 0

    def vacia(self) -> bool:
        return self.tope is None

    def insertar(self, x):
        """Apila un elemento (push)."""
        nuevo_nodo = Nodo(x)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.cantidad += 1
        return x

    def suprimir(self):
        """Desapila y devuelve el elemento del tope (pop)."""
        if self.vacia():
            raise IndexError("La pila está vacía")
        x = self.tope.dato
        self.tope = self.tope.siguiente
        self.cantidad -= 1
        return x

    def recorrer(self):
        """Muestra los elementos desde el tope hasta la base."""
        actual = self.tope
        if actual is None:
            print("Pila vacía")
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def mostrar_tope(self):
        """Devuelve el elemento en el tope sin eliminarlo (peek)."""
        if self.vacia():
            return None
        return self.tope.dato
```

## Base Teórica de Colas

Las colas, al igual que las pilas, son secuencias de elementos que pueden crecer y contraerse siguiendo la política **FIFO** (First In, First Out), o "primero en entrar, primero en salir". Esto establece un orden temporal entre los elementos.

### Especificación

Una **cola** es una secuencia de cero o más elementos de un tipo determinado que obedece a la política FIFO:

**C = (a₁, a₂, ..., aₙ), n ≥ 0**

Si la cola tiene elementos (n > 0), entonces:
*   `a₁` es el **primer** elemento (el que más tiempo lleva esperando).
*   `aₙ` es el **último** elemento (el que acaba de llegar).

La cola crece por un extremo (el **frente** o **final**) y se contrae por el opuesto (el **principio** o **frente**). Un nuevo elemento ingresa después del último, y el elemento que sale es siempre el primero.

Podemos imaginar **C** como una cola de clientes esperando ser atendidos por un cajero. Cada `aᵢ` representa un cliente.

### TAD Cola

| Nombre   | Encabezado       | Función (Entrada)                                                             | Salida                                                                                              |
| :------- | :--------------- | :---------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| Insertar | `Insertar(C, X)` | Ingresa el elemento `X` en la cola `C`.                                       | `C = (a₁, a₂, ..., aₙ, X)`                                                                          |
| Suprimir | `Suprimir(C, X)` | Si `C` no está vacía, elimina el elemento que más tiempo ha estado en la cola. | Si `n > 0`: `C = (a₂, ..., aₙ)` y `X = a₁`. Error en caso contrario.                               |
| Recorrer | `Recorrer(C)`    | Procesa todos los elementos de `C` siguiendo la política FIFO.                | Está sujeta al proceso que se realice sobre los elementos.                                          |
| Crear    | `Crear(C)`       | Inicializa `C`.                                                               | `C = ( )` (cola vacía).                                                                             |
| Vacía    | `Vacía(C)`       | Evalúa si `C` tiene elementos.                                                | `True` si `C` no tiene elementos, `False` en caso contrario.                                        |

### Simulaciones

Una de las áreas donde el TAD Cola es más útil es en la **simulación**, la técnica que permite imitar el comportamiento de un sistema del mundo real a lo largo del tiempo. Esto nos permite analizar, predecir o mejorar su comportamiento sin riesgos reales.

*   **Simulación discreta:** Las variables de estado cambian en puntos específicos en el tiempo.
*   **Simulación continua:** Las variables cambian de forma constante en el tiempo.

Un programa de simulación representa el estado del sistema mediante variables. Permite obtener datos clave, como la longitud máxima de una cola o el tiempo promedio de espera, para fundamentar decisiones (ej., número de cajeros necesarios, tamaño del espacio de espera).

La principal dificultad es traducir el sistema físico a estructuras de datos y algoritmos informáticos.

#### Ejemplo: Simulación de un Cajero Automático

**Objetivo:** Conocer el tiempo promedio de espera de los clientes en la cola.

**Componentes del sistema:**
1.  **Cajero/Servidor:** Se representa con un contador que indica cuántos minutos faltan para terminar la transacción actual. Si es `0`, está libre.
2.  **Cola de clientes:** Cada cliente se representa por el momento (reloj) en que llegó al sistema.
3.  **Reloj:** Un contador que avanza minuto a minuto hasta el tiempo máximo de simulación.

**Eventos por minuto:**
*   Puede llegar (o no) un nuevo cliente a la cola.
*   Si el cajero está libre y la cola no está vacía, comienza a atender al primer cliente.
*   Los clientes que aún esperan en la cola incrementan su tiempo de espera.

**Algoritmo en pseudocódigo:**
```
Ingresar: Frecuencia de llegada (x), Tiempo de atención (y), Tiempo máximo de simulación.
Inicializar Reloj = 0, Cajero = 0 (libre), Cola vacía, TiempoAcumulado = 0, ClientesAtendidos = 0.

MIENTRAS Reloj < Tiempo máximo HACER
    SI (llega un cliente según frecuencia x) ENTONCES
        Insertar(Cola, Reloj)  # Se guarda el tiempo de llegada
    FIN SI

    SI Cajero == 0 ENTONCES  # Si el cajero está libre
        SI NO Vacía(Cola) ENTONCES
            Suprimir(Cola, HoraLlegadaCliente)
            TiempoEspera = Reloj - HoraLlegadaCliente
            TiempoAcumulado = TiempoAcumulado + TiempoEspera
            ClientesAtendidos = ClientesAtendidos + 1
            Cajero = y  # Ocupar al cajero por 'y' minutos
        FIN SI
    FIN SI

    Reloj = Reloj + 1
    SI Cajero > 0 ENTONCES
        Cajero = Cajero - 1  # Descontar un minuto de atención
    FIN SI
FIN MIENTRAS

SI ClientesAtendidos > 0 ENTONCES
    TiempoPromedio = TiempoAcumulado / ClientesAtendidos
    Reportar(TiempoPromedio)
FIN SI
```

### Representación del TAD Cola

#### Representación Secuencial Lineal
Se utilizan dos índices, `pr` (primero) y `ul` (último), para evitar desplazar todos los elementos cada vez que se suprime uno.

![[2026-02-07_07-11-30.png]]
*Estructura: un arreglo `items`, y los índices `pr` y `ul`.*

#### Representación Secuencial Circular (Recomendada)
Es una mejora de la anterior. Cuando `ul` llega al final físico del arreglo, puede "dar la vuelta" y utilizar las posiciones al inicio que hayan sido liberadas por supresiones, siempre que haya espacio total disponible.

![[2026-02-07_07-20-45.png]]
*Estructura: un arreglo `items`, índices `pr` y `ul`, y un contador `cant` para saber cuántos elementos hay.*

#### Representación Encadenada
Similar a la pila encadenada, pero se necesitan dos referencias: una al primer nodo (`pr`) y otra al último (`ul`), para que la inserción al final sea eficiente.

![[2026-02-07_07-26-52.png]]
*Estructura: punteros `pr` y `ul` a los extremos de una lista enlazada simple.*

### Implementación en Python

#### Representación Secuencial Circular
```python
class ColaSecuencial:
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.items = [None] * capacidad
        self.pr = 0  # Índice del primer elemento
        self.ul = 0  # Índice donde se insertará el próximo elemento
        self.cant = 0  # Número de elementos actuales

    def vacia(self) -> bool:
        return self.cant == 0

    def llena(self) -> bool:
        return self.cant == self.capacidad

    def insertar(self, x):
        """Encola un elemento (enqueue)."""
        if self.llena():
            raise OverflowError("La cola está llena")
        self.items[self.ul] = x
        self.ul = (self.ul + 1) % self.capacidad  # Avance circular
        self.cant += 1
        return x

    def suprimir(self):
        """Desencola y devuelve el primer elemento (dequeue)."""
        if self.vacia():
            raise IndexError("La cola está vacía")
        x = self.items[self.pr]
        self.items[self.pr] = None  # Opcional
        self.pr = (self.pr + 1) % self.capacidad  # Avance circular
        self.cant -= 1
        return x

    def recorrer(self):
        """Muestra los elementos en orden de salida (del primero al último)."""
        if self.vacia():
            print("Cola vacía")
            return
        i = self.pr
        for _ in range(self.cant):
            print(self.items[i])
            i = (i + 1) % self.capacidad
```

#### Representación Encadenada
```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaEncadenada:
    def __init__(self):
        self.pr = None  # Primer elemento (frente de la cola)
        self.ul = None  # Último elemento (final de la cola)
        self.cant = 0

    def vacia(self) -> bool:
        return self.pr is None

    def insertar(self, x):
        """Encola un elemento (enqueue)."""
        nuevo_nodo = Nodo(x)
        if self.vacia():
            self.pr = nuevo_nodo
        else:
            self.ul.siguiente = nuevo_nodo
        self.ul = nuevo_nodo
        self.cant += 1
        return x

    def suprimir(self):
        """Desencola y devuelve el primer elemento (dequeue)."""
        if self.vacia():
            raise IndexError("La cola está vacía")
        x = self.pr.dato
        self.pr = self.pr.siguiente
        if self.pr is None:  # Si la cola quedó vacía
            self.ul = None
        self.cant -= 1
        return x

    def recorrer(self):
        """Muestra los elementos en orden de salida (del primero al último)."""
        actual = self.pr
        if actual is None:
            print("Cola vacía")
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def primer_elemento(self):
        """Devuelve el primer elemento sin eliminarlo (front/peek)."""
        if self.vacia():
            return None
        return self.pr.dato
```

---
**TE SIENTES DETERMINADO**