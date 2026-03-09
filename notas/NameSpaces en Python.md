---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-02-17T15:25:00
Revision: 2026-02-17T15:48:00
---
# Tabla de Contenidos

- [[#¿Qué es un namespace?|¿Qué es un namespace?]]
- [[#Importancia de los namespaces|Importancia de los namespaces]]
- [[#Ejemplos en código|Ejemplos en código]]
	- [[#Ejemplos en código#Namespace local de una función|Namespace local de una función]]
	- [[#Ejemplos en código#Namespace global de un módulo|Namespace global de un módulo]]
	- [[#Ejemplos en código#Namespace de una clase y de sus instancias|Namespace de una clase y de sus instancias]]
	- [[#Ejemplos en código#Acceso a variables globales desde una función|Acceso a variables globales desde una función]]
	- [[#Ejemplos en código#Namespace anidado (nonlocal)|Namespace anidado (nonlocal)]]
- [[#Conclusión|Conclusión]]
# Namespaces en Python

Los **namespaces** (espacios de nombres) son una funcionalidad fundamental en Python que permite organizar y vincular nombres a objetos, controlando así el ámbito (*scope*) de cada módulo o programa.

## ¿Qué es un namespace?

Un namespace es, en esencia, un mapeo entre nombres y objetos (o referencias a objetos). La inmensa mayoría de los namespaces en Python se implementan mediante [[Diccionarios en Python#Diccionarios en Python|diccionarios]].

Aunque no son visibles directamente, los namespaces están presentes en todas partes. Por ejemplo:
- Una función tiene su propio namespace que contiene todas las variables locales definidas dentro de ella, junto con sus referencias.
- Un módulo también tiene un namespace con todas las variables, funciones y clases definidas en ese módulo.
- Una clase posee un namespace con sus atributos (variables y métodos).

Gracias a esta organización, **no hay colisión** entre nombres iguales que conviven en un mismo programa. Dos objetos pueden tener un atributo llamado `edad`, pero pertenecen a namespaces diferentes y se accede a ellos mediante la notación de punto (`objeto1.edad`, `objeto2.edad`). Modificar uno no afecta al otro.

Cuando Python busca un atributo, lo hace en este orden:
1. Namespace de la instancia.
2. Namespace de la clase.
3. Namespaces de las clases padre (en caso de herencia).

El concepto de namespace es una consecuencia directa del modelo de Python, donde **todo son referencias**. Las referencias están ligadas a nombres, y los namespaces permiten gestionarlas. Cada declaración (módulo, función, clase, etc.) tiene su propio namespace.

## Importancia de los namespaces

Además de evitar colisiones, los namespaces sirven para:

- **Controlar la vida de los objetos**: Cuando un objeto ya no tiene ningún nombre que haga referencia a él (es decir, no queda ninguna entrada en ningún namespace que lo señale), el recolector de basura puede eliminarlo. Esto se gestiona a través de los namespaces.

- **Definir el ámbito (scope)**: Python utiliza los namespaces para saber qué variables son accesibles en cada momento. Por ejemplo, dentro de una función, el namespace local contiene las [[Scope de una Variable en Python#Ámbito Local (Local Scope)|variables locales]]. Fuera de ella, solo se ven las globales y las built-in.

Cuando declaramos una variable como `global` o `nonlocal`, le estamos indicando a Python que el nombre debe resolverse en un namespace diferente (el del módulo o el de la función envolvente, respectivamente) en lugar de crear uno nuevo en el ámbito local.

## Ejemplos en código

Veamos algunos ejemplos que ilustran el funcionamiento de los namespaces.

### Namespace local de una función

```python
def mi_funcion():
    a = 10
    b = "hola"
    print("Namespace local:", locals())

mi_funcion()
# Salida: {'a': 10, 'b': 'hola'}
```

`locals()` devuelve un diccionario con el namespace local actual.

### Namespace global de un módulo

```python
# En el intérprete o en un script
x = 5
y = [1, 2, 3]

def saludar():
    pass

print("Namespace global:", globals())
# Muestra un diccionario con todas las variables, funciones y objetos definidos
# en el ámbito global, incluyendo '__name__', '__file__', etc.
```

`globals()` devuelve el namespace del módulo actual.

### Namespace de una clase y de sus instancias

```python
class MiClase:
    clase_attr = "compartido"   # atributo de clase

    def __init__(self, valor):
        self.instancia_attr = valor   # atributo de instancia

    def metodo(self):
        pass

# Namespace de la clase
print(MiClase.__dict__)
# Muestra los atributos de la clase: '__module__', '__init__', 'metodo', 'clase_attr', etc.

obj1 = MiClase(42)
obj2 = MiClase(99)

# Namespace de la instancia obj1
print(obj1.__dict__)   # {'instancia_attr': 42}
print(obj2.__dict__)   # {'instancia_attr': 99}
```

Cada instancia tiene su propio namespace (`__dict__`) con sus atributos particulares. La clase tiene otro namespace con los atributos compartidos.

### Acceso a variables globales desde una función

```python
contador = 0

def incrementar():
    global contador
    contador += 1
    print("Dentro:", locals())

incrementar()
print("Fuera:", globals()['contador'])
```

Aquí, `global contador` hace que el nombre se resuelva en el namespace global, no en el local.

### Namespace anidado (nonlocal)

```python
def exterior():
    mensaje = "Hola"

    def interior():
        nonlocal mensaje
        mensaje += " mundo"
        print("Interior locals:", locals())

    interior()
    print("Exterior locals:", locals())

exterior()
```

`nonlocal` indica que `mensaje` pertenece al namespace de la función envolvente (`exterior`), no al local de `interior`.

## Conclusión

Los namespaces son una parte esencial de cómo Python organiza la información. Comprenderlos ayuda a escribir código más claro, a evitar errores de ámbito y a aprovechar características como los closures o la introspección con `locals()`, `globals()` y `__dict__`.

---
__TE SIENTES DETERMINADO__