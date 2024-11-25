import cv2

# Ruta del video original y el video de salida
video_path = "video_masked_white.avi"
output_path = "video_umbralizado.avi"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: No se pudo abrir el video.")
    exit()

# Obtener propiedades del video original
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Crear el objeto de escritura de video
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height), isColor=False)

# Umbral fijo
threshold_value = 90

while True:
    ret, frame = cap.read()
    if not ret:
        print("Fin del video o error al leer fotogramas.")
        break

    # Convertir a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar umbral binario
    _, binary_frame = cv2.threshold(gray_frame, threshold_value, 255, cv2.THRESH_BINARY)

    # Escribir el fotograma procesado en el video de salida
    out.write(binary_frame)

    # Mostrar el video procesado (opcional)
    cv2.imshow("Video Umbralizado", binary_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(30) == ord('q'):
        break

# Liberar recursos
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video procesado guardado en: {output_path}")
