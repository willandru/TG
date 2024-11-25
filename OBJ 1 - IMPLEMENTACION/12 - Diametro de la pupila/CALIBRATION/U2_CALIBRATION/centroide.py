import cv2
import numpy as np

# Ruta del video
video_path = "video_umbralizado.avi"
output_path = "video_centroide.avi"

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

    # Dibujar el centroide en el fotograma original
    output_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
    cv2.circle(output_frame, (center_x, center_y), 5, (0, 0, 255), -1)  # Dibuja un círculo rojo

    # Mostrar y guardar el fotograma procesado
    cv2.imshow("Centroide", output_frame)
    out.write(output_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(30) == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video procesado con centroides guardado en: {output_path}")
