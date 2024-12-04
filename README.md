Este código utiliza OpenCV y Pygame para detectar el estado de los ojos de una persona en tiempo real mediante la webcam. Si detecta que los ojos están cerrados durante un periodo prolongado, activa una alarma sonora.

Resumen del Código
Funcionalidades principales
Detección de rostro y ojos

Usa clasificadores pre-entrenados de Haar Cascade (haarcascade_frontalface_default.xml y haarcascade_eye.xml).
Detecta rostros y ojos en los fotogramas capturados por la webcam.
Monitorización del estado de los ojos

Si no se detectan ojos en el rostro, incrementa un contador de ojos cerrados.
Si el contador alcanza un valor crítico (por ejemplo, 3), activa una alarma sonora y reinicia el contador.
Alarma sonora

Usa Pygame para reproducir un archivo de audio ("alarma.mp3") cuando se detecta somnolencia.
Interfaz en tiempo real

Muestra el video capturado por la webcam con rectángulos que marcan la detección de rostros y el estado de alerta.
Descripción del Flujo
Carga de modelos pre-entrenados
Se cargan los clasificadores de OpenCV para detección de rostros y ojos.
Captura de video
Se inicializa la captura de video desde la webcam con cv2.VideoCapture(0).
Procesamiento de cada fotograma
Se convierte el fotograma a escala de grises.
Se detectan caras y ojos en el fotograma.
Si no se detectan ojos en una cara, se incrementa el contador de ojos cerrados.
Activación de la alarma
Si el contador alcanza un umbral (3 ciclos consecutivos sin detectar ojos abiertos), se activa una alarma sonora.
Interfaz gráfica
Se dibujan rectángulos sobre las caras detectadas.
Se muestra un mensaje "Durmiendo" si se activa la alarma.
Salir del programa
El programa se detiene cuando el usuario presiona la tecla q.
Dependencias Requeridas
Bibliotecas

OpenCV: Para detección de caras y ojos.
Pygame: Para manejar la reproducción de audio.
Archivos Adicionales

alarma.mp3: Archivo de audio para la alarma sonora.
Modelos Haar Cascade:
haarcascade_frontalface_default.xml
haarcascade_eye.xml
