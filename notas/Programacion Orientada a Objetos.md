---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - paradigma
proyecto: aprendizaje-programacion
Creacion: 2026-02-16T10:12:00
Revision: 2026-02-16T13:23:00
---
# Programación Orientada a Objetos

La programación orientada a objetos (POO) es un [paradigma de programación](https://es.wikipedia.org/wiki/Paradigma_de_programaci%C3%B3n) que basa todo su concepto en **objetos**. Este paradigma hereda del paradigma imperativo y utiliza como principal concepto de diseño la [programación modular](https://informatecdigital.com/que-es-programacion-modular/).

La POO surge para solucionar una limitación del paradigma imperativo tradicional: el escaso uso de la [[Funciones en Python#1. Abstracción|abstracción]] o, mejor dicho, lo poco que se podía abstraer. La solución fue implementar procesos que ocultaran la implementación y permitieran acceder a ella mediante una interfaz definida y controlada por el programador, ocultando la complejidad gracias a la [[Funciones en Python#2. Encapsulación|encapsulación]].

## Características de Diseño

En la programación imperativa tradicional, todo debía describirse: cada proceso y cada toma de decisiones.

La POO encara la resolución de los problemas desde la óptica del **objeto**, donde cada uno tiene un propósito y una tarea únicos, permitiendo una **alta cohesión**. Además, como cada objeto es independiente, se logra un **bajo acoplamiento**, de modo que un cambio en un objeto no afecta directamente al funcionamiento de otro.

El objeto abstrae los datos o características y los convierte en sus **atributos**; también abstrae los procedimientos o comportamientos para convertirlos en **métodos** que actúan sobre dichos datos.

Los métodos son, en la práctica, muy similares a los procedimientos de la programación imperativa tradicional, y los **mensajes** se pueden pensar como las invocaciones a dichos métodos.

El programador agrupa las características comunes de un conjunto de objetos y crea una **clase** a partir de ellas. La clase es el molde con el cual se crean los objetos. Los descendientes de estas clases se construyen mediante el mecanismo llamado **herencia**, capturando sus métodos y atributos para luego añadir los propios.

## Elementos Básicos de la Programación Orientada a Objetos

1. Objetos
2. Clases
3. Métodos y Mensajes
4. Herencia

### Objetos

Los objetos se pueden considerar entidades físicas o conceptuales que se caracterizan por tener **atributos** (estado) y **comportamientos** (métodos). El comportamiento queda determinado por un conjunto de servicios que el objeto puede brindar y un conjunto de responsabilidades que debe asumir.

El objeto debe **encapsular** estado (atributos) y comportamiento (métodos). La encapsulación permite:
- **Alta cohesión**: cada objeto realiza una tarea específica y no múltiples tareas, dando a cada objeto un propósito concreto.
- **Bajo acoplamiento**: al ser independientes, un cambio en un objeto no afecta el funcionamiento de otro.

**Atributos de un objeto**: describen la abstracción de las características individuales que posee un objeto (por ejemplo, color, material, tamaño).
**Comportamientos**: representan las operaciones que pueden ser realizadas por un objeto (por ejemplo, rodar, saltar).

Ejemplo:
- Objeto: pelota
- Comportamientos: rodar, saltar
- Estado: color: rojo, material: cuero, tamaño: pequeño

Además de estado y comportamiento, el objeto debe tener **identidad propia**, lo que permite diferenciarlo de otros objetos independientemente de su estado. Así, dos objetos con los mismos valores en sus atributos (como dos pelotas idénticas) siguen siendo objetos distintos.

Las acciones de un objeto se desencadenan como consecuencia de un estímulo externo: un **mensaje** que le envía otro objeto. Esto permite que el comportamiento modifique el estado, relacionando así estado y comportamiento.

Los objetos informáticos definen una representación abstracta de entidades del mundo real o virtual, con el objetivo de controlarlos o simularlos.

### Clases

Una clase abstrae las características de un conjunto de objetos con estado y comportamiento similares. La clase es el **molde** o base con la cual se crean los objetos. Si muchos objetos comparten características comunes, puedes crear ese molde para generar más.

Una **instancia** de una clase (o simplemente instancia) es un objeto creado a partir de una clase. Un ejemplo de la vida real: la clase "Perro" sabe que los perros ladran, tienen pelaje, cuatro patas, etc. Eso es el molde. Tu perro (o cualquier perro concreto) es una **instancia** de esa clase: tiene su propio pelaje de un color, ladra de una forma particular, etc.

Formalmente, una clase es una descripción de un conjunto de objetos, ya que consta de comportamientos y atributos que resumen las características comunes del conjunto.

Esta posibilidad es una de las grandes ventajas de la POO: definir clases significa **reutilizar código**.

Para permitir la encapsulación, los atributos de una clase solo deberían ser manipulables a través de sus métodos. Por ello existen distintos **niveles de visibilidad** (o encapsulación):

- **Atributos públicos**: pueden ser accedidos por cualquier objeto.
- **Atributos protegidos**: pueden ser accedidos por el objeto que los define y por los objetos de sus subclases (hijos). La clase padre **no** puede acceder a los atributos protegidos de sus hijos.
- **Atributos privados**: solo pueden ser accedidos por el objeto que los define.

En Python, esta distinción se realiza por convención (un guion bajo para protegido, dos guiones bajos para privado, aunque el lenguaje no los hace realmente inaccesibles).

### Métodos y Mensajes

Los objetos tienen la capacidad de actuar; la acción ocurre cuando reciben un **mensaje** o se les **invoca** a realizar una acción.

Cada objeto recibe, interpreta y responde a mensajes enviados por otros objetos.

Los comportamientos que caracterizan a un conjunto de objetos residen en la clase y se denominan **métodos**. Estos métodos son el código que se ejecuta para responder a un mensaje, siendo el mensaje la llamada o invocación a un método.

Las clases pueden tener dos tipos de variables (atributos) que se manifiestan al crear objetos:

- **Variables de instancia**: son aquellas que cada objeto toma al ser creado y que le dan valores personalizados. Por ejemplo, el color de una pelota puede ser "rojo" para una instancia y "azul" para otra.
- **Variables de clase**: pertenecen a la clase y son compartidas por todas sus instancias. Todos los objetos creados a partir de esa clase verán el mismo valor. Por ejemplo, una variable `num_patas` en la clase `Perro` podría ser 4 para todos los perros.

**Ejemplo** (en pseudocódigo):

```python
class Perro:
    # Variable de clase
    num_patas = 4

    def __init__(self, nombre, raza):
        # Variables de instancia
        self.nombre = nombre
        self.raza = raza

# Crear dos perros (instancias)
perro1 = Perro("Fido", "Labrador")
perro2 = Perro("Rex", "Pastor Alemán")

print(perro1.nombre)   # Fido (instancia)
print(perro2.nombre)   # Rex (instancia)
print(perro1.num_patas) # 4 (clase)
print(perro2.num_patas) # 4 (clase)
```

### Herencia

La herencia es la capacidad que tiene una clase para tomar los métodos y atributos de otra y luego añadir los suyos propios. Hay dos formas de pensar la herencia:

**Generalización (de abajo arriba):**
Partes de un conjunto de clases concretas y construyes una clase general (**superclase**) que agrupa los componentes comunes. Luego, las clases originales heredan de esa superclase y añaden sus particularidades.

**Especialización (de arriba abajo):**
Partes de una clase general y creas clases más específicas (**subclases**) que heredan los comportamientos de la general y añaden los suyos propios.

Ambas son formas distintas de pensar, pero no influyen en la construcción lógica de un programa; naturalmente llegan a los mismos resultados.

En la herencia, podemos clasificar las clases según tengan o no instancias directas:

- **Clase abstracta**: es una clase de la cual **no** se pueden crear instancias directas. Sirve como base para que otras clases (concretas) hereden de ella. Por ejemplo, una clase `Figura` podría ser abstracta, y de ella heredarían `Círculo` y `Cuadrado`, que sí son instanciables.
- **Clase concreta**: es una clase que puede ser instanciada; existe al menos un objeto de esa clase.

```
[Clase Abstracta: Figura]
       ↑            ↑
       |            |
[Clase Concreta: Círculo]  [Clase Concreta: Cuadrado]
```

También existen distintos tipos de herencia según el número de superclases:

- **Herencia simple**: una subclase hereda de una única superclase.
- **Herencia múltiple**: una subclase hereda de varias superclases.

```
Herencia simple:
    [Animal]
        ↑
        |
    [Perro]

Herencia múltiple:
    [Volador]   [Nadador]
         ↑         ↑
          \       /
           [Pato]
```

Podemos decir entonces que, dentro de una jerarquía de clases, la herencia propaga características de la clase superior a sus descendientes, de modo que varias clases pueden compartir una misma descripción.

## Relaciones entre Clases

Si bien existen clases que pueden vivir aisladas, la gran mayoría necesitan cooperar con otras. Las relaciones entre clases expresan cómo se comunican los objetos de esas clases entre sí y muestran el **acoplamiento** entre ellas.

El **acoplamiento** se define como el número de clases con las que una clase concreta está relacionada. Una clase está acoplada si sus objetos lo están; un objeto está acoplado con otro si uno de ellos actúa sobre el otro.

Según el tipo de acoplamiento, distinguimos:

- **Asociación**
- **Agregación**
- **Generalización / Especialización (Herencia)**

### Asociación

Una asociación es una conexión entre dos clases que refleja un vínculo existente en el ámbito de la aplicación. Puede ser unidireccional o bidireccional. La asociación no implica que una clase contenga a la otra ni que haya subordinación; simplemente indica que los objetos de ambas clases pueden relacionarse.

```
[Persona] ——— trabaja en ———> [Empresa]
```

A veces es necesario añadir información propia de la relación, y surgen dos variantes:

#### Clase Asociación
Representa una asociación entre dos objetos de la cual **nace una única instancia** de una clase que pertenece a esa relación. Por ejemplo, de la relación entre `RegistroCivil` y `Persona` nace un objeto único `ActaDeNacimiento`. Para cada par (RegistroCivil, Persona) hay un solo `ActaDeNacimiento`.

#### Clase que Modela la Asociación
Para una dupla de objetos relacionados, pueden existir **múltiples instancias** de una clase asociada. Por ejemplo, entre `Alumno` y `Materia` pueden generarse varios `Comprobante` de inscripción a lo largo del tiempo.

### Agregación

La agregación utiliza dos conceptos clave:

- **Reutilización**: uso de clases u objetos desarrollados y probados en un contexto, incorporados en una aplicación diferente. La forma más simple de reutilizar una clase es crear una nueva clase que la contenga. Esto se logra mediante la **composición**.
- **Extensión**: aprovechar clases desarrolladas para construir nuevas clases (en la misma u otra aplicación). La herencia es un caso típico de extensión.

La agregación consiste en definir como atributos de una clase a objetos de otras clases ya definidas. Es una relación **no simétrica** (todo/parte) donde una clase cumple un papel predominante (contenedor) sobre la otra (contenida). Se utiliza para modelar relaciones "tiene-un" o "parte-de".

Para detectar agregaciones, podemos observar si:
- Los objetos de una clase están subordinados a los de otra.
- Una acción sobre objetos de una clase implica una acción sobre objetos de otra.
- Los valores de los atributos de un objeto se propagan en los valores de los atributos de otro.

Hay dos formas de implementar la agregación:

#### Agregación propiamente dicha
El objeto contenedor tiene **referencias** a los objetos contenidos, pero estos pueden existir independientemente. La destrucción del contenedor **no implica** la destrucción de los contenidos. Sus ciclos de vida son independientes.

#### Composición
Es la forma más fuerte de agregación. El objeto contenedor **crea y posee** las partes; los objetos contenidos **no tienen sentido** fuera del contenedor. La destrucción del contenedor implica la destrucción de sus partes. Hay una relación de existencia entre el todo y cada parte.

## Polimorfismo

El polimorfismo es otro concepto clave de la POO. Se define como la capacidad que tienen objetos de clases diferentes, relacionadas mediante herencia, de responder de forma distinta a una misma llamada a un método.

Se basa en modificar (sobrescribir) el comportamiento heredado de la clase padre para adaptarlo a las necesidades de la subclase. Así, aunque dos objetos reciban el mismo mensaje (llamada al mismo método), pueden ejecutar comportamientos diferentes.

El polimorfismo fomenta la **extensibilidad** del software: se pueden añadir nuevos tipos de objetos que respondan de forma distinta sin modificar el código base que los utiliza.

## Persistencia

La **persistencia** designa la capacidad de un objeto para trascender en el tiempo o el espacio. Un objeto persistente conserva su estado en un sistema de almacenamiento permanente (esto se conoce como **pasivación** del objeto).

El objeto puede ser reconstruido posteriormente por otro proceso y se comportará exactamente igual que en el proceso inicial, manteniendo su estado previo.

---
__TE SIENTES DETERMINADO__