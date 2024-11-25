import cv2
import numpy as np

# Ruta del video original
video_path = "18-10-24_12-44-17_VIDEO_OJO_UX.avi"
output_path = "video_masked_white.avi"

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

# Crear una máscara circular de diámetro 190
diameter = 180
radius = diameter // 2
mask = np.zeros((frame_height, frame_width), dtype=np.uint8)

# Definir el centro del círculo
center_x, center_y = frame_width // 2, frame_height // 2
cv2.circle(mask, (center_x, center_y), radius, 255, -1)  # Círculo blanco en fondo negro

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video o error al leer fotogramas.")
        break

    # Aplicar la máscara al fotograma
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    masked_frame = cv2.bitwise_and(frame, mask_bgr)

    # Reemplazar el fondo negro con blanco
    white_background = np.full_like(frame, 255)  # Crear un fondo blanco
    output_frame = np.where(mask_bgr == 0, white_background, masked_frame)  # Reemplazar negro por blanco

    # Mostrar y guardar el fotograma procesado
    cv2.imshow("Video con Máscara Circular (Fondo Blanco)", output_frame)
    out.write(output_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(30) == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video procesado con máscara circular guardado en: {output_path}")
