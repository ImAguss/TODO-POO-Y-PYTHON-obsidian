---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
  - poo
proyecto: aprendizaje-python
Creacion: 2026-03-09T12:00:00
Revision: 2026-03-09T12:00:00
---
# Relaciones entre Clases en Python

En POO, las clases rara vez existen aisladas. La mayoría cooperan entre sí, y estas cooperaciones se expresan mediante **relaciones**. El tipo de relación determina el grado de [[Programacion Orientada a Objetos#Relaciones entre Clases|acoplamiento]] entre las clases.

En Python, estas relaciones se implementan mediante atributos que referencian a otros objetos. La diferencia clave entre cada tipo de relación está en **quién crea los objetos**, **quién los destruye**, y **cómo se gestionan sus ciclos de vida**.

## Asociación

La [[Programacion Orientada a Objetos#Asociación|asociación]] es la relación más débil: un objeto conoce a otro y puede enviarle mensajes, pero ambos tienen ciclos de vida independientes. No hay relación de contención.

### Asociación unidireccional

Un objeto tiene una referencia a otro, pero no viceversa:

```python
class Gobernador:
    def __init__(self, dni, nombre_apellido):
        self.__dni = dni
        self.__nombre_apellido = nombre_apellido

    def __str__(self):
        return f"DNI: {self.__dni}, Nombre: {self.__nombre_apellido}"

class Provincia:
    def __init__(self, nombre, cantidad_habitantes):
        self.__nombre = nombre
        self.__cantidad_habitantes = cantidad_habitantes
        self.__gobernador = None  # Referencia opcional

    def set_gobernador(self, gobernador):
        self.__gobernador = gobernador

    def __str__(self):
        return f"Provincia: {self.__nombre}, Habitantes: {self.__cantidad_habitantes}, Gobernador: {self.__gobernador}"

# Uso
gobernador = Gobernador(27888111, "Marcelo Orrego")
provincia = Provincia("San Juan", 681055)
provincia.set_gobernador(gobernador)
```

La `Provincia` conoce a su `Gobernador`, pero `Gobernador` no necesariamente conoce a la `Provincia`.

### Asociación bidireccional

Ambos objetos tienen referencias mutuas. Esto introduce el problema de la **[[Como python maneja la memoria#El Problema con Referencias Circulares|referencia circular]]**:

```python
class Provincia:
    def __init__(self, nombre, cantidad_habitantes, gobernador=None):
        self.__nombre = nombre
        self.__cantidad_habitantes = cantidad_habitantes
        self.__gobernador = gobernador

    def set_gobernador(self, gobernador):
        self.__gobernador = gobernador

    def set_gobernador_bidireccional(self, gobernador):
        """Establece la relación en ambas direcciones"""
        self.__gobernador = gobernador
        gobernador.set_provincia(self)  # ¡Cuidado con referencias circulares!

class Gobernador:
    def __init__(self, dni, nombre_apellido, provincia=None):
        self.__dni = dni
        self.__nombre_apellido = nombre_apellido
        self.__provincia = provincia

    def set_provincia(self, provincia):
        self.__provincia = provincia

# Uso
provincia = Provincia("San Juan", 681055)
gobernador = Gobernador(27888111, "Marcelo Orrego")
provincia.set_gobernador_bidireccional(gobernador)
```

### Asociación con cardinalidad N

Cuando una clase se relaciona con múltiples instancias de otra, se usa una colección:

```python
class Factura:
    def __init__(self, numero, fecha, importe, cuit, denominacion):
        self.__numero = numero
        self.__fecha = fecha
        self.__importe = importe
        self.__cuit = cuit
        self.__denominacion = denominacion

    def get_total(self):
        return self.__importe

class Cliente:
    def __init__(self, id_cliente, nombre, direccion):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__direccion = direccion
        self.__facturas = []  # Colección de objetos asociados

    def add_factura(self, factura):
        self.__facturas.append(factura)

    def get_total_compras(self):
        return sum(f.get_total() for f in self.__facturas)
```

El `Cliente` puede tener múltiples `Factura` asociadas. Ambos existen independientemente.

## Clase Asociación

La [[Programacion Orientada a Objetos#Clase Asociación|clase asociación]] surge cuando la relación entre dos objetos tiene **atributos propios**. Por cada par de objetos relacionados, existe una **única instancia** de la clase asociación.

El ejemplo clásico: entre `RegistroCivil` y `Persona` existe un `ActaNacimiento`. Para cada combinación (registro, persona), hay exactamente un acta.

```python
class Persona:
    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    def __str__(self):
        return f"DNI: {self.__dni}\nApellido: {self.__apellido}, Nombre: {self.__nombre}"

class ActaNacimiento:
    """Clase asociación: une Persona con RegistroCivil"""

    def __init__(self, nro_acta, nro_libro, fecha_inscripcion, persona, registro_civil):
        self.__numero_acta = nro_acta
        self.__numero_libro = nro_libro
        self.__fecha_inscripcion = fecha_inscripcion
        self.__persona = persona
        self.__registro_civil = registro_civil

    def __str__(self):
        return (f"Fecha: {self.__fecha_inscripcion}\n"
                f"Libro: {self.__numero_libro}, Acta: {self.__numero_acta}\n"
                f"{self.__persona}")

class RegistroCivil:
    __acta_actual = 100
    __libro_actual = 5

    def __init__(self, denominacion, domicilio):
        self.__denominacion = denominacion
        self.__domicilio = domicilio
        self.__actas = []

    @classmethod
    def get_nueva_acta(cls):
        cls.__acta_actual += 1
        return cls.__acta_actual

    def inscribir_persona(self, persona, fecha):
        """Crea el ActaNacimiento que vincula persona con este registro"""
        nro_acta = self.get_nueva_acta()
        acta = ActaNacimiento(nro_acta, self.__libro_actual, fecha, persona, self)
        self.__actas.append(acta)
        return acta

    def mostrar_actas(self):
        for acta in self.__actas:
            print(acta)

# Uso
registro = RegistroCivil("Registro Cuarta Zona", "Av. Córdoba y Urquiza")
persona1 = Persona(20112113, "Carlos", "Vargas")
persona2 = Persona(3444222, "Anastacia", "Arboleda")

registro.inscribir_persona(persona1, "28/01/2019")
registro.inscribir_persona(persona2, "28/01/2019")
registro.mostrar_actas()
```

La clase `ActaNacimiento` no pertenece a `Persona` ni a `RegistroCivil`. Es una **entidad independiente** que materializa la relación.

## Clase que Modela la Asociación

A diferencia de la clase asociación, una [[Programacion Orientada a Objetos#Clase que Modela la Asociación|clase que modela la asociación]] permite **múltiples instancias** para un mismo par de objetos relacionados.

Ejemplo: un `Medico` atiende a un `Paciente` múltiples veces. Cada atención genera una `Prescripcion` diferente.

```python
class Medico:
    def __init__(self, dni, matricula, especialidad, apellido, nombre):
        self.__dni = dni
        self.__matricula = matricula
        self.__especialidad = especialidad
        self.__apellido = apellido
        self.__nombre = nombre
        self.__prescripciones = []

    def add_prescripcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)

class Paciente:
    def __init__(self, dni, apellido, nombre):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__prescripciones = []

    def add_prescripcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)

class Prescripcion:
    """Modela la relación Medico-Paciente. Puede haber múltiples por par."""

    def __init__(self, fecha, diagnostico, medicacion, presentacion, dosis, medico, paciente):
        self.__fecha = fecha
        self.__diagnostico = diagnostico
        self.__medicacion = medicacion
        self.__presentacion = presentacion
        self.__dosis = dosis
        self.__medico = medico
        self.__paciente = paciente

        # Actualizar ambas partes de la relación
        self.__medico.add_prescripcion(self)
        self.__paciente.add_prescripcion(self)

# Uso: mismo médico y paciente, múltiples prescripciones
medico = Medico(19327881, 1125, "Clínica Médica", "González", "Jorge")
paciente = Paciente(14555699, "Vergara", "Andrea")

prescripcion1 = Prescripcion("11/01/2025", "Rinitis", "Hexaler", "10 comprimidos", "1 por día", medico, paciente)
prescripcion2 = Prescripcion("29/01/2025", "Otitis", "Ciriax Gotas", "envase 10 ml", "2 gotas cada 8h", medico, paciente)
```

Cada `Prescripcion` es un objeto distinto que vincula al mismo par (Medico, Paciente).

## Agregación

La [[Programacion Orientada a Objetos#Agregación propiamente dicha|agregación]] es una relación **todo/parte** donde:
- El contenedor tiene referencias a los contenidos
- Los objetos contenidos pueden existir independientemente
- La destrucción del contenedor **NO** implica la destrucción de los contenidos
- Los ciclos de vida son independientes

Es una relación "tiene-un" débil: un `Pedido` tiene `Bebida`s y `Plato`s, pero esos objetos existían antes y seguirán existiendo después.

```python
class Bebida:
    def __init__(self, denominacion, presentacion, precio):
        self.__denominacion = denominacion
        self.__presentacion = presentacion
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def get_denominacion(self):
        return self.__denominacion

class Plato:
    def __init__(self, descripcion, precio):
        self.__descripcion = descripcion
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def get_descripcion(self):
        return self.__descripcion

class Mozo:
    def __init__(self, id_mozo, apellido, nombre):
        self.__id_mozo = id_mozo
        self.__apellido = apellido
        self.__nombre = nombre

class Pedido:
    """Contenedor: agrega Bebidas y Platos"""

    __contador_pedidos = 0

    def __init__(self, numero_mesa, mozo, bebida=None, plato=None):
        self.__id_pedido = None
        self.__numero_mesa = numero_mesa
        self.__mozo = mozo  # Asociación: el mozo existe independientemente
        self.__bebidas = []  # Agregación: referencias a bebidas existentes
        self.__platos = []   # Agregación: referencias a platos existentes

        if bebida:
            self.add_bebida(bebida, 1)
        if plato:
            self.add_plato(plato, 1)

    def add_bebida(self, bebida, cantidad):
        """Agrega referencias a bebidas existentes"""
        for _ in range(cantidad):
            self.__bebidas.append(bebida)  # No creamos la bebida, solo la referenciamos

    def add_plato(self, plato, cantidad):
        """Agrega referencias a platos existentes"""
        for _ in range(cantidad):
            self.__platos.append(plato)

    def cerrar_pedido(self):
        self.__class__.__contador_pedidos += 1
        self.__id_pedido = self.__class__.__contador_pedidos

        total = 0
        print(f"Pedido número: {self.__id_pedido}")
        print("Bebidas:")
        for bebida in self.__bebidas:
            print(f"  {bebida.get_denominacion():20s} {bebida.get_precio():8.2f}")
            total += bebida.get_precio()
        print("Platos:")
        for plato in self.__platos:
            print(f"  {plato.get_descripcion():20s} {plato.get_precio():8.2f}")
            total += plato.get_precio()
        print(f"Total: {total:8.2f}")

# Uso: los objetos se crean fuera del Pedido
bebida1 = Bebida("Coca cola", "1/2 litro", 4000)
bebida2 = Bebida("Aquarius", "1/2 litro", 3500)
plato1 = Plato("Lomo especial", 13250)
mozo = Mozo(1, "López", "Carlos")

pedido1 = Pedido(1, mozo, bebida1, plato1)
pedido1.add_bebida(bebida2, 2)
pedido1.cerrar_pedido()

del pedido1  # El pedido se destruye...

# ...pero las bebidas y platos siguen existiendo
print(bebida1.get_denominacion())  # "Coca cola" - sigue vivo
print(plato1.get_descripcion())    # "Lomo especial" - sigue vivo
```

**Clave**: `Bebida`, `Plato` y `Mozo` se crean **fuera** de `Pedido`. `Pedido` solo guarda referencias. Si `Pedido` se destruye, los otros objetos siguen existiendo.

## Composición

La [[Programacion Orientada a Objetos#Composición|composición]] es la forma más fuerte de agregación:
- El contenedor **crea** los objetos contenidos
- Los objetos contenidos **no tienen sentido** fuera del contenedor
- La destrucción del contenedor **implica** la destrucción de los contenidos
- Los ciclos de vida están fuertemente acoplados

Es una relación "tiene-un" fuerte: un `Profesor` tiene una `CuentaCampus`, y esa cuenta no tiene razón de existir sin el profesor.

```python
class CuentaCampus:
    """Clase contenido: pertenece exclusivamente a un Profesor"""

    __dominio = "@unsj-cuim.edu.ar"
    __id_cuenta = 0

    def __init__(self, nombre, apellido, dni):
        self.__class__.__id_cuenta += 1 # Se podria hacer con un @classmethod
        self.__id = self.__class__.__id_cuenta
        self.__usuario = f"{nombre.lower()}.{apellido.lower()}"
        self.__email = self.__usuario + self.__dominio
        self.__clave = str(dni)  # Clave por defecto: DNI

    def get_email(self):
        return self.__email

    def set_clave(self, nueva_clave):
        self.__clave = nueva_clave

class Profesor:
    """Clase contenedora: crea y posee CuentaCampus"""

    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        # La cuenta se crea DENTRO del profesor
        self.__cuenta = CuentaCampus(nombre, apellido, dni)

    def get_email(self):
        return self.__cuenta.get_email()

    def cambiar_clave(self, nueva_clave):
        self.__cuenta.set_clave(nueva_clave)

# Uso
profesor = Profesor(12345678, "Juan", "Pérez")
print(profesor.get_email())  # juan.perez@unsj-cuim.edu.ar

del profesor  # Al destruir el profesor...
# ...la CuentaCampus también se destruye (no hay referencia externa)
```

**Clave**: `CuentaCampus` se crea **dentro** de `Profesor.__init__`. No hay forma de acceder a la cuenta desde afuera excepto a través del profesor. Si el profesor se elimina, la cuenta desaparece con él.

### Diferencia práctica: quién crea y quién destruye

| Relación | ¿Quién crea? | ¿Quién destruye? | Ciclo de vida |
|----------|--------------|------------------|---------------|
| Asociación | Cualquiera | Independiente | Independiente |
| Agregación | Fuera del contenedor | Independiente | Independiente |
| Composición | Dentro del contenedor | El contenedor | Acoplado |

```python
# Asociación: objetos independientes
gobernador = Gobernador(...)
provincia = Provincia(...)
provincia.set_gobernador(gobernador)  # Solo referencia

# Agregación: objetos creados afuera
bebida = Bebida("Coca", "500ml", 1000)
pedido = Pedido(mozo, mesa)
pedido.add_bebida(bebida)  # Referencia a objeto existente

# Composición: objeto creado adentro
profesor = Profesor(dni, nombre, apellido)  # Crea CuentaCampus internamente
# No hay forma de crear CuentaCampus sin Profesor
```

## Cuándo usar cada relación

| Relación | Cuándo usar |
|----------|-------------|
| **Asociación** | Los objetos colaboran pero son independientes. Ej: Cliente - Factura |
| **Clase Asociación** | La relación tiene atributos y es única por par de objetos. Ej: Persona - ActaNacimiento |
| **Clase que modela asociación** | La relación tiene atributos y puede repetirse. Ej: Médico - Prescripción - Paciente |
| **Agregación** | El contenedor usa objetos que existen por sí mismos. Ej: Pedido - Bebida |
| **Composición** | El contenido no tiene sentido sin el contenedor. Ej: Profesor - CuentaCampus |

## Resumen

```python
# Asociación: referencia simple, vidas independientes
class A:
    def __init__(self):
        self.b = None  # A conoce a B

# Agregación: colección de referencias, vidas independientes
class Contenedor:
    def __init__(self):
        self.partes = []  # Referencias a objetos creados afuera

    def add_parte(self, parte):
        self.partes.append(parte)  # Solo guarda referencia

# Composición: el contenedor crea y posee las partes
class Contenedor:
    def __init__(self):
        self.parte = Parte()  # Crea la parte internamente
```

---
__TE SIENTES DETERMINADO__