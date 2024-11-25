import cv2
import numpy as np

# Ruta del video
video_path = 'video_filled.avi'
original_video = "18-10-24_12-44-17_VIDEO_OJO_UX.avi"
cap = cv2.VideoCapture(video_path)

# Verifica si el video fue cargado correctamente
if not cap.isOpened():
    print("Error al abrir el video")
    exit()

# Lista para almacenar los diámetros detectados
diameters = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Suavizar la imagen para reducir ruido
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detectar círculos usando la Transformada de Hough
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=30,
                               param1=70, param2=15, minRadius=20, maxRadius=25)

    # Si se detectan círculos
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            radius = i[2]  # Radio del círculo
            diameter = 2 * radius  # Calcular el diámetro
            diameters.append(diameter)

            # Dibujar el círculo detectado en el frame
            cv2.circle(frame, (i[0], i[1]), radius, (0, 255, 0), 2)
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)  # Centro del círculo

    # Mostrar el frame procesado
    cv2.imshow('Detección de Círculos', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()

# Convertir los diámetros a una lista simple de enteros
diameters = list(map(int, diameters))

# Mostrar los diámetros detectados
print("Diámetros detectados:", diameters)
