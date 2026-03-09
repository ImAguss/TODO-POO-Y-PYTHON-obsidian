---
estado: Terminado
tags:
  - aprendizaje
  - programacion
  - python
  - testing
proyecto: aprendizaje-python
Creacion: 2026-03-04T14:30:00
Revision: 2026-03-07T15:48:00
---
# Testing con unittest en Python

El **testing** es una práctica fundamental en el desarrollo de software. Consiste en verificar que el código funciona como se espera y que los cambios no rompen funcionalidad existente.

Las **pruebas unitarias** se enfocan en probar la menor cantidad de código posible: una función, un método, o una clase de forma aislada.

Python incluye en su biblioteca estándar el módulo `unittest`, inspirado en el framework JUnit de Java.

## Estructura básica de un test

```python
import unittest

class TestNumeros(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

    def test_int_str(self):
        self.assertEqual(1, '1')

if __name__ == '__main__':
    unittest.main()
```

Ejecutar este código produce:

```
F.
======================================================================
FAIL: test_int_str (__main__.TestNumeros)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_numeros.py", line 8, in test_int_str
    self.assertEqual(1, '1')
AssertionError: 1 != '1'

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

### Convenciones importantes

| Convención | Descripción |
|------------|-------------|
| Clase hereda de `unittest.TestCase` | Obligatorio para usar aserciones |
| Métodos comienzan con `test_` | Solo estos métodos se ejecutan como tests |
| Archivo nombrado `test_*.py` | El descubridor automático los encuentra |

## Métodos de aserción

`TestCase` proporciona métodos para comparar valores:

### Aserciones básicas

| Método | Verifica |
|--------|----------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` |
| `assertIsNot(a, b)` | `a is not b` |
| `assertIsNone(x)` | `x is None` |
| `assertIsNotNone(x)` | `x is not None` |

### Aserciones con comparaciones

| Método | Verifica |
|--------|----------|
| `assertGreater(a, b)` | `a > b` |
| `assertGreaterEqual(a, b)` | `a >= b` |
| `assertLess(a, b)` | `a < b` |
| `assertLessEqual(a, b)` | `a <= b` |

### Aserciones con colecciones

| Método | Verifica |
|--------|----------|
| `assertIn(a, b)` | `a in b` |
| `assertNotIn(a, b)` | `a not in b` |
| `assertCountEqual(a, b)` | Mismos elementos, sin importar orden |

### Aserciones con excepciones

| Método | Verifica |
|--------|----------|
| `assertRaises(Error, func, *args)` | `func(*args)` lanza `Error` |
| `assertRaisesRegex(Error, pattern, func)` | El mensaje coincide con el patrón |

### Aserciones con aproximaciones

| Método | Verifica |
|--------|----------|
| `assertAlmostEqual(a, b)` | `round(a - b, 7) == 0` |
| `assertNotAlmostEqual(a, b)` | No aproximadamente igual |

### Ejemplo completo

```python
import unittest

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def es_par(self, n):
        return n % 2 == 0

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar_positivos(self):
        resultado = self.calc.sumar(2, 3)
        self.assertEqual(resultado, 5)

    def test_sumar_negativos(self):
        self.assertEqual(self.calc.sumar(-1, -2), -3)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
        self.assertAlmostEqual(self.calc.dividir(1, 3), 0.333, places=2)

    def test_dividir_por_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_es_par(self):
        self.assertTrue(self.calc.es_par(4))
        self.assertFalse(self.calc.es_par(7))

if __name__ == '__main__':
    unittest.main()
```

## Setup y Teardown

Para pruebas que requieren configuración previa o limpieza posterior, `TestCase` proporciona métodos especiales:

### Nivel de método

```python
class TestBaseDeDatos(unittest.TestCase):

    def setUp(self):
        """Se ejecuta ANTES de cada método de test."""
        self.conn = crear_conexion()
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Se ejecuta DESPUÉS de cada método de test."""
        self.cursor.close()
        self.conn.close()

    def test_insertar(self):
        self.cursor.execute("INSERT INTO usuarios VALUES (1, 'Juan')")
        self.conn.commit()
        # tearDown cerrará la conexión automáticamente

    def test_consultar(self):
        # setUp creó una conexión nueva
        self.cursor.execute("SELECT * FROM usuarios")
        resultados = self.cursor.fetchall()
        self.assertEqual(len(resultados), 0)  # Base limpia para cada test
```

### Nivel de clase

```python
class TestConRecursoCostoso(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Se ejecuta UNA VEZ antes de todos los tests de la clase."""
        cls.recurso_costoso = crear_recurso_lento()

    @classmethod
    def tearDownClass(cls):
        """Se ejecuta UNA VEZ después de todos los tests de la clase."""
        cls.recurso_costoso.liberar()

    def test_1(self):
        # Usa cls.recurso_costoso
        pass

    def test_2(self):
        # Usa el mismo recurso (no se recrea)
        pass
```

| Método | Momento de ejecución |
|--------|---------------------|
| `setUp()` | Antes de cada test |
| `tearDown()` | Después de cada test |
| `setUpClass()` | Una vez antes de todos los tests |
| `tearDownClass()` | Una vez después de todos los tests |

## Mensajes personalizados en aserciones

Todos los métodos de aserción aceptan un mensaje personalizado:

```python
def test_edad_usuario(self):
    usuario = Usuario(nombre="Juan", edad=25)
    self.assertGreater(usuario.edad, 0, "La edad debe ser positiva")
    self.assertLess(usuario.edad, 150, "La edad debe ser realista")
```

## Skip tests: deshabilitar pruebas

A veces necesitas saltar tests temporalmente:

```python
import unittest
import sys

class TestCondicional(unittest.TestCase):

    @unittest.skip("Funcionalidad no implementada aún")
    def test_futura(self):
        self.assertEqual(1, 2)  # Nunca se ejecuta

    @unittest.skipIf(sys.version_info < (3, 10), "Requiere Python 3.10+")
    def test_python_310(self):
        # Solo se ejecuta en Python 3.10+
        pass

    @unittest.skipUnless(sys.platform == "linux", "Solo en Linux")
    def test_solo_linux(self):
        # Solo se ejecuta en Linux
        pass

    @unittest.expectedFailure
    def test_falla_esperadamente(self):
        # Si falla, se cuenta como éxito
        # Si pasa, se cuenta como fallo inesperado
        self.assertEqual(1, 2)
```

## Organizar tests en suites

Puedes agrupar tests manualmente:

```python
import unittest

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(1 + 1, 2)

class TestResta(unittest.TestCase):
    def test_resta_positivos(self):
        self.assertEqual(5 - 3, 2)

# Crear suite manualmente
suite = unittest.TestSuite()
suite.addTest(TestSuma('test_suma_positivos'))
suite.addTest(TestResta('test_resta_positivos'))

# Ejecutar suite
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```

## Descubrimiento automático de tests

`unittest` puede descubrir y ejecutar todos los tests en un directorio:

```bash
# Descubre tests en el directorio actual
python -m unittest discover

# Especificar directorio y patrón
python -m unittest discover -s tests -p "test_*.py"

# Con verbose
python -m unittest discover -v
```

Estructura típica de proyecto:

```
proyecto/
├── src/
│   └── calculadora.py
└── tests/
    ├── __init__.py
    ├── test_calculadora.py
    └── test_otra_cosa.py
```

## Desarrollo guiado por tests (TDD)

TDD es una metodología donde el test se escribe **antes** que el código:

### Ciclo TDD

1. **Red**: Escribe un test que falla (porque el código no existe)
2. **Green**: Escribe el código mínimo para que el test pase
3. **Refactor**: Mejora el código manteniendo el test pasando

### Ejemplo de ciclo TDD

```python
# Paso 1: RED - Test que falla
class TestValidador(unittest.TestCase):
    def test_email_valido(self):
        validador = ValidadorEmail()
        self.assertTrue(validador.es_valido("usuario@dominio.com"))
        self.assertFalse(validador.es_valido("correo_sin_arroba"))

# Ejecutar test: FAILS - ValidadorEmail no existe

# Paso 2: GREEN - Código mínimo
import re

class ValidadorEmail:
    def es_valido(self, email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(patron, email))

# Ejecutar test: PASSES

# Paso 3: REFACTOR - Mejorar si es necesario
# El código funciona, quizás agregar más tests para edge cases
```

### Ventajas de TDD

| Ventaja | Descripción |
|---------|-------------|
| Diseño guiado | Los tests definen la interfaz antes de implementar |
| Documentación viva | Los tests documentan el comportamiento esperado |
| Confianza en refactoring | Los tests detectan regresiones |
| Menos bugs | Se piensa en los casos límite desde el inicio |

## Buenas prácticas

### Un test, una cosa

```python
# MAL: Un test verifica muchas cosas
def test_usuario(self):
    u = Usuario("Juan")
    self.assertEqual(u.nombre, "Juan")
    self.assertTrue(u.activo)
    self.assertEqual(u.permisos, [])

# BIEN: Un test por verificación
def test_nombre_usuario(self):
    u = Usuario("Juan")
    self.assertEqual(u.nombre, "Juan")

def test_usuario_activo_por_defecto(self):
    u = Usuario("Juan")
    self.assertTrue(u.activo)

def test_usuario_sin_permisos(self):
    u = Usuario("Juan")
    self.assertEqual(u.permisos, [])
```

### Tests independientes

```python
# MAL: Tests dependen entre sí
class TestMal(unittest.TestCase):
    def test_crear(self):
        self.usuario = Usuario("Juan")  # Guarda en self
        self.assertEqual(self.usuario.nombre, "Juan")

    def test_modificar(self):
        self.usuario.nombre = "Pedro"  # Depende de test_crear
        self.assertEqual(self.usuario.nombre, "Pedro")

# BIEN: Cada test es independiente
class TestBien(unittest.TestCase):
    def setUp(self):
        self.usuario = Usuario("Juan")  # Nuevo para cada test

    def test_nombre_inicial(self):
        self.assertEqual(self.usuario.nombre, "Juan")

    def test_modificar_nombre(self):
        self.usuario.nombre = "Pedro"
        self.assertEqual(self.usuario.nombre, "Pedro")
```

### Nombres descriptivos

```python
# MAL: Nombres genéricos
def test_1(self): pass
def test_funcion(self): pass

# BIEN: Nombres que describen el escenario
def test_sumar_dos_numeros_positivos(self): pass
def test_sumar_numero_negativo_y_positivo(self): pass
def test_sumar_con_cero(self): pass
def test_sumar_lanza_error_con_strings(self): pass
```

### Probar casos límite

```python
class TestDivision(unittest.TestCase):
    def test_division_normal(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_division_por_cero(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_division_negativos(self):
        self.assertEqual(dividir(-10, 2), -5)

    def test_division_cero_numerador(self):
        self.assertEqual(dividir(0, 5), 0)

    def test_division_resultado_decimal(self):
        self.assertAlmostEqual(dividir(7, 3), 2.333, places=2)
```

## Ejecutar tests

```bash
# Ejecutar un archivo específico
python -m unittest test_calculadora.py

# Ejecutar una clase específica
python -m unittest test_calculadora.TestCalculadora

# Ejecutar un test específico
python -m unittest test_calculadora.TestCalculadora.test_sumar_positivos

# Verbosidad (muestra nombres de tests)
python -m unittest test_calculadora.py -v

# Descubrir todos los tests
python -m unittest discover
```

## Resumen

| Concepto | Implementación |
|----------|---------------|
| Clase de test | `class TestX(unittest.TestCase)` |
| Método de test | `def test_algo(self):` |
| Aserciones | `self.assertEqual()`, `self.assertTrue()`, etc. |
| Setup por test | `def setUp(self):` |
| Teardown por test | `def tearDown(self):` |
| Setup por clase | `@classmethod def setUpClass(cls):` |
| Saltar test | `@unittest.skip("motivo")` |
| Ejecutar | `python -m unittest discover` |

---
__TE SIENTES DETERMINADO__