---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-22T18:35:00
Revision: 2026-01-22T18:35:00
---
# Sets en Python

Los **sets** (conjuntos) en Python son una colección **mutable** de elementos **desordenados**, **únicos** e **inmutables**. Los sets son ideales para operaciones matemáticas de conjuntos y para eliminar duplicados de forma eficiente.

## Operaciones de los sets en Python

Uno de los puntos fuertes de los sets son sus operaciones matemáticas. Estas operaciones pueden combinar y filtrar elementos de múltiples sets de manera sorprendentemente rápida, mucho más que combinando listas e iterándolas.

```python
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
```

### Unión

Una unión simplemente reúne todos los elementos que están en A **o** en B:

```python
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# Unión usando .union()
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 8}

# Unión usando el operador |
print(A | B)       # {1, 2, 3, 4, 5, 6, 8}
```

![[sets.png]]

### Intersección

La intersección retorna solamente los elementos que están en A **y** en B:

```python
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# Usando el método
print(A.intersection(B))  # {1, 2, 4}

# Usando el operador &
print(A & B)              # {1, 2, 4}
```

![[set_intersection.png]]

### Diferencia

Esto retornará solamente los elementos que estén presentes en A pero **no** en B:

```python
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# Usando el método
print(A.difference(B))  # {6, 8}

# Usando el operador -
print(A - B)            # {6, 8}
```

**Nota importante**: El orden importa en la diferencia:

```python
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

print(B.difference(A))  # {3, 5}
print(B - A)            # {3, 5}
```

![[set_difference.png]]

### Diferencia Simétrica

La diferencia simétrica retorna los elementos que son **únicos** entre A y B (los que están en A o en B, pero no en ambos):

```python
A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

print(A.symmetric_difference(B))  # {3, 5, 6, 8}
```

Se puede interpretar como la operación inversa de la intersección:

![[set_symmetric_difference.png]]

## Supersets, Subsets y Membership usando sets

Definamos dos sets:
```python
A = {1, 2, 3, 4, 5}
B = {1, 2, 4}
```

Decimos que:
- **A es un superset de B**: todos los elementos de B también están en A
- **B es un subset de A**: B está completamente contenido en A

Podemos verificar estas relaciones:

```python
A = {1, 2, 3, 4, 5}
B = {1, 2, 4}

print(A.issuperset(B))  # True
print(B.issubset(A))    # True
```

![[superset_subset.png]]

También se pueden usar los operadores de membresía `in` y `not in`:

```python
B = {1, 2, 4}
print(1 in B)   # True
print(3 in B)   # False
print(5 not in B)  # True
```

## Creando y manipulando sets en Python

Hay varias maneras de crear sets en Python. Puedes definir un set usando llaves `{}` o usando la función `set()`:

```python
# Dos formas equivalentes
S = {1, 10, 100}
S = set([1, 10, 100])  # A partir de una lista
```

**¡Importante!**: La única forma de inicializar un set vacío es con la función `set()`:

```python
S = set()   # Set vacío ✅
S = {}      # ¡Esto crea un diccionario vacío, NO un set! ❌
```

### Modificando sets

Los sets pueden modificarse con los métodos `.add()` y `.remove()`:

```python
S = set()

S.add(2)
print(S)  # {2}

S.remove(2)
print(S)  # set()
```

**Notas importantes:**
- Llamar a `.add()` con un elemento que ya existe no hace nada (los sets solo guardan valores únicos)
- Llamar a `.remove()` con un valor que no está en el set lanza un `KeyError`
- Para eliminar sin error si el elemento no existe, usa `.discard()`

```python
S = {1, 2, 3}
S.add(2)      # No hace nada, el 2 ya existe
S.remove(4)   # KeyError: 4
S.discard(4)  # No hace nada, no lanza error
```

### Combinando sets con `.update()`

El método `.update()` combina sets:

```python
A = {1, 2, 3}
B = {3, 4, 5}

S = set()
S.update(A)
print(S)  # {1, 2, 3}

S.update(B)
print(S)  # {1, 2, 3, 4, 5}
```

### Copiando y limpiando sets

Los métodos `.copy()` y `.clear()` sirven para duplicar sets y eliminar todos sus elementos:

```python
S1 = {1, 2, 3}
S2 = S1.copy()  # Copia independiente de S1
S1.clear()      # Vacía S1

print(S1)  # set()
print(S2)  # {1, 2, 3}
```

### Iterando sobre sets

Puedes iterar sobre sets usando bucles [[Estructuras Iterativas en Python#Estructura `for`|for]]:

```python
S = {1, 2, 3, 4, 5}
for number in S:
    print(number)
```

**¡Cuidado!**: El orden de iteración sobre los elementos es **no garantizado**. Aunque a veces parezca ordenado, si el orden de los elementos es esencial para tu programa, no uses sets.

## Métodos útiles de sets

| Método | Descripción | Ejemplo |
|--------|-------------|---------|
| `.add(x)` | Añade x al set | `S.add(4)` |
| `.remove(x)` | Elimina x (error si no existe) | `S.remove(3)` |
| `.discard(x)` | Elimina x (sin error si no existe) | `S.discard(3)` |
| `.pop()` | Elimina y retorna un elemento aleatorio | `S.pop()` |
| `.clear()` | Elimina todos los elementos | `S.clear()` |
| `.copy()` | Retorna una copia superficial | `S2 = S.copy()` |
| `.update(iterable)` | Añade elementos de un iterable | `S.update([4,5])` |
| `.union(other)` | Retorna unión de conjuntos | `A.union(B)` |
| `.intersection(other)` | Retorna intersección | `A & B` |
| `.difference(other)` | Retorna diferencia | `A - B` |
| `.symmetric_difference(other)` | Retorna diferencia simétrica | `A ^ B` |
| `.issubset(other)` | Verifica si es subconjunto | `A.issubset(B)` |
| `.issuperset(other)` | Verifica si es superconjunto | `A.issuperset(B)` |
| `.isdisjoint(other)` | Verifica si no hay elementos en común | `A.isdisjoint(B)` |

## ¿Dónde se pueden usar los sets?

### 1. Eliminar duplicados de una lista
Una de las aplicaciones más comunes de los sets es eliminar elementos duplicados:

```python
valores = [1, 2, 2, 1, 3, 4, 1, 2, 3, 4, 1]
valores_unicos = list(set(valores))

print(valores_unicos)  # [1, 2, 3, 4]
```

### 2. Filtrar datos
Los sets son excelentes para análisis de datos y filtrado:

```python
todos_clientes = {104, 203, 255, 289, 448}
clientes_compraron_X = {104, 448}
clientes_compraron_Y = {104, 255, 289}
```

Respondamos preguntas comunes:

```python
# 1. ¿Qué clientes compraron X pero no Y?
print(clientes_compraron_X.difference(clientes_compraron_Y))  # {448}

# 2. ¿Qué clientes compraron ambos?
print(clientes_compraron_X.intersection(clientes_compraron_Y))  # {104}

# 3. ¿Qué clientes no compraron nada?
compradores = clientes_compraron_X.union(clientes_compraron_Y)
print(todos_clientes.difference(compradores))  # {203}

# 4. ¿Qué clientes compraron X o Y (o ambos)?
print(clientes_compraron_X.union(clientes_compraron_Y))  # {104, 255, 289, 448}

# 5. ¿Algún cliente compró ambos productos?
print(len(clientes_compraron_X.intersection(clientes_compraron_Y)) > 0)  # True

# 6. ¿Los productos tienen clientes exclusivos?
exclusivos_X = clientes_compraron_X - clientes_compraron_Y
exclusivos_Y = clientes_compraron_Y - clientes_compraron_X
print("Exclusivos de X:", exclusivos_X)  # {448}
print("Exclusivos de Y:", exclusivos_Y)  # {255, 289}
```

### 3. Encontrar elementos comunes entre listas
```python
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

comunes = set(lista1) & set(lista2)
print(comunes)  # {4, 5}
```

### 4. Verificar si todos los elementos de una lista son únicos
```python
def todos_unicos(elementos):
    return len(elementos) == len(set(elementos))

print(todos_unicos([1, 2, 3, 4]))  # True
print(todos_unicos([1, 2, 2, 3]))  # False
```

## Sets Inmutables: `frozenset`

Python también tiene conjuntos inmutables llamados `frozenset`. Son útiles cuando necesitas un conjunto que no cambie (por ejemplo, como clave en un diccionario):

```python
# Set mutable (normal)
S = {1, 2, 3}
S.add(4)  # Funciona

# frozenset (inmutable)
F = frozenset([1, 2, 3])
# F.add(4)  # Error: 'frozenset' object has no attribute 'add'

# Útil como clave de diccionario
diccionario = {
    frozenset([1, 2]): "conjunto A",
    frozenset([3, 4]): "conjunto B"
}
```

## Comparación con otras estructuras

| Característica | Set | Lista | Tupla | Diccionario |
|----------------|-----|-------|-------|-------------|
| **Orden** | No | Sí | Sí | Sí (desde Python 3.7) |
| **Mutabilidad** | Sí | Sí | No | Sí |
| **Elementos únicos** | Sí | No | No | Sí (solo claves) |
| **Acceso por índice** | No | Sí | Sí | Por clave |
| **Operaciones de conjuntos** | Sí | No | No | Solo claves |

## Ejemplo práctico completo

```python
# Análisis de preferencias de usuarios
usuarios_peliculas = {
    'Ana': {'acción', 'comedia', 'drama'},
    'Luis': {'acción', 'suspenso', 'terror'},
    'María': {'comedia', 'romance', 'drama'},
    'Carlos': {'acción', 'comedia', 'terror'}
}

# Todas las categorías únicas
todas_categorias = set()
for categorias in usuarios_peliculas.values():
    todas_categorias.update(categorias)
print("Todas las categorías:", todas_categorias)

# Categorías más populares (intersección de todos)
categorias_comunes = set.intersection(*usuarios_peliculas.values())
print("Categorías que a todos les gustan:", categorias_comunes)

# Recomendaciones personalizadas para Ana
def recomendar(usuario_actual, usuarios_peliculas):
    preferencias_actual = usuarios_peliculas[usuario_actual]
    recomendaciones = set()
    
    for usuario, preferencias in usuarios_peliculas.items():
        if usuario != usuario_actual:
            # Recomendar lo que al otro le gusta y al actual no
            nuevas = preferencias - preferencias_actual
            recomendaciones.update(nuevas)
    
    return recomendaciones

print("Recomendaciones para Ana:", recomendar('Ana', usuarios_peliculas))
```

---
**TE SIENTES DETERMINADO** 
