import cv2
import numpy as np

# Rutas del video
video_path = 'video_filled.avi'  # Procesado
original_video = '18-10-24_12-44-17_VIDEO_OJO_UX.avi'  # Original
output_video_path = 'video_with_detected_circles.avi'

# Cargar los videos
cap_processed = cv2.VideoCapture(video_path)
cap_original = cv2.VideoCapture(original_video)

# Verifica si los videos fueron cargados correctamente
if not cap_processed.isOpened() or not cap_original.isOpened():
    print("Error al abrir uno de los videos")
    exit()

# Obtener las propiedades del video original
frame_width = int(cap_original.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_original.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap_original.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Crear el objeto para guardar el video procesado
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

# Lista para almacenar los diámetros detectados
diameters = []

while True:
    # Leer frames de ambos videos
    ret_processed, frame_processed = cap_processed.read()
    ret_original, frame_original = cap_original.read()

    if not ret_processed or not ret_original:
        break

    # Convertir el fotograma procesado a escala de grises
    gray = cv2.cvtColor(frame_processed, cv2.COLOR_BGR2GRAY)

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
            diameter = 2 * int(radius)  # Convertir a entero normal
            diameters.append(diameter)

            # Dibujar el círculo detectado en el video original
            cv2.circle(frame_original, (i[0], i[1]), radius, (0, 255, 0), 2)
            cv2.circle(frame_original, (i[0], i[1]), 2, (0, 0, 255), 3)  # Centro del círculo

    # Escribir el frame procesado en el nuevo video
    out.write(frame_original)

    # Mostrar el frame procesado
    cv2.imshow('Detección de Círculos en el Video Original', frame_original)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap_processed.release()
cap_original.release()
out.release()
cv2.destroyAllWindows()

# Convertir los diámetros a una lista simple de enteros
diameters = list(map(int, diameters))

# Mostrar los diámetros detectados
print(diameters)
