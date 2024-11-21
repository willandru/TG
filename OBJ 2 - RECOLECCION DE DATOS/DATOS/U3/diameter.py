import cv2
import numpy as np

# Abre el video
video_path = '18-10-24_15-25-20_VIDEO_OJO_UX.avi'
cap = cv2.VideoCapture(video_path)

# Verifica si el video fue cargado correctamente
if not cap.isOpened():
    print("Error al abrir el video")

# Definir las propiedades del nuevo video (output)
output_path = 'video_con_circulos.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codificador para el video de salida
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Lista para almacenar los diámetros
diameters = []

# Procesa cada frame
while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # Sale cuando se terminen los frames

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Recorta una región de interés (ROI) en el centro del frame
    crop_size = 30
    center_x, center_y = gray.shape[1] // 2, gray.shape[0] // 2
    x_start = center_x - crop_size
    y_start = center_y - crop_size
    cropped_img = gray[y_start:y_start + 2 * crop_size, x_start:x_start + 2 * crop_size]

    # Aplica un filtro de suavizado
    cropped_img = cv2.medianBlur(cropped_img, 5)

    # Detecta círculos usando la Transformada de Hough
    circles = cv2.HoughCircles(cropped_img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=0, maxRadius=0)
    
    # Si se detectan círculos, dibújalos en el frame original ajustando las coordenadas
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Ajusta las coordenadas del círculo para dibujarlas en el frame original
            center = (i[0] + x_start, i[1] + y_start)
            radius = i[2]
            # Guarda el diámetro (2 * radio)
            diameters.append(2 * radius)
            # Dibuja el círculo externo
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            # Dibuja el centro del círculo
            cv2.circle(frame, center, 2, (0, 0, 255), 3)

    # Escribe el frame procesado en el nuevo video
    out.write(frame)

    # Muestra el frame procesado (opcional)
    cv2.imshow('Frame con Círculos Detectados', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera recursos
cap.release()
out.release()
cv2.destroyAllWindows()

# Imprime o guarda los diámetros
print("Diámetros detectados:", diameters)
