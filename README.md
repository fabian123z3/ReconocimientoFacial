# 📸 Sistema de Registro de Asistencia por Reconocimiento Facial

Este proyecto es un script en Python que utiliza la cámara web de tu computadora para realizar reconocimiento facial en tiempo real. Compara el rostro detectado con una base de datos local de imágenes de empleados y, si encuentra una coincidencia, registra automáticamente la hora de ingreso en un archivo CSV.

## ✨ Funcionalidades

- **Carga Dinámica de Datos**: Lee automáticamente todas las imágenes de la carpeta de empleados y usa los nombres de los archivos como los nombres de las personas.
- **Reconocimiento en Tiempo Real**: Captura una imagen directamente desde la cámara web (Webcam) para buscar coincidencias.
- **Tolerancia Ajustable**: Utiliza un umbral de distancia matemática (`0.6`) para determinar si un rostro coincide o si pertenece a un "desconocido".
- **Feedback Visual**: Si se reconoce a un empleado, abre una ventana mostrando la captura con un recuadro verde alrededor del rostro y el nombre de la persona.
- **Registro Automático**: Escribe el nombre del empleado y la hora exacta de su reconocimiento en un archivo `registro.csv`.

## 🛠️ Requisitos y Dependencias

Para ejecutar este proyecto, necesitas Python 3.x y las siguientes librerías. Puedes instalarlas ejecutando:

```bash
pip install opencv-python numpy face-recognition
