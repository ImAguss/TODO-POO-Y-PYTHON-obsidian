---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - fundamentales
  - algoritmos
proyecto: aprendizaje-programacion
Creacion: 2026-02-09T12:23:00
Revision: 2026-02-09T12:23:00
---
# Tabla de Contenidos

- [[#¿Qué es la Recursión?|¿Qué es la Recursión?]]
- [[#¿Por qué usar la Recursión?|¿Por qué usar la Recursión?]]
- [[#La Recursión en Python|La Recursión en Python]]
- [[#Ejemplos de Recursión|Ejemplos de Recursión]]
	- [[#Ejemplos de Recursión#Cuenta regresiva|Cuenta regresiva]]
	- [[#Ejemplos de Recursión#Cálculo del factorial|Cálculo del factorial]]
- [[#Comparación entre solución recursiva y no recursiva|Comparación entre solución recursiva y no recursiva]]
# Recursión

## ¿Qué es la Recursión?

La recursión tiene varias definiciones similares. Se puede definir como el acto de volver hacia atrás o el acto de definir una función u objeto en términos de sí mismo.

En esencia, algo recursivo es aquello que está definido en términos de sí mismo. Las situaciones autoreferenciales suelen ocurrir en la vida real, aunque a veces cueste identificarlas rápidamente. Por ejemplo, para describir la cantidad de gente que conforma tus ancestros, podrías decir:

**Tus ancestros** = (Tus ancestros) + (Los padres de tus ancestros)

Nota cómo el concepto de "ancestros" se define a sí mismo. Esto es un claro indicador de una definición recursiva. En programación, la recursión tiene un significado preciso: se refiere a una técnica de codificación en la cual una función se llama o se invoca a sí misma.

## ¿Por qué usar la Recursión?

La gran mayoría de los problemas en programación se pueden resolver sin usar recursión. Técnicamente, la recursión no es necesaria.

Sin embargo, existen situaciones que se piensan de forma más intuitiva de manera autoreferencial, como el ejemplo de los ancestros. Si estás diseñando un algoritmo con casos de ese estilo, las soluciones recursivas suelen ser más claras y concisas.

Otro buen ejemplo es recorrer una estructura de tipo **árbol binario**. Esto sucede porque el árbol es una estructura anidada que se presta para una definición recursiva. Un algoritmo no recursivo para recorrer estructuras anidadas tiende a ser más engorroso, mientras que la solución recursiva es relativamente más elegante.

De todas formas, la recursión no debería usarse en toda situación. Hay varios factores a considerar:

- Para algunos problemas, la solución recursiva, aunque posible, puede ser más engorrosa que elegante.
- Las implementaciones recursivas tienden a consumir más memoria que las no recursivas, porque deben *recordar* el estado en el que quedan las variables o funciones.
- En algunos casos, usar recursión resultará en tiempos de ejecución más lentos, justamente por el punto anterior.

El factor más determinante a la hora de usar recursión es la **legibilidad**. Pero aún así, depende de las circunstancias.

## La Recursión en Python

Cuando llamas a una función en Python, el intérprete crea un nuevo **espacio de nombres** (*namespace*) local, de modo que los nombres definidos en esa función no colisionen con nombres idénticos definidos en cualquier otra parte. Una función puede llamar a otra, e incluso si ambas definen objetos con los mismos nombres, todo funcionará correctamente porque existen en *namespaces* separados.

Considera el siguiente ejemplo:

```python
def function():
    x = 10
    function()
```

Cuando `function()` se ejecuta por primera vez, Python crea un *namespace* y asigna el valor `10` a `x` en ese *namespace*. Luego se llama recursivamente a la función. Esto hace que, en la segunda ejecución, el intérprete cree un segundo *namespace* donde `10` se asigna a otro `x`. Entonces existen dos instancias con el nombre `"x"` que son distintas y pueden coexistir sin colisionar, gracias a los *namespaces*.

Desafortunadamente, ejecutar esta función produce un error que nos sirve para entender mejor la recursividad:

```python
>>> function()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in function
  File "<stdin>", line 3, in function
  File "<stdin>", line 3, in function
  [Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded
```

Por cómo está escrita, la función se ejecutaría indefinidamente ya que no hay nada que detenga la recursión. En la práctica, esto no puede suceder porque las computadoras tienen memoria limitada, pero Python no lo permite: el intérprete limita el número máximo de veces que una función puede llamarse recursivamente. Cuando se alcanza ese límite, se genera un `RecursionError`.

```python
>>> from sys import getrecursionlimit
>>> getrecursionlimit()
1000

>>> from sys import setrecursionlimit
>>> setrecursionlimit(2000)
>>> getrecursionlimit()
2000
```

Técnicamente puedes modificar este límite, pero no es recomendado a menos que sea estrictamente necesario y sepas lo que estás haciendo.

Por lo tanto, las funciones que se llaman a sí mismas deben eventualmente encontrar una forma de detenerse. Esto hace que las funciones recursivas tengan usualmente esta estructura:

- **Caso(s) base:** Uno o más casos que se resuelven sin recursión, para detenerla.
- **Paso recursivo:** Cada llamada recursiva debe acercar progresivamente la solución hacia el/los caso(s) base.

## Ejemplos de Recursión

### Cuenta regresiva

Uno de los ejemplos más sencillos es una función que realiza una cuenta regresiva desde un número positivo hasta 0.

```python
def countdown(n):
    print(n)
    if n == 0:
        return             # Termina la recursión
    else:
        countdown(n - 1)   # Llamada recursiva

countdown(5)
```
**Salida:**
```
5
4
3
2
1
0
```

Aquí se aplican los conceptos mencionados: existe un caso base (`n == 0`) y cada llamada acerca a `n` hacia ese caso base.

Una mejora para evitar problemas con números negativos sería:

```python
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)
```

Esto evita que un número negativo provoque una sucesión infinita de llamadas.

Como mencionamos, toda función recursiva puede expresarse de manera no recursiva. Aquí la variante iterativa:

```python
def countdown(n):
    while n >= 0:
        print(n)
        n -= 1
```

### Cálculo del factorial

El siguiente ejemplo involucra el concepto del [factorial](https://es.wikipedia.org/wiki/Factorial). Al igual que la cuenta regresiva, esta función matemática es reductiva y se define en términos de sí misma, lo que la hace candidata para la recursión.

Una forma de visualizarlo:

![[jsturtz-factorial-example.496c01139673.png]]

Una vez identificados el caso base y cómo las llamadas se acercan a él, podemos programar la función recursiva:

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

factorial(4)  # Devuelve 24
```

Si no entiendes la sintaxis del `if` en una sola línea, puedes revisar [[Condicionales en Python#Expresiones Condicionales (Operador Ternario)|Operador Ternario en IF]].

Observa que en esta función recursiva se utiliza `return`. Esto cambia ligeramente su comportamiento: cada vez que se llama a la función dentro del `return`, esta queda en espera de que la llamada recursiva devuelva su valor. Se va formando una [[Pilas y Colas#Base Teórica de Pilas|pila]] de llamadas pendientes; cuando se alcanza el caso base, la pila se desapila siguiendo la filosofía LIFO (Last In, First Out).

Para verlo en acción, podemos añadir mensajes de depuración:

```python
def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n - 1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value

factorial(4)
```
**Salida:**
```
factorial() called with n = 4
factorial() called with n = 3
factorial() called with n = 2
factorial() called with n = 1
-> factorial(1) returns 1
-> factorial(2) returns 2
-> factorial(3) returns 6
-> factorial(4) returns 24
24
```

La función recursiva no es la única opción. Aquí la versión iterativa:

```python
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
```

## Comparación entre solución recursiva y no recursiva

Para evaluar el tiempo de ejecución, puedes usar la función `timeit()` del módulo `timeit`. Esta función soporta varios formatos; usaremos el siguiente:

```python
timeit(<comando>, setup=<cadena_de_configuración>, number=<iteraciones>)
```

**Versión recursiva:**

```python
>>> setup_string = """
... print("Recursive:")
... def factorial(n):
...     return 1 if n <= 1 else n * factorial(n - 1)
... """
>>> from timeit import timeit
>>> timeit("factorial(4)", setup=setup_string, number=10000000)
Recursive:
4.957105500000125
```

**Versión iterativa:**

```python
>>> setup_string = """
... print("Iterative:")
... def factorial(n):
...     return_value = 1
...     for i in range(2, n + 1):
...         return_value *= i
...     return return_value
... """
>>> from timeit import timeit
>>> timeit("factorial(4)", setup=setup_string, number=10000000)
Iterative:
3.733752099999947
```

Podemos ver que la versión iterativa es más rápida, aunque la diferencia es apenas perceptible a menos que se realicen millones de llamadas. Debes considerar esto si tu algoritmo necesita ejecutarse muchas veces, ya que en esos casos es mejor priorizar un tiempo de ejecución menor.

--- 
**TE SIENTES DETERMINADO**