---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-21T18:38:00
Revision: 2026-01-21T18:56:00
---
# Listas en Python

Una **lista** es una estructura de datos ordenada y mutable que almacena una colección de elementos separados por comas (`,`) y encerrados entre corchetes (`[]`). Pueden contener elementos de diferentes tipos de datos, aunque lo común es que todos sean del mismo tipo para mantener la coherencia.

```python
cuadrados = [1, 4, 9, 16, 25]
cuadrados
```
```
[1, 4, 9, 16, 25]
```

## Operaciones básicas con listas

### Indexación y *Slicing* (rebanado)
Al igual que los strings, las listas pueden ser indexadas y "rebanadas". El *slicing* siempre retorna una **nueva lista** con los elementos seleccionados.

```python
# Indexación (devuelve el elemento en esa posición)
cuadrados[0]   # Primer elemento
1
cuadrados[-1]  # Último elemento
25

# Slicing (devuelve una nueva lista)
cuadrados[-3:]  # Últimos tres elementos
[9, 16, 25]
cuadrados[1:4]  # Elementos del índice 1 al 3
[4, 9, 16]
```

### Concatenación
Las listas soportan la operación de concatenación con el operador `+`:

```python
cuadrados + [36, 49, 64, 81, 100]
```
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## Mutabilidad: La característica clave

**A diferencia de los strings, las listas son mutables.** Esto significa que puedes modificar sus elementos después de crearlas. Cuando modificas una lista, estás cambiando el objeto original en memoria, no creando uno nuevo.

```python
cubos = [1, 8, 27, 65, 125]  # ¡Hay un error aquí!
4 ** 3  # El cubo de 4 es 64, ¡no 65!
64

# Corregimos el valor directamente
cubos[3] = 64  # Reemplazamos el valor incorrecto
cubos
```
```
[1, 8, 27, 64, 125]
```

### Añadir elementos con `.append()`
El método `.append()` añade un elemento al **final** de la lista:

```python
cubos.append(216)    # Añade el cubo de 6 (6³ = 216)
cubos.append(7 ** 3) # Añade el cubo de 7 (7³ = 343)
cubos
```
```
[1, 8, 27, 64, 125, 216, 343]
```

## ¡Cuidado con las referencias!

**En Python, la asignación nunca copia datos, solo crea referencias.** Cuando asignas una lista a una variable, la variable **apunta** a la misma lista en memoria. Cualquier cambio se reflejará en todas las variables que referencien esa lista.

```python
rgb = ["Rojo", "Verde", "Azul"]

rgba = rgb  # ¡Esto NO crea una copia!

id(rgb) == id(rgba)  # Ambas referencian el MISMO objeto
True

rgba.append("Alfa")  # Modificamos a través de rgba

rgb  # ¡rgb también se modifica!
```
```
["Rojo", "Verde", "Azul", "Alfa"]
```

### Cómo crear una copia real
Para evitar este problema, necesitas crear una **copia explícita**. El *slicing* completo (`[:]`) es una forma común de hacerlo:

```python
rgb_correcto = rgba[:]  # Esto SÍ crea una copia nueva

rgb_correcto[-1] = "Alpha"  # Modificamos solo la copia

rgb_correcto
```
```
["Rojo", "Verde", "Azul", "Alpha"]
```
```python
rgba  # La lista original permanece intacta
```
```
["Rojo", "Verde", "Azul", "Alfa"]
```

**Nota**: Esto crea una **copia superficial** (*shallow copy*). Para listas anidadas, necesitarías una **copia profunda** (*deep copy*) usando `copy.deepcopy()` del módulo `copy`.

## 🔍 Copia Superficial vs. Copia Profunda: Explicación Detallada

Este es un concepto **CRUCIAL** para entender cómo funcionan las copias en Python, especialmente con listas anidadas.

### 📊 **Diferencia Fundamental**

| Tipo de Copia | ¿Qué hace? | Objetos Simples | Objetos Anidados | Modificar Original Afecta Copia |
|---------------|------------|-----------------|------------------|--------------------------------|
| **Copia Superficial** | Crea nuevo objeto, pero **referencia** los mismos objetos internos | ✅ Copia completa | ❌ Comparte referencias | ✅ SI (objetos anidados) |
| **Copia Profunda** | Crea nuevo objeto y **copia recursiva** de todos los objetos internos | ✅ Copia completa | ✅ Copia completa | ❌ NO |

### **Copia Superficial (Shallow Copy)**
Una copia superficial crea un **nuevo objeto contenedor**, pero **NO copia los objetos dentro de él**. En su lugar, inserta **REFERENCIAS** a los objetos originales.

```python
# Ejemplo de copia superficial
lista_original = [1, 2, [3, 4], 5]
copia_superficial = lista_original[:]  # o list(lista_original)

# Modificar lista INTERNA (la anidada)
lista_original[2].append(999)

print(f"Original: {lista_original}")  # [1, 2, [3, 4, 999], 5]
print(f"Copia superficial: {copia_superficial}")  # [1, 2, [3, 4, 999], 5] ❌
# ¡Ambas comparten la misma lista interna [3, 4]!
```

**Métodos para copia superficial:**
```python
lista = [1, [2, 3], 4]
copia1 = lista[:]              # slicing completo
copia2 = list(lista)           # constructor list()
copia3 = lista.copy()          # método .copy() (Python 3.3+)
copia4 = copy.copy(lista)      # función copy.copy()
```

### **Copia Profunda (Deep Copy)**
Una copia profunda crea un **nuevo objeto** y luego, **de forma recursiva**, inserta **copias** de los objetos encontrados en el original.

