# 1ro en cmd python3 -m pip install opencv-python
# https://github.com/opencv/opencv/tree/master/data/haarcascades
import cv2  # Importa la librería OpenCV para el procesamiento de imágenes

# para controlar arduino
# pip install pyserial


import serial  # Importa la librería PySerial para la comunicación con Arduino
import time  # Importa la librería time para manejar retardos

# Iniciar la conexión serial con Arduino en el puerto COM8 a 9600 baudios
arduino = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)  # Espera 2 segundos para asegurarse de que Arduino está listo

# Cargar el clasificador de rostros de OpenCV (modelo preentrenado Haarcascade)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Iniciar la captura de video desde la cámara (cámara 0 por defecto)
captura = cv2.VideoCapture(0)

# Variable para rastrear si anteriormente se detectó un rostro
rostro_detectado_anteriormente = False  

while True:
    # Capturar un fotograma de la cámara
    ret, img = captura.read()
    if not ret:  # Si no se pudo capturar el fotograma, salir del bucle
        break

    # Convertir la imagen a escala de grises para mejorar la detección de rostros
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en la imagen en escala de grises, los ultimos 2 parametros es para mejorar la deteccion
    # se puede cambiar esos valores si no funciona
    caras = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(caras) > 0:  # Si se detecta al menos un rostro
        if not rostro_detectado_anteriormente:  # Si antes no había rostro detectado
            print("Rostro detectado")  # Imprimir mensaje en la consola
            arduino.write(b'A')  # Enviar 'A' por el puerto serie a Arduino
            rostro_detectado_anteriormente = True  # Actualizar el estado

        # Dibujar rectángulos alrededor de los rostros detectados
        for (x, y, w, h) in caras:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    else:  # Si no se detecta ningún rostro
        if rostro_detectado_anteriormente:  # Si antes había un rostro detectado
            print("Rostro perdido")  # Imprimir mensaje en la consola
            arduino.write(b'B')  # Enviar 'B' por el puerto serie a Arduino
            rostro_detectado_anteriormente = False  # Actualizar el estado

    # Mostrar la imagen con los rectángulos en una ventana
    cv2.imshow('img', img)

    # Esperar 30ms por una tecla, si es ESC (código 27), salir del bucle
    key = cv2.waitKey(30)
    if key == 27:
        break

# Liberar la cámara y cerrar todas las ventanas de OpenCV
captura.release()
cv2.destroyAllWindows()

# Cerrar la conexión con Arduino
arduino.close()
