---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-09T20:11:00
Revision: 2026-02-09T20:59:00
---
# Tabla de Contenidos

- [[#Más sobre los módulos|Más sobre los módulos]]
	- [[#Más sobre los módulos#Formas de importar|Formas de importar]]
- [[#Cómo Python busca los módulos|Cómo Python busca los módulos]]
	- [[#Cómo Python busca los módulos#Puntos clave|Puntos clave]]
- [[#Archivos Python "Compilados" (`.pyc`)|Archivos Python "Compilados" (`.pyc`)]]
- [[#[[Módulos Built-in de Python]]|[[Módulos Built-in de Python]]]]
- [[#La función `dir()`|La función `dir()`]]
- [[#Paquetes|Paquetes]]
- [[#Importando `*` desde un paquete|Importando `*` desde un paquete]]
- [[#Referencias entre subpaquetes (imports relativos)|Referencias entre subpaquetes (imports relativos)]]
- [[#Paquetes en múltiples directorios|Paquetes en múltiples directorios]]
# Módulos en Python

Un **módulo** es un archivo con extensión `.py` que contiene definiciones (funciones, clases, variables) y código ejecutable. El nombre del archivo (sin la extensión) se convierte en el nombre del módulo, disponible en la variable global `__name__`.

Sigamos el siguiente ejemplo, un módulo llamado `fibo.py`:

```python
# Fibonacci numbers module

def fib(n):
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

def fib2(n):
    """Retorna una lista con la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
```

Si realizamos la importación:

```python
import fibo
```

Esto añade el nombre `fibo` al *namespace* actual. Para acceder a las funciones internas debemos usar el nombre del módulo como prefijo:

```python
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__  # Retorna 'fibo'
```

También podemos asignar una función a un nombre local:

```python
fib = fibo.fib
fib(500)
```

## Más sobre los módulos

Un módulo puede contener definiciones de funciones, clases y variables, así como código ejecutable (instrucciones). Este código se ejecuta **solo la primera vez** que el módulo es importado, o cuando se ejecuta como script.

Cada módulo tiene su propio *namespace* privado, que actúa como ámbito global para todas las funciones definidas en él. Esto evita colisiones entre nombres de diferentes módulos, incluso si son iguales.

Los módulos pueden importar otros módulos. Las declaraciones de importación pueden ubicarse en cualquier parte del módulo (aunque por convención se colocan al inicio).

### Formas de importar

Podemos importar funciones específicas de un módulo:

```python
from fibo import fib, fib2
fib(500)  # Ahora podemos usar fib directamente
```

Renombrar (alias) un módulo completo:

```python
import fibo as fib
fib.fib(500)
```

O combinar ambas formas:

```python
from fibo import fib as fibonacci
fibonacci(500)
```

También es posible importar todo el contenido de un módulo (no recomendado en producción por legibilidad):

```python
from fibo import *
fib(500)
```

Esta forma importa todos los nombres definidos en el módulo, excepto aquellos que comienzan con un guion bajo (`_`).

## Cómo Python busca los módulos

Cuando escribes `import spam`, Python sigue este orden de búsqueda:

1. **Módulos incorporados (*built-in*)** – como `sys`, `os`, `math`, listados en `sys.builtin_module_names`.
2. **Archivos `.py` en `sys.path`** – si no es un módulo *built-in*, busca un archivo `spam.py` en las carpetas de `sys.path`, que se inicializa en este orden:
    1. Directorio del script actual (donde se ejecuta el programa).
    2. Variables de entorno `PYTHONPATH` (lista de carpetas separadas por `:` en Linux/macOS o `;` en Windows).
    3. Rutas por defecto de instalación (incluye `site-packages`, donde están los paquetes instalados con `pip`).

### Puntos clave

- `sys.path` es modificable durante la ejecución del programa.
- El script actual tiene prioridad sobre librerías estándar. Por ejemplo, si creas un archivo `math.py`, Python usará ese en lugar del módulo `math` estándar.

## Archivos Python "Compilados" (`.pyc`)

Python guarda una versión compilada (bytecode) de cada módulo en un archivo `.pyc` dentro de la carpeta `__pycache__`. Esto acelera la carga del módulo en futuras importaciones.

**¿Cómo funciona?**
- En la primera importación, Python compila el archivo `.py` a bytecode (`.pyc`) y lo guarda en `__pycache__`.
- En importaciones posteriores, usa el `.pyc` si el código fuente no ha cambiado.

**Notas importantes:**
- Esto **no** mejora la velocidad de ejecución, solo la de carga.
- Python no usa cache para el script principal (el que se ejecuta directamente), solo para módulos importados.
- Si el archivo fuente `.py` no existe, no se generará el `.pyc`.

**Información adicional de la documentación oficial:**
- Los archivos `.pyc` son independientes de la plataforma, por lo que pueden compartirse entre sistemas con diferentes arquitecturas.
- Python verifica la fecha de modificación del archivo fuente contra la del `.pyc` para decidir si debe recompilar.
- Puedes desactivar la generación de `.pyc` con la opción `-B` o la variable de entorno `PYTHONDONTWRITEBYTECODE`.
- El directorio `__pycache__` contiene archivos con nombres que incluyen la versión de Python (ej: `módulo.cpython-310.pyc`) para evitar conflictos entre versiones.

## [[Módulos Built-in de Python]]

Python incluye una biblioteca estándar con módulos integrados, algunos de los cuales están directamente en el intérprete (como `sys`, `math`, `os`). Estos proporcionan acceso a operaciones que no forman parte del núcleo del lenguaje, pero que son esenciales para muchas tareas.

Algunos módulos son específicos del sistema operativo. Por ejemplo, `winreg` solo funciona en Windows.

## La función `dir()`

La función nativa `dir()` nos permite explorar los nombres definidos en un módulo o en el ámbito actual.

```python
import fibo, sys

dir(fibo)  # Muestra los nombres definidos en fibo: ['__name__', 'fib', 'fib2']
dir(sys)   # Muestra una larga lista de nombres del módulo sys
```

Sin argumentos, `dir()` lista los nombres definidos actualmente en el ámbito del script principal:

```python
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib

dir()  # ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

`dir()` no lista los nombres de las funciones y variables incorporadas (como `print`, `len`, etc.). Para verlas, importa el módulo `builtins`:

```python
import builtins
dir(builtins)  # Lista todas las funciones y excepciones incorporadas
```

## Paquetes

Los paquetes son una forma de estructurar módulos en directorios. Por ejemplo, supongamos que quieres diseñar un paquete para manejar archivos de sonido. Una estructura típica sería:

```
sound/                          # Paquete principal
      __init__.py               # Inicializa el paquete sound
      formats/                  # Subpaquete para conversiones de formato
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              ...
      effects/                  # Subpaquete para efectos de sonido
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  # Subpaquete para filtros
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

El archivo `__init__.py` en cada directorio es **necesario** para que Python trate ese directorio como un paquete. Este archivo puede estar vacío o contener código de inicialización. Su presencia le indica a Python que el directorio debe ser tratado como un paquete, lo que previene que directorios con nombres comunes (como `string`) oculten módulos válidos.

**Nota:** El `__init__.py` puede estar vacío, pero también se utiliza para ejecutar código de inicialización del paquete, definir la variable `__all__` (ver más abajo) o exponer ciertas funciones a nivel del paquete.

Para usar los módulos del paquete, separamos las carpetas con puntos:

```python
import sound.effects.echo
from sound.effects.echo import echofilter
```

Cuando usas `from package import item`, `item` puede ser un submódulo, un subpaquete, o cualquier nombre definido en el paquete (como una función, clase o variable). Python primero verifica si `item` está definido en el paquete; si no, asume que es un módulo e intenta cargarlo. Si no lo encuentra, lanza una excepción `ImportError`.

## Importando `*` desde un paquete

Al usar `from sound.effects import *`, Python importaría todos los submódulos del paquete `effects`. Esto puede ser lento si hay muchos módulos.

Para controlar qué se importa con `*`, el paquete puede definir una lista `__all__` en su `__init__.py`:

```python
# sound/effects/__init__.py
__all__ = ["echo", "surround", "reverse"]
```

Ahora, `from sound.effects import *` importará solo los tres módulos listados.

**Nota sobre el ejemplo de la documentación:**

Existe un posbile caso donde `__all__` incluye el nombre de una función que "sombrea" a un submódulo. Supongamos que en `sound/effects/__init__.py` tenemos:

```python
__all__ = [
    "echo",      # Se refiere al archivo 'echo.py'
    "surround",  # Se refiere al archivo 'surround.py'
    "reverse",   # ¡¡¡Ahora se refiere a la función 'reverse', no al módulo 'reverse.py'!!!
]

def reverse(msg: str):  # Esta función "sombrea" al submódulo 'reverse.py'
    return msg[::-1]
```

En este caso, `reverse` en `__all__` se refiere a la función definida en `__init__.py`, no al módulo `reverse.py`. Por lo tanto, `from sound.effects import *` importará la función `reverse` en lugar del módulo. Esto puede causar confusión, por lo que se recomienda evitar nombrar funciones igual que submódulos.

## Referencias entre subpaquetes (imports relativos)

Cuando los paquetes están estructurados en subdirectorios, puedes usar importaciones relativas para referirte a módulos hermanos o padres. Los imports relativos usan puntos:

- `.` se refiere al paquete actual.
- `..` se refiere al paquete padre.

Ejemplo dentro del módulo `sound/effects/echo.py`:

```python
from . import surround      # Importa el módulo surround del mismo paquete (effects)
from .. import formats      # Importa el paquete formats del nivel superior
from ..filters import equalizer  # Importa el módulo equalizer del paquete filters
```

**Importante:** Los imports relativos se basan en el nombre del módulo actual. Dado que el módulo principal (el script que se ejecuta) no tiene un paquete padre, los módulos diseñados para ser el programa principal deben usar siempre **imports absolutos**.

## Paquetes en múltiples directorios

Los paquetes soportan un atributo especial `__path__`. Este atributo se inicializa como una lista que contiene el nombre del directorio que contiene el `__init__.py` del paquete, antes de que se ejecute el código de ese archivo. Esta variable se puede modificar, lo que afecta las búsquedas futuras de módulos y subpaquetes dentro del paquete.

Aunque esta característica no se usa a menudo, puede utilizarse para extender el conjunto de módulos que se encuentran en un paquete (por ejemplo, para incluir módulos en diferentes directorios).

--- 
**TE SIENTES DETERMINADO**