import cv2
import pygame

# Inicializar Pygame para las alertas de audio
pygame.init()

# Cargar el archivo de sonido para la alarma
pygame.mixer.music.load("alarma.mp3") # Reemplazar "alarma.mp3" con la ruta del archivo de sonido

# Función para mostrar una alerta sonora
def show_alert():
 pygame.mixer.music.play() # Reproduce el sonido de la alarma

# Cargar clasificadores pre-entrenados para detectar la cara y los ojos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Inicializar la captura de vídeo desde la webcam
cap = cv2.VideoCapture(0)

# Inicializar el contador para los ojos cerrados
closed_eyes_count = 0

# Bucle infinito para procesar cada fotograma de la webcam
while True:
 ret, frame = cap.read() # Leer un fotograma desde la webcam
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convertir el fotograma a escala de grises
 faces = face_cascade.detectMultiScale(gray, 1.3, 5) # Detectar caras en el fotograma

 # Iterar sobre cada cara detectada
 for (x, y, w, h) in faces:
 cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Dibujar un rectángulo alrededor de la cara
 roi_gray = gray[y:y+h, x:x+w] # Extraer la región de interés (ROI) donde se detectaron los ojos
 eyes = eye_cascade.detectMultiScale(roi_gray) # Detectar ojos en la ROI

 # Si no se detectan ojos, incrementar el contador
 if len(eyes) == 0:
 closed_eyes_count += 1
 print(f"Ojos cerrados, contador: {closed_eyes_count}") # Impresión de depuración
 else:
 closed_eyes_count = 0 # Reiniciar el contador si se detectan ojos abiertos

 # Si el contador alcanza 3, activar la alarma
 if closed_eyes_count >= 3:
 print("Activando alarma...") # Impresión de depuración
 cv2.putText(frame, "Durmiendo", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
 show_alert() # Llamar a la función para mostrar la alarma
 closed_eyes_count = 0 # Reiniciar el contador de ojos cerrados

 # Mostrar el fotograma con la cara y los ojos detectados
 cv2.imshow("Deteccion de sueno", frame)

 # Salir del bucle si se presiona la tecla 'q'
 if cv2.waitKey(1) & 0xFF == ord('q'):
 break

# Liberar la captura de video y destruir todas las ventanas de OpenCV
cap.release()
cv2.destroyAllWindows()
