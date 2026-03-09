---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
proyecto: aprendizaje-python
Creacion: 2026-03-02T21:37:00
Revision: 2026-03-02T22:03:00
---
# Como funciona la encapsulacion en Python

La [[Funciones en Python#2. Encapsulación|encapsulación]] es uno de los pilares de la programación orientada a objetos. Consiste en **ocultar los detalles internos de implementación** y exponer solo lo necesario para interactuar con un objeto. El objetivo es proteger el estado interno de un objeto de modificaciones accidentales o incorrectas, proporcionando una interfaz controlada para acceder y modificar sus datos.

En lenguajes como Java o C++, la encapsulación se implementa mediante modificadores de acceso estrictos (`public`, `protected`, `private`) que el compilador hace cumplir. Python toma un enfoque diferente: **no tiene modificadores de acceso reales**. En su lugar, utiliza convenciones de nombres y algunas técnicas internas para señalar la intención del programador.

Esta diferencia filosófica es importante. Python sigue el principio de que "somos todos adultos consentidos": el lenguaje no te impide acceder a atributos internos, pero confía en que respetarás las convenciones. Esto hace el código más flexible y menos burocrático, pero requiere disciplina por parte del programador. Lo cual puede llegar a ser un arma de doble filo.

## Los tres niveles de acceso en Python

Python reconoce conceptualmente tres niveles de acceso a los atributos y métodos de una clase: público, protegido y privado. Sin embargo, a diferencia de otros lenguajes, estos niveles no son impuestos por el compilador sino señalados mediante convenciones de nombres.

### Atributos públicos

Un atributo público es aquel que puede ser accedido desde cualquier parte del código: desde dentro de la clase, desde clases derivadas, y desde código externo. En Python, **todos los atributos son públicos por defecto** a menos que se indique lo contrario mediante convenciones.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Público
        self.edad = edad        # Público
    
    def presentarse(self):      # Método público
        return f"Hola, soy {self.nombre}"

>>> p = Persona("Aguss", 25)
>>> p.nombre              # Acceso directo
'Aguss'
>>> p.nombre = "María"    # Modificación directa
>>> p.nombre
'María'
```

Los atributos públicos forman parte de la interfaz de la clase. Son los datos que la clase expone deliberadamente para que otros objetos o código externo puedan leerlos y modificarlos. No hay restricciones ni validaciones automáticas: si un atributo es público, cualquiera puede cambiarlo a cualquier valor.

### Atributos protegidos

Un atributo protegido está destinado a ser accedido solo desde dentro de la clase y sus subclases. En Python, se señala con un **guion bajo al inicio** del nombre:

```python
class Cuenta:
    def __init__(self, saldo):
        self._saldo = saldo      # Protegido por convención
    
    def depositar(self, monto):
        self._saldo += monto

class CuentaPremium(Cuenta):
    def obtener_saldo(self):
        return self._saldo       # Accesible desde subclase

>>> c = Cuenta(1000)
>>> c._saldo              # Técnicamente accesible desde fuera
1000
>>> c._saldo = -500       # Técnicamente modificable
```

El guion bajo es solo una señal para otros programadores: "este atributo es interno, no lo uses directamente". Python no impide el acceso desde fuera de la clase. El atributo sigue siendo perfectamente accesible y modificable.

La convención del guion bajo tiene algunos efectos prácticos adicionales:

- Los atributos con un guion bajo no se importan con `from modulo import *` (a menos que se defina explícitamente en `__all__`)
- En el intérprete interactivo, el guion bajo se usa para el último resultado, por lo que es una convención conocida

Es importante entender que los atributos protegidos en Python son más una documentación viva que una restricción técnica. Si un programador decide acceder a `_saldo` desde fuera de la clase, el código funcionará, pero estará rompiendo el contrato que la clase establece.

### Atributos privados

Un atributo privado está destinado a ser accedido únicamente desde dentro de la clase donde se define, ni siquiera desde sus subclases. En Python, se señala con **dos guiones bajos al inicio** del nombre:

```python
class SecureVault:
    def __init__(self, password):
        self.__password = password    # Privado con name mangling
    
    def verificar(self, intento):
        return intento == self.__password

>>> vault = SecureVault("secreto123")
>>> vault.__password
AttributeError: 'SecureVault' object has no attribute '__password'
```

A diferencia del guion simple, el doble guion bajo activa un mecanismo llamado **[[Clases en Python#La "encapsulación fantasma"|name mangling]]** (alteración de nombres). Python renombra el atributo internamente: `__password` se convierte en `_SecureVault__password`. Esto hace que el atributo no sea directamente accesible usando su nombre original desde fuera de la clase.

Sin embargo, esto **no es verdadera privacidad**. El atributo sigue siendo accesible si conocés el nombre modificado:

```python
>>> vault._SecureVault__password
'secreto123'
>>> vault._SecureVault__password = "hackeado"
>>> vault.verificar("hackeado")
True
```

El name mangling existe principalmente para **evitar colisiones de nombres** en jerarquías de herencia complejas, no para proporcionar seguridad real. Si una clase base define `__atributo` y una subclase también define `__atributo`, cada uno tendrá su propia versión con nombres diferentes: `_ClaseBase__atributo` y `_ClaseDerivada__atributo`.

## Name mangling en profundidad

El name mangling es el mecanismo que Python utiliza para "ocultar" atributos con doble guion bajo. Entender cómo funciona es útil para depurar código y para entender por qué Python no tiene privacidad real.

### Cómo funciona el name mangling

Cuando Python encuentra un identificador que comienza con dos guiones bajos y no termina con dos guiones bajos, lo transforma automáticamente:

```python
class Ejemplo:
    def __init__(self):
        self.__privado = "oculto"
        self.__otro__ = "esto no se mangleará"
    
    def __metodo_privado(self):
        return "método oculto"

>>> e = Ejemplo()
>>> dir(e)
['_Ejemplo__metodo_privado', '_Ejemplo__privado', '__otro__', ...]
```

La regla de transformación es: `__nombre` → `_NombreDeLaClase__nombre`. Observá que:

- Solo se aplica a nombres que comienzan con dos guiones bajos
- No se aplica si el nombre termina con dos guiones bajos (estos son métodos especiales como `__init__`)
- El nombre de la clase se preserva con su primer guion bajo si lo tiene

### ¿Por qué existe el name mangling?

El name mangling no fue diseñado para seguridad, sino para evitar colisiones de nombres en herencia:

```python
class Base:
    def __init__(self):
        self.__valor = "base"

class Derivada(Base):
    def __init__(self):
        super().__init__()
        self.__valor = "derivada"    # No sobrescribe el de Base

>>> d = Derivada()
>>> d._Base__valor
'base'
>>> d._Derivada__valor
'derivada'
```

Sin name mangling, `__valor` en `Derivada` sobrescribiría el de `Base`, causando problemas difíciles de depurar. Con name mangling, cada clase tiene su propia versión "privada".

### Ver atributos privados

Podés ver todos los atributos de un objeto, incluidos los privados con name mangling:

```python
>>> obj = SecureVault("secreto")
>>> dir(obj)
['__class__', '__delattr__', ..., '_SecureVault__password', ...]

>>> obj.__dict__
{'_SecureVault__password': 'secreto'}
```

El hecho de que los atributos "privados" sean visibles con `dir()` y accesibles con el nombre modificado refuerza la idea de que Python no tiene privacidad real, solo convenciones y mecanismos de namespace.

## Getters y setters: el enfoque Java vs Python

En lenguajes como Java, es común definir todos los atributos como privados y proporcionar métodos públicos para acceder y modificar cada uno:

```java
// Enfoque Java típico
public class Persona {
    private String nombre;
    private int edad;
    
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public int getEdad() {
        return edad;
    }
    
    public void setEdad(int edad) {
        this.edad = edad;
    }
}
```

Este patrón tiene ventajas: si en el futuro necesitás agregar validación al setter, podés hacerlo sin cambiar la interfaz. Pero también tiene desventajas: mucho código repetitivo, y los getters/setters triviales no agregan valor.

### El anti-patrón en Python

Muchos programadores que vienen de Java aplican el mismo patrón en Python:

```python
# ANTI-PATRÓN: getters y setters triviales
class Persona:
    def __init__(self):
        self._nombre = None
        self._edad = None
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad
```

Esto es innecesario en Python. Si no necesitás validación ni lógica especial, simplemente usá atributos públicos:

```python
# Enfoque Python simple
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

>>> p = Persona("Aguss", 25)
>>> p.nombre
'Aguss'
>>> p.edad = 26    # Asignación directa
```

La ventaja de este enfoque es la simplicidad. El código es más corto, más legible, y hace exactamente lo que se espera.

### ¿Qué pasa si después necesitás validación?

Acá es donde Python brilla. Si empezaste con un atributo público y después necesitás agregar validación, podés convertirlo en una property sin cambiar la interfaz:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre        # Sigue siendo público
        self.edad = edad            # Ahora con validación

>>> p = Persona("Aguss", 25)
>>> p.edad = -5      # Siempre funcionó...
>>> p.edad
-5                   # ...pero ahora edad negativa no tiene sentido
```

Si necesitás validar, agregás `@property` sin cambiar cómo se usa la clase:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad          # Ahora protegido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        if valor < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = valor

>>> p = Persona("Aguss", 25)
>>> p.edad = -5
ValueError: La edad no puede ser negativa
>>> p.edad = 26      # Sigue funcionando igual que antes
```

El código que usaba `p.edad = valor` sigue funcionando exactamente igual. La interfaz no cambió, solo se agregó validación interna.

## El decorador @property

El [[Decoradores#Decoradores en Python|decorador]] `@property` es la forma pitónica de implementar getters, setters y deleters. Permite acceder a métodos como si fueran atributos, manteniendo la capacidad de agregar lógica de validación, cálculo o control de acceso.

### Getter con @property

```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def radio(self):
        """Getter: permite acceder como atributo"""
        return self._radio
    
    @property
    def area(self):
        """Property de solo lectura: atributo calculado"""
        import math
        return math.pi * self._radio ** 2

>>> c = Circulo(5)
>>> c.radio       # No es c.radio(), es c.radio (sin paréntesis)
5
>>> c.area        # Se calcula cada vez que se accede
78.53981633974483
```

Las ventajas del getter con `@property`:

- La sintaxis de acceso es natural: `obj.atributo` en lugar de `obj.get_atributo()`
- Podés agregar lógica sin cambiar la interfaz
- Podés crear atributos calculados que se actualicen automáticamente
- El código que usa la clase no necesita saber si el valor se almacena o se calcula

### Setter con @atributo.setter

El setter permite validar y procesar valores antes de asignarlos:

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = None
        self.precio = precio       # Usa el setter para validar
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo")
        if not isinstance(valor, (int, float)):
            raise TypeError("El precio debe ser un número")
        self._precio = valor

>>> p = Producto("Laptop", 1500)
>>> p.precio = -100
ValueError: El precio no puede ser negativo
>>> p.precio = "gratis"
TypeError: El precio debe ser un número
>>> p.precio = 1200     # Asignación válida
```

Observá que en `__init__` usamos `self.precio = precio` (no `self._precio = precio`) para que la validación se aplique también durante la inicialización.

### Deleter con @atributo.deleter

El deleter permite ejecutar código cuando se elimina un atributo con `del`:

```python
class ArchivoTemporal:
    def __init__(self, nombre):
        self.nombre = nombre
        self._contenido = ""
        self._abierto = True
    
    @property
    def contenido(self):
        if not self._abierto:
            raise ValueError("El archivo está cerrado")
        return self._contenido
    
    @contenido.setter
    def contenido(self, valor):
        if not self._abierto:
            raise ValueError("El archivo está cerrado")
        self._contenido = valor
    
    @contenido.deleter
    def contenido(self):
        print(f"Limpiando contenido de {self.nombre}")
        self._contenido = ""
        self._abierto = False

>>> f = ArchivoTemporal("temp.txt")
>>> f.contenido = "datos importantes"
>>> del f.contenido
Limpiando contenido de temp.txt
>>> f.contenido
ValueError: El archivo está cerrado
```

El deleter es útil para limpiar recursos, cerrar conexiones, o ejecutar cualquier lógica de limpieza cuando se elimina un atributo.

### Property de solo lectura

Si definís solo el getter, la property es de solo lectura:

```python
class Token:
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    # No hay setter, así que es de solo lectura

>>> t = Token("abc123")
>>> t.valor
'abc123'
>>> t.valor = "xyz"
AttributeError: can't set attribute 'valor'
```

Esto es útil para valores que no deberían cambiar después de la creación del objeto, como identificadores, tokens de autenticación, o constantes derivadas.

## Propiedades calculadas y cacheadas

Una ventaja de `@property` es que podés crear atributos que se calculan dinámicamente:

```python
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @property
    def area(self):
        return self.base * self.altura
    
    @property
    def perimetro(self):
        return 2 * (self.base + self.altura)

>>> r = Rectangulo(5, 3)
>>> r.area
15
>>> r.perimetro
16
>>> r.base = 10
>>> r.area      # Se recalcula automáticamente
30
```

El área y perímetro no se almacenan, se calculan cada vez. Si el rectángulo cambia, los valores se actualizan automáticamente.

Si el cálculo es costoso y querés cachear el resultado:

```python
class Analisis:
    def __init__(self, datos):
        self.datos = datos
        self._cache_resultado = None
    
    @property
    def resultado_complejo(self):
        if self._cache_resultado is None:
            print("Calculando...")
            self._cache_resultado = sum(x ** 2 for x in self.datos)
        return self._cache_resultado

>>> a = Analisis([1, 2, 3, 4, 5])
>>> a.resultado_complejo
Calculando...
55
>>> a.resultado_complejo    # Usa el caché
55
```

## Cuándo usar @property

`@property` es útil cuando:

1. **Necesitás validación** antes de asignar un valor
2. **Necesitás calcular** un valor dinámicamente
3. **Necesitás transformar** datos al leer o escribir
4. **Necesitás mantener compatibilidad** con código existente que accede a atributos directamente
5. **Necesitás controlar acceso** (solo lectura, logging, etc.)

No uses `@property` para:

1. Operaciones costosas que parecen simples (el usuario espera que acceder a un atributo sea rápido)
2. Acciones con efectos secundarios visibles (guardar en base de datos, enviar emails)
3. Todo por defecto "por si acaso" (empezá con atributos públicos, agregá property cuando la necesites)

## La filosofía de Python sobre privacidad

Python fue diseñado con la filosofía de que "somos todos adultos consentidos". El lenguaje no impide el acceso a los atributos internos de un objeto, pero proporciona mecanismos para señalar la intención:

- **Sin prefijo**: Público, parte de la interfaz
- **Un guion bajo**: Protegido, uso interno, no tocar desde fuera
- **Dos guiones bajos**: Privado, name mangling para evitar colisiones

Esta filosofía tiene ventajas y desventajas:

### Ventajas

- **Flexibilidad**: Podés acceder a atributos internos para debugging o casos especiales
- **Menos código repetitivo**: No necesitás escribir getters/setters triviales
- **Interfaz limpia**: El código cliente usa sintaxis natural de atributos
- **Refactoring fácil**: Podés empezar simple y agregar complejidad después

### Desventajas

- **Requiere disciplina**: El programador debe respetar las convenciones
- **Documentación implícita**: Las convenciones no son obvias para principiantes
- **No hay enforcement**: Un error puede no detectarse hasta runtime

### El principio de "we're all consenting adults"

El diseño de Python asume que si alguien accede a un atributo "privado", es porque tiene una buena razón. La documentación y las convenciones son suficientes para guiar el uso correcto.

```python
# Python confía en que sabés lo que hacés
class API:
    def __init__(self, key):
        self.__key = key    # "Privado" pero accesible

>>> api = API("secret-key")
>>> api._API__key    # Técnicamente posible, pero viola la convención
'secret-key'
```

Si accedés a `_API__key`, estás rompiendo el contrato. Python no te lo impide, pero asume que sabés las consecuencias.

## Resumen

| Concepto | Sintaxis | Accesibilidad | Propósito |
|----------|----------|---------------|-----------|
| Público | `nombre` | Desde cualquier parte | Interfaz pública |
| Protegido | `_nombre` | Convención: clase y subclases | Uso interno |
| Privado | `__nombre` | Name mangling: `_Clase__nombre` | Evitar colisiones |
| Property | `@property` | Controlado por getters/setters | Validación y cálculo |

La encapsulación en Python es más una cuestión de convención y buena fe que de imposición técnica. El lenguaje proporciona las herramientas para señalar la intención (`_`, `__`, `@property`), pero confía en que los programadores las respetarán.

---
__TE SIENTES DETERMINADO__
