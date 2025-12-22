# Plan de Pruebas – Sistema de Gestión de Tareas  
**Proyecto académico – UNIMINUTO**

Este repositorio contiene el Plan de Pruebas del Sistema de Gestión de Tareas solicitado en el Anexo II, aplicando pruebas manuales, automatizadas (simuladas) y gestión de defectos utilizando GitHub como herramienta principal de control y seguimiento.

---

## 1. Objetivo del plan de pruebas
Garantizar que las funcionalidades del sistema cumplan con los requisitos descritos en el Anexo II mediante la aplicación de pruebas manuales, diseño de pruebas automatizadas, documentación de resultados y registro de incidentes.

---

## 2. Alcance
El plan cubre las siguientes funcionalidades clave del sistema:

- Registro de usuarios  
- Inicio de sesión  
- Creación de tareas  
- Edición de tareas  
- Archivado de tareas  
- Asignación de tareas  
- Filtrado de tareas  
- Búsqueda de tareas  
- Visualización de tareas completadas  
- Actualización del perfil del usuario

---

## 3. Tipos de pruebas realizadas

### 3.1 Pruebas manuales
Las pruebas manuales fueron documentadas como **Issues**, utilizando la siguiente estructura:

- Precondiciones  
- Pasos de prueba  
- Datos de prueba  
- Resultado esperado  

Se crearon **10 casos de prueba (CP01 – CP10)**, cada uno etiquetado y asignado al milestone del proyecto.

### 3.2 Pruebas automatizadas (diseño simulado)
En la carpeta `/automation/` se incluyen ejemplos simulados de:

- Pruebas unitarias  
- Pruebas de integración  
- Pruebas E2E simuladas con Selenium WebDriver  

Estos archivos muestran cómo se estructurarían las automatizaciones en un proyecto real.

### 3.3 Registro de defectos
Se crearon **3 bugs simulados** documentados mediante Issues:

- Validación incorrecta de campos  
- Fallos en filtros  
- Fallos en actualización de foto de perfil  

Cada bug contiene:

- Severidad  
- Prioridad  
- Pasos para reproducir  
- Resultado esperado  
- Resultado obtenido  

---

## 4. Gestión mediante GitHub

Se utilizaron varias funcionalidades de GitHub:

### ✔ Issues  
Para documentar casos de prueba y defectos.

### ✔ Labels  
Clasificación por tipo de prueba, severidad y estado.

### ✔ Milestones  
Agrupación del ciclo de pruebas del proyecto.

### ✔ Projects (Kanban board)  
Flujo de trabajo del proceso QA:  
Backlog → Ready → In Progress → In Review → Done

### ✔ Readme  
Documentación general del plan de pruebas.

---

## 5. Evidencia incluida en el repositorio

- 10 casos de prueba manuales  
- 3 bugs simulados  
- Tablero Kanban con estados de ejecución  
- Archivos de automatización simulada  
- Labels configurados  
- Milestone creado y asignado  

---

## 6. Conclusiones

El uso de GitHub como herramienta de gestión permite:

- Organizar las fases de pruebas  
- Mantener trazabilidad completa  
- Documentar defectos y casos de prueba  
- Simular el proceso de QA de un proyecto profesional  
- Preparar el entorno para futuras automatizaciones reales

Este repositorio evidencia el cumplimiento del Anexo II y la correcta aplicación de procesos de pruebas manuales, automatizadas y de gestión.

---

## Autor
Repositorio creado por *Isabel Rojas* para la actividad académica del curso de **Pruebas de Software y Aseguramiento de la Calidad**.
