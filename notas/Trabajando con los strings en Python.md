---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-08T11:22:00
Revision: 2026-01-08T15:19:00
---
# Tabla de Contenidos

- [[#¿Qué son los Strings?|¿Qué son los Strings?]]
- [[#Comillas dentro de Comillas|Comillas dentro de Comillas]]
- [[#Strings Multilínea|Strings Multilínea]]
- [[#Los Strings son Arrays|Los Strings son Arrays]]
- [[#Iterando sobre Strings|Iterando sobre Strings]]
- [[#Longitud de un String|Longitud de un String]]
- [[#Verificación de Contenido|Verificación de Contenido]]
- [[#Slicing (Rebanado) de Strings|Slicing (Rebanado) de Strings]]
	- [[#Slicing (Rebanado) de Strings#Slicing Básico|Slicing Básico]]
	- [[#Slicing (Rebanado) de Strings#Desde el Principio|Desde el Principio]]
	- [[#Slicing (Rebanado) de Strings#Hasta el Final|Hasta el Final]]
	- [[#Slicing (Rebanado) de Strings#Índices Negativos|Índices Negativos]]
	- [[#Slicing (Rebanado) de Strings#Con Paso (Step)|Con Paso (Step)]]
- [[#Métodos Comunes de Strings|Métodos Comunes de Strings]]
	- [[#Métodos Comunes de Strings#Cambio de Mayúsculas/Minúsculas|Cambio de Mayúsculas/Minúsculas]]
	- [[#Métodos Comunes de Strings#Eliminación de Espacios|Eliminación de Espacios]]
	- [[#Métodos Comunes de Strings#Búsqueda y Reemplazo|Búsqueda y Reemplazo]]
	- [[#Métodos Comunes de Strings#División y Unión|División y Unión]]
	- [[#Métodos Comunes de Strings#Verificación de Contenido|Verificación de Contenido]]
- [[#Concatenación de Strings|Concatenación de Strings]]
	- [[#Concatenación de Strings#Usando el operador `+`|Usando el operador `+`]]
	- [[#Concatenación de Strings#Usando `+=`|Usando `+=`]]
- [[#Formateo de Strings|Formateo de Strings]]
	- [[#Formateo de Strings#Método `format()` (tradicional)|Método `format()` (tradicional)]]
	- [[#Formateo de Strings#f-Strings (Python 3.6+ - RECOMENDADO)|f-Strings (Python 3.6+ - RECOMENDADO)]]
	- [[#Formateo de Strings#Métodos de Formateo Avanzado|Métodos de Formateo Avanzado]]
- [[#Caracteres de Escape|Caracteres de Escape]]
	- [[#Caracteres de Escape#Raw Strings (Strings crudos)|Raw Strings (Strings crudos)]]
- [[#Métodos Especializados (string module)|Métodos Especializados (string module)]]
	- [[#Métodos Especializados (string module)#Plantillas de Strings (Template)|Plantillas de Strings (Template)]]
- [[#Métodos de Validación|Métodos de Validación]]
- [[#Métodos de Alineación y Relleno|Métodos de Alineación y Relleno]]
- [[#Tabla de Traducción (translate)|Tabla de Traducción (translate)]]
- [[#Métodos de Partición|Métodos de Partición]]
- [[#Métodos de División Avanzada|Métodos de División Avanzada]]
- [[#Métodos de Codificación|Métodos de Codificación]]
- [[#Comparación de Strings|Comparación de Strings]]
- [[#Conversión entre Strings y Otros Tipos|Conversión entre Strings y Otros Tipos]]
- [[#Performance Consideraciones|Performance Consideraciones]]
	- [[#Performance Consideraciones#Concatenación vs Join|Concatenación vs Join]]
- [[#Resumen de Métodos Esenciales|Resumen de Métodos Esenciales]]
- [[#Ejemplo Práctico Completo|Ejemplo Práctico Completo]]
# Trabajando con Strings en Python

## ¿Qué son los Strings?

Los strings (cadenas de texto) son secuencias de caracteres encerradas entre comillas simples (`'`), dobles (`"`) o triples (`'''` o `"""`).

```python
print("Hola")        # Comillas dobles
print('Mundo')       # Comillas simples
# Output: Hola
# Output: Mundo
```

## Comillas dentro de Comillas

Puedes usar comillas dentro de un string siempre que no sean del mismo tipo que las comillas exteriores:

```python
print("It's alright")                # Comilla simple dentro de dobles
print('Él se llama "Juan"')         # Comillas dobles dentro de simples
print("Él se llama 'Juan'")         # Comillas simples dentro de dobles

# Output: It's alright
# Output: Él se llama "Juan"
# Output: Él se llama 'Juan'
```

## Strings Multilínea

Usa comillas triples (`'''` o `"""`) para crear strings que abarquen múltiples líneas:

```python
texto = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(texto)

# Output:
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.
```

**Nota:** Los saltos de línea se mantienen exactamente en la misma posición que en el código.

## Los Strings son Arrays

En Python, los strings son **secuencias inmutables** de caracteres. No existe un tipo "carácter" separado; un solo carácter es simplemente un string de longitud 1.

```python
texto = "Hola, Mundo!"
print(texto[0])      # 'H' - primer carácter
print(texto[7])      # 'M' - octavo carácter
# Output: H
# Output: M
```

## Iterando sobre Strings

Como los strings son secuencias, podemos iterar sobre ellos:

```python
# Usando for
for letra in "banana":
    print(letra)
# Output: b
# Output: a
# Output: n
# Output: a
# Output: n
# Output: a

# Usando while
texto = "Python"
i = 0
while i < len(texto):
    print(texto[i])
    i += 1
```

## Longitud de un String

La función `len()` devuelve la longitud (número de caracteres) de un string:

```python
texto = "Hola, Mundo!"
print(len(texto))  # 12
# Output: 12
```

## Verificación de Contenido

Usa los operadores `in` y `not in` para verificar si un substring está presente:

```python
texto = "Las mejores cosas en la vida son gratis!"

# Verificación directa
print("gratis" in texto)       # True
print("caro" in texto)         # False

# En condicionales
if "gratis" in texto:
    print("Sí, 'gratis' está presente")
    # Output: Sí, 'gratis' está presente

# Verificación negativa
if "caro" not in texto:
    print("No, 'caro' NO está presente")
    # Output: No, 'caro' NO está presente
```

## Slicing (Rebanado) de Strings

El slicing permite extraer partes de un string usando la sintaxis `[inicio:fin:paso]`.

### Slicing Básico
```python
texto = "Hola, Mundo!"
print(texto[2:5])    # 'la,' (desde índice 2 hasta 4)
# Output: la,
```

### Desde el Principio
```python
texto = "Hola, Mundo!"
print(texto[:5])     # 'Hola,' (desde inicio hasta índice 4)
# Output: Hola,
```

### Hasta el Final
```python
texto = "Hola, Mundo!"
print(texto[7:])     # 'Mundo!' (desde índice 7 hasta el final)
# Output: Mundo!
```

### Índices Negativos
```python
texto = "Hola, Mundo!"
print(texto[-6:-1])  # 'Mundo' (desde 6 caracteres antes del final hasta 1 antes del final)
print(texto[-5:])    # 'undo!' (últimos 5 caracteres)
# Output: Mundo
# Output: undo!
```

### Con Paso (Step)
```python
texto = "Python"
print(texto[::2])    # 'Pto' (todos los caracteres, paso 2)
print(texto[::-1])   # 'nohtyP' (string invertido)
# Output: Pto
# Output: nohtyP
```

## Métodos Comunes de Strings

### Cambio de Mayúsculas/Minúsculas
```python
texto = "Hola, Mundo!"
print(texto.upper())      # 'HOLA, MUNDO!'
print(texto.lower())      # 'hola, mundo!'
print(texto.capitalize()) # 'Hola, mundo!'
print(texto.title())      # 'Hola, Mundo!'
print(texto.swapcase())   # 'hOLA, mUNDO!'
```

### Eliminación de Espacios
```python
texto = "   Hola, Mundo!   "
print(texto.strip())      # 'Hola, Mundo!' (elimina espacios en ambos extremos)
print(texto.lstrip())     # 'Hola, Mundo!   ' (elimina espacios izquierda)
print(texto.rstrip())     # '   Hola, Mundo!' (elimina espacios derecha)

# Eliminar caracteres específicos
texto = "###Hola###"
print(texto.strip('#'))   # 'Hola'
# Output: Hola
```

### Búsqueda y Reemplazo
```python
texto = "Hola, Mundo!"

# Buscar substrings
print(texto.find("Mundo"))     # 6 (posición donde empieza)
print(texto.find("Python"))    # -1 (no encontrado)
print(texto.index("Mundo"))    # 6 (igual que find pero lanza error si no encuentra)

# Contar ocurrencias
print(texto.count("o"))        # 2 (dos letras 'o')

# Reemplazar
print(texto.replace("Mundo", "Python"))  # 'Hola, Python!'
```

### División y Unión
```python
# División (split)
texto = "manzana,banana,cereza"
print(texto.split(","))        # ['manzana', 'banana', 'cereza']

# Unión (join)
lista = ['Hola', 'Mundo']
print(" ".join(lista))         # 'Hola Mundo'
print("-".join(lista))         # 'Hola-Mundo'
```

### Verificación de Contenido
```python
texto = "Python123"

print(texto.isalpha())     # False (no todos son letras)
print(texto.isalnum())     # True (letras y números)
print(texto.isdigit())     # False (no todos son dígitos)
print(texto.islower())     # False (hay mayúsculas)
print(texto.isupper())     # False (hay minúsculas)
print(texto.isspace())     # False (no son solo espacios)
```

## Concatenación de Strings

### Usando el operador `+`
```python
a = "Hola"
b = "Mundo"
c = a + b
print(c)  # 'HolaMundo'

# Con espacio
c = a + " " + b
print(c)  # 'Hola Mundo'
```

### Usando `+=`
```python
saludo = "Hola"
saludo += " Mundo"
print(saludo)  # 'Hola Mundo'
```

## Formateo de Strings

### Método `format()` (tradicional)
```python
nombre = "Juan"
edad = 25

# Posicional
texto = "Me llamo {} y tengo {} años".format(nombre, edad)
print(texto)  # 'Me llamo Juan y tengo 25 años'

# Con nombres
texto = "Me llamo {nombre} y tengo {edad} años".format(nombre="Ana", edad=30)
print(texto)  # 'Me llamo Ana y tengo 30 años'

# Formato numérico
precio = 49.955
texto = "Precio: {:.2f} dólares".format(precio)
print(texto)  # 'Precio: 49.96 dólares'
```

### f-Strings (Python 3.6+ - RECOMENDADO)
```python
nombre = "Carlos"
edad = 28

# Básico
texto = f"Me llamo {nombre} y tengo {edad} años"
print(texto)  # 'Me llamo Carlos y tengo 28 años'

# Expresiones
precio = 59
cantidad = 3
texto = f"Total: ${precio * cantidad:.2f}"
print(texto)  # 'Total: $177.00'

# Llamadas a funciones
def calcular_iva(monto):
    return monto * 0.21

texto = f"IVA: ${calcular_iva(100):.2f}"
print(texto)  # 'IVA: $21.00'

# Alineación y formato
numero = 42
print(f"{numero:10}")     # '        42' (ancho 10, alineado derecha)
print(f"{numero:<10}")    # '42        ' (alineado izquierda)
print(f"{numero:^10}")    # '    42    ' (centrado)
print(f"{numero:010}")    # '0000000042' (relleno con ceros)
```

### Métodos de Formateo Avanzado
```python
# Datos de ejemplo
productos = [
    {"nombre": "Manzana", "precio": 1.5, "stock": 100},
    {"nombre": "Banana", "precio": 0.8, "stock": 50},
    {"nombre": "Cereza", "precio": 3.2, "stock": 25},
]

# Tabla formateada
print(f"{'Producto':<10} {'Precio':>10} {'Stock':>10}")
print("-" * 32)
for producto in productos:
    print(f"{producto['nombre']:<10} ${producto['precio']:>9.2f} {producto['stock']:>10}")
# Output:
# Producto        Precio     Stock
# --------------------------------
# Manzana          $1.50        100
# Banana           $0.80         50
# Cereza           $3.20         25
```

## Caracteres de Escape

Los caracteres de escape comienzan con `\` y permiten insertar caracteres especiales:

```python
print("Comillas dobles: \"texto\"")     # "texto"
print("Comilla simple: \'texto\'")      # 'texto'
print("Backslash: \\")                   # \
print("Nueva línea: Hola\nMundo")       # Hola (nueva línea) Mundo
print("Tabulación: Nombre\tEdad")       # Nombre    Edad
print("Retorno de carro: Hola\rMundo")  # Mundo (sobrescribe)
print("Backspace: Hola\bMundo")         # HolMundo (elimina 'a')
```

### Raw Strings (Strings crudos)
```python
# Raw string ignora caracteres de escape
print(r"C:\Usuarios\Nombre\Documentos")  # C:\Usuarios\Nombre\Documentos
print("C:\\Usuarios\\Nombre\\Documentos") # Mismo resultado con escapes

# Útil para expresiones regulares y paths
path = r"C:\Users\Admin\Desktop"
regex = r"\d{3}-\d{3}-\d{4}"  # Patrón para teléfono
```

## Métodos Especializados (string module)

El módulo `string` de Python proporciona constantes y clases útiles:

```python
import string

# Constantes útiles
print(string.ascii_letters)   # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.ascii_lowercase) # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase) # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)          # '0123456789'
print(string.hexdigits)       # '0123456789abcdefABCDEF'
print(string.octdigits)       # '01234567'
print(string.punctuation)     # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
print(string.whitespace)      # ' \t\n\r\x0b\x0c'
```

### Plantillas de Strings (Template)
```python
from string import Template

# Plantilla segura para substitución
plantilla = Template("Hola, $nombre. Tienes $edad años.")
texto = plantilla.substitute(nombre="Ana", edad=25)
print(texto)  # 'Hola, Ana. Tienes 25 años.'

# Con diccionario
datos = {"nombre": "Carlos", "edad": 30}
texto = plantilla.substitute(datos)
print(texto)  # 'Hola, Carlos. Tienes 30 años.'

# Safe substitute (no lanza error si falta variable)
texto = plantilla.safe_substitute(nombre="Luis")
print(texto)  # 'Hola, Luis. Tienes $edad años.'
```

## Métodos de Validación

```python
texto = "Python3"

# Verificaciones comunes
print(texto.startswith("Py"))    # True
print(texto.endswith("3"))       # True

# Verificación de identificadores válidos
print("variable1".isidentifier())  # True
print("1variable".isidentifier())  # False
print("for".isidentifier())        # True (pero es palabra reservada)
```

## Métodos de Alineación y Relleno

```python
texto = "Python"

print(texto.center(20, "*"))   # '*******Python*******'
print(texto.ljust(15, "-"))    # 'Python---------'
print(texto.rjust(15, "-"))    # '---------Python'
print(texto.zfill(10))         # '0000Python' (relleno con ceros a izquierda)
```

## Tabla de Traducción (translate)

```python
# Crear tabla de traducción
tabla = str.maketrans("áéíóú", "aeiou")
texto = "café corazón"
print(texto.translate(tabla))  # 'cafe corazon'

# Eliminar caracteres
tabla = str.maketrans("", "", "0123456789")
texto = "Python3 es mejor que Python2"
print(texto.translate(tabla))  # 'Python es mejor que Python'
```

## Métodos de Partición

```python
texto = "usuario@dominio.com"

# Partition - divide en 3 partes (antes, separador, después)
print(texto.partition("@"))  # ('usuario', '@', 'dominio.com')

# Rpartition - busca desde la derecha
texto = "uno.dos.tres"
print(texto.rpartition("."))  # ('uno.dos', '.', 'tres')
```

## Métodos de División Avanzada

```python
texto = "línea1\nlínea2\nlínea3"

# splitlines - divide por líneas
print(texto.splitlines())       # ['línea1', 'línea2', 'línea3']
print(texto.splitlines(True))   # ['línea1\n', 'línea2\n', 'línear3'] (mantiene \n)

# rsplit - divide desde la derecha
texto = "uno.dos.tres.cuatro"
print(texto.split(".", 2))      # ['uno', 'dos', 'tres.cuatro'] (máximo 2 splits)
print(texto.rsplit(".", 2))     # ['uno.dos', 'tres', 'cuatro'] (desde derecha)
```

## Métodos de Codificación

```python
texto = "café ñandú"

# Codificación
codificado = texto.encode("utf-8")
print(codificado)  # b'caf\xc3\xa9 \xc3\xb1and\xc3\xba'

# Decodificación
decodificado = codificado.decode("utf-8")
print(decodificado)  # 'café ñandú'

# Diferentes codificaciones
print(texto.encode("ascii", "ignore"))   # b'caf  and' (ignora errores)
print(texto.encode("ascii", "replace"))  # b'caf? ?and?' (reemplaza con ?)
```

## Comparación de Strings

```python
# Comparación lexicográfica (orden alfabético)
print("abc" < "abd")      # True
print("abc" == "abc")     # True
print("ABC" < "abc")      # True (mayúsculas antes que minúsculas en ASCII)

# Comparación case-insensitive
print("Python".lower() == "python".lower())  # True
```

## Conversión entre Strings y Otros Tipos

```python
# De string a otros tipos
print(int("42"))           # 42
print(float("3.14"))       # 3.14
print(bool("True"))        # True (cualquier string no vacío es True)
print(bool(""))            # False (string vacío es False)

# De otros tipos a string
print(str(42))             # "42"
print(str([1, 2, 3]))      # "[1, 2, 3]"
print(str(3.14))           # "3.14"
```

## Performance Consideraciones

### Concatenación vs Join
```python
# INEFICIENTE (crea múltiples strings temporales)
resultado = ""
for i in range(10000):
    resultado += str(i)

# EFICIENTE (usa lista + join)
partes = []
for i in range(10000):
    partes.append(str(i))
resultado = "".join(partes)
```

## Resumen de Métodos Esenciales

| Categoría | Métodos Clave | Uso Común |
|-----------|--------------|-----------|
| **Búsqueda** | `find()`, `index()`, `rfind()`, `rindex()`, `count()` | Localizar substrings |
| **Verificación** | `startswith()`, `endswith()`, `isalpha()`, `isdigit()`, `isalnum()` | Validar contenido |
| **Modificación** | `lower()`, `upper()`, `strip()`, `replace()`, `split()` | Transformar strings |
| **Formateo** | `format()`, f-strings, `center()`, `ljust()`, `rjust()` | Dar formato y alinear |
| **Unión/División** | `join()`, `split()`, `splitlines()`, `partition()` | Combinar y separar |

## Ejemplo Práctico Completo

```python
# Procesamiento de datos de usuario
def procesar_nombre_completo(nombre_completo):
    """Procesa un nombre completo y lo formatea correctamente."""
    
    # Limpiar y estandarizar
    nombre = nombre_completo.strip().lower()
    
    # Capitalizar cada palabra
    nombre = nombre.title()
    
    # Separar nombre y apellido
    partes = nombre.split()
    
    if len(partes) >= 2:
        nombre = partes[0]
        apellido = " ".join(partes[1:])
        
        # Crear diferentes formatos
        formato_completo = f"{nombre} {apellido}"
        formato_iniciales = f"{nombre[0]}. {apellido}"
        formato_apellido_nombre = f"{apellido}, {nombre}"
        
        return {
            "completo": formato_completo,
            "iniciales": formato_iniciales,
            "apellido_nombre": formato_apellido_nombre,
            "email": f"{nombre.lower()}.{apellido.lower().replace(' ', '')}@empresa.com"
        }
    return None

# Uso
resultado = procesar_nombre_completo("  juan carlos perez garcia  ")
print(resultado)
# Output:
# {
#   'completo': 'Juan Carlos Perez Garcia',
#   'iniciales': 'J. Carlos Perez Garcia',
#   'apellido_nombre': 'Carlos Perez Garcia, Juan',
#   'email': 'juan.carlosperezgarcia@empresa.com'
# }
```

**Nota importante:** Todos los métodos de strings en Python **devuelven nuevos strings**, no modifican el string original (los strings son inmutables).

---
__TE SIENTES DETERMINADO__