---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-08T12:36:00
Revision: 2026-01-08T15:16:00
---
# Tabla de Contenidos

- [[#Introducción a las Estructuras Condicionales|Introducción a las Estructuras Condicionales]]
- [[#La Declaración `if` Básica|La Declaración `if` Básica]]
	- [[#La Declaración `if` Básica#Ejemplos Básicos:|Ejemplos Básicos:]]
- [[#Grupos de Instrucciones: Identación y Bloques|Grupos de Instrucciones: Identación y Bloques]]
	- [[#Grupos de Instrucciones: Identación y Bloques#Bloques Anidados:|Bloques Anidados:]]
	- [[#Grupos de Instrucciones: Identación y Bloques#¿Cómo lo Hacen Otros Lenguajes?|¿Cómo lo Hacen Otros Lenguajes?]]
- [[#`else` y `elif`|`else` y `elif`]]
	- [[#`else` y `elif`#La Declaración `else`|La Declaración `else`]]
	- [[#`else` y `elif`#La Declaración `elif` (else if)|La Declaración `elif` (else if)]]
	- [[#`else` y `elif`#Alternativa Elegante con Diccionarios|Alternativa Elegante con Diccionarios]]
- [[#If en una Sola Línea|If en una Sola Línea]]
	- [[#If en una Sola Línea#Sintaxis básica:|Sintaxis básica:]]
	- [[#If en una Sola Línea#Múltiples instrucciones en una línea:|Múltiples instrucciones en una línea:]]
	- [[#If en una Sola Línea#Uso común: Debugging|Uso común: Debugging]]
- [[#Expresiones Condicionales (Operador Ternario)|Expresiones Condicionales (Operador Ternario)]]
	- [[#Expresiones Condicionales (Operador Ternario)#Sintaxis:|Sintaxis:]]
	- [[#Expresiones Condicionales (Operador Ternario)#Funcionamiento:|Funcionamiento:]]
- [[#La Instrucción `pass`|La Instrucción `pass`]]
	- [[#La Instrucción `pass`#Error sin `pass`:|Error sin `pass`:]]
	- [[#La Instrucción `pass`#Solución con `pass`:|Solución con `pass`:]]
- [[#La Declaración `match`/`case` (Python 3.10+)|La Declaración `match`/`case` (Python 3.10+)]]
	- [[#La Declaración `match`/`case` (Python 3.10+)#Sintaxis Básica:|Sintaxis Básica:]]
	- [[#La Declaración `match`/`case` (Python 3.10+)#¿Por qué usar `match` en lugar de `if`/`elif`/`else`?|¿Por qué usar `match` en lugar de `if`/`elif`/`else`?]]
	- [[#La Declaración `match`/`case` (Python 3.10+)#Comparación `match` vs `if`:|Comparación `match` vs `if`:]]
	- [[#La Declaración `match`/`case` (Python 3.10+)#Pattern Matching Avanzado:|Pattern Matching Avanzado:]]
	- [[#La Declaración `match`/`case` (Python 3.10+)#Cuándo usar cada estructura:|Cuándo usar cada estructura:]]
- [[#Ejemplos Prácticos Completos|Ejemplos Prácticos Completos]]
	- [[#Ejemplos Prácticos Completos#Sistema de Autenticación:|Sistema de Autenticación:]]
	- [[#Ejemplos Prácticos Completos#Sistema de Calificaciones:|Sistema de Calificaciones:]]
	- [[#Ejemplos Prácticos Completos#Validación de Entrada de Usuario:|Validación de Entrada de Usuario:]]
- [[#Buenas Prácticas con Condicionales|Buenas Prácticas con Condicionales]]
	- [[#Buenas Prácticas con Condicionales#1. Evitar condicionales demasiado largas:|1. Evitar condicionales demasiado largas:]]
	- [[#Buenas Prácticas con Condicionales#2. Usar early returns:|2. Usar early returns:]]
	- [[#Buenas Prácticas con Condicionales#3. Elegir la estructura correcta:|3. Elegir la estructura correcta:]]
- [[#Errores Comunes y Cómo Evitarlos|Errores Comunes y Cómo Evitarlos]]
	- [[#Errores Comunes y Cómo Evitarlos#1. Falta de identación:|1. Falta de identación:]]
	- [[#Errores Comunes y Cómo Evitarlos#2. Confundir `=` con `==`:|2. Confundir `=` con `==`:]]
	- [[#Errores Comunes y Cómo Evitarlos#3. Comparaciones encadenadas (Python las soporta):|3. Comparaciones encadenadas (Python las soporta):]]
	- [[#Errores Comunes y Cómo Evitarlos#4. Olvidar los dos puntos `:`:|4. Olvidar los dos puntos `:`:]]
# Condicionales en Python

## Introducción a las Estructuras Condicionales

Las estructuras condicionales permiten que tu programa tome decisiones basadas en condiciones específicas. En Python, la estructura básica es el `if`.

## La Declaración `if` Básica

La forma más simple de un `if` en Python es:

```python
if <expresión>:
    <instrucción>
```

- **`<expresión>`**: Cualquier expresión que se evalúe como `True` (verdadero) o `False` (falso) en un contexto booleano
- **`<instrucción>`**: Código Python válido que se ejecutará si la expresión es verdadera
- **`:` (dos puntos)**: Obligatorios para indicar el inicio del bloque de código

**Característica única de Python**: No usa paréntesis ni llaves para delimitar bloques. En su lugar, usa **identación (sangría)** para definir qué código pertenece al `if`.

### Ejemplos Básicos:
```python
>>> x = 0
>>> y = 5

# Condición verdadera
>>> if x < y:
...     print('sí')
sí

# Condición falsa (no se ejecuta)
>>> if y < x:
...     print('sí')
# No hay output

# Valores truthy/falsy
>>> if x:  # x = 0 → Falsy
...     print('sí')
# No se ejecuta

>>> if y:  # y = 5 → Truthy
...     print('sí')
sí

# Expresiones booleanas
>>> if x or y:  # True (y es truthy)
...     print('sí')
sí

>>> if x and y:  # False (x es falsy)
...     print('sí')
# No se ejecuta

# Operador 'in'
>>> if 'aul' in 'grault':  # True
...     print('sí')
sí

>>> if 'quux' in ['foo', 'bar', 'baz']:  # False
...     print('sí')
# No se ejecuta
```

## Grupos de Instrucciones: Identación y Bloques

En Python, la identación no es solo una convención de estilo, es parte fundamental del lenguaje. Define qué instrucciones pertenecen a cada bloque.

```python
if <expresión>:
    <instrucción>
    <instrucción>
    ...
    <instrucción>

<instrucción_siguiente>
```

![[t.78f3bacaa261.png]]
**Ejemplo práctico:**
```python
if 'foo' in ['bar', 'baz', 'qux']:
    print('La expresión era verdadera')
    print('Ejecutando instrucción en el bloque')
    print('...')
    print('Listo.')
print('Después del condicional')

# Output: "Después del condicional" (el if era falso)
```

### Bloques Anidados:
```python
# blocks.py
if 'foo' in ['foo', 'bar', 'baz']:
    print('Condición exterior es verdadera')
    
    if 10 > 20:
        print('Condición interior 1')
    
    print('Entre condiciones interiores')
    
    if 10 < 20:
        print('Condición interior 2')
    
    print('Fin de la condición exterior')
print('Después de la condición exterior')
```

**Output:**
```
Condición exterior es verdadera
Entre condiciones interiores
Condición interior 2
Fin de la condición exterior
Después de la condición exterior
```

**Nota importante:** En Python, necesitas una línea en blanco adicional cuando ingresas declaraciones multilínea en una sesión REPL. Esto se debe a la "regla del lado" (off-side rule), que le permite al intérprete saber cuándo has terminado de ingresar un bloque.

### ¿Cómo lo Hacen Otros Lenguajes?

Lenguajes como C, C++, Java o Perl usan llaves `{}` para agrupar bloques:

```c
// Esto es C, no Python
if (condición) {
    instrucción;
    instrucción;
    ...
    instrucción;
}
instrucción_siguiente;
```

![[t.7dbd895afc69.png]]

**Ventaja de Python:** La identación obligatoria hace que el código sea más legible y consistente. Todos los programadores Python usan el mismo estilo de identación.

## `else` y `elif`

### La Declaración `else`

El `else` proporciona una alternativa cuando la condición del `if` es falsa:

```python
>>> x = 20

>>> if x < 50:
...     print('(primer bloque)')
...     print('x es pequeño')
... else:
...     print('(segundo bloque)')
...     print('x es grande')
(primer bloque)
x es pequeño

>>> x = 120
>>> if x < 50:
...     print('(primer bloque)')
...     print('x es pequeño')
... else:
...     print('(segundo bloque)')
...     print('x es grande')
(segundo bloque)
x es grande
```

### La Declaración `elif` (else if)

`elif` permite verificar múltiples condiciones en secuencia:

```python
if <expresión1>:
    <instrucción(es)>
elif <expresión2>:
    <instrucción(es)>
elif <expresión3>:
    <instrucción(es)>
    ...
else:
    <instrucción(es)>
```

**Ejemplo:**
```python
>>> nombre = 'Juan'
>>> if nombre == 'Federico':
...     print('Hola Federico')
... elif nombre == 'Alejandro':
...     print('Hola Alejandro')
... elif nombre == 'Juan':
...     print('Hola Juan')
... elif nombre == 'Arnoldo':
...     print('Hola Arnoldo')
... else:
...     print("No sé quién eres!")
Hola Juan
```

### Alternativa Elegante con Diccionarios

Para casos donde cada condición lleva a una acción simple (como un `print()`), podemos usar diccionarios:

```python
>>> saludos = {
...     'Federico': 'Hola Federico',
...     'Alejandro': 'Hola Alejandro',
...     'Juan': 'Hola Juan',
...     'Arnoldo': 'Hola Arnoldo'
... }

>>> print(saludos.get('Juan', "No sé quién eres!"))
Hola Juan

>>> print(saludos.get('Ricardo', "No sé quién eres!"))
No sé quién eres!
```

El método `.get()` de los diccionarios busca una clave y devuelve su valor si la encuentra, o un valor por defecto si no.

## If en una Sola Línea

Python permite escribir `if` en una sola línea:

### Sintaxis básica:
```python
if <expresión>: <instrucción>
```

### Múltiples instrucciones en una línea:
```python
if <expresión>: <instrucción1>; <instrucción2>; ...; <instrucción_n>
```

**Ejemplo:**
```python
>>> x = 2
>>> if x == 1: print('foo'); print('bar'); print('baz')
... elif x == 2: print('qux'); print('quux')
... else: print('corge'); print('grault')
qux
quux

>>> x = 3
>>> if x == 1: print('foo'); print('bar'); print('baz')
... elif x == 2: print('qux'); print('quux')
... else: print('corge'); print('grault')
corge
grault
```

### Uso común: Debugging
```python
debugging = True  # Cambiar a True para activar debugging

# ... mucho código ...

if debugging: print('A punto de llamar a la función foo()')
foo()
```

**Advertencia:** Esta forma compacta es útil para casos simples, pero puede reducir la legibilidad en condiciones complejas.

## Expresiones Condicionales (Operador Ternario)

Python tiene un operador ternario que funciona como expresión (no como declaración):

### Sintaxis:
```python
<expr1> if <expresión_condicional> else <expr2>
```

### Funcionamiento:
1. Evalúa `<expresión_condicional>`
2. Si es `True`, devuelve `<expr1>`
3. Si es `False`, devuelve `<expr2>`

**Ejemplos:**
```python
>>> lloviendo = False
>>> print("Vamos a la", 'playa' if not lloviendo else 'biblioteca')
Vamos a la playa

>>> lloviendo = True
>>> print("Vamos a la", 'playa' if not lloviendo else 'biblioteca')
Vamos a la biblioteca

>>> edad = 12
>>> categoria = 'menor' if edad < 21 else 'adulto'
>>> categoria
'menor'

>>> 'sí' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
'no'
```

**Comparación con C:**
```c
// En C/C++/Java/JavaScript
condición ? expr1 : expr2

// En Python (más legible)
expr1 if condición else expr2
```

**Uso apropiado:** Ideal para asignaciones simples y expresiones, no para bloques de código complejos.

## La Instrucción `pass`

Python no permite bloques vacíos. Si necesitas un bloque que no haga nada (como placeholder), usa `pass`:

### Error sin `pass`:
```python
# foo.py
if True:

print('foo')
```

**Error al ejecutar:**
```
  File "foo.py", line 3
    print('foo')
        ^
IndentationError: expected an indented block
```

### Solución con `pass`:
```python
# foo.py
if True:
    pass

print('foo')
```

**Output:**
```
foo
```

**Usos comunes de `pass`:**
- Placeholder para funciones/clases que implementarás después
- Bloque `except` vacío (aunque generalmente no recomendado)
- Condiciones donde no quieres hacer nada

```python
def función_por_implementar():
    pass  # Implementaré esto más tarde

class ClaseBase:
    pass  # Clase abstracta o por extender
```

## La Declaración `match`/`case` (Python 3.10+)

Python 3.10 introdujo el `match` statement, similar al `switch` de otros lenguajes.

### Sintaxis Básica:
```python
match <valor>:
    case <patrón1>:
        <instrucciones>
    case <patrón2>:
        <instrucciones>
    case _:  # Caso por defecto (como else)
        <instrucciones>
```

**Ejemplo:**
```python
>>> comando = '¡Hola, Mundo!'
>>> match comando:
...     case '¡Hola, Mundo!':
...         print('¡Hola a ti también!')
...     case '¡Adiós, Mundo!':
...         print('¡Hasta luego!')
...     case other:
...         print('No se encontró coincidencia')
¡Hola a ti también!
```

**Nota:** `match` y `case` son **palabras clave suaves** (soft keywords), lo que significa que aún puedes usarlas como nombres de variables, aunque no es recomendable.

### ¿Por qué usar `match` en lugar de `if`/`elif`/`else`?

1. **Más legible** para patrones complejos
2. **Pattern matching** más poderoso
3. **Menos propenso a errores** en largas cadenas de condiciones

### Comparación `match` vs `if`:

**Con `match` (más limpio):**
```python
def manejador_archivos_v1(comando):
    match comando.split():
        case ['mostrar']:
            print('Listar todos los archivos y directorios:')
            # código para listar archivos
        case ['eliminar', *archivos]:
            print(f'Eliminando archivos: {archivos}')
            # código para eliminar archivos
        case _:
            print('Comando no reconocido')
```

**Con `if`/`elif` (más verboso):**
```python
def manejador_archivos_v2(comando):
    partes = comando.split()
    if len(partes) == 1 and partes[0] == 'mostrar':
        print('Listar todos los archivos y directorios:')
        # código para listar archivos
    elif len(partes) >= 2 and partes[0] == 'eliminar':
        archivos = partes[1:]
        print(f'Eliminando archivos: {archivos}')
        # código para eliminar archivos
    else:
        print('Comando no reconocido')
```

### Pattern Matching Avanzado:

**Múltiples patrones:**
```python
match comando.split():
    case ['mostrar']:
        print('Listando archivos...')
    case ['eliminar' | 'borrar', *archivos] if '--preguntar' in archivos:
        # Eliminar con confirmación
        archivos_a_eliminar = [f for f in archivos if '.' in f]
        print(f'Confirmar: Eliminar archivos: {archivos_a_eliminar}')
    case ['eliminar' | 'borrar', *archivos]:
        # Eliminar sin confirmación
        print(f'Eliminando archivos: {archivos}')
    case _:
        print('Comando no reconocido')
```

**Patrones con tipos:**
```python
def procesar_dato(dato):
    match dato:
        case int() | float():
            print(f'Número: {dato}')
        case str():
            print(f'String: {dato}')
        case list():
            print(f'Lista con {len(dato)} elementos')
        case dict():
            print(f'Diccionario con {len(dato)} claves')
        case _:
            print(f'Tipo desconocido: {type(dato)}')
```

### Cuándo usar cada estructura:

| Estructura | Mejor para | Ejemplo |
|------------|------------|---------|
| `if` simple | Una condición | `if usuario.activo:` |
| `if`/`else` | Dos alternativas | `if edad >= 18: ... else: ...` |
| `if`/`elif`/`else` | Múltiples condiciones | Menús, categorías |
| Operador ternario | Asignaciones condicionales | `estado = "activo" if conexión else "inactivo"` |
| `match`/`case` | Pattern matching complejo | Procesamiento de comandos, estructuras de datos |

## Ejemplos Prácticos Completos

### Sistema de Autenticación:
```python
def verificar_acceso(usuario, rol, hora_actual):
    """Verifica si un usuario tiene acceso al sistema."""
    
    # Verificar horario laboral (9-17)
    if not (9 <= hora_actual < 17):
        return "Acceso denegado: Fuera de horario laboral"
    
    # Verificar usuario activo
    if usuario.estado != "activo":
        return "Acceso denegado: Usuario inactivo"
    
    # Verificar permisos según rol
    match rol:
        case "admin":
            return "Acceso completo concedido"
        case "editor":
            return "Acceso de edición concedido"
        case "visor":
            return "Acceso de solo lectura concedido"
        case _:
            return "Acceso denegado: Rol no válido"

# Uso
class Usuario:
    def __init__(self, estado):
        self.estado = estado

usuario = Usuario("activo")
print(verificar_acceso(usuario, "admin", 14))  # Acceso completo concedido
print(verificar_acceso(usuario, "editor", 19)) # Acceso denegado: Fuera de horario laboral
```

### Sistema de Calificaciones:
```python
def obtener_calificacion(puntaje):
    """Convierte un puntaje numérico a calificación literal."""
    
    # Usando if/elif/else
    if puntaje >= 90:
        return "A"
    elif puntaje >= 80:
        return "B"
    elif puntaje >= 70:
        return "C"
    elif puntaje >= 60:
        return "D"
    else:
        return "F"

    # Alternativa con match (Python 3.10+)
    # match puntaje:
    #     case _ if puntaje >= 90: return "A"
    #     case _ if puntaje >= 80: return "B"
    #     case _ if puntaje >= 70: return "C"
    #     case _ if puntaje >= 60: return "D"
    #     case _: return "F"

# Uso con operador ternario para mensaje adicional
def obtener_mensaje_calificacion(puntaje):
    calificacion = obtener_calificacion(puntaje)
    mensaje = "¡Excelente!" if calificacion in ["A", "B"] else "Necesita mejorar"
    return f"Calificación: {calificacion}. {mensaje}"

print(obtener_mensaje_calificacion(95))  # Calificación: A. ¡Excelente!
print(obtener_mensaje_calificacion(65))  # Calificación: D. Necesita mejorar
```

### Validación de Entrada de Usuario:
```python
def procesar_comando(entrada_usuario):
    """Procesa comandos del usuario usando match."""
    
    # Limpiar y dividir la entrada
    partes = entrada_usuario.strip().lower().split()
    
    if not partes:  # Entrada vacía
        return "Error: Comando vacío"
    
    match partes:
        case ["salir"] | ["quit"] | ["exit"]:
            return "Saliendo del programa..."
        
        case ["ayuda"] | ["help"]:
            return "Comandos disponibles: salir, ayuda, listar, crear <nombre>"
        
        case ["listar"]:
            return "Listando elementos..."
        
        case ["crear", nombre] if len(nombre) >= 3:
            return f"Creando '{nombre}'..."
        
        case ["crear", nombre]:
            return "Error: El nombre debe tener al menos 3 caracteres"
        
        case ["eliminar", *elementos]:
            if not elementos:
                return "Error: Especifica qué eliminar"
            return f"Eliminando: {', '.join(elementos)}"
        
        case _:
            return f"Error: Comando '{partes[0]}' no reconocido"

# Pruebas
print(procesar_comando("  Ayuda  "))      # Comandos disponibles...
print(procesar_comando("crear mi_archivo")) # Creando 'mi_archivo'...
print(procesar_comando("crear ab"))        # Error: El nombre debe tener...
print(procesar_comando("eliminar a b c"))  # Eliminando: a, b, c
```

## Buenas Prácticas con Condicionales

### 1. Evitar condicionales demasiado largas:
```python
# ❌ Menos legible
if (usuario.activo and usuario.tiene_permisos and not usuario.suspendido and hora_actual < 18):
    # ...

# ✅ Mejor
usuario_valido = (usuario.activo and 
                  usuario.tiene_permisos and 
                  not usuario.suspendido)
hora_valida = hora_actual < 18

if usuario_valido and hora_valida:
    # ...
```

### 2. Usar early returns:
```python
# ❌ Condicionales anidadas
def procesar_pedido(pedido):
    if pedido.valido:
        if pedido.en_stock:
            if pedido.cliente_activo:
                # Procesar pedido
                return "Éxito"
            else:
                return "Cliente inactivo"
        else:
            return "Sin stock"
    else:
        return "Pedido inválido"

# ✅ Early returns (más legible)
def procesar_pedido(pedido):
    if not pedido.valido:
        return "Pedido inválido"
    
    if not pedido.en_stock:
        return "Sin stock"
    
    if not pedido.cliente_activo:
        return "Cliente inactivo"
    
    # Procesar pedido
    return "Éxito"
```

### 3. Elegir la estructura correcta:
```python
# Para diccionarios de mapeo → Usar dict
colores_rgb = {
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255)
}
color = colores_rgb.get("rojo", (0, 0, 0))

# Para pattern matching → Usar match/case
match evento.tipo:
    case "click":
        manejar_click(evento)
    case "tecla":
        manejar_tecla(evento)
    case _:
        manejar_desconocido(evento)

# Para rangos/valores numéricos → Usar if/elif
if puntaje >= 90:
    calif = "A"
elif puntaje >= 80:
    calif = "B"
# ...
```

## Errores Comunes y Cómo Evitarlos

### 1. Falta de identación:
```python
# ❌ Error
if True:
print("Hola")  # IndentationError

# ✅ Correcto
if True:
    print("Hola")
```

### 2. Confundir `=` con `==`:
```python
# ❌ Asignación en lugar de comparación
if x = 5:  # SyntaxError
    print("x es 5")

# ✅ Comparación correcta
if x == 5:
    print("x es 5")
```

### 3. Comparaciones encadenadas (Python las soporta):
```python
# ✅ Esto funciona en Python (no en todos los lenguajes)
if 0 <= edad < 18:
    print("Menor de edad")

# Equivale a:
if 0 <= edad and edad < 18:
    print("Menor de edad")
```

### 4. Olvidar los dos puntos `:`:
```python
# ❌ Falta el :
if True  # SyntaxError
    print("Hola")

# ✅ Con :
if True:
    print("Hola")
```


**Recuerda:** La elección entre `if`/`elif`/`else`, operador ternario o `match`/`case` depende de la situación específica y de la versión de Python que uses. Cada herramienta tiene su lugar y uso apropiado.

---
__TE SIENTES DETERMINADO__