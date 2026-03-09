---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-17T17:32:00
Revision: 2026-01-20T20:16:00
---
# Tabla de Contenido
- [[#Beneficios de las funciones|Beneficios de las funciones]]
	- [[#Beneficios de las funciones#1. Abstracción|1. Abstracción]]
	- [[#Beneficios de las funciones#2. Encapsulación|2. Encapsulación]]
	- [[#Beneficios de las funciones#3. Modularidad|3. Modularidad]]
	- [[#Beneficios de las funciones#4. Reusabilidad|4. Reusabilidad]]
	- [[#Beneficios de las funciones#5. Mantenibilidad|5. Mantenibilidad]]
	- [[#Beneficios de las funciones#6. Testabilidad|6. Testabilidad]]
- [[#Definiendo funciones en Python|Definiendo funciones en Python]]
- [[#Llamando funciones en Python|Llamando funciones en Python]]
	- [[#Llamando funciones en Python#Argumentos posicionales|Argumentos posicionales]]
	- [[#Llamando funciones en Python#Argumentos por palabra clave (*keyword arguments*)|Argumentos por palabra clave (*keyword arguments*)]]
- [[#Retornando valores desde una función|Retornando valores desde una función]]
	- [[#Retornando valores desde una función#1. Producir un efecto (side effect)|1. Producir un efecto (side effect)]]
	- [[#Retornando valores desde una función#2. Retornando valores explícitos|2. Retornando valores explícitos]]
	- [[#Retornando valores desde una función#3. Salida temprana de funciones|3. Salida temprana de funciones]]
	- [[#Retornando valores desde una función#4. Retornando valores booleanos|4. Retornando valores booleanos]]
	- [[#Retornando valores desde una función#5. Retornando iteradores y generadores|5. Retornando iteradores y generadores]]
	- [[#Retornando valores desde una función#6. Creando cierres (*closures*)|6. Creando cierres (*closures*)]]
- [[#Características avanzadas de funciones|Características avanzadas de funciones]]
	- [[#Características avanzadas de funciones#1. Valores por defecto para parámetros|1. Valores por defecto para parámetros]]
		- [[#1. Valores por defecto para parámetros#⚠️ **¡ADVERTENCIA! Peligro con valores por defecto mutables**|⚠️ **¡ADVERTENCIA! Peligro con valores por defecto mutables**]]
	- [[#Características avanzadas de funciones#2. Número variable de argumentos: `*args` y `**kwargs`|2. Número variable de argumentos: `*args` y `**kwargs`]]
		- [[#2. Número variable de argumentos: `*args` y `**kwargs`#`*args` (argumentos posicionales variables)|`*args` (argumentos posicionales variables)]]
		- [[#2. Número variable de argumentos: `*args` y `**kwargs`#`**kwargs` (argumentos de palabra clave variables)|`**kwargs` (argumentos de palabra clave variables)]]
		- [[#2. Número variable de argumentos: `*args` y `**kwargs`#Combinando todo|Combinando todo]]
	- [[#Características avanzadas de funciones#3. Argumentos solo-posicionales y solo-nombre|3. Argumentos solo-posicionales y solo-nombre]]
		- [[#3. Argumentos solo-posicionales y solo-nombre#Solo-posicionales (`/`)|Solo-posicionales (`/`)]]
		- [[#3. Argumentos solo-posicionales y solo-nombre#Solo-nombre (`*`)|Solo-nombre (`*`)]]
	- [[#Características avanzadas de funciones#4. Desempaquetando argumentos al llamar|4. Desempaquetando argumentos al llamar]]
	- [[#Características avanzadas de funciones#5. Documentación y anotaciones|5. Documentación y anotaciones]]
		- [[#5. Documentación y anotaciones#Docstrings|Docstrings]]
		- [[#5. Documentación y anotaciones#Anotaciones de tipo|Anotaciones de tipo]]
	- [[#Características avanzadas de funciones#6. Funciones asíncronas (breve introducción)|6. Funciones asíncronas (breve introducción)]]
# Funciones en Python

Las funciones son una parte **FUNDAMENTAL** del desarrollo de software. La inmensa mayoría de lenguajes actuales *mainstream* soportan esta funcionalidad.

Una función, en pocas palabras, es un **bloque de código reutilizable** que puede ser invocado mediante un identificador definido por el programador, resultando en la ejecución de dicho código. Esto ofrece **MUCHÍSIMAS** ventajas para estructurar y organizar programas.

## Beneficios de las funciones

¿Cuáles son las ventajas o beneficios que nos dan las funciones? Hay varias razones de peso para definirlas en nuestros códigos:

### 1. Abstracción
La abstracción significa ocultar la complejidad o el funcionamiento interno de una tarea detrás de una interfaz simple, permitiendo al usuario realizarla sin preocuparse por los detalles técnicos. Esta funcionalidad compleja puede estar encapsulada en funciones.

*   **Ejemplo cotidiano**: Sabes que al girar el volante a la derecha, el auto se mueve en esa dirección, pero no conoces todos los procesos mecánicos intermedios.
*   **Ejemplo en programación**: La mayoría de los programadores no saben qué hace internamente `print()`, solo saben que si le pasan un objeto o texto, este se imprime en pantalla. La función `print()` es la interfaz que abstrae la complejidad de enviar datos a la salida estándar. Esto pasa igual con todas las [[Funciones Nativas en Python]].

### 2. Encapsulación
La encapsulación se refiere a agrupar o **encapsular** comportamientos y datos dentro de una unidad, restringiendo el acceso directo a algunos de sus componentes internos.

Cuando defines una función y desarrollas su lógica interna, estás juntando variables, bucles y estructuras condicionales que, por defecto, solo pueden ser accedidas dentro del ámbito (**scope**) de esa función. Lo único que puedes hacer desde fuera es invocar a la función para que ejecute todo su bloque de código (aunque también puedes especificar qué datos de entrada y salida son accesibles). Esto es encapsular o restringir el acceso.

### 3. Modularidad
La modularidad es un principio de diseño que consiste en dividir un problema grande en subproblemas más pequeños y manejables, que en conjunto resuelven el problema general. En programación, es dividir un programa en componentes separados, independientes e intercambiables, donde cada componente **encapsula** una parte específica de la funcionalidad.

Las funciones permiten precisamente esto: dividir el programa en piezas más pequeñas que cumplen un rol específico.

**Ejemplo sin funciones (código lineal):**
```python
# Main program
# Read the file
<statement_0>
<statement_1>
...
<statement_n>

# Process the file
<statement_0>
<statement_1>
...
<statement_n>

# Write the result to another file
<statement_0>
<statement_1>
...
<statement_n>
```

**Ejemplo con funciones (código modular):**
```python
def read_file():
    <statement_0>
    <statement_1>
    ...
    <statement_n>

def process_file():
    <statement_0>
    <statement_1>
    ...
    <statement_n>

def write_file():
    <statement_0>
    <statement_1>
    ...
    <statement_n>

# Main program
read_file()
process_file()
write_file()
```

Esta alternativa modular nos permite reutilizar cada bloque de código las veces que queramos y hace que el flujo del programa sea más fácil de seguir y mantener.

### 4. Reusabilidad
La reusabilidad es la habilidad de usar código existente en nuevos contextos sin tener que repetir bloques de instrucciones cada vez que surge la necesidad.

Las funciones son excelentes para esto porque, mediante un identificador (su nombre), podemos llamar a ese bloque de código cuantas veces sea necesario, sin reescribirlo.

### 5. Mantenibilidad
En programación, decimos que un código es *mantenible* si es fácil y rápido de entender, corregir, mejorar o adaptar con el tiempo. Una base de código mantenible es limpia, está bien estructurada y es modular, lo que permite a los desarrolladores hacer cambios con el menor riesgo de romper el programa o introducir *bugs*.

Las funciones cumplen un rol esencial en esto porque:
*   **Descomponen** el código en pequeñas partes lógicas.
*   **Fomentan** la reusabilidad y la consistencia.
*   **Facilitan** el *testing* y la depuración (*debugging*).
*   **Incentivan** tener una documentación clara (mediante *docstrings*).

### 6. Testabilidad
La *testabilidad* se refiere a qué tan fácil es probar una pieza de código para asegurarse de que cumple con lo esperado. Escribir funciones con argumentos claros y valores de retorno definidos hace que esta tarea sea más sencilla y predecible, ya que puedes aislar y probar cada función individualmente.

## Definiendo funciones en Python

La sintaxis general para definir una función es la siguiente:

```python
def function_name([parameters]):
    <block>
```

A continuación, un desglose de los componentes de esta sintaxis:

| Componente      | Descripción                                                                                          |
| :-------------- | :--------------------------------------------------------------------------------------------------- |
| `def`           | La palabra clave que inicia la definición de la función.                                             |
| `function_name` | Un [[Sintaxis Basica Python#Identificadores\|identificador]] de Python válido que nombra la función. |
| `[parameters]`  | Una lista opcional y separada por comas de parámetros formales para la función.                      |
| `:`             | La puntuación que denota el final del encabezado de la función.                                      |
| `<block>`       | El bloque de código o **cuerpo** de la función.                                                      |

El cuerpo (`<block>`) es una serie de sentencias que se ejecutarán al llamar a la función. Se define por indentación, al igual que los bloques de código asociados con una estructura de control como `if` o `while`.

**Nota**: A veces, durante la planificación, un programador sabe qué funciones necesitará pero aún no ha definido su implementación. En Python, se usa la palabra clave `pass` para crear un "boceto" o una función que no hace nada temporalmente. Esto es útil para estructurar el programa sin tener que escribir toda la lógica de inmediato.

```python
>>> def funcion_por_implementar():
...     pass  # TODO: Implementar más tarde
...
>>> funcion_por_implementar()  # No hace nada, pero no genera error
```

## Llamando funciones en Python

La forma de invocar o llamar a una función es la siguiente:
```python
function_name([arguments])
```

Los **argumentos** representan los valores concretos que le brindas a la función. Estos valores serán tomados y representados por los **parámetros** definidos en la función.

**Nota crucial**: Distingue entre **parámetros** y **argumentos**.
*   **Parámetros**: Son las variables listadas dentro de los paréntesis en la **definición** de la función. Es lo que la función *espera recibir*.
*   **Argumentos**: Son los valores reales que se pasan a la función cuando esta es **invocada**.

Los argumentos son opcionales (una función puede no tener parámetros). Sin embargo, en Python **es obligatorio usar los paréntesis** al invocar una función, incluso si no se pasan argumentos.

### Argumentos posicionales
La forma más común de llamar a una función es especificando la posición de cada argumento, lo que se conoce como **argumentos posicionales**.

```python
>>> def calcular_costo(item, cantidad, precio):
...     print(f"{cantidad} {item} cuestan ${cantidad * precio:.2f}")
...
```

Para llamar a esta función, los argumentos deben estar **en el mismo orden** en que se definieron los parámetros:
```python
>>> calcular_costo("bananas", 6, 0.74)
6 bananas cuestan $4.44
```

Los argumentos posicionales pueden causar problemas si no se tiene cuidado. Si el orden no coincide, obtendremos resultados inesperados o errores:
```python
>>> calcular_costo("bananas", 0.74, 6)  # Orden incorrecto
0.74 bananas cuestan $4.44  # Resultado ilógico

>>> calcular_costo(6, "bananas", 0.74)  # Orden incorrecto
Traceback (most recent call last):
    ...
TypeError: can't multiply sequence by non-int of type 'float'  # Error
```

**Nota**: La **firma de una función** consiste en su nombre seguido de la lista de sus parámetros entre paréntesis: `calcular_costo(item, cantidad, precio)`. Además del orden, la **cantidad** de argumentos debe coincidir con la cantidad de parámetros, a menos que se usen valores por defecto (ver más adelante).

### Argumentos por palabra clave (*keyword arguments*)
Al invocar una función, podemos especificar explícitamente a qué parámetro va dirigido cada valor usando la sintaxis `argumento=valor`. Esto se llama pasar **argumentos por palabra clave**.

```python
>>> calcular_costo(item="bananas", cantidad=6, precio=0.74)
6 bananas cuestan $4.44
```

Esta forma **evita el problema del orden**, ya que cada argumento se asocia directamente con su parámetro correspondiente. También mejora mucho la legibilidad del código:
```python
# Usando argumentos posicionales (menos claro)
actualizar_producto(1234, 15, 2.55, "31-12-2025")

# Usando argumentos por palabra clave (más explícito)
actualizar_producto(
    id_producto=1234,
    cantidad=15,
    precio=2.55,
    fecha_expiracion="31-12-2025"
)
```

**Combinando ambos estilos**: Se pueden mezclar argumentos posicionales y por palabra clave en una misma llamada, pero **los argumentos posicionales deben ir primero**.
```python
>>> calcular_costo("bananas", cantidad=6, precio=0.74)  # ✅ Correcto
6 bananas cuestan $4.44

>>> calcular_costo(item="bananas", 6, precio=0.74)  # ❌ Error
  File "<input>", line 1
SyntaxError: positional argument follows keyword argument
```

## Retornando valores desde una función

En general, las funciones pueden realizar una o más de las siguientes acciones:
1.  Causar un efecto (como imprimir o modificar algo).
2.  Retornar un valor al código que la invocó.
3.  Ambas cosas (causar un efecto y retornar un valor).

### 1. Producir un efecto (side effect)
En Python, una función puede modificar un objeto que esté fuera de su ámbito local. Este cambio se conoce como **efecto secundario** (*side effect*).

```python
>>> def duplicar(numeros):
...     for i, _ in enumerate(numeros):
...         numeros[i] *= 2  # Modifica la lista original
...
>>> mi_lista = [1, 2, 3, 4, 5]
>>> duplicar(mi_lista)
>>> mi_lista
[2, 4, 6, 8, 10]  # ¡La lista original fue modificada!
```

Esto sucede porque las listas son **mutables**. Aunque es posible, **no es una práctica recomendada** modificar objetos mutables pasados como argumentos, ya que puede hacer que el programa sea difícil de razonar y depurar.

Una solución más segura es **crear y retornar una nueva lista**:
```python
>>> def duplicar_seguro(numeros):
...     resultado = []
...     for numero in numeros:
...         resultado.append(numero * 2)
...     return resultado  # Retorna una copia modificada
...
>>> original = [1, 2, 3, 4, 5]
>>> nueva_lista = duplicar_seguro(original)
>>> nueva_lista
[2, 4, 6, 8, 10]
>>> original  # La lista original permanece intacta
[1, 2, 3, 4, 5]
```

### 2. Retornando valores explícitos
Para que una función devuelva un valor al código que la llamó, se utiliza la sentencia `return`. Esta sentencia cumple dos propósitos:
1.  Pasar datos de vuelta al invocador.
2.  Terminar la ejecución de la función inmediatamente, devolviendo el control al invocador.

```python
>>> def identidad(x):
...     return x
...
>>> resultado = identidad(42)
>>> resultado
42
```

**¡Importante!**: La sentencia `return` **solo puede usarse dentro del cuerpo de una función**.

Si retornas múltiples valores separados por comas, Python los empaquetará automáticamente en una **tupla**:
```python
>>> def crear_punto(x, y):
...     return x, y  # Equivalente a: return (x, y)
...
>>> punto = crear_punto(2, 4)
>>> punto
(2, 4)
```

Una función puede retornar **cualquier tipo de objeto**, incluyendo otras funciones, diccionarios, listas, etc.
```python
>>> def obtener_config():
...     return {"uno": 1, "dos": 2, "tres": 3}
...
>>> config = obtener_config()
>>> config["dos"]
2
```

Si una función no tiene una sentencia `return`, o si la sentencia `return` no especifica un valor, la función retorna automáticamente el objeto especial `None`.
```python
>>> def funcion_sin_return():
...     print("Hola")
...
>>> resultado = funcion_sin_return()
Hola
>>> print(resultado)
None
```

### 3. Salida temprana de funciones
Dado que `return` termina la función, se puede usar para salir de ella de manera temprana bajo ciertas condiciones, a menudo dentro de estructuras `if`.

```python
from pathlib import Path

def leer_contenido_archivo(ruta_archivo):
    path = Path(ruta_archivo)

    if not path.exists():
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        return  # Sale temprano, retorna None

    if not path.is_file():
        print(f"Error: '{ruta_archivo}' no es un archivo.")
        return  # Sale temprano, retorna None

    return path.read_text(encoding="utf-8")  # Retorna el contenido
```

### 4. Retornando valores booleanos
Un uso común de `return` es en funciones **predicado** o de verificación, que retornan `True` o `False` dependiendo de una condición.

```python
>>> def es_par(numero):
...     return numero % 2 == 0  # La expresión ya evalúa a True/False
...
>>> es_par(2)
True
>>> es_par(3)
False
```

### 5. Retornando iteradores y generadores
Un **generador** es un tipo especial de iterador que produce valores "sobre la marcha", uno a la vez, en lugar de crear y almacenar toda una secuencia en memoria. Esto es muy eficiente para conjuntos de datos grandes. Se crean usando la palabra clave `yield`.

```python
>>> def promedio_acumulado(numeros):
...     total = 0
...     for indice, numero in enumerate(numeros, start=1):
...         total += numero
...         yield total / indice  # Pausa y devuelve un valor
...
>>> valores = [5, 3, 8, 2, 5]  # Simula un conjunto grande de datos
>>> for prom_acum in promedio_acumulado(valores):
...     print(f"Promedio acumulado: {prom_acum:.2f}")
...
Promedio acumulado: 5.00  # (5)/1
Promedio acumulado: 4.00  # (5+3)/2
Promedio acumulado: 5.33  # (5+3+8)/3
Promedio acumulado: 4.50  # (5+3+8+2)/4
Promedio acumulado: 4.60  # (5+3+8+2+5)/5
```

La palabra clave `yield` **pausa** la función, guarda su estado local, y retorna un valor. Cuando la función se "reanuda" (por ejemplo, en la siguiente iteración de un bucle `for`), continúa ejecutándose justo después del `yield`.

### 6. Creando cierres (*closures*)
Un **cierre** (*closure*) es una función interna que recuerda, accede y utiliza variables de la función externa que la encierra, incluso después de que esta última haya terminado su ejecución.

```python
>>> def funcion_externa():
...     valor = 42
...     def cierre_interno():
...         # ¡Recuerda 'valor' de funcion_externa!
...         print(f"El valor es: {valor}!")
...     return cierre_interno  # Retorna la función, no la llama
...
>>> mi_funcion = funcion_externa()
>>> mi_funcion()  # Aunque funcion_externa ya terminó, cierre_interno recuerda 'valor'
El valor es: 42!
```

Dentro de `funcion_externa()`, defines una variable local `valor` y una función interna `cierre_interno()`. Esta función interna imprime un mensaje usando `valor`. Al retornar `cierre_interno` (sin paréntesis, es decir, el objeto función), creas un **cierre** que "recuerda" el entorno donde fue creado.

**Uso práctico**: Crear funciones con "estado" o configuración específica.
```python
>>> def generar_potencia(exponente):
...     def potencia(base):
...         return base ** exponente
...     return potencia
...
>>> cuadrado = generar_potencia(2)
>>> cuadrado(4)  # 4**2
16
>>> cuadrado(6)  # 6**2
36
>>> cubo = generar_potencia(3)
>>> cubo(3)  # 3**3
27
>>> cubo(5)  # 5**3
125
```
`cuadrado` y `cubo` son funciones distintas, cada una con su propio "estado" (el valor de `exponente` que recordaron cuando fueron creadas).

## Características avanzadas de funciones

### 1. Valores por defecto para parámetros
Puedes asignar un valor por defecto a un parámetro en la definición de la función. Si al invocar la función no se proporciona un argumento para ese parámetro, se usará el valor por defecto.

```python
>>> def saludar(nombre="Mundo"):
...     print(f"¡Hola, {nombre}!")
...
>>> saludar()
¡Hola, Mundo!
>>> saludar("Pythonista")
¡Hola, Pythonista!
```

**Orden importante**: Los parámetros con valor por defecto deben ir **después** de los que no lo tienen (los obligatorios).
```python
>>> def saludar_detallado(nombre, detallado=False):
...     if detallado:
...         print(f"¡Hola, {nombre}! Bienvenido/a a Python.")
...     else:
...         print(f"¡Hola, {nombre}!")
...
>>> saludar_detallado("Ana")
¡Hola, Ana!
>>> saludar_detallado("Ana", detallado=True)
¡Hola, Ana! Bienvenido/a a Python.
```

#### ⚠️ **¡ADVERTENCIA! Peligro con valores por defecto mutables**
**Este es uno de los errores más comunes y sutiles en Python.** **NUNCA** uses un objeto mutable (como una lista `[]` o un diccionario `{}`) como valor por defecto.

```python
# ❌¡FUNCION PELIGROSA! ¡NO HAGAS ESTO!
def agregar_elemento_mal(elemento, objetivo=[]):
    objetivo.append(elemento)
    return objetivo

print("=== FUNCIÓN PELIGROSA (objetivo=[]) ===")
resultado1 = agregar_elemento_mal(1)
print(f"Llamada 1: {resultado1}")  # [1]
resultado2 = agregar_elemento_mal(2)
print(f"Llamada 2: {resultado2}")  # [1, 2] ¡SORPRESA!
resultado3 = agregar_elemento_mal(3)
print(f"Llamada 3: {resultado3}")  # [1, 2, 3]
print(f"¿Mismo objeto? {resultado1 is resultado2 is resultado3}")  # True
```

**¿Qué pasó?** El valor por defecto (la lista `[]`) **se evalúa solo una vez**, cuando se define la función. Todas las llamadas posteriores comparten **esa misma lista en memoria**. Modificarla en una llamada afecta a todas las demás.

**✅ SOLUCIÓN CORRECTA**: Usa `None` como valor por defecto y crea el objeto mutable dentro de la función.
```python
# ✅ FUNCIÓN SEGURA
def agregar_elemento_bien(elemento, objetivo=None):
    if objetivo is None:  # Si no se pasó una lista, crea una nueva
        objetivo = []
    objetivo.append(elemento)
    return objetivo

print("\n=== FUNCIÓN SEGURA (objetivo=None) ===")
resultado1 = agregar_elemento_bien(1)
print(f"Llamada 1: {resultado1}")  # [1]
resultado2 = agregar_elemento_bien(2)
print(f"Llamada 2: {resultado2}")  # [2] ✅
resultado3 = agregar_elemento_bien(3)
print(f"Llamada 3: {resultado3}")  # [3] ✅
print(f"¿Mismo objeto? {resultado1 is resultado2}")  # False
```

### 2. Número variable de argumentos: `*args` y `**kwargs`
#### `*args` (argumentos posicionales variables)
Permite a una función aceptar cualquier número de argumentos posicionales. Dentro de la función, `args` es una **tupla** que contiene todos los argumentos extra posicionales.

```python
>>> def promedio(*args):
...     print(f"Argumentos recibidos (como tupla): {args}")
...     return sum(args) / len(args)
...
>>> promedio(1, 2, 3, 4, 5, 6)
Argumentos recibidos (como tupla): (1, 2, 3, 4, 5, 6)
3.5
>>> promedio(7, 8, 9)
Argumentos recibidos (como tupla): (7, 8, 9)
8.0
```

#### `**kwargs` (argumentos de palabra clave variables)
Permite a una función aceptar cualquier número de argumentos por palabra clave. Dentro de la función, `kwargs` es un **diccionario** que contiene todos los argumentos extra con nombre.

```python
>>> def generar_reporte(**kwargs):
...     print("Reporte:")
...     for clave, valor in kwargs.items():
...         print(f"  - {clave.capitalize()}: {valor}")
...
>>> generar_reporte(producto="Teclado", precio=25.99, cantidad=10, categoria="Hardware")
Reporte:
  - Producto: Teclado
  - Precio: 25.99
  - Cantidad: 10
  - Categoria: Hardware
```

#### Combinando todo
Puedes combinar parámetros normales, `*args` y `**kwargs`. El orden **debe ser**:
1.  Parámetros normales (posicionales o con valor por defecto).
2.  `*args`
3.  `**kwargs`

```python
def funcion_maestra(a, b, *args, opcion=True, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"opcion: {opcion}")
    print(f"kwargs: {kwargs}")

funcion_maestra(1, 2, 3, 4, 5, opcion=False, x=10, y=20)
# a: 1, b: 2
# args: (3, 4, 5)
# opcion: False
# kwargs: {'x': 10, 'y': 20}
```

### 3. Argumentos solo-posicionales y solo-nombre
#### Solo-posicionales (`/`)
Usa una barra `/` en la lista de parámetros. Todos los parámetros a su izquierda **deben** pasarse por posición.

```python
>>> def formatear_nombre(nombre, apellido, /, titulo=None):
...     nombre_completo = f"{nombre} {apellido}"
...     if titulo:
...         nombre_completo = f"{titulo} {nombre_completo}"
...     return nombre_completo
...
>>> formatear_nombre("Jane", "Doe")  # ✅ Correcto
'Jane Doe'
>>> formatear_nombre("Jane", "Doe", titulo="Dra.")  # ✅ Correcto
'Dra. Jane Doe'
>>> formatear_nombre("Jane", apellido="Doe")  # ❌ Error
TypeError: formatear_nombre() got some positional-only arguments passed as keyword arguments: 'apellido'
```

#### Solo-nombre (`*`)
Usa un asterisco `*` solo en la lista de parámetros. Todos los parámetros a su derecha **deben** pasarse por palabra clave.

```python
>>> def crear_usuario(nombre, *, email, es_admin=False):
...     print(f"Usuario '{nombre}' creado.")
...     print(f"Email: {email}, Admin: {es_admin}")
...
>>> crear_usuario("Ana", email="ana@ejemplo.com")  # ✅ Correcto
Usuario 'Ana' creado.
Email: ana@ejemplo.com, Admin: False
>>> crear_usuario("Ana", "ana@ejemplo.com")  # ❌ Error (email debe ser por keyword)
TypeError: crear_usuario() takes 1 positional argument but 2 were given
```

### 4. Desempaquetando argumentos al llamar
Así como `*` y `**` recogen argumentos en la definición, también sirven para **desempaquetar** secuencias y diccionarios al invocar una función.

```python
>>> def mostrar_info(x, y, z):
...     print(f"x={x}, y={y}, z={z}")
...
>>> lista = [1, 2, 3]
>>> mostrar_info(*lista)  # Desempaqueta la lista en 3 argumentos posicionales
x=1, y=2, z=3

>>> dicc = {'x': 10, 'y': 20, 'z': 30}
>>> mostrar_info(**dicc)  # Desempaqueta el diccionario en argumentos por nombre
x=10, y=20, z=30
```

### 5. Documentación y anotaciones
#### Docstrings
Es una [[Trabajando con los strings en Python#Strings Multilínea|cadena de texto literal]] ubicada como **primera sentencia** en el cuerpo de una función. Sirve para documentar su propósito, uso, parámetros y valores de retorno. Se accede mediante `funcion.__doc__`.

```python
def promedio(*numeros):
    """
    Calcula el promedio de una serie de números.

    Args:
        *numeros (float o int): Uno o más valores numéricos.

    Returns:
        float: La media aritmética de los valores proporcionados.

    Raises:
        ZeroDivisionError: Si no se proporcionan argumentos.

    Examples:
        >>> promedio(10, 20, 30)
        20.0
        >>> promedio(5, 15)
        10.0
    """
    return sum(numeros) / len(numeros)

print(promedio.__doc__)  # Imprime la documentación
```

#### Anotaciones de tipo
Proporcionan **metadatos** sobre los tipos esperados de los argumentos y el valor de retorno. No imponen restricciones en tiempo de ejecución, pero son útiles para herramientas de análisis estático como **mypy** y para la claridad del código.

```python
def sumar(a: int | float, b: int | float) -> int | float:
    """Suma dos números."""
    return a + b

# Python ejecutará esto sin error (las anotaciones son solo sugerencias).
resultado = sumar("3", "4")  # Retorna '34' (concatenación de strings)
print(resultado)

# Pero mypy detectará el error de tipo antes de ejecutar:
# $ mypy script.py
# script.py:6: error: Argument 1 to "sumar" has incompatible type "str"; expected "int | float" [arg-type]
# script.py:6: error: Argument 2 to "sumar" has incompatible type "str"; expected "int | float" [arg-type]
```

Las anotaciones se almacenan en el diccionario `__annotations__` de la función:
```python
>>> sumar.__annotations__
{'a': int | float, 'b': int | float, 'return': int | float}
```

### 6. Funciones asíncronas (breve introducción)
Python soporta programación asíncrona con `async`/`await`. Una función definida con `async def` es una **corrutina**. No se ejecuta inmediatamente al llamarla, sino que retorna un objeto corrutina que debe ser gestionado por un *event loop* (normalmente con `asyncio.run()`).

```python
import asyncio

async def obtener_datos():
    print("Iniciando solicitud...")
    await asyncio.sleep(2)  # Simula una operación de red (no bloqueante)
    print("Datos recibidos.")
    return {"usuario": "Ana", "estado": "activo"}

async def main():
    datos = await obtener_datos()  # 'await' pausa main() hasta que obtener_datos() termine
    print(f"Datos: {datos}")

# Ejecuta la corrutina principal
asyncio.run(main())
```

---

**TE SIENTES DETERMINADO** 🔥
