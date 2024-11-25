import cv2
import numpy as np

# Ruta del video
original_video = "18-10-24_12-44-17_VIDEO_OJO_UX.avi"
video_path = "video_umbralizado.avi"
output_path = "video_circular_mask.avi"

# Cargar el video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: No se pudo abrir el video.")
    exit()

# Obtener las propiedades del video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Crear el objeto para guardar el video procesado
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Parámetro para el diámetro del círculo de la máscara
circle_diameter = 55
circle_radius = circle_diameter // 2

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video o error al leer fotogramas.")
        break

    # Convertir a escala de grises (por si no lo está)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Invertir los valores de la imagen para que el objeto oscuro sea brillante
    inverted_frame = cv2.bitwise_not(gray_frame)

    # Calcular el centroide basado en la intensidad invertida
    height, width = inverted_frame.shape
    total_intensity = np.sum(inverted_frame)

    if total_intensity > 0:  # Evitar división por cero
        # Crear matrices de coordenadas (x, y)
        y_indices, x_indices = np.indices((height, width))
        center_x = int(np.sum(x_indices * inverted_frame) / total_intensity)
        center_y = int(np.sum(y_indices * inverted_frame) / total_intensity)
    else:
        center_x, center_y = width // 2, height // 2  # Centro geométrico si no hay intensidad

    # Crear una máscara circular basada en el centroide
    mask = np.zeros((height, width), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), circle_radius, 255, -1)  # Círculo blanco en el centro

    # Aplicar la máscara al fotograma original
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Convertir las áreas negras fuera del círculo a blanco
    white_background = np.full_like(frame, 255)
    final_frame = np.where(mask[:, :, None] == 0, white_background, masked_frame)

    # Mostrar y guardar el fotograma procesado
    cv2.imshow("Video con Máscara Circular", final_frame)
    out.write(final_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(30) == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video con máscara circular guardado en: {output_path}")
