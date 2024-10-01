import numpy as np
import cv2 


# Abre el video
video_path = 'ojo.mp4'
cap = cv2.VideoCapture(video_path)

# Verifica si el video fue cargado correctamente
if not cap.isOpened():
    print("Error al abrir el video")

# Especifica el número del frame que deseas extraer (por ejemplo, el frame 100)
frame_number = 100

# Salta al frame deseado
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

# Lee el frame
ret, frame = cap.read()

if ret:
    # Muestra el frame en una ventana
    cv2.imshow('Frame', frame)

    # Guarda el frame como una imagen
    cv2.imwrite('frame_extraido.png', frame)

    # Espera a que se presione una tecla para cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"No se pudo leer el frame {frame_number}")

# Libera el video
cap.release()



