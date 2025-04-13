# Gestor de Tareas

Este proyecto consiste en el desarrollo de una aplicación de línea de comandos para la gestión de tareas personales. El sistema permite al usuario cargar, visualizar, completar y guardar tareas, ofreciendo una experiencia funcional y simple.

## Finalidad del Proyecto

El objetivo principal de este proyecto es demostrar competencias técnicas en el desarrollo de aplicaciones en Python, haciendo uso de principios fundamentales de programación orientada a objetos, validación de entrada, manipulación de archivos JSON, y separación de responsabilidades mediante la modularización del código.

Este proyecto también sirve como muestra de buenas prácticas en el diseño de programas mantenibles y extensibles, aplicando principios de documentación y pruebas automatizadas.

## Conocimientos Demostrados

- Programación orientada a objetos (OOP)
- Estructuración modular del código
- Validación de datos de entrada
- Serialización y persistencia de datos con JSON
- Lectura y escritura de archivos
- Uso de `unittest` para pruebas automáticas
- Documentación con docstrings
- Gestión de versiones con Git y GitHub:
  - Uso de ramas separadas para cada módulo o funcionalidad
  - Commits descriptivos y ordenados
  - Pull Requests para revisión y seguimiento de cambios


## Precondiciones

- El archivo `tareas.json` debe existir o poder ser creado en el directorio raíz del proyecto.
- El usuario debe ingresar fechas en el formato **YYYY-MM-DD**; cualquier otro formato será rechazado.
- Las tareas nuevas deben tener una **descripción no vacía** para ser agregadas.
- El entorno debe permitir lectura y escritura en archivos para guardar el progreso.
- El sistema asume que los datos cargados desde el archivo `.json` están estructurados correctamente (según lo generado por `Tarea.to_dict()`).

## Postcondiciones

- Si se agrega una tarea válida, esta quedará registrada en memoria y se podrá guardar en `tareas.json`.
- Si se marca una tarea como completada, su estado se actualizará y aparecerá tachada al listar tareas.
- Si se guarda la sesión, el archivo `tareas.json` reflejará el estado actualizado del sistema.
- En caso de entrada inválida, el sistema notificará el error pero continuará funcionando sin interrupciones.

## 📌 Autor

> [**Axel Hernandez**](https://github.com/axelher006)  


