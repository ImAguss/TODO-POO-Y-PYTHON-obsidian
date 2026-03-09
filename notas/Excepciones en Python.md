---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-15T15:05:00
Revision: 2026-01-15T19:44:00
---
# Tabla de Contenidos
- [[#Entendiendo las excepciones y los errores de sintaxis|Entendiendo las excepciones y los errores de sintaxis]]
	- [[#Entendiendo las excepciones y los errores de sintaxis#Error de sintaxis|Error de sintaxis]]
	- [[#Entendiendo las excepciones y los errores de sintaxis#Excepciones|Excepciones]]
- [[#Provocando excepciones con `raise`|Provocando excepciones con `raise`]]
- [[#Depurando con `assert`|Depurando con `assert`]]
	- [[#Depurando con `assert`#`raise` vs `assert`: Diferencias clave|`raise` vs `assert`: Diferencias clave]]
- [[#Manejando excepciones: `try` y `except`|Manejando excepciones: `try` y `except`]]
	- [[#Manejando excepciones: `try` y `except`#Captura de múltiples excepciones|Captura de múltiples excepciones]]
	- [[#Manejando excepciones: `try` y `except`#Evita el `except:` desnudo|Evita el `except:` desnudo]]
- [[#Afinando el control: `else` y `finally`|Afinando el control: `else` y `finally`]]
	- [[#Afinando el control: `else` y `finally`#La cláusula `else`|La cláusula `else`]]
	- [[#Afinando el control: `else` y `finally`#La cláusula `finally`|La cláusula `finally`]]
- [[#Jerarquía de excepciones y creación de las propias|Jerarquía de excepciones y creación de las propias]]
	- [[#Jerarquía de excepciones y creación de las propias#Jerarquía de excepciones integradas|Jerarquía de excepciones integradas]]
	- [[#Jerarquía de excepciones y creación de las propias#Creando excepciones personalizadas|Creando excepciones personalizadas]]
- [[#Encadenamiento de excepciones (`raise... from`)|Encadenamiento de excepciones (`raise... from`)]]
- [[#Mejores prácticas|Mejores prácticas]]
# Excepciones en Python

## Entendiendo las excepciones y los errores de sintaxis

En Python, existen dos tipos principales de errores: **errores de sintaxis** y **excepciones**.

### Error de sintaxis

Los errores de sintaxis (también llamados errores de *parsing*) ocurren cuando el intérprete detecta una instrucción escrita de manera incorrecta, es decir, que viola las reglas gramaticales del lenguaje. Este tipo de error impide que el programa comience a ejecutarse.

>>> print(0 / 0))
  File "<stdin>", line 1
    print(0 / 0))
                ^
SyntaxError: unmatched ')'

*   El **resaltado (^)** señala la ubicación aproximada donde el analizador detectó el error.
*   El **mensaje de error** ("unmatched ')'") proporciona información útil sobre la causa. Un buen programador siempre presta atención a estos mensajes para depurar rápidamente.

### Excepciones

Las excepciones son errores que ocurren **durante la ejecución** de un programa que es sintácticamente correcto. Es decir, Python puede interpretar la instrucción, pero al intentar ejecutarla surge un problema.

>>> print(0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

*   **Traceback (Rastreo)**: Muestra la pila de llamadas: el camino que siguió el programa hasta llegar a la línea que causó el error. Es útil para rastrear el origen del problema en programas complejos.
*   **Tipo de Excepción**: La última línea indica el tipo específico de excepción (`ZeroDivisionError`). Python tiene muchas excepciones integradas (como `NameError`, `TypeError`, `FileNotFoundError`), cada una diseñada para un tipo de error particular.
*   **Mensaje de Detalle**: Junto al tipo de excepción, suele haber un mensaje que describe el error con más precisión ("division by zero").

En resumen: un **SyntaxError** es un error de escritura que detiene el programa antes de ejecutarse, mientras que una **Excepción** es un error de lógica o de entorno que ocurre mientras el programa ya se está ejecutando.

## Provocando excepciones con `raise`

Existen situaciones en las que es necesario detener el flujo del programa de forma voluntaria cuando se cumple una condición de error. Para ello se utiliza la palabra clave **`raise`**.

![[raise.3931e8819e08.avif]]

Incluso puedes personalizar el mensaje de error:

```python
number = 10
if number > 5:
    raise Exception(f"El número no debe exceder 5. ({number=})")
print(number)  # Esta línea NUNCA se ejecuta
```
```
Traceback (most recent call last):
  File "./low.py", line 3, in <module>
    raise Exception(f"El número no debe exceder 5. ({number=})")
Exception: El número no debe exceder 5. (number=10)
```

**Punto clave**: Cuando se ejecuta `raise`, el flujo normal del programa se interrumpe inmediatamente. En el ejemplo, la llamada a `print()` nunca se alcanza.

## Depurando con `assert`

Python ofrece un mecanismo específico para verificar suposiciones durante el desarrollo: la excepción **`AssertionError`** y la palabra clave **`assert`**.

![[assert.f6d344f0c0b4.png]]

`assert` actúa como un guardián condicional. Su lógica es: "**Afirmo que esta condición es verdadera. Si no lo es, hay un error en mi lógica y el programa debe detenerse**".

```python
# Sintaxis: assert condición, "mensaje opcional"
number = 1
assert number < 5, f"El número no debe exceder 5. ({number=})"
print(number)  # Se ejecuta porque la condición es True
```
```python
number = 10
assert number < 5, f"El número no debe exceder 5. ({number=})"
print(number)  # Nunca se ejecuta
```
```
Traceback (most recent call last):
  File "./low.py", line 2, in <module>
    assert (number < 5), f"El número no debe exceder 5. ({number=})"
            ^^^^^^^^^^
AssertionError: El número no debe exceder 5. (number=10)
```

### `raise` vs `assert`: Diferencias clave

| Característica | `raise` | `assert` |
| :--- | :--- | :--- |
| **Propósito** | Señalar **cualquier condición de error** en tiempo de ejecución. | Verificar **suposiciones internas** del programador (depuración). |
| **Uso en producción** | Sí. Es el mecanismo correcto para manejar errores esperados. | No. Deberían desactivarse. |
| **Control** | El programador decide cuándo y qué excepción lanzar. | Siempre lanza `AssertionError`. |
| **Desactivación** | No se puede desactivar. | Se desactiva ejecutando Python con el flag `-O` (`python -O programa.py`). |

**Regla de oro**: Usa `assert` para comprobar que tu código funciona como tú esperas ("este valor nunca debería ser negativo"). Usa `raise` para manejar errores que podrían ocurrir en producción y de los que el programa debe recuperarse ("el archivo de configuración no existe").

## Manejando excepciones: `try` y `except`

Para evitar que un programa termine abruptamente por una excepción, Python permite **capturarla** y **manejarla** mediante los bloques `try` y `except`.

![[try_except.c94eabed2c59.png]]

```python
def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Esta función solo puede ejecutarse en sistemas Linux.")
    print("Haciendo cosas de Linux...")

try:
    linux_interaction()
except RuntimeError as error:  # Captura SOLO RuntimeError
    print(f"Error capturado: {error}")
    print("La función linux_interaction() no se ejecutó.")
```
```
Error capturado: Esta función solo puede ejecutarse en sistemas Linux.
La función linux_interaction() no se ejecutó.
```

### Captura de múltiples excepciones

Puedes especificar varios bloques `except` para manejar diferentes tipos de errores de forma específica.

```python
try:
    linux_interaction()           # Puede lanzar RuntimeError
    with open("file.log") as file:# Puede lanzar FileNotFoundError
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(f"Error de archivo: {fnf_error}")
except RuntimeError as error:
    print(f"Error de sistema: {error}")
```

**⚠️ Importante**: Python ejecuta el bloque `try` hasta encontrar la **primera excepción**, luego salta al bloque `except` que la coincida. El orden de los bloques `except` **sí importa**: deben ir de la excepción más específica a la más general.

### Evita el `except:` desnudo

Un `except:` sin especificar el tipo de excepción capturará **cualquier error**, incluyendo `KeyboardInterrupt` (Ctrl+C) y `SystemExit`, lo que puede hacer que tu programa sea imposible de detener de forma elegante. Es una mala práctica que puede ocultar errores inesperados.

```python
# ❌ EVITA ESTO
try:
    operacion_riesgosa()
except:
    print("Algo pasó") # Oculta el error real

# ✅ HAZ ESTO
try:
    operacion_riesgosa()
except ValueError:  # Captura solo el error que esperas
    print("Hubo un ValueError")
except Exception as e:  # Captura otras excepciones genéricas de forma explícita
    print(f"Ocurrió un error inesperado: {e}")
```

## Afinando el control: `else` y `finally`

### La cláusula `else`

Se ejecuta **solo si el bloque `try` no lanzó ninguna excepción**. Es el lugar perfecto para colocar código que depende del éxito del `try`.

![[try_except_else.703aaeeb63d3.png]]

```python
try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    # Este código solo corre si linux_interaction() NO falló
    print("Haciendo aún más cosas de Linux...")
```

### La cláusula `finally`

Se ejecuta **siempre, sin importar si hubo una excepción o no, e incluso si hay un `return`, `break` o `continue` en el `try` o `except`.** Es esencial para tareas de limpieza (cerrar archivos, liberar conexiones de red).

![[try_except_else_finally.a7fac6c36c55.png]]

```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
    # Podría ocurrir una excepción aquí...
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    # ESTO SIEMPRE SE EJECUTA
    archivo.close()  # Asegura que el archivo se cierre incluso si hay error
    print("Limpieza completada.")
```

**Flujo resumido**:
1.  Se ejecuta el código en `try`.
2.  Si hay excepción, se salta a `except`. Si no, se salta a `else`.
3.  **Finalmente**, y sin falta, se ejecuta el bloque `finally`.

## Jerarquía de excepciones y creación de las propias

### Jerarquía de excepciones integradas

Todas las excepciones en Python derivan de la clase `BaseException`. Es importante conocer esta jerarquía para capturar excepciones de forma efectiva.

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── ArithmeticError (OverflowError, ZeroDivisionError)
    ├── LookupError (IndexError, KeyError)
    ├── OSError (FileNotFoundError, PermissionError)
    ├── ValueError
    ├── TypeError
    └── ... muchas más
```

*   **`Exception`** es la clase base para casi todas las excepciones que tu programa querrá manejar.
*   Capturar una clase base también captura todas sus subclases. Por ejemplo, un `except OSError:` atrapará tanto `FileNotFoundError` como `PermissionError`.
*   **No** se debe manejar `BaseException` directamente, ya que atraparía cosas como `KeyboardInterrupt`.

### Creando excepciones personalizadas

Cuando ninguna excepción integrada describe adecuadamente tu error, puedes crear una propia.

```python
# 1. Define una nueva clase que herede de Exception (o de una subclase)
class PlatformException(Exception):
    """Excepción lanzada cuando la plataforma del sistema es incompatible."""

# 2. Úsala con raise como cualquier otra excepción
def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise PlatformException("Esta función solo puede ejecutarse en sistemas Linux.")
    print("Haciendo cosas de Linux...")

# 3. Mánéjala de forma específica
try:
    linux_interaction()
except PlatformException as e:
    print(f"Error de plataforma: {e}")
```

**Ventajas**:
*   **Claridad**: Tu código comunica errores específicos del dominio de tu aplicación.
*   **Control**: Puedes capturar y manejar esta excepción de manera muy precisa, separándola de otros errores genéricos.

## Encadenamiento de excepciones (`raise... from`)

A veces, al manejar una excepción, surge otra. Para mostrar claramente la relación causa-efecto, puedes **encadenar excepciones**.

```python
try:
    # Supongamos que esto falla porque el archivo no existe
    with open("config.json") as f:
        config = json.load(f)
except FileNotFoundError as original_error:
    # Transformamos el error en uno más significativo para nuestro programa
    raise ConfigurationError("No se pudo cargar la configuración") from original_error
```
```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'config.json'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
ConfigurationError: No se pudo cargar la configuración
```

Usar `raise NuevaExcepcion from ExcepcionOriginal` crea un vínculo explícito entre ambos errores, lo que es invaluable para depurar. Si no quieres mostrar la cadena, puedes usar `raise NuevaExcepcion from None`.

---

## Mejores prácticas

1.  **Lee los mensajes de error**: El *Traceback* y el tipo de excepción son tus mejores aliados para depurar.
2.  **Sé específico al capturar**: Evita `except:` generales. Captura solo las excepciones que esperas y sabes manejar.
3.  **Usa `else` para el éxito**: Coloca en `else` el código que debe ejecutarse solo si no hubo errores en el `try`.
4.  **Usa `finally` para limpiar**: Garantiza que los recursos (archivos, conexiones) se liberen siempre.
5.  **Levanta excepciones significativas**: Usa `raise` con el tipo de excepción más apropiado o crea tus propias clases de excepción.
6.  **`assert` es para desarrolladores**: Úsalo para verificar invariantes en tu código durante el desarrollo, no para manejar errores en producción.
7.  **Documenta tus excepciones**: Si creas una excepción personalizada, usa un *docstring* para explicar cuándo se lanza.


---
__TE SIENTES DETERMINADO__