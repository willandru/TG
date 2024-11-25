import cv2
import numpy as np

# Ruta del video original
video_path = "  video_circular_mask.avi"
output_path = "video_filled.avi"

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

# Crear un kernel para la operación de cierre (filling holes)
kernel = np.ones((29, 29), np.uint8)  # Kernel de tamaño 5x5, ajustable

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video o error al leer fotogramas.")
        break

    # Convertir a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar un umbral simple (ajusta según el video)
    _, thresholded = cv2.threshold(gray_frame, 50, 255, cv2.THRESH_BINARY_INV)

    # Llenar agujeros usando MORPH_CLOSE
    filled = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

    # Convertir a BGR para guardar
    filled_frame = cv2.cvtColor(filled, cv2.COLOR_GRAY2BGR)

    # Mostrar y guardar el fotograma procesado
    cv2.imshow("Video con Agujeros Llenados", filled_frame)
    out.write(filled_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(30) == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video procesado con agujeros llenados guardado en: {output_path}")
