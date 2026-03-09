---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-06T15:13:00
Revision: 2026-01-06T15:35:00
---
# Tabla de contenidos
- [[#Archivos|Archivos]]
	- [[#Archivos#Ejecución Directa (Shebang)|Ejecución Directa (Shebang)]]
- [[#Identificadores|Identificadores]]
- [[#Palabras Reservadas (Keywords)|Palabras Reservadas (Keywords)]]
- [[#Líneas e Indentación|Líneas e Indentación]]
- [[#Sentencias Multi-Línea|Sentencias Multi-Línea]]
- [[#Comillas en Python|Comillas en Python]]
- [[#Comentarios en Python|Comentarios en Python]]
- [[#Múltiples Sentencias en una Línea|Múltiples Sentencias en una Línea]]
- [[#Grupos de Sentencias como *Suites* (Bloques)|Grupos de Sentencias como *Suites* (Bloques)]]
- [[#Argumentos de Línea de Comandos en Python|Argumentos de Línea de Comandos en Python]]

# Sintaxis Básica de Python

## Archivos

*   La extensión de los archivos de Python es **`.py`**.
*   Ejemplo de código: `print("Hola mundo")`
*   Para ejecutar un script desde la terminal: `python3 test.py`

### Ejecución Directa (Shebang)

Al agregar `#!/usr/bin/python3` al **inicio** del archivo (la primera línea), y luego otorgarle permisos de ejecución con `chmod +x test.py`, puedes ejecutarlo directamente como: `./test.py`.

## Identificadores

Un identificador es un nombre usado para **identificar** una variable, función, clase, módulo u otro objeto.

**Reglas de Nomenclatura:**
*   Deben comenzar con una letra (A-Z o a-z) o un guion bajo (`_`).
*   Pueden contener letras, dígitos (0-9) y guiones bajos (`_`).
*   Python es **sensible a mayúsculas y minúsculas** (`miVariable` y `Mivariable` son diferentes).
*   **No se permiten** caracteres especiales como `&`, `,`, `;`, `$`, `%`.

**Convenciones de Estilo (PEP 8):**
*   **Nombres de Clase:** Comienzan con una letra mayúscula (ej: `MiClase`, `CocheElectrico`).
*   **Otros identificadores** (variables, funciones, módulos): Comienzan con una letra minúscula. Para nombres compuestos, se usa el guion bajo (`snake_case`) por convención (ej: `nombre_usuario`, `calcular_promedio`).
*   **Identificador Privado:** Un solo guion bajo al inicio (`_variable_privada`) indica que es para uso interno (aunque técnicamente es accesible).
*   **Identificador Fuertemente Privado:** Dos guiones bajos al inicio (`__variable_muy_privada`) activan el *name mangling* de Python, haciendo el nombre más difícil de acceder desde fuera de su clase.
*   **Nombre Especial del Lenguaje:** Identificadores que comienzan y terminan con dos guiones bajos (`__init__`, `__str__`) son métodos especiales definidos por Python.

## Palabras Reservadas (Keywords)

La siguiente lista son palabras clave del lenguaje Python. **No pueden ser usadas** como nombres de variables, constantes o identificadores. Todas están en minúsculas.

|          |          |            |
|----------|----------|------------|
| `and`    | `as`     | `assert`   |
| `break`  | `class`  | `continue` |
| `def`    | `del`    | `elif`     |
| `else`   | `except` | `False`    |
| `finally`| `for`    | `from`     |
| `global` | `if`     | `import`   |
| `in`     | `is`     | `lambda`   |
| `None`   | `nonlocal`| `not`     |
| `or`     | `pass`   | `raise`    |
| `return` | `True`   | `try`      |
| `while`  | `with`   | `yield`    |

## Líneas e Indentación

Python **no usa llaves `{}`** para definir bloques de código. En su lugar, utiliza **indentación (sangría)** para delimitar bloques lógicos (como los cuerpos de funciones, bucles o condicionales).

*   La cantidad de espacios en la indentación es flexible (comúnmente 4 espacios), pero **debe ser consistente** dentro del mismo bloque.
*   Todo el código que pertenezca al mismo bloque debe tener el mismo nivel de indentación.

**Ejemplo:**
```python
if True:
    print("Verdadero")  # Parte del bloque 'if'
    print("Aún en el if")  # También parte del bloque 'if'
else:
    print("Falso")  # Parte del bloque 'else'
print("Fuera del if/else")  # Fuera de cualquier bloque, sin indentación
```

## Sentencias Multi-Línea

Por lo general, cada sentencia en Python termina con una nueva línea. Sin embargo, puedes extender una sentencia a múltiples líneas usando la **barra invertida (`\`)**.

**Ejemplo con `\`:**
```python
total = item_uno + \
        item_dos + \
        item_tres
```

**Nota Importante:** La barra invertida **no es necesaria** cuando la continuación de línea ocurre dentro de paréntesis `()`, corchetes `[]` o llaves `{}`. Esto es más común y considerado más legible.

**Ejemplo preferido (sin `\`):**
```python
# Dentro de una lista
dias = ['Lunes', 'Martes', 'Miércoles',
        'Jueves', 'Viernes']

# Dentro de paréntesis (para llamadas a funciones largas, condiciones, etc.)
if (condicion_larga_uno and
    condicion_larga_dos):
    hacer_algo()
```

## Comillas en Python

Python acepta comillas simples (`'`), dobles (`"`) y triples (`'''` o `"""`) para definir cadenas de texto (*strings*).

*   La única regla es que el tipo de comilla que abre la cadena debe ser la misma que la que la cierra.
*   Las comillas triples permiten cadenas que abarcan **múltiples líneas**.

**Ejemplos:**
```python
palabra = 'palabra'
oracion = "Esta es una oración."
parrafo = """Este es un párrafo.
Está compuesto por múltiples
líneas y oraciones."""
```

## Comentarios en Python

Los comentarios son líneas de texto ignoradas por el intérprete, usadas para documentar el código.

1.  **Comentario de Una Línea:** Comienza con el símbolo `#`.
    ```python
    # Este es un comentario
    print("Hola")  # Este también es un comentario después del código
    ```

2.  **Comentario Multi-Línea (Docstring):** Se escribe entre comillas triples. Aunque técnicamente son *strings*, si se colocan justo después de la definición de una función, clase o módulo, se convierten en **docstrings** (documentación accesible con `help()`).
    ```python
    '''
    Este es un comentario
    que ocupa múltiples líneas.
    Se usa comúnmente como docstring.
    '''
    
    def mi_funcion():
        """
        Esta es la documentación (docstring) de la función.
        Explica lo que hace la función.
        """
        pass
    ```

## Múltiples Sentencias en una Línea

Puedes escribir varias sentencias en una sola línea separándolas con un **punto y coma (`;`)**. Sin embargo, esta práctica **no se recomienda** generalmente, ya que reduce la legibilidad del código.

**Ejemplo (evitar si es posible):**
```python
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```

## Grupos de Sentencias como *Suites* (Bloques)

En Python, un grupo de sentencias individuales que forman un **bloque de código único** se llama ***suite***.

Las sentencias compuestas o complejas (como `if`, `while`, `def`, `class`) requieren:
1.  Una **línea de cabecera** que termina con dos puntos (`:`).
2.  Una ***suite*** indentada que sigue a la cabecera.

**Estructura general:**
```python
if expresion:
    suite  # Bloque de código para el 'if' (indentado)
elif expresion:
    suite  # Bloque para el 'elif'
else:
    suite  # Bloque para el 'else'

def nombre_funcion(argumentos):
    suite  # Cuerpo de la función (indentado)

class NombreClase:
    suite  # Cuerpo de la clase (indentado)
```

## Argumentos de Línea de Comandos en Python

Muchos programas pueden recibir información sobre cómo deben ejecutarse a través de la línea de comandos.

*   **Ayuda del Intérprete:** Puedes ver las opciones básicas del intérprete de Python con `-h`.
    ```bash
    $ python3 -h
    ```

*   **Scripts con Argumentos:** Puedes programar tus propios scripts para que acepten y procesen argumentos desde la terminal (por ejemplo, `python3 mi_script.py arg1 arg2`). Esto se logra utilizando la lista `sys.argv` o módulos más avanzados como `argparse`.

**Nota:** Los Argumentos de Línea de Comandos es un tema más avanzado que se estudia mejor después de haber cubierto conceptos fundamentales como funciones y módulos.

---
__TE SIENTES DETERMINADO__