```python
# Ejemplo de copia profunda
import copy

lista_original = [1, 2, [3, 4], 5]
copia_profunda = copy.deepcopy(lista_original)

# Modificar lista INTERNA (la anidada)
lista_original[2].append(999)

print(f"Original: {lista_original}")  # [1, 2, [3, 4, 999], 5]
print(f"Copia profunda: {copia_profunda}")  # [1, 2, [3, 4], 5] ✅
# ¡Cada lista tiene su PROPIA copia de la lista interna!
```

### **¿Cuándo usar cada una?**
- **Usa copia superficial** cuando:
  - La lista NO tiene objetos mutables anidados
  - Quieres una copia rápida y no te importa compartir referencias internas
  - Ejemplo: `[1, 2, 3, 4, 5]` (lista simple de números)

- **Usa copia profunda** cuando:
  - La lista tiene objetos mutables anidados (listas dentro de listas, diccionarios, etc.)
  - Necesitas una copia completamente independiente
  - Ejemplo: `[[1, 2], [3, 4], {'a': 5}]` (estructura compleja anidada)

### **Caso práctico: Matriz (lista de listas)**
```python
# Matriz 2x2 - lista de listas
matriz = [[1, 2], [3, 4]]

# ❌ Copia superficial (ERROR común)
copia_mala = matriz[:]  # o list(matriz)
matriz[0][0] = 99

print(f"Matriz original: {matriz}")  # [[99, 2], [3, 4]]
print(f"Copia mala: {copia_mala}")   # [[99, 2], [3, 4]] ❌

# ✅ Copia profunda (SOLUCIÓN correcta)
import copy
copia_buena = copy.deepcopy(matriz)
matriz[1][1] = 77

print(f"Matriz original: {matriz}")  # [[99, 2], [3, 77]]
print(f"Copia buena: {copia_buena}") # [[99, 2], [3, 4]] ✅
```

## Modificaciones avanzadas con *Slicing*

Las asignaciones con *slicing* son poderosas: pueden reemplazar, insertar o eliminar secciones enteras de una lista, e incluso cambiar su tamaño.

```python
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letras
```
```
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

### Reemplazar una sección
```python
# Reemplazar elementos en posiciones 2 a 4 (índices 2, 3, 4)
letras[2:5] = ['C', 'D', 'E']
letras
```
```
['a', 'b', 'C', 'D', 'E', 'f', 'g']
```

### Eliminar elementos
```python
# Eliminar elementos en posiciones 2 a 4
letras[2:5] = []  # Los reemplazamos con una lista vacía
letras
```
```
['a', 'b', 'f', 'g']
```

### Limpiar toda la lista
```python
# Vaciar completamente la lista
letras[:] = []
letras
```
```
[]
```

## Listas anidadas

Las listas pueden contener otras listas, creando estructuras multidimensionales:

```python
a = ['a', 'b', 'c']
n = [1, 2, 3]

# Lista que contiene dos listas
x = [a, n]
x
```
```
[['a', 'b', 'c'], [1, 2, 3]]
```

### Acceder a elementos en listas anidadas
```python
x[0]       # Primera lista interna
['a', 'b', 'c']

x[0][1]    # Segundo elemento de la primera lista
'b'

x[1][-1]   # Último elemento de la segunda lista
3
```

## Métodos útiles de listas (de la documentación)

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `.append(x)` | Añade `x` al final | `lst.append(4)` |
| `.extend(iterable)` | Extiende con elementos de un iterable | `lst.extend([4,5])` |
| `.insert(i, x)` | Inserta `x` en posición `i` | `lst.insert(1, 10)` |
| `.remove(x)` | Elimina la primera ocurrencia de `x` | `lst.remove(3)` |
| `.pop([i])` | Elimina y devuelve elemento en `i` (último si no se especifica) | `lst.pop()` |
| `.clear()` | Elimina todos los elementos | `lst.clear()` |
| `.index(x[, start[, end]])` | Devuelve índice de `x` | `lst.index(5)` |
| `.count(x)` | Cuenta ocurrencias de `x` | `lst.count(2)` |
| `.sort(key=None, reverse=False)` | Ordena la lista *in-place* | `lst.sort()` |
| `.reverse()` | Invierte la lista *in-place* | `lst.reverse()` |
| `.copy()` | Devuelve una copia superficial | `nueva = lst.copy()` |

### Ejemplos prácticos:

```python
# Crear una lista
numeros = [3, 1, 4, 1, 5, 9, 2]

# Ordenar (modifica la lista original)
numeros.sort()
numeros  # [1, 1, 2, 3, 4, 5, 9]

# Contar elementos
numeros.count(1)  # 2 (hay dos unos)

# Encontrar índice
numeros.index(4)  # 3 (el 4 está en índice 3)

# Eliminar por índice y obtener valor
valor = numeros.pop(2)  # Elimina el elemento en índice 2 (el 2)
valor  # 2
numeros  # [1, 1, 3, 4, 5, 9]
```

## Comprensión de listas (*List Comprehensions*)

Una forma concisa y poderosa de crear listas:

```python
# Crear lista de cuadrados del 0 al 9
cuadrados = [x**2 for x in range(10)]
cuadrados  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Con condición: solo pares al cuadrado
pares_cuadrados = [x**2 for x in range(10) if x % 2 == 0]
pares_cuadrados  # [0, 4, 16, 36, 64]
```

## Verificación de membresía

Puedes verificar si un elemento está en una lista con `in`:

```python
vocales = ['a', 'e', 'i', 'o', 'u']
'a' in vocales  # True
'z' in vocales  # False
```

---
**TE SIENTES DETERMINADO** 💪
