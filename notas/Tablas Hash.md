---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - estructuras
proyecto: aprendizaje-programacion
Creacion: 2026-02-02T15:40:00
Revision: 2026-02-06T09:02:00
---
# Tabla de Contenidos
- [[#Entendiendo la función Hash|Entendiendo la función Hash]]
	- [[#Entendiendo la función Hash#Examinando la función nativa `hash()` de Python|Examinando la función nativa `hash()` de Python]]
	- [[#Entendiendo la función Hash#Yendo a profundidad con la función Hash de Python|Yendo a profundidad con la función Hash de Python]]
	- [[#Entendiendo la función Hash#¿Cuáles son las propiedades que identifican a una función hash?|¿Cuáles son las propiedades que identifican a una función hash?]]
	- [[#Entendiendo la función Hash#Comparación entre la identidad de un objeto y su hash|Comparación entre la identidad de un objeto y su hash]]
	- [[#Entendiendo la función Hash#Creando nuestra propia función Hash|Creando nuestra propia función Hash]]
		- [[#Creando nuestra propia función Hash#El papel del módulo para restringir el rango|El papel del módulo para restringir el rango]]
- [[#Repasando Conceptos Clave y Profundizando|Repasando Conceptos Clave y Profundizando]]
	- [[#Repasando Conceptos Clave y Profundizando#Casos de ejemplo|Casos de ejemplo]]
	- [[#Repasando Conceptos Clave y Profundizando#Hashing Perfecto|Hashing Perfecto]]
	- [[#Repasando Conceptos Clave y Profundizando#Técnicas de Transformación de Claves|Técnicas de Transformación de Claves]]
	- [[#Repasando Conceptos Clave y Profundizando#¿Qué es una Colisión?|¿Qué es una Colisión?]]
	- [[#Repasando Conceptos Clave y Profundizando#Aspectos importantes al implementar Hashing|Aspectos importantes al implementar Hashing]]
		- [[#Aspectos importantes al implementar Hashing#La elección de la función de transformación **H**|La elección de la función de transformación **H**]]
	- [[#Repasando Conceptos Clave y Profundizando#Política de Manejo de Colisiones|Política de Manejo de Colisiones]]
	- [[#Repasando Conceptos Clave y Profundizando#Factor de Carga|Factor de Carga]]

# Tablas Hash

Inventadas a mediados del siglo pasado, las tablas hash son una estructura de datos clásica que desde su creación ha sido fundamental en el mundo de la programación. Hoy en día se usa para una gran cantidad de tareas, como indexar bases de datos —haciendo que su tiempo de acceso sea totalmente ínfimo—, implementaciones de conjuntos (*sets*), computar valores, etc.

Suele confundirse con los [[Diccionarios en Python#Diccionarios en Python|diccionarios de Python]], ya que este tipo de dato usa *hashing* para relacionar sus claves-valor. Pero las tablas hash son más una implementación subyacente; los diccionarios son un tipo de dato que implementa una tabla hash personalizada.

## Entendiendo la función Hash

Una función hash convierte un dato o valor en una secuencia fija de bytes llamada valor hash o código hash. Es un número que actuará como una huella digital, usualmente de tamaño mucho menor al dato original. Un uso común está en las imágenes ISO de Linux, ya que ofrecen opciones para descargar su hash MD5 o SHA-2, que son algoritmos que permiten verificar la integridad de las ISOs y asegurar que no se descargue un archivo corrupto.

Además de verificar la integridad de datos y formar parte del núcleo de los diccionarios, las funciones hash ayudan en otros campos, uno de los más importantes es el de seguridad y criptografía. Por ejemplo, para almacenar contraseñas hasheadas en una base de datos y mitigar riesgos en caso de filtraciones. Las firmas digitales incluyen hash para crear un resumen del mensaje antes del encriptado. La famosa blockchain es otro ejemplo común que usa funciones hash con propósitos criptográficos.

**Nota:** Aunque las funciones hash criptográficas son terriblemente interesantes, son un tipo especial que no cubriré en esta nota, quizás en otra en el futuro.

Implementar una buena función hash de manera correcta es una tarea difícil que requiere un entendimiento avanzado de funciones matemáticas y, sobre todo, de números primos.

Python, como no, trae un módulo llamado `hashlib` que nos provee una variedad de funciones hash conocidas, incluyendo las criptográficas y otros algoritmos útiles. Además, el lenguaje de forma nativa posee una [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|función hash genérica]] usada principalmente en estructuras como diccionarios y conjuntos (*sets*).

### Examinando la función nativa `hash()` de Python

Si ya sabes cómo implementar una función hash o quieres hacer prototipos rápidos, quizás te sirva saber cómo funciona la función `hash()` que ofrece Python. Aunque solo hablamos de Python, la inmensa mayoría de lenguajes de programación actuales posee módulos o funciones hash genéricas en su núcleo.

La función `hash` puede hashear cualquier objeto dentro de Python, y como todo es un objeto, se puede hashear prácticamente cualquier cosa:

```python
>>> hash(3.14)
322818021289917443

>>> hash(3.14159265358979323846264338327950288419716939937510)
326490430436040707

>>> hash("Lorem")
7677195529669851635

>>> hash("Lorem ipsum dolor sit amet, consectetur adipisicing elit,"
... "sed do eiusmod tempor incididunt ut labore et dolore magna"
... "aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
... "ullamco laboris nisi ut aliquip ex ea commodo consequat."
... "Duis aute irure dolor in reprehenderit in voluptate velit"
... "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
... "occaecat cupidatat non proident, sunt in culpa qui officia"
... "deserunt mollit anim id est laborum.")
1107552240612593693
```

A primera vista, por los *outputs*, parece que la función hash por defecto es [No determinística](https://en.wikipedia.org/wiki/Nondeterministic_algorithm), ya que los resultados son muy distintos. Sin embargo, esto no podría estar más lejos de la realidad.

Mientras estés en la misma sesión del intérprete, no tendrás problemas con el resultado de la función `hash`, ya que siempre retornará un valor determinístico para un mismo objeto inmutable:

```python
>>> hash("Lorem")
7677195529669851635
>>> hash("Lorem")
7677195529669851635
>>> hash("Lorem")
7677195529669851635
```

Esto sucede porque los valores hash son inmutables y no cambian durante el tiempo de vida del objeto en memoria. Pero cada vez que salgas y entres a Python, la función `hash` retornará valores distintos para el mismo *input* en diferentes ejecuciones, lo que podría llevar a pensar que es una función no determinística.

```bash
$ python -c 'print(hash("Lorem"))'
6182913096689556094
$ python -c 'print(hash("Lorem"))'
1756821463709528809
$ python -c 'print(hash("Lorem"))'
8971349716938911741
```

Aunque parece algo sin sentido y molesto, se hace por seguridad: para evitar que se exploten vulnerabilidades que poseen los algoritmos hash, como provocar colisiones intencionales en las tablas (concepto que veremos más adelante). Estas colisiones podrían provocar una [Denegación de Servicio (DoS)](https://es.wikipedia.org/wiki/Ataque_de_denegación_de_servicio), un ataque común contra algoritmos hash.

Gracias a esta vulnerabilidad, Python habilita la aleatorización del hash para algunos *inputs*, como las cadenas de texto (*strings*). Esto hace que los ataques sean más difíciles, ya que los valores hash son mucho menos predecibles entre diferentes ejecuciones del intérprete.

Si aún así quieres continuar bajo tu propio riesgo, puedes especificar una semilla fija para desactivar la aleatorización:

**En Linux/macOS:**
```bash
$ PYTHONHASHSEED=1 python -c 'print(hash("Lorem"))'
440669153173126140
$ PYTHONHASHSEED=1 python -c 'print(hash("Lorem"))'
440669153173126140
```
**En Windows:**
```cmd
C:\> set PYTHONHASHSEED=1
C:\> python -c "print(hash('Lorem'))"
440669153173126140
C:\> python -c "print(hash('Lorem'))"
440669153173126140
```

Con estos comportamientos podemos deducir y definir a las funciones hash como **funciones determinísticas** dentro de una misma ejecución, lo cual es uno de los puntos fundamentales dentro de esta estructura de datos.

Y cuando dijimos que en Python se puede aplicar una función hash a cualquier cosa, es a cualquier objeto:

```python
>>> hash(None)
5904497366826
>>> hash(hash)
2938107101725
>>> class Person:
...     pass
...
>>> hash(Person)
5904499092884
>>> hash(Person())
8738841746871
>>> hash(Person())
8738841586112
```

Aquí tenemos un comportamiento interesante: se puede hashear una clase u objeto personalizado, que como sabemos es un tipo mutable. Pero si intentamos hashear una lista, que también es mutable, obtenemos un error:

```python
>>> hash([1, 2, 3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```

Esto sucede porque Python hashea los objetos o clases personalizados usando su identidad en memoria (su dirección), la cual es constante para la vida del objeto, sin importar su contenido. Esto no se hace con las listas porque, a diferencia de una clase vacía, cambiar el contenido de una lista es una operación común y esperada. Si se permitiera hashear listas mutables, cada modificación cambiaría el resultado del hash, rompiendo la propiedad determinística fundamental de las funciones hash.

Pero entonces, ¿por qué a un objeto (que también es mutable) se le puede aplicar una función hash? Como mencioné, se logra gracias a su identidad, pero esto tiene problemas. Uno principal es que rompe un principio del hashing: **"Si se le aplica hash a dos *inputs* iguales, entonces se debe obtener el mismo resultado"**. Esto se rompe si hasheamos la identidad de los objetos en Python, ya que dos objetos con el mismo contenido (iguales) no tienen la misma identidad, y por lo tanto producirían hashes diferentes.

Una buena práctica sería especificar que el objeto se comporte como un tipo de dato inmutable. En ese caso, podremos aplicar *hashing* sin problemas, ya que lo hará en base a su contenido, que al ser inmutable no rompe la propiedad determinística. Por ejemplo, definiendo el método especial `__hash__` junto con `__eq__`:

```python
class Producto:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __eq__(self, otro):
        return isinstance(otro, Producto) and self.id == otro.id

    def __hash__(self):
        # El hash se basa en el atributo inmutable 'id'
        return hash(self.id)

# Ahora dos objetos con el mismo id son iguales y tienen el mismo hash
p1 = Producto(101, "Laptop")
p2 = Producto(101, "Laptop")
print(hash(p1) == hash(p2))  # True
print(p1 == p2)               # True
```

### Yendo a profundidad con la función Hash de Python

Otra característica interesante de la función hash es que siempre produce una salida de tamaño fijo, sin importar qué tan grande sea la entrada. En Python, un valor hash es un entero con una magnitud moderada. Ocasionalmente puede ser negativo.

```python
>>> hash("Lorem")
-972535290375435184
```

La consecuencia natural de los números de tamaño fijo es que la mayoría de la información original se pierde de forma irreversible durante el proceso. Esto está bien si quieres que el hash resultante actúe como un resumen del dato original. Pero el hecho de que las funciones hash en general asignen valores infinitos dentro de un espacio finito, tarde o temprano lleva al problema de las **Colisiones**, que ocurre cuando dos entradas diferentes producen el mismo valor hash.

**Nota:** Si te gustan más las matemáticas, puedes usar el [principio del palomar](https://es.wikipedia.org/wiki/Principio_del_palomar) para describir las funciones hash de forma más formal:

*Dados `n` ítems y `m` contenedores, si `n > m`, entonces hay al menos un contenedor con más de un ítem.*

En este contexto, los ítems son un número potencialmente infinito de valores que ingresas a la función hash, mientras que los contenedores son sus valores hash asignados a partir de un conjunto finito.

Las colisiones dentro de las tablas hash son un concepto esencial que revisaremos con más profundidad más adelante. De momento, debes saber que las colisiones deben evitarse lo máximo posible para implementar una función hash que sea estable, segura y predecible, ya que son una potencial brecha de seguridad para atacantes maliciosos.

En la práctica, esto significa que las funciones hash deben asignar una distribución uniforme de valores dentro del espacio disponible. Esto se puede visualizar con la distribución que hace la función hash de Python:

```python
# hash_distribution.py
from collections import Counter

def distribute(items, num_containers, hash_function=hash):
    return Counter([hash_function(item) % num_containers for item in items])

def plot(histogram):
    for key in sorted(histogram):
        count = histogram[key]
        padding = (max(histogram.values()) - count) * " "
        print(f"{key:3} {'■' * count}{padding} ({count})")
```

**Explicación del código:**
*   `distribute(items, num_containers, hash_function=hash)`: Toma una lista de `items`, un número de `num_containers` (contenedores o "cubos") y una función hash. Calcula el hash de cada ítem, aplica la operación módulo (`%`) con `num_containers` para restringir el valor a un índice dentro del rango de contenedores, y cuenta cuántos ítems caen en cada uno.
*   `plot(histogram)`: Toma el histograma (el objeto `Counter`) e imprime una representación visual simple con bloques (■) para mostrar la distribución.

```python
>>> from hash_distribution import plot, distribute
>>> from string import printable  # printable contiene todos los caracteres ASCII imprimibles

>>> plot(distribute(printable, num_containers=2))
0 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ (51)
1 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (49)

>>> plot(distribute(printable, num_containers=5))
0 ■■■■■■■■■■■■■■■            (15)
1 ■■■■■■■■■■■■■■■■■■■■■■■■■■ (26)
2 ■■■■■■■■■■■■■■■■■■■■■■     (22)
3 ■■■■■■■■■■■■■■■■■■         (18)
4 ■■■■■■■■■■■■■■■■■■■        (19)
```

Cuando hay solamente dos contenedores, esperarías una distribución cercana al 50-50. Añadir más contenedores resultará en que algunos se llenen más que otros. Como se puede ver, la función hash de Python tiene una distribución bastante buena, pero no perfecta.

Relacionado a eso, la distribución uniforme de los valores hash es típicamente pseudoaleatoria, lo cual es especialmente importante para las funciones hash criptográficas. Esto previene que potenciales atacantes usen un análisis estadístico para tratar de predecir la correlación entre la entrada y salida. Considera alterar una sola letra dentro de una cadena y verás cuánto afecta al hash resultante:

```python
>>> hash("Lorem")
1090207136701886571
>>> hash("Loren")
4415277245823523757
```

Es un valor hash totalmente diferente, a pesar de que la diferencia radica solamente en una letra. Esto hace que las funciones hash produzcan un **efecto avalancha**, que básicamente significa que un pequeño cambio en la entrada provoca un cambio enorme e impredecible en la salida. Igualmente, esta característica no es esencial para los propósitos de implementar una tabla hash básica.

En la mayoría de casos, la función hash exhibe otra característica que no es esencial pero es curiosa: se comporta como una función de un solo camino (*one-way function*), porque invertir el proceso para obtener la entrada original a partir del hash es computacionalmente imposible en la mayoría de los casos. Sin embargo, existe una excepción notable con los enteros pequeños en Python:

```python
>>> hash(42)
42
```

Para números enteros no muy grandes, Python a menudo devuelve el mismo valor como su hash (esto es una optimización interna). Esto **no** significa que la función sea invertible en general. Para la inmensa mayoría de entradas (cadenas, tuplas, objetos), es imposible recuperar el dato original a partir del valor hash.

A pesar de todo, calcular los valores hash en Python o en cualquier implementación bien hecha es rápido, incluso para entradas gigantes. En una computadora moderna, llamar a la función `hash()` con una cadena de 100 millones de caracteres retorna instantáneamente. Si no fuera tan rápido, la sobrecarga computacional del cálculo del hash anularía los beneficios de usar *hashing* en primer lugar.

### ¿Cuáles son las propiedades que identifican a una función hash?

Basado en lo que vimos hasta ahora, podemos sacar algunas conclusiones a través de las propiedades de las funciones hash en general, donde también haremos una comparación con las funciones criptográficas:

| Característica | Función Hash Genérica | Función Hash Criptográfica |
| :--- | :---: | :---: |
| **Determinística** (misma entrada → misma salida en una ejecución) | ✔️ | ✔️ |
| **Entrada Universal** (puede procesar cualquier dato) | ✔️ | ✔️ |
| **Salida de Tamaño Fijo** | ✔️ | ✔️ |
| **Rápida de Calcular** | ✔️ | ✔️ |
| **Distribución Uniforme** (salidas repartidas equitativamente) | ✔️ | ✔️ |
| **Distribución Aleatoria** (sin correlación predecible entrada/salida) | | ✔️ |
| **Semilla Aleatorizable** (para prevenir ataques) | | ✔️ |
| **Función de un Solo Camino** (prácticamente irreversible) | | ✔️ |
| **Efecto Avalancha** (cambio mínimo → cambio máximo en salida) | | ✔️ |

Las propiedades adicionales que tienen las funciones hash criptográficas proveen una garantía de seguridad mucho más fuerte.

### Comparación entre la identidad de un objeto y su hash

Probablemente una de las formas más sencillas de una implementación hash imaginable es la de la función nativa `id()`, que nos da la identidad (dirección en memoria) de un objeto.

```python
>>> id("Lorem")
139836146678832
```

La función `id()` funciona como algunas funciones hash: toma una entrada (el objeto) y produce un número de tamaño fijo (su dirección). **Pero es importante no confundir su intención.** `id()` y `hash()` tienen propósitos totalmente diferentes. El acceso a la memoria es predecible y no tiene una distribución uniforme, lo cual es inseguro y enormemente ineficiente para *hashing*. Por último, dos objetos iguales en contenido producirán `id`s distintos, lo cual rompe un principio fundamental del *hashing* basado en contenido.

### Creando nuestra propia función Hash

Diseñar una función hash que cumpla con todos los requisitos desde cero es difícil. Como se mencionó anteriormente, usar la función nativa `hash()` de Python ayuda a hacer prototipos rápidos. Sin embargo, intentar construir una función desde la nada es una gran forma de aprender cómo funciona.

En este ejercicio, puedes limitarte a hacer cálculos matemáticos simples que generen valores hash determinísticos.

```python
>>> def hash_function(text):
...     return sum(ord(character) for character in text)

>>> hash_function("Lorem")
511
>>> hash_function("Loren")
512
>>> hash_function("Loner")
512
```

Dado que en esencia el *hashing* se basa en usar una función matemática para calcular un número arbitrario a partir de una entrada, la función utilizada varía mucho del propósito. La función del ejemplo tiene un problema: calcula el hash en base a las letras pero no toma en cuenta su orden. Esto la hace predecible y propensa a colisiones (como vemos con "Loren" y "Loner").

Te estarás preguntando que esa función solo funciona para cadenas. Una forma de solucionarlo sería convertir cualquier dato a cadena con la [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|función `str()`]]:

```python
>>> def hash_function(key):
...     return sum(ord(character) for character in str(key))

>>> hash_function("Lorem")
511
>>> hash_function(3.14)
198
>>> hash_function(True)
416
```

Pero esto provoca que tipos de datos diferentes que se representen igual como cadena produzcan una colisión:

```python
>>> hash_function("3.14")
198
>>> hash_function(3.14)
198
```

Una solución es usar la [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|función `repr()`]], que da la representación oficial del objeto, diferenciando tipos:

```python
>>> def hash_function(key):
...     return sum(ord(character) for character in repr(key))

>>> hash_function("3.14")
276  # repr("3.14") es "'3.14'"
>>> hash_function(3.14)
198  # repr(3.14) es '3.14'
```

Para solucionar el problema del orden de los caracteres, podemos incorporar el índice (posición) de cada uno en el cálculo, por ejemplo, multiplicándolo:

```python
>>> def hash_function(key):
...     return sum(
...         index * ord(character)
...         for index, character in enumerate(repr(key), start=1)
...     )
```

Si te confunde cómo funciona esta iteración, puedes revisar [[Estructuras Iterativas en Python#Iterar con índices usando Funciones Nativas en Python 📋 Lista Completa de Funciones Incorporadas enumerate()|Iterar con Enumerate]].

Ahora nuestra función hash es más universal y sufre menos colisiones por anagramas. Pero hay otro problema: la salida crece con el tamaño de la entrada.

```python
>>> hash_function("Tiny")
1801
>>> hash_function("This has a somewhat medium length.")
60919
>>> hash_function("This is very long and slow!" * 1_000_000)  # Enorme
33304504435500117
```

#### El papel del módulo para restringir el rango

Una forma muy común de garantizar que la salida de la función hash esté dentro de un rango específico (por ejemplo, el tamaño de nuestra tabla) es usar la **operación módulo (`%`)**. Esta operación devuelve el resto de la división, limitando efectivamente el resultado a un número entre `0` y `num_containers - 1`.

```python
>>> hash_function("Tiny") % 100
1
>>> hash_function("This has a somewhat medium length.") % 100
19
>>> hash_function("This is very long and slow!" * 1_000_000) % 100
17
```

**La disyuntiva:** A medida que reduces el rango de salida (usando un módulo pequeño), aumenta la probabilidad de **colisiones**, porque hay menos "cajones" disponibles para un número potencialmente grande de entradas distintas. Es una compensación entre el tamaño de la tabla (memoria) y la frecuencia de colisiones.

Si observamos la distribución de nuestra función hash mejorada, notamos que aún no es perfecta:

```python
>>> from hash_distribution import plot, distribute
>>> from string import printable
>>> plot(distribute(printable, 6, hash_function))
  0 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (31)
  1 ■■■■                              (4)
  2 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (31)
  4 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ (33)
  5 ■                                 (1)
```

La distribución está desequilibrada: los contenedores 1 y 5 casi no se usan, y el 3 ni siquiera aparece. Esto indica que muchas entradas distintas están "colisionando" en los mismos pocos contenedores (0, 2, 4). Una función hash ideal debería distribuir las entradas de manera más uniforme entre todos los contenedores.

Esto demuestra que diseñar una buena función hash es un desafío que requiere refinamiento según las necesidades específicas de los datos que se manejen.

## Repasando Conceptos Clave y Profundizando

Como bien sabemos, el *hashing* se basa en almacenar elementos en direcciones de memoria aprovechando el acceso directo. Esto se logra mediante transformaciones **H** de claves **K** en direcciones **D**:

**H : K → D**

El espacio direccionable es usualmente un arreglo. Por lo tanto, el *hashing* es una transformación **H** que convierte las claves en índices del arreglo para aprovechar el acceso directo a los elementos.

### Casos de ejemplo

Sabemos que si los elementos tienen un conjunto de claves que corresponde exactamente al número de elementos a almacenar (y son todas distintas), podemos usar una **tabla de acceso directo**. Por ejemplo:

Si tenemos que guardar 1000 empleados con números de legajo únicos del 000 al 999, necesitamos una tabla con 1000 entradas. En este caso:
*   K = { ki / 000 <= ki <= 999 }
*   D = { di / 000 <= di <= 999 }

Podemos usar la **función identidad**:
**H(k) = id(k) = k**

Si `k = 100`, entonces `H(100) = 100`. El elemento se almacena directamente en la posición 100 del arreglo.

![[2026-02-06_05-09-38.png]]

Esta es una situación ideal. Todas las posiciones de la tabla T están ocupadas de manera útil, y para dos claves distintas se cumple que tienen transformaciones distintas: si `k1 != k2`, entonces `H(k1) != H(k2)`. Esto representa un **hashing perfecto**.

*Hashing* utiliza conceptos matemáticos como [inyectividad, sobreyectividad y biyectividad](https://es.wikipedia.org/wiki/Biyecci%C3%B3n,_inyecci%C3%B3n_y_sobreyecci%C3%B3n), así como el concepto general de [función](https://es.wikipedia.org/wiki/Funci%C3%B3n_(matem%C3%A1tica)).

### Hashing Perfecto

El hashing perfecto ocurre cuando la función de transformación **H** es biyectiva, permitiendo una eficiencia O(1) igual a la de las tablas de acceso directo.

El problema es que el ejemplo anterior no refleja situaciones del mundo real. Aunque la cantidad de claves a almacenar sea **N**, el conjunto de valores posibles para esas claves suele ser mucho mayor que el espacio disponible (**M**).

Un ejemplo más real: usar el DNI (con valores entre ~5.000.000 y 50.000.000) como clave para 1000 empleados. Sería absurdo asignar decenas de millones de espacios de memoria. En este caso, donde el conjunto de claves posibles es mayor que las entradas disponibles (**|K| > M**), es donde inevitablemente se pueden producir **colisiones**.

### Técnicas de Transformación de Claves

Una alternativa a las tablas de acceso directo (que no son prácticas en casos reales) es usar una **tabla hash**. Es una estructura de disposición secuencial (como un arreglo) que, en lugar de usar la clave directamente como índice, utiliza una **función de dispersión (hash)** **h(k)** para calcular un índice dentro de los límites de la tabla.

Es crucial elegir un tamaño de tabla **M** proporcional a la cantidad de elementos **N** que se espera almacenar, y una función de dispersión adecuada que minimice conflictos.

### ¿Qué es una Colisión?

Una colisión ocurre cuando la función de dispersión **H** asigna la misma dirección **d** a dos claves distintas **k1** y **k2**.
Es decir, si `k1 != k2` pero `H(k1) == H(k2) == d`.
En este caso, **k1** y **k2** se llaman **claves sinónimas**.

### Aspectos importantes al implementar Hashing

Podemos distinguir dos aspectos cruciales al usar esta técnica:
1.  La elección de la función de transformación **H**.
2.  La política de manejo de colisiones que se implementará.

#### La elección de la función de transformación **H**

Si los valores posibles del conjunto de claves tienen la misma probabilidad de ocurrencia, debemos encontrar una función **H** que:
1.  Distribuya las claves de manera **uniforme** en el rango de direcciones.
2.  Sea **eficiente** (rápida de calcular). El objetivo del *hashing* es la velocidad.

La elección depende mucho del lote de claves específico. A continuación, algunas funciones de transformación sencillas y comunes, donde **k** es una clave, **M** el tamaño de la tabla y **N** el número de elementos.

**Método de la División**
`h(k) = k mod M`
Este método produce resultados satisfactorios en muchos casos, **especialmente si M es un número primo** no cercano a una potencia de 2.

*   **Ejemplo:** Para una tabla de tamaño `M = 13` (primo) y claves `k = {15, 27, 44, 70}`:
    *   `15 % 13 = 2`
    *   `27 % 13 = 1`
    *   `44 % 13 = 5`
    *   `70 % 13 = 5` **(¡Colisión entre 44 y 70!)**

*¿Por qué un número primo?*
Elegir un tamaño **M** primo ayuda a lograr una distribución más uniforme, especialmente cuando las claves tienen patrones (como ser múltiplos de un número). Si **M** tiene muchos divisores, es más probable que claves con ciertas regularidades terminen en los mismos contenedores. Un primo solo es divisible por 1 y sí mismo, reduciendo este riesgo.

**Método de la Extracción**
Consiste en extraer de la clave los dígitos que varían más aleatoriamente (ej., los últimos 3 dígitos de un DNI).
*   **Ejemplo:** Para DNI `k = 35.208.741`, extraer los últimos 3 dígitos: `h(k) = 741`.

**Método del Plegado**
Divide la clave en partes (generalmente del mismo tamaño que el número de dígitos deseado en la dirección) y las suma.
*   **Ejemplo:** Para `k = 123456` y direcciones de 2 dígitos (`M=100`). Dividir en partes de 2: `12 | 34 | 56`. Sumar: `h(k) = 12 + 34 + 56 = 102`. Aplicar módulo si es necesario: `102 % 100 = 2`.

**Método del Cuadrado Medio**
Eleva la clave al cuadrado y extrae los dígitos centrales del resultado.
*   **Ejemplo:** Para `k = 123`. `k² = 15129`. Extraer 3 dígitos centrales (elige una posición fija): `512`. Entonces `h(123) = 512`.

**¿Qué sucede con las claves alfanuméricas?**
Se transforman a números. La forma más sencilla es sumar los valores ASCII de cada carácter.

`h("AMOR") = ASCII('A') + ASCII('M') + ASCII('O') + ASCII('R') = 65 + 77 + 79 + 82 = 303`

El problema es que anagramas como "AMOR" y "ROMA" producen el mismo hash (303). Para solucionarlo, se incorpora la posición del carácter, multiplicando su valor ASCII por un peso (como el índice o una base elevada a la potencia del índice).

`h("AMOR") = 65*1 + 77*2 + 79*3 + 82*4 = 65 + 154 + 237 + 328 = 784`
`h("ROMA") = 82*1 + 79*2 + 77*3 + 65*4 = 82 + 158 + 231 + 260 = 731`

En todas las funciones, el resultado final debe ajustarse (usando módulo `% M`) para que pertenezca al rango de direcciones de la tabla `[0, M-1]`.

### Política de Manejo de Colisiones

Debemos elegir una función que minimice colisiones, pero es importante aceptar que **siempre ocurrirán** cuando el espacio de claves posibles sea mayor que el tamaño de la tabla (**|K| > M**). Un ejemplo famoso es la **paradoja del cumpleaños**: en un grupo de sólo 23 personas, hay más de un 50% de probabilidad de que al menos dos compartan cumpleaños (colisión). Con 88 personas, es casi seguro que haya tres o más con la misma fecha. El espacio (365 días) es limitado frente al número de "inserciones" (personas).

Por esta razón, necesitamos una política para manejar las colisiones cuando ocurran. Las estrategias principales son:

1.  **Encadenamiento (Dispersión Abierta o *Chaining*)**
2.  **Uso de *Buckets* o Cubos**
3.  **Direccionamiento Abierto (*Open Addressing*)**

**1. Encadenamiento (Dispersión Abierta)**
Cada posición de la tabla **T** es la cabeza de una lista enlazada. Todos los elementos cuya clave `hash` a la misma dirección **d** se almacenan en la lista asociada a `T[d]`.
*   **Inserción:** Se añade el nuevo elemento al final (o principio) de la lista en `T[h(k)]`.
*   **Búsqueda:** Se calcula `h(k)`, luego se recorre la lista en `T[h(k)]` buscando la clave `k`.
*   **Ventaja:** Simple, la tabla nunca se "llena" (las listas pueden crecer).
*   **Desventaja:** El acceso deja de ser estrictamente O(1). En el peor caso (todas las claves en una lista), la complejidad es O(n). Se usa memoria adicional para los nodos de la lista.

![[2026-02-06_07-56-58.png]]
*Representación gráfica del encadenamiento. Cada cubo es una lista enlazada.*

**2. Uso de *Buckets* (Cubos)**
Cada entrada de la tabla **T** es un *bucket* (cubo) de tamaño fijo **b** que puede contener más de un registro (ej., un arreglo pequeño de tamaño b).
*   **Inserción:** Se calcula `d = h(k)`. Si el bucket `T[d]` tiene espacio, se inserta ahí. Si está lleno, el registro se envía a un **área de *overflow*** separada.
*   **Búsqueda:** Se busca primero en `T[h(k)]`. Si no está y el bucket estaba lleno, se busca en el área de *overflow* asociada a esa dirección.
*   **Ventaja:** Reduce el overhead de memoria comparado con listas enlazadas si **b** se elige bien.
*   **Desventaja:** Si el área de *overflow* crece mucho, el rendimiento se degrada. Se debe dimensionar cuidadosamente.

![[2026-02-06_08-09-20.png]]
*Representación gráfica del método de buckets con un área de overflow.*

**Dispersión Cerrada vs. Abierta:**
*   **Dispersión Abierta (ej., Encadenamiento):** El espacio para almacenar colisiones es externo a la tabla principal (listas). Es potencialmente ilimitado.
*   **Dispersión Cerrada (ej., *Buckets* y Direccionamiento Abierto):** El espacio para almacenar colisiones está dentro de la tabla principal o en un área predefinida y limitada (como el área de *overflow*).

**3. Direccionamiento Abierto**
Todos los elementos se almacenan directamente en la tabla **T**. No hay estructuras auxiliares. Cuando ocurre una colisión en `d = h(k)`, se busca una celda alternativa **vacía** dentro de la misma tabla siguiendo una **secuencia de prueba** predefinida `p(k, i)`, donde `i` es el número de intento.
*   **Inserción:** Se calcula `d = h(k)`. Si `T[d]` está libre, se inserta. Si está ocupado, se calcula `d1 = p(k, 1)`. Si `T[d1]` está libre, se inserta. Si no, se prueba `d2 = p(k, 2)`, y así sucesivamente.
*   **Búsqueda:** Se sigue la misma secuencia de prueba `p(k, i)` hasta encontrar la clave (éxito) o una celda vacía (fracaso, la clave no existe).
*   **Ventaja:** No usa memoria extra. Todo está en un solo arreglo, lo que puede ser más eficiente en memoria y caché.
*   **Desventaja:** La tabla tiene un límite máximo de elementos (N ≤ M). El rendimiento se degrada severamente cuando la tabla se llena.

**Secuencias de prueba comunes:**

*   **Prueba Lineal:** `p(k, i) = (h(k) + i) % M`
    *   **Problema:** Produce **agrupamiento primario**. Las celdas ocupadas tienden a formar bloques largos y contiguos, lo que hace que las búsquedas e inserciones posteriores dentro de ese bloque sean más lentas.
    *   **Ejemplo:** Con `M=7`, `h(k)=k % 7`. Insertar claves `16, 8, 19, 4`.
        *   `h(16)=2` -> T[2]=16
        *   `h(8)=1` -> T[1]=8
        *   `h(19)=5` -> T[5]=19
        *   `h(4)=4` -> T[4]=4
        *   Ahora, insertar `5`. `h(5)=5`, pero T[5] está ocupado. La secuencia lineal prueba: (5+1)%7=6. T[6] está libre. Se inserta en T[6].
        *   Se forma un pequeño grupo en las posiciones 4,5,6.

*   **Prueba Cuadrática:** `p(k, i) = (h(k) + c1*i + c2*i²) % M` (con `c1` y `c2` constantes).
    *   Ayuda a reducir el agrupamiento primario, pero puede producir **agrupamiento secundario**: dos claves diferentes con el mismo hash inicial (`h(k1) = h(k2)`) seguirán exactamente la misma secuencia de prueba, creando un "camino" de colisiones.

*   **Doble Hashing:** `p(k, i) = (h1(k) + i * h2(k)) % M`
    *   Se usan **dos funciones hash distintas**. `h1(k)` da la posición inicial. `h2(k)` da el "salto" entre intentos.
    *   **Ventaja principal:** Si `h2(k)` es distinto para claves diferentes, **evita tanto el agrupamiento primario como el secundario**. Dos claves que colisionen en `h1` probablemente tendrán diferentes valores de `h2`, por lo que seguirán secuencias de prueba diferentes.
    *   **Ejemplo:** `h1(k) = k % 7`, `h2(k) = 5 - (k % 5)`. Para `k=19` y `k=33`:
        *   `h1(19)=5`, `h2(19)=5 - (19%5)=5-4=1`. Secuencia: 5, (5+1)%7=6, (5+2)%7=0, ...
        *   `h1(33)=5`, `h2(33)=5 - (33%5)=5-3=2`. Secuencia: 5, (5+2)%7=0, (5+4)%7=2, ...
        *   Las secuencias divergen desde el primer intento.

### Factor de Carga

El **factor de carga** (α) de una tabla hash se define como la razón entre el número de elementos almacenados (N) y el tamaño total de la tabla (M):

**α = N / M**

*   **Interpretación:** Indica cuán "llena" está la tabla.
*   **Importancia:** El rendimiento de una tabla hash (especialmente con direccionamiento abierto) se degrada rápidamente a medida que α se acerca a 1 (tabla saturada).
*   **Recomendación:** Para mantener un buen rendimiento, es común redimensionar la tabla (incrementar M y rehashear todos los elementos) cuando α supera un umbral (ej., 0.7 para direccionamiento abierto). Para encadenamiento, se puede tolerar α > 1, pero un α muy alto indica listas muy largas y rendimiento pobre.

--- 
**TE SIENTES DETERMINADO**