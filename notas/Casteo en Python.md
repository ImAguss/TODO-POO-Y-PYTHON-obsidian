---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-01-15T14:42:00
Revision: 2026-01-15T14:59:00
---
# Casteo en Python

En programación, la **conversión de tipos** (o *type casting*) es el proceso de convertir un dato de un tipo a otro. Por ejemplo, convertir un entero a string, o un float a entero.

En Python existen dos formas principales de conversión:
- **Conversión implícita** (automática)
- **Conversión explícita** (manual)

## Conversión implícita en Python

En ciertas situaciones, el intérprete de Python convierte automáticamente los tipos de datos sin intervención del programador.

### Ejemplo: De entero a flotante

```python
numero_entero = 123
numero_flotante = 1.23

nuevo_numero = numero_entero + numero_flotante

# Mostrar nuevo valor y tipo de dato resultante
print("Valor:", nuevo_numero)
print("Tipo de dato:", type(nuevo_numero))
```
Salida:
```
Valor: 124.23
Tipo de dato: <class 'float'>
```

**¿Por qué ocurre esto?** Python siempre prioriza convertir a tipos de datos **más amplios** o **más precisos** para evitar pérdida de información. En este caso, convierte el entero a flotante para preservar la parte decimal.

### Jerarquía implícita de conversión
Python sigue un orden jerárquico implícito:
```
bool → int → float → complex
```
Donde la conversión siempre va hacia tipos "más grandes" o "más precisos".

**Nota importante**: 
- No todas las conversiones implícitas son posibles. Por ejemplo:
  ```python
  '12' + 23  # TypeError: can only concatenate str (not "int") to str
  ```
- Python **no** realiza conversiones que puedan ser ambiguas o que no tengan sentido desde una perspectiva humana.
- Para estos casos, Python ofrece como solución las **conversiones explícitas**.

## Conversión explícita en Python

En este tipo de conversión, el programador convierte **manualmente** el tipo de dato de un objeto hacia el tipo deseado según el contexto.

Para esto se usan las **funciones constructoras de tipos** nativas de Python:
- `int()` - convierte a entero
- `float()` - convierte a flotante
- `str()` - convierte a string
- `bool()` - convierte a booleano
- `list()` - convierte a lista
- `tuple()` - convierte a tupla
- `set()` - convierte a conjunto
- `dict()` - convierte a diccionario

Este proceso también se llama **casteo** o **typecasting**, ya que el programador "invoca" explícitamente el cambio.

### Ejemplo: Sumar un string a un entero usando conversión explícita

```python
num_string = '12'
num_entero = 23

print("Tipo de dato de num_string antes del casteo:", type(num_string))

# Conversión explícita (casteo)
num_string = int(num_string)

print("Tipo de dato de num_string después del casteo:", type(num_string))

num_suma = num_entero + num_string

print("Suma:", num_suma)
print("Tipo de dato de num_suma:", type(num_suma))
```
Salida:
```
Tipo de dato de num_string antes del casteo: <class 'str'>
Tipo de dato de num_string después del casteo: <class 'int'>
Suma: 35
Tipo de dato de num_suma: <class 'int'>
```

## Casos comunes de conversión explícita

### 1. String a numérico
```python
# String a entero
edad = int("25")
print(f"Edad: {edad}, Tipo: {type(edad)}")

# String a flotante
precio = float("19.99")
print(f"Precio: {precio}, Tipo: {type(precio)}")

# Con espacios (se ignoran)
numero = int("  42  ")
print(f"Número: {numero}")  # 42
```

### 2. Numérico a string
```python
# Entero a string
anio = str(2024)
print(f"Año: '{anio}', Tipo: {type(anio)}")

# Flotante a string
pi_str = str(3.14159)
print(f"Pi como string: '{pi_str}'")

# Formateando números como strings
temperatura = f"{23.5}°C"  # f-string convierte automáticamente
print(f"Temperatura: {temperatura}")
```

### 3. Conversiones entre colecciones
```python
# Lista a tupla
lista = [1, 2, 3]
tupla = tuple(lista)
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")

# Tupla a lista
tupla = (4, 5, 6)
lista = list(tupla)
print(f"Lista: {lista}, Tipo: {type(lista)}")

# String a lista de caracteres
texto = "Python"
lista_caracteres = list(texto)
print(f"Caracteres: {lista_caracteres}")

# Lista a conjunto (elimina duplicados)
numeros = [1, 2, 2, 3, 3, 3]
conjunto = set(numeros)
print(f"Conjunto: {conjunto}")  # {1, 2, 3}
```

### 4. Conversiones a booleanos
```python
# Valores que evalúan a False
print(bool(0))      # False
print(bool(0.0))    # False
print(bool(""))     # False (string vacío)
print(bool([]))     # False (lista vacía)
print(bool({}))     # False (diccionario vacío)
print(bool(None))   # False

# Valores que evalúan a True
print(bool(42))     # True
print(bool(-1))     # True
print(bool("Hola")) # True
print(bool([1,2]))  # True
print(bool(3.14))   # True
```

## Consideraciones importantes del casteo

### 1. Pérdida de datos en conversiones numéricas
```python
# Float a int (pierde la parte decimal)
numero_flotante = 3.99
numero_entero = int(numero_flotante)
print(f"3.99 convertido a int: {numero_entero}")  # 3 (NO 4)

# Int a float (sin pérdida, pero cambia tipo)
entero = 5
flotante = float(entero)
print(f"5 convertido a float: {flotante}")  # 5.0
```

### 2. Validación de datos
```python
# Intentar convertir string no numérico
try:
    resultado = int("abc123")
except ValueError as e:
    print(f"Error: {e}")  # invalid literal for int()

# Forma segura con validación
def convertir_seguro(valor, tipo=int):
    try:
        return tipo(valor)
    except (ValueError, TypeError):
        return None

print(convertir_seguro("123"))    # 123
print(convertir_seguro("12.5"))   # None (no es entero)
print(convertir_seguro("12.5", float))  # 12.5
```

### 3. Casteo con tipos incompatibles
```python
# ¿Qué pasa con esto?
lista = [1, 2, 3]
try:
    diccionario = dict(lista)
except ValueError as e:
    print(f"No se puede convertir lista a dict directamente: {e}")
    
# Pero esto sí funciona (lista de tuplas clave-valor)
lista_pares = [("a", 1), ("b", 2)]
diccionario = dict(lista_pares)
print(diccionario)  # {'a': 1, 'b': 2}
```

### 4. Casteo de valores especiales
```python
# None a otros tipos
print(int(0))           # 0 (None no se puede convertir a int)
print(str(None))        # "None"
print(bool(None))       # False

# Booleanos a números
print(int(True))        # 1
print(int(False))       # 0
print(float(True))      # 1.0
```

## Comparación: Implícita vs. Explícita

| Característica | Conversión implícita | Conversión explícita |
|----------------|----------------------|----------------------|
| **Iniciada por** | Intérprete de Python | Programador |
| **Control** | Automático | Manual |
| **Pérdida de datos** | Minimizada (siempre a tipos más amplios) | Posible (según conversión) |
| **Ejemplo** | `3 + 2.5 = 5.5` | `int("10") + 5 = 15` |
| **Riesgo de error** | Bajo (solo en casos ambiguos) | Alto (si datos no compatibles) |
| **Uso típico** | Operaciones matemáticas mixtas | Procesamiento de entrada de usuario, lectura de archivos |

## Puntos clave a recordar

1. **La conversión de tipo** es el proceso de cambiar un objeto de un tipo de dato a otro.

2. **La conversión implícita** es realizada automáticamente por el intérprete de Python cuando es seguro hacerlo, generalmente hacia tipos de datos más amplios.

3. **Python prioriza evitar la pérdida de datos** en conversiones implícitas.

4. **La conversión explícita** (type casting) requiere que el programador use funciones como `int()`, `float()`, `str()`, etc.

5. **En el type casting, puede ocurrir pérdida de datos**, especialmente al convertir de tipos más precisos a menos precisos (float → int).

6. **Siempre validar datos** antes de convertirlos para evitar errores en tiempo de ejecución.

7. **Considerar el contexto**: Algunas conversiones pueden tener resultados inesperados:
   ```python
   # ¿Qué esperas que haga esto?
   print(bool("False"))  # True (porque string no vacío)
   print(int(True))      # 1
   ```

## Buenas prácticas

1. **Usar conversiones explícitas** cuando la intención debe ser clara:
   ```python
   # Mejor:
   edad = int(input("Edad: "))
   
   # Que:
   edad = input("Edad: ")  # edad es string, puede causar errores después
   ```

2. **Manejar errores** con try-except:
   ```python
   try:
       numero = float(entrada_usuario)
   except ValueError:
       print("Por favor ingrese un número válido")
   ```

3. **Conocer los límites** de cada tipo:
   ```python
   # Enteros en Python 3 no tienen límite práctico
   grande = int("9" * 1000)  # Funciona
   
   # Pero floats tienen precisión limitada
   muy_grande = float("1e308")  # OK
   demasiado_grande = float("1e309")  # inf (infinito)
   ```

4. **Usar funciones de verificación** cuando sea apropiado:
   ```python
   # Verificar antes de convertir
   if entrada.isdigit():
       numero = int(entrada)
   else:
       print("No es un número entero válido")
   ```


---
__TE SIENTES DETERMINADO__