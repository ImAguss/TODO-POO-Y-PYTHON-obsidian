---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-08T15:19:00
Revision: 2026-02-02T22:18:00
---
# Tabla de Contenidos

- [[#Estructura `for`|Estructura `for`]]
	- [[#Estructura `for`#Partes del bucle `for`:|Partes del bucle `for`:]]
	- [[#Estructura `for`#Ejemplo básico:|Ejemplo básico:]]
	- [[#Estructura `for`#¿Qué es un iterable?|¿Qué es un iterable?]]
	- [[#Estructura `for`#Iterable vacío:|Iterable vacío:]]
- [[#Tipos de iterables nativos en Python|Tipos de iterables nativos en Python]]
	- [[#Tipos de iterables nativos en Python#1. Secuencias (ordenadas)|1. Secuencias (ordenadas)]]
	- [[#Tipos de iterables nativos en Python#2. Colecciones (no ordenadas o con orden especial)|2. Colecciones (no ordenadas o con orden especial)]]
		- [[#2. Colecciones (no ordenadas o con orden especial)#Diccionarios:|Diccionarios:]]
		- [[#2. Colecciones (no ordenadas o con orden especial)#Sets:|Sets:]]
- [[#Usos avanzados del bucle `for`|Usos avanzados del bucle `for`]]
	- [[#Usos avanzados del bucle `for`#Bucles `for` anidados|Bucles `for` anidados]]
- [[#Control de flujo en bucles: `break`, `continue` y `else`|Control de flujo en bucles: `break`, `continue` y `else`]]
	- [[#Control de flujo en bucles: `break`, `continue` y `else`#`break`|`break`]]
	- [[#Control de flujo en bucles: `break`, `continue` y `else`#`continue`|`continue`]]
	- [[#Control de flujo en bucles: `break`, `continue` y `else`#`else` en bucles|`else` en bucles]]
		- [[#`else` en bucles#En bucles `for`:|En bucles `for`:]]
		- [[#`else` en bucles#En bucles `while`:|En bucles `while`:]]
- [[#Formas "pythónicas" de iterar|Formas "pythónicas" de iterar]]
	- [[#Formas "pythónicas" de iterar#Iterar múltiples iterables en paralelo con `zip()`|Iterar múltiples iterables en paralelo con `zip()`]]
	- [[#Formas "pythónicas" de iterar#Concatenar iterables con `chain()`|Concatenar iterables con `chain()`]]
	- [[#Formas "pythónicas" de iterar#Repetir una acción N veces|Repetir una acción N veces]]
	- [[#Formas "pythónicas" de iterar#Iterar en orden inverso o ordenado|Iterar en orden inverso o ordenado]]
- [[#Errores comunes en bucles `for`|Errores comunes en bucles `for`]]
	- [[#Errores comunes en bucles `for`#1. Modificar la colección durante la iteración|1. Modificar la colección durante la iteración]]
	- [[#Errores comunes en bucles `for`#2. Cambiar la variable de iteración|2. Cambiar la variable de iteración]]
	- [[#Errores comunes en bucles `for`#3. Ignorar excepciones potenciales|3. Ignorar excepciones potenciales]]
- [[#`for` loops vs. Comprehensions|`for` loops vs. Comprehensions]]
- [[#Iteraciones asíncronas con `async for`|Iteraciones asíncronas con `async for`]]
- [[#Estructura `while`|Estructura `while`]]
	- [[#Estructura `while`#Partes del bucle `while`:|Partes del bucle `while`:]]
	- [[#Estructura `while`#Ejemplo básico:|Ejemplo básico:]]
- [[#Usos efectivos de bucles `while`|Usos efectivos de bucles `while`]]
	- [[#Usos efectivos de bucles `while`#1. Ejecutar tareas basadas en una condición|1. Ejecutar tareas basadas en una condición]]
	- [[#Usos efectivos de bucles `while`#2. Número desconocido de iteraciones|2. Número desconocido de iteraciones]]
	- [[#Usos efectivos de bucles `while`#3. Eliminar elementos de una colección|3. Eliminar elementos de una colección]]
	- [[#Usos efectivos de bucles `while`#4. Recibir entrada del usuario|4. Recibir entrada del usuario]]
	- [[#Usos efectivos de bucles `while`#5. Iterar manualmente con `next()`|5. Iterar manualmente con `next()`]]
	- [[#Usos efectivos de bucles `while`#6. Emular bucles `do-while`|6. Emular bucles `do-while`]]
- [[#Bucles `while` para eventos "infinitos"|Bucles `while` para eventos "infinitos"]]
	- [[#Bucles `while` para eventos "infinitos"#Ejemplo: juego de adivinanzas|Ejemplo: juego de adivinanzas]]
- [[#Bucles infinitos: intencionales vs. accidentales|Bucles infinitos: intencionales vs. accidentales]]
	- [[#Bucles infinitos: intencionales vs. accidentales#Bucles infinitos accidentales|Bucles infinitos accidentales]]
	- [[#Bucles infinitos: intencionales vs. accidentales#Bucles infinitos intencionales|Bucles infinitos intencionales]]
- [[#Resumen comparativo|Resumen comparativo]]
- [[#Buenas prácticas finales|Buenas prácticas finales]]
# Estructuras Iterativas en Python

Python ofrece dos tipos principales de estructuras iterativas: **`for`** y **`while`**. Cada una tiene ventajas y casos de uso específicos.

---

## Estructura `for`

El bucle **`for`** se utiliza principalmente cuando se conoce de antemano la cantidad de iteraciones o cuando se necesita recorrer una colección de datos específica.

En Python, los bucles `for` son *compound statements* (sentencias compuestas), formados por un **encabezado** y un **bloque de código** que se ejecuta repetidamente.

```python
for variable in iterable:
    <cuerpo>
```

### Partes del bucle `for`:
- **`for`**: palabra clave que inicia el bucle.
- **`variable`**: variable que toma el valor de cada elemento del iterable en cada iteración.
- **`in`**: conecta la variable con el iterable.
- **`iterable`**: colección de datos sobre la cual iterar.
- **`<cuerpo>`**: bloque de una o más sentencias a ejecutar en cada iteración.

### Ejemplo básico:
```python
colores = ["rojo", "verde", "azul", "amarillo"]

for color in colores:
    print(color)
```
Salida:
```
rojo
verde
azul
amarillo
```

---

### ¿Qué es un iterable?
En Python, un **iterable** es cualquier objeto que se puede recorrer. Es una colección de datos sobre la cual se puede iterar. Ejemplos comunes son:
- Listas
- Tuplas
- Strings
- Diccionarios
- Sets

**Nota técnica**: Python distingue entre *iterables* e *iteradores*.
- **Iterables**: implementan el protocolo iterable a través del método `.__iter__()`.
- **Iteradores**: implementan el protocolo del iterador con `.__iter__()` y `.__next__()`.
- Todos los iteradores son iterables, pero no todos los iterables son iteradores. Los iteradores son los que realmente manejan la iteración en los bucles `for`.

### Iterable vacío:
Si el iterable está vacío, el bloque de código no se ejecuta:
```python
for item in []:
    print(item)  # No se imprime nada
```

---

## Tipos de iterables nativos en Python

### 1. Secuencias (ordenadas)
Incluyen **listas, tuplas, strings y rangos**. La iteración sigue el orden de la secuencia:

```python
# Lista
numeros = [1, 2, 3, 4]
for numero in numeros:
    print(numero)

# Tupla
persona = ("Jane", 25, "Python Dev", "Canada")
for campo in persona:
    print(campo)

# String
texto = "abcde"
for caracter in texto:
    print(caracter)

# Rango
for indice in range(5):
    print(indice)
```

### 2. Colecciones (no ordenadas o con orden especial)
#### Diccionarios:
Hay varias formas de iterar un diccionario:

```python
estudiantes = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
}

# Iterar sobre las claves (forma implícita)
for estudiante in estudiantes:
    print(estudiante)

# Iterar sobre las claves (forma explícita)
for estudiante in estudiantes.keys():
    print(estudiante)

# Acceder a valores usando la clave
for estudiante in estudiantes:
    print(estudiante, "->", estudiantes[estudiante])

# Iterar solo sobre valores
for nota in estudiantes.values():
    print(nota)

# Iterar sobre pares clave-valor (recomendado)
for estudiante, nota in estudiantes.items():
    print(estudiante, "->", nota)
```

#### Sets:
Los sets son colecciones **desordenadas**, por lo que el orden de iteración es impredecible:

```python
herramientas = {"Django", "Flask", "pandas", "NumPy"}
for herramienta in herramientas:
    print(herramienta)
```

---

## Usos avanzados del bucle `for`

### Bucles `for` anidados
Se utilizan para trabajar con estructuras multidimensionales o combinaciones:

```python
# Tabla de multiplicar
for numero in range(1, 11):
    for producto in range(numero, numero * 11, numero):
        print(f"{producto:>4d}", end="")
    print()
```

---

## Control de flujo en bucles: `break`, `continue` y `else`

### `break`
Termina **inmediatamente** el bucle completo:

```python
numeros = [1, 3, 5, 7, 9]
objetivo = 5

for numero in numeros:
    print(f"Procesando {numero}...")
    if numero == objetivo:
        print(f"¡Objetivo encontrado: {objetivo}!")
        break
```

### `continue`
Termina la **iteración actual** y pasa a la siguiente:

```python
numeros = [1, 2, 3, 4, 5, 6]

for numero in numeros:
    print(f"numero = {numero}")
    if numero % 2 != 0:
        continue
    print(f"¡{numero} es par!")
```

### `else` en bucles
El bloque `else` se ejecuta **solo si el bucle termina normalmente** (sin un `break`).

#### En bucles `for`:
Se ejecuta al **agotar el iterable**:

```python
numeros = [1, 3, 5, 7, 9]
objetivo = 42

for numero in numeros:
    print(f"Procesando {numero}...")
    if numero == objetivo:
        print(f"¡Objetivo encontrado: {objetivo}!")
        break
else:
    print(f"Objetivo no encontrado: {objetivo}")
```

#### En bucles `while`:
Se ejecuta cuando la **condición se vuelve falsa** (útil para detectar finalización natural vs. interrupción por `break`):

```python
import random
import time

MAX_INTENTOS = 5
intentos = 0

while intentos < MAX_INTENTOS:
    intentos += 1
    print(f"Intento {intentos}: Conectando al servidor...")
    time.sleep(0.3)
    
    if random.choice([False, False, False, True]):
        print("¡Conexión exitosa!")
        break
    print("Conexión fallida. Reintentando...")
else:
    print("Todos los intentos fallaron. No se pudo conectar.")
```

---

## Formas "pythónicas" de iterar

### Iterar con índices usando [[Funciones Nativas en Python#📋 Lista Completa de Funciones Incorporadas|enumerate()]]
Evita el anti-patrón de usar `range(len(colección))`:

```python
frutas = ["naranja", "manzana", "mango", "limón"]

# Forma NO recomendada
for indice in range(len(frutas)):
    fruta = frutas[indice]
    print(indice, fruta)

# Forma recomendada con enumerate()
for indice, fruta in enumerate(frutas):
    print(indice, fruta)
```

### Iterar múltiples iterables en paralelo con `zip()`
Combina elementos de varios iterables:

```python
numeros = [1, 2, 3]
letras = ["a", "b", "c"]

for numero, letra in zip(numeros, letras):
    print(numero, "->", letra)
```
**Nota**: `zip()` se detiene cuando el iterable más corto se agota.

### Concatenar iterables con `chain()`
Itera sobre varios iterables secuencialmente:

```python
from itertools import chain

primero = [7, 6, 1]
segundo = [4, 1]
tercero = [8, 0, 6]

for valor in chain(primero, segundo, tercero):
    print(valor**2)
```

### Repetir una acción N veces
Usando `range()` con variable de descarte (`_`):

```python
for _ in range(3):
    print("Toc, toc, toc")
    print("¡Penny!")
```

### Iterar en orden inverso o ordenado
- **`reversed()`**: para iterar en orden inverso
- **`sorted()`**: para iterar en orden específico

```python
acciones = ["Escribir texto", "Seleccionar texto", "Cortar texto", "Pegar texto"]

# En orden inverso
for accion in reversed(acciones):
    print(f"Deshacer: {accion}")

# Ordenar diccionario por valores
estudiantes = {"Alice": 89.5, "Bob": 76.0, "Charlie": 92.3}

estudiantes_ordenados = sorted(
    estudiantes.items(), 
    key=lambda item: item[1],  # Ordenar por valor (nota)
    reverse=True
)

for nombre, nota in estudiantes_ordenados:
    print(f"{nombre}: {nota}")
```

---

## Errores comunes en bucles `for`

### 1. Modificar la colección durante la iteración
**Problema**: Al agregar o eliminar elementos, se puede alterar la secuencia de iteración:

```python
# EJEMPLO PELIGROSO:
numeros = [2, 4, 6, 8]
for numero in numeros:
    if numero % 2 == 0:
        numeros.remove(numero)  # ¡Problema!
print(numeros)  # Resultado: [4, 8] (no vacío como se esperaría)
```

**Solución**: Iterar sobre una copia:
```python
numeros = [2, 4, 6, 8]
for numero in numeros[:]:  # Copia con slicing
    if numero % 2 == 0:
        numeros.remove(numero)
print(numeros)  # Resultado: []
```

**Mejor solución**: Crear una nueva lista:
```python
numeros = [2, 1, 4, 6, 5, 8]
procesados = []

for numero in numeros:
    if numero % 2 != 0:
        procesados.append(numero**2)
print(procesados)  # [1, 25]
```

### 2. Cambiar la variable de iteración
Reasignar la variable de iteración **no afecta** a la colección original:

```python
nombres = ["Alice", "Bob", "John", "Jane"]

for nombre in nombres:
    nombre = nombre.upper()  # Solo cambia la variable temporal
    print(nombre)

print(nombres)  # ['Alice', 'Bob', 'John', 'Jane'] (sin cambios)
```

### 3. Ignorar excepciones potenciales
Si ocurre una excepción no manejada, el bucle termina prematuramente:

```python
archivos = ["archivo1.txt", "archivo2.txt", "archivo3.txt"]

# SIN manejo de errores (puede fallar):
for archivo in archivos:
    with open(archivo, "r") as f:
        print(f.read())

# CON manejo de errores (robusto):
for archivo in archivos:
    try:
        with open(archivo, "r") as f:
            print(f"Contenido de {archivo}:")
            print(f.read())
    except FileNotFoundError:
        print(f"Error: {archivo} no encontrado. Omitiendo.")
```

---

## `for` loops vs. Comprehensions

Cuando se necesita transformar datos y crear una nueva colección, las **list comprehensions** suelen ser más concisas:

```python
# Con bucle for
cubos = []
for numero in range(10):
    cubos.append(numero**3)

# Con list comprehension (más "pythónico")
cubos = [numero**3 for numero in range(10)]
```

---

## Iteraciones asíncronas con `async for`

Permite iterar sobre iterables asíncronos:

```python
import asyncio

class RangoAsincrono:
    def __init__(self, inicio, fin):
        self.data = range(inicio, fin)
    
    async def __aiter__(self):
        for indice in self.data:
            await asyncio.sleep(0.5)
            yield indice

async def main():
    async for indice in RangoAsincrono(0, 5):
        print(indice)

asyncio.run(main())
```

---

## Estructura `while`

El bucle `while` ejecuta su bloque de código **mientras** una condición sea verdadera. También es un *compound statement*.

```python
while condicion:
    <cuerpo>
```

### Partes del bucle `while`:
- **`while`**: palabra clave que inicia el bucle.
- **`condicion`**: expresión evaluada como verdadera o falsa.
- **`<cuerpo>`**: bloque de código a ejecutar en cada iteración.

### Ejemplo básico:
```python
numero = 5
while numero != 0:
    print(numero)
    numero -= 1
```

**¡Cuidado con los bucles infinitos!** Si la condición nunca se vuelve falsa, el bucle continuará indefinidamente (se puede detener con Ctrl+C).

---

## Usos efectivos de bucles `while`

### 1. Ejecutar tareas basadas en una condición
Esperar a que se cumpla una condición (archivo creado, servidor disponible, etc.):

```python
import time
from pathlib import Path

nombre_archivo = Path("hola.txt")

print(f"Esperando que se cree {nombre_archivo.name}...")

while not nombre_archivo.exists():
    print("Archivo no encontrado. Reintentando en 1 segundo...")
    time.sleep(1)

print(f"¡{nombre_archivo} encontrado! Procesando...")
```

### 2. Número desconocido de iteraciones
Cuando no se sabe cuántas veces se ejecutará el bucle:

```python
import random
import time

def leer_temperatura():
    return random.uniform(20.0, 30.0)

while True:
    temperatura = leer_temperatura()
    print(f"Temperatura: {temperatura:.2f}°C")
    
    if temperatura >= 28:
        print("¡Temperatura objetivo alcanzada! Deteniendo monitoreo.")
        break
    
    time.sleep(1)
```

### 3. Eliminar elementos de una colección
Más seguro que con un `for` cuando se modifica la colección:

```python
colores = ["rojo", "azul", "amarillo", "verde"]

while colores:
    color = colores.pop(-1)  # Elimina desde el final
    print(f"Procesando color: {color}")
```

### 4. Recibir entrada del usuario
Patrón común para interacción continua:

```python
# Forma tradicional
linea = input("Escribe algo: ")
while linea != "detener":
    print(linea)
    linea = input("Escribe algo: ")

# Forma con operador walrus (:=) (Python 3.8+)
while (linea := input("Escribe algo: ")) != "detener":
    print(linea)
```

### 5. Iterar manualmente con `next()`
Control fino sobre la iteración:

```python
solicitudes = ["primera solicitud", "segunda solicitud", "tercera solicitud"]

print("\nCon bucle for:")
for solicitud in solicitudes:
    print(f"Manejando {solicitud}")

print("\nCon bucle while:")
it = iter(solicitudes)
while True:
    try:
        solicitud = next(it)
    except StopIteration:
        break
    print(f"Manejando {solicitud}")
```

### 6. Emular bucles `do-while`
Python no tiene bucles `do-while`, pero se pueden emular:

```python
while True:
    numero = int(input("Ingresa un número positivo: "))
    print(numero)
    if not numero > 0:
        break
```

---

## Bucles `while` para eventos "infinitos"

Aplicaciones comunes:
- Frameworks de GUI
- Videojuegos
- Aplicaciones asíncronas
- Servidores

### Ejemplo: juego de adivinanzas
```python
from random import randint

MINIMO, MAXIMO = 1, 10
numero_secreto = randint(MINIMO, MAXIMO)
pista = ""

# Bucle principal del juego
while True:
    intento = input(f"Adivina un número entre {MINIMO} y {MAXIMO} {pista}: ")
    numero = int(intento)
    
    if numero > numero_secreto:
        pista = f"(menor que {numero})"
    elif numero < numero_secreto:
        pista = f"(mayor que {numero})"
    else:
        break

print(f"¡Adivinaste! El número secreto es {numero}")
```

---

## Bucles infinitos: intencionales vs. accidentales

### Bucles infinitos accidentales
Ocurren por errores de lógica:

```python
# ¡PROBLEMA! Nunca llega a 0
numero = 5
while numero != 0:
    print(numero)
    numero -= 2  # Pasa de 1 a -1, luego -3, -5...
```

**Solución**: definir mejor la condición:
```python
numero = 5
while numero > 0:
    print(numero)
    numero -= 2
```

### Bucles infinitos intencionales
Deben incluir condiciones de salida claras:

```python
MAX_INTENTOS = 3
contrasena_correcta = "secreto123"
intentos = 0

while True:
    contrasena = input("Contraseña: ").strip()
    intentos += 1
    
    if contrasena == contrasena_correcta:
        print("¡Inicio de sesión exitoso!")
        break
    
    if intentos >= MAX_INTENTOS:
        print("Demasiados intentos fallidos.")
        break
    else:
        print(f"Contraseña incorrecta. {MAX_INTENTOS - intentos} intentos restantes.")
```

---

## Resumen comparativo

| Característica | `for` | `while` |
|----------------|-------|---------|
| **Cuándo usarlo** | Iterar sobre colecciones conocidas | Condiciones dinámicas/desconocidas |
| **Control de iteraciones** | Determinado por el iterable | Determinado por condición booleana |
| **Riesgo de infinito** | Bajo (excepto con generadores infinitos) | Alto (si condición nunca es falsa) |
| **Modificar colección** | Riesgoso (usar copia) | Más seguro (reevalúa condición) |
| **Ejecución mínima** | 0 veces (iterable vacío) | 0 veces (condición falsa inicialmente) |

---

## Buenas prácticas finales

1. **Preferir `for` sobre `while`** cuando sea posible (menos propenso a errores).
2. **Usar `enumerate()`** para obtener índices en lugar de `range(len())`.
3. **Usar `zip()`** para iterar múltiples iterables en paralelo.
4. **Considerar comprehensions** para transformaciones simples.
5. **Manejar excepciones** dentro de bucles para evitar terminaciones prematuras.
6. **Evitar modificar colecciones** durante la iteración; crear nuevas si es necesario.
7. **Asegurar condiciones de salida** claras en bucles `while`.
8. **Usar `break` y `continue`** con moderación para mantener legibilidad.

---
__TE SIENTES DETERMINADO__