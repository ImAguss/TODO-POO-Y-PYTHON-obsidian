# POO y Python

## Convenciones de Enlaces

Este Proyecto distingue entre dos tipos de conexiones:

### Derivación `[[Nota]]`

Se usa cuando una nota **genera o desarrolla** otra nota. Es una relación jerárquica padre→hijo.

```
Funciones en Python → deriva en → [[Funciones Nativas en Python]]
```

### Relación `[[Nota#Sección|Texto]]`

Se usa para conectar conceptos **relacionados** entre notas. Es una conexión transversal. Siempre incluye el pipe `|` para personalizar el texto visible.

```
Clases en Python --se relaciona con--> [[NameSpaces en Python#Namespace de una clase|namespace de la clase]]
```

## Atajos de Obsidian

### Atajos Nativos Esenciales

| Atajo                  | Acción                               |
| ---------------------- | ------------------------------------ |
| `Ctrl + O`             | Abrirquick switcher (buscar notas)   |
| `Ctrl + N`             | Nueva nota                           |
| `Ctrl + P`             | Command palette                      |
| `Alt + E`              | Alternar modo edición/lectura        |
| `Ctrl + Shift + F`     | Buscar en todos los archivos         |
| `Ctrl + G`             | Abrir graph view                     |
| `Ctrl + [`             | Retroceder en el historial           |
| `Ctrl + ]`             | Avanzar en el historial              |
| `Ctrl + Click`         | Abrir enlace en nuevo panel          |
| `Ctrl + Shift + Click` | Abrir enlace en panel derecho        |
| `Alt + Click`          | Abrir enlace en nuevo panel vertical |
| `Ctrl + W`             | Cerrar panel actual                  |
| `Ctrl + T`             | Abrir nueva pestaña                  |
| `Ctrl + 1-9`           | Cambiar a pestaña 1-9                |

### Formateo

| Atajo | Acción |
|-------|--------|
| `Ctrl + B` | **Negrita** |
| `Ctrl + I` | *Cursiva* |
| `Ctrl + K` | Insertar enlace externo |
| `` Ctrl + ` `` | Código en línea |
| `Ctrl + Shift + C` | Bloque de código |
| `Ctrl + Shift + M` | Insertar matemáticas |

### Listas y Tareas

| Atajo | Acción |
|-------|--------|
| `Ctrl + L` | Insertar lista con checkbox |
| `Ctrl + Enter` | Toggle checkbox |
| `Tab` | Indentar |
| `Shift + Tab` | Desindentar |

### Navegación

| Atajo | Acción |
|-------|--------|
| `Ctrl + Alt + ←` | Retroceder |
| `Ctrl + Alt + →` | Avanzar |
| `Ctrl + Home` | Ir al inicio del documento |
| `Ctrl + End` | Ir al final del documento |

### Paneles

| Atajo | Acción |
|-------|--------|
| `Ctrl + \` | Toggle sidebar izquierdo |
| `Ctrl + Shift + E` | Toggle file explorer |
| `Ctrl + Shift + G` | Toggle graph view |

## Plugins Instalados

| Plugin | Descripción |
|--------|-------------|
| **flashcards-obsidian** | Repetición espaciada con flashcards |
| **obsidian-plugin-toc** | Generación de tabla de contenidos |
| **auto-hide-cursor** | Ocultar cursor automáticamente |
| **obsidian-hider** | Ocultar elementos de la UI |
| **obsidian-style-settings** | Personalización de temas |

## Formato de las Notas

### Frontmatter YAML

```yaml
---
estado: Terminado|En Progreso|Borrador
tags:
  - tag1
  - tag2
proyecto: nombre-proyecto
Creacion: YYYY-MM-DDTHH:MM:SS
Revision: YYYY-MM-DDTHH:MM:SS
---
```

### Cierre de Nota

Las notas finalizan con:

```
---
__TE SIENTES DETERMINADO__
```

## Temas Principales

### Python

- **Fundamentos**: Sintaxis, variables, condicionales, estructuras iterativas
- **Estructuras de datos**: Listas, tuplas, sets, diccionarios
- **Funciones**: Definición, lambdas, decoradores, iteradores
- **POO**: Clases, métodos, herencia, encapsulación, relaciones entre clases
- **Avanzado**: NameSpaces, scope, gestión de memoria, módulos

### Estructuras de Datos y Algoritmos

- Arrays, listas enlazadas, tablas hash
- Pilas y colas
- Recursión
- Algoritmos de ordenamiento

## Filosofía

Este proyecto sigue el principio de **atomicidad**: cada nota contiene una idea principal clara y concisa. Las conexiones entre notas crean una red de conocimiento que facilita el descubrimiento de relaciones inesperadas y la síntesis de nuevas ideas.

---

*Construido con [Obsidian](https://obsidian.md)*
