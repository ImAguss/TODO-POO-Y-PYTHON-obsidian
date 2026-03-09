---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-16T08:18:00
Revision: 2026-02-16T09:36:00
---
# Tabla de Contenidos

- [[#Ámbito Local (Local Scope)|Ámbito Local (Local Scope)]]
- [[#Ámbito Enclosing (Funciones Anidadas)|Ámbito Enclosing (Funciones Anidadas)]]
- [[#Ámbito Global (Global Scope)|Ámbito Global (Global Scope)]]
- [[#Ámbito Built‑in|Ámbito Built‑in]]
- [[#Bloques, Bucles y Comprensiones|Bloques, Bucles y Comprensiones]]
	- [[#Bloques, Bucles y Comprensiones#Comprensiones (listas, diccionarios, conjuntos)|Comprensiones (listas, diccionarios, conjuntos)]]
- [[#Uso de la palabra clave `global`|Uso de la palabra clave `global`]]
- [[#Uso de la palabra clave `nonlocal`|Uso de la palabra clave `nonlocal`]]
- [[#Las funciones [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|locals() y globals()]]|Las funciones [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|locals() y globals()]]]]
- [[#Errores comunes y cómo solucionarlos|Errores comunes y cómo solucionarlos]]
- [[#Buenas prácticas para mantener el ámbito simple|Buenas prácticas para mantener el ámbito simple]]
# Ámbito (Scope) de una Variable en Python

El ámbito (o alcance) de una variable en Python sigue el orden **LEGB**:

- **Local**: El ámbito de la función actual.
- **Enclosing** (o no local): Ámbito de funciones que envuelven a la función actual (aplica a funciones anidadas, como se vio en [[Decoradores#Funciones internas y cierres (closures)|Decoradores]]).
- **Global**: El nivel superior del módulo, es decir, el espacio de nombres (*namespace*) del módulo.
- [[Módulos Built-in de Python#Tabla de Contenidos|Built-in]]: Nombres predefinidos por Python, como `len`, `print` o las excepciones incorporadas (provienen del módulo `builtins`).

Las funciones locales pueden acceder a todos los niveles superiores (enclosing, global y built‑in), pero esos niveles no pueden acceder directamente a las variables locales. Dicho de otro modo: **los niveles internos ven a los externos, pero los externos no ven a los internos**.

## Ámbito Local (Local Scope)

Las variables asignadas dentro de una función son locales a esa función, a menos que se hayan declarado en un nivel superior. Desde fuera de la función no son visibles.

```python
def show_order_id():
    order_id = 42
    print("dentro de la función:", order_id)

show_order_id()
print("fuera de la función:", order_id)  # NameError: name 'order_id' is not defined
```

Python determina el ámbito en tiempo de compilación. Si una función asigna una variable en cualquier parte de su cuerpo, esa variable se considera local en toda la función, incluso si se intenta leer antes de la asignación:

```python
discount_rate = 0.10   # variable a nivel de módulo (global)

def price_with_discount(amount_cents):
    # Aquí se intenta leer discount_rate, pero luego se asigna,
    # por lo que Python la trata como local y no encuentra valor.
    print("descuento configurado:", discount_rate)
    discount_rate = 0.20   # esta asignación hace que discount_rate sea local
    return int(amount_cents * (1 - discount_rate))

# UnboundLocalError: cannot access local variable 'discount_rate'
# where it is not associated with a value
```

## Ámbito Enclosing (Funciones Anidadas)

Las funciones definidas dentro de otra pueden acceder a las variables de la función que las envuelve. Para modificar esas variables (reasignarlas) se necesita la palabra clave `nonlocal`.

```python
def make_step_counter():
    count = 0                     # ámbito enclosing para increment()

    def increment():
        nonlocal count            # indica que count pertenece al ámbito enclosing
        count += 1
        return count

    return increment

step = make_step_counter()
print(step())   # 1
print(step())   # 2
```

Sin `nonlocal`, la asignación `count += 1` crearía una nueva variable local `count` dentro de `increment()`, perdiendo la conexión con la variable exterior.

## Ámbito Global (Global Scope)

Las variables asignadas en el nivel superior de un módulo viven en el espacio de nombres global. Cualquier función puede leerlas, pero para modificarlas (reasignarlas) debe declararlas como `global`.

```python
greeting = "Hola"

def greet_city(city_name):
    print(greeting, city_name)   # solo lectura de la variable global

def set_greeting(new_greeting):
    global greeting
    greeting = new_greeting      # reasigna la variable global

greet_city("Madrid")     # Hola Madrid
set_greeting("Hey")
greet_city("Barcelona")  # Hey Barcelona
```

**Nota:** Usar variables globales de forma excesiva dificulta la depuración y el mantenimiento. Siempre que sea posible, es mejor pasar valores como parámetros y retornar resultados.

## Ámbito Built‑in

El ámbito built‑in contiene los nombres que Python pone a disposición de forma automática, como `len`, `print`, `range`, `Exception`, etc. Cualquier función o módulo puede acceder a ellos.

```python
list = [1, 2, 3]     # ¡Esto oculta el constructor incorporado list!
list("abc")          # TypeError: 'list' object is not callable
del list             # eliminamos el conflicto
```

No hay que confundir estos nombres con las palabras clave del lenguaje (`if`, `for`, `while`, etc.), que forman parte de la sintaxis y no se pueden usar como [[Sintaxis Basica Python#Identificadores|identificadores]].

## Bloques, Bucles y Comprensiones

En Python, las estructuras de bloque como `if`, `for`, `while` y `with` **no crean un nuevo ámbito**. Las variables asignadas dentro de ellos pertenecen al ámbito de la función (o módulo) que los contiene.

```python
if True:
    status = "listo"
print(status)   # "listo"

for i in range(3):
    pass
print(i)        # 2 (el último valor del bucle)
```

### Comprensiones (listas, diccionarios, conjuntos)

Las variables de iteración en las [[Listas en Python#Comprensión de listas (*List Comprehensions*)|comprensiones]] **tienen su propio ámbito local** y no se filtran al ámbito exterior.

```python
numbers = [1, 2, 3]
[x for x in numbers]
print("x" in globals() or "x" in locals())   # False
```

Esto es muy conveniente, pues evita que las variables de control de las comprensiones contaminen el espacio de nombres.

## Uso de la palabra clave `global`

Se emplea dentro de una función para indicar que una variable pertenece al ámbito global (nivel de módulo) y se desea reasignar.

```python
tax_rate = 0.08

def configure_tax(rate):
    global tax_rate
    tax_rate = float(rate)

def total_with_tax(cents):
    return int(cents * (1 + tax_rate))

configure_tax(0.10)
print(total_with_tax(1000))   # 1100
```

## Uso de la palabra clave `nonlocal`

Se usa dentro de una función anidada para indicar que una variable pertenece al ámbito de la función que la envuelve (enclosing) y se desea modificar.

```python
def make_accumulator(start=0):
    total = start
    def add(amount):
        nonlocal total
        total += amount
        return total
    return add

acc = make_accumulator()
print(acc(5))   # 5
print(acc(10))  # 15
```

Si se usa `nonlocal` para una variable que no existe en ningún ámbito enclosing, se produce un `SyntaxError`.

## Las funciones [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|locals() y globals()]]

Estas funciones son útiles para inspección y depuración, **no para modificar variables**. En Python 3.13, cada llamada a `locals()` dentro de una función devuelve una copia independiente; modificar esa copia no afecta a las variables reales.

```python
def probe():
    project = "alpha"
    snap1 = locals()
    snap1["project"] = "beta"   # solo modifica la copia
    observed = project            # sigue siendo "alpha"
    snap2 = locals()              # nueva copia con el valor real
    return snap1["project"], observed, snap2["project"]

print(probe())   # ('beta', 'alpha', 'alpha')
```

`globals()` se comporta de manera análoga. Es mejor usar estas funciones solo para leer información, no para escribir.

## Errores comunes y cómo solucionarlos

- **`UnboundLocalError` por asignar dentro de una función**  
  Si una variable se asigna en cualquier parte del cuerpo, Python la considera local. Leerla antes de la asignación provoca este error.  
  *Solución:* usar `nonlocal` o `global` según corresponda, o cambiar el diseño para evitar lecturas prematuras.

- **Esperar ámbito de bloque en `if/for/while/with`**  
  Las variables definidas dentro de estos bloques persisten fuera de ellos.  
  *Solución:* si se necesita un aislamiento más estricto, se puede envolver el código en una función auxiliar.

- **Ocultar nombres del ámbito built‑in (`list`, `dict`, `sum`, etc.)**  
  Asignar a nombres como `list` provoca que ya no se pueda usar el constructor incorporado.  
  *Solución:* elegir nombres descriptivos y evitar colisiones (por ejemplo, `customer_list` en lugar de `list`).

- **Olvidar `nonlocal` en cierres**  
  Si se intenta modificar una variable de una función envolvente sin `nonlocal`, se crea una variable local nueva.  
  *Solución:* declarar explícitamente `nonlocal`.

- **Confundir palabras clave con nombres built‑in**  
  Las palabras clave (`if`, `for`, etc.) son parte de la sintaxis y no se pueden usar como identificadores. Los nombres built‑in sí pueden ser reasignados, pero no es recomendable.

## Buenas prácticas para mantener el ámbito simple

1. **Definir las variables en el ámbito más restringido posible.** Funciones pequeñas y cohesivas ayudan.
2. **Pasar datos por parámetros y retornar valores.** Minimiza el uso de globales.
3. **Usar cierres de forma intencionada.** Documentar qué variables capturan y emplear `nonlocal` cuando sea necesario.
4. **Elegir nombres descriptivos y no conflictivos.** Evita sombrear nombres built‑in.
5. **Tratar `locals()` y `globals()` como herramientas de solo lectura.** No se debe confiar en ellas para modificar variables.

---
__TE SIENTES DETERMINADO__