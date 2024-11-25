import cv2
import numpy as np
import os
import csv

## FOR CALIBRATION

DIAMETER_1 = 160
THRESHOLD_VALUE = 60
DIAMETER_2 = 51
N_KERNEL_FILL = 3
PARAM_1=25
PARAM_2=15

def apply_circular_mask(video_path):
    """
    Apply a circular mask to a video, replacing the black background with white, and save the output.

    Parameters:
    - video_path: str, path to the input video.

    Output:
    - Saves the processed video as 'video_masked_white.avi' in the same directory as the input video.
    """
    # Ruta de salida basada en el video original
    output_path = video_path.replace(".avi", "_masked_white.avi")

    # Cargar el video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: No se pudo abrir el video.")
        return

    # Obtener las propiedades del video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Crear el objeto para guardar el video procesado
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Crear una máscara circular de diámetro fijo
    diameter = DIAMETER_1
    radius = diameter // 2
    mask = np.zeros((frame_height, frame_width), dtype=np.uint8)

    # Definir el centro del círculo
    center_x, center_y = frame_width // 2, (frame_height // 2)+50
    cv2.circle(mask, (center_x, center_y), radius, 255, -1)  # Círculo blanco en fondo negro

    while True:
        ret, frame = cap.read()
        if not ret:
            print("MASK::Fin del video o error al leer fotogramas.")
            break

        # Aplicar la máscara al fotograma
        mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        masked_frame = cv2.bitwise_and(frame, mask_bgr)

        # Reemplazar el fondo negro con blanco
        white_background = np.full_like(frame, 255)  # Crear un fondo blanco
        output_frame = np.where(mask_bgr == 0, white_background, masked_frame)  # Reemplazar negro por blanco

        # Escribir el fotograma procesado
        out.write(output_frame)

    # Liberar recursos
    cap.release()
    out.release()

    print(f"Video procesado con máscara circular guardado en: {output_path}")
    return output_path


def apply_binary_threshold(video_path):
    """
    Apply a fixed binary threshold to a video and save the output.

    Parameters:
    - video_path: str, path to the input video.

    Output:
    - Saves the processed video as 'video_umbralizado.avi' in the same directory as the input video.
    """
    # Ruta del video de salida
    output_path = video_path.replace(".avi", "_umbralizado.avi")

    # Cargar el video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: No se pudo abrir el video.")
        return

    # Obtener propiedades del video original
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Crear el objeto de escritura de video
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height), isColor=False)

    # Umbral fijo
    threshold_value = THRESHOLD_VALUE

    while True:
        ret, frame = cap.read()
        if not ret:
            print("THRESH::Fin del video o error al leer fotogramas.")
            break

        # Convertir a escala de grises
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Aplicar umbral binario
        _, binary_frame = cv2.threshold(gray_frame, threshold_value, 255, cv2.THRESH_BINARY)

        # Escribir el fotograma procesado en el video de salida
        out.write(binary_frame)

        

        # Presiona 'q' para salir
        if cv2.waitKey(30) == ord('q'):
            break

    # Liberar recursos
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Video procesado guardado en: {output_path}")
    return output_path



def apply_dynamic_circular_mask(video_path):
    """
    Apply a dynamic circular mask based on the centroid of intensity in each frame of a video.

    Parameters:
    - video_path: str, path to the input video.

    Output:
    - Saves the processed video as '<original_name>_circular_mask.avi' in the same directory.
    """
    # Ruta del video de salida
    output_path = video_path.replace(".avi", "_circular_mask.avi")

    # Cargar el video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: No se pudo abrir el video.")
        return None

    # Obtener las propiedades del video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Crear el objeto para guardar el video procesado
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Parámetro para el diámetro del círculo de la máscara
    circle_diameter = DIAMETER_2
    circle_radius = circle_diameter // 2

    while True:
        ret, frame = cap.read()
        if not ret:
            print("DYN_MASK::Fin del video o error al leer fotogramas.")
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

        # Escribir el fotograma procesado en el video de salida
        out.write(final_frame)

    # Liberar recursos
    cap.release()
    out.release()

    print(f"Video con máscara circular guardado en: {output_path}")
    return output_path



def fill_holes_in_video(video_path):
    """
    Fill holes in each frame of a video using morphological closing and save the output.

    Parameters:
    - video_path: str, path to the input video.

    Output:
    - Saves the processed video as '<original_name>_filled.avi' in the same directory.
    """
    # Ruta del video de salida
    output_path = video_path.replace(".avi", "_filled.avi")

    # Cargar el video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: No se pudo abrir el video.")
        return None

    # Obtener las propiedades del video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Crear el objeto para guardar el video procesado
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Crear un kernel para la operación de cierre
    kernel = np.ones((N_KERNEL_FILL, N_KERNEL_FILL), np.uint8)  # Kernel de tamaño ajustable

    while True:
        ret, frame = cap.read()
        if not ret:
            print("FILL::Fin del video o error al leer fotogramas.")
            break

        # Convertir a escala de grises
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Aplicar un umbral simple (ajusta según el video)
        _, thresholded = cv2.threshold(gray_frame, 50, 255, cv2.THRESH_BINARY_INV)

        # Llenar agujeros usando MORPH_CLOSE
        filled = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

        # Convertir a BGR para guardar
        filled_frame = cv2.cvtColor(filled, cv2.COLOR_GRAY2BGR)

        # Escribir el fotograma procesado en el video de salida
        out.write(filled_frame)

    # Liberar recursos
    cap.release()
    out.release()

    print(f"Video procesado con agujeros llenados guardado en: {output_path}")
    return output_path


import cv2
import numpy as np

def detect_circles_and_overlay(processed_video_path, original_video_path):
    """
    Detect circles in a processed video, overlay the detected circles on the original video, and save the output.

    Parameters:
    - processed_video_path: str, path to the processed (filled) video.
    - original_video_path: str, path to the original video.

    Output:
    - Saves the processed video with circles as '<original_name>_with_circles.avi'.
    - Prints a list of detected diameters.
    """
    # Ruta del video de salida
    output_video_path = original_video_path.replace(".avi", "_with_circles.avi")

    # Cargar los videos
    cap_processed = cv2.VideoCapture(processed_video_path)
    cap_original = cv2.VideoCapture(original_video_path)

    # Verifica si los videos fueron cargados correctamente
    if not cap_processed.isOpened() or not cap_original.isOpened():
        print("Error al abrir uno de los videos")
        return None

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
                                   param1=PARAM_1, param2=PARAM_2, minRadius=20, maxRadius=25)

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

        # Escribir el frame procesado en el video de salida
        out.write(frame_original)

    # Liberar recursos
    cap_processed.release()
    cap_original.release()
    out.release()

    # Convertir los diámetros a una lista simple de enteros
    diameters = list(map(int, diameters))

    print("DIAMETROS DETECTADOS")
    print(f"Video procesado guardado en: {output_video_path}")
    return output_video_path, diameters



# List for storing all diameters for each video
all_diameters = []

# Get all .avi files in the current directory
avi_files = [f for f in os.listdir() if f.endswith(".avi")]

# Process each video
for original_video in avi_files:
    print(f"Processing: {original_video}")

    # Apply processing steps
    video = apply_circular_mask(original_video)
    video = apply_binary_threshold(video)
    video = apply_dynamic_circular_mask(video)
    video = fill_holes_in_video(video)
    video, diameters = detect_circles_and_overlay(video, original_video)

    # Store the diameters for this video
    all_diameters.append(diameters)

    print(f"Processed video: {original_video}")
    print(f"Detected diameters: {diameters}")

# Print all diameters
print("All diameters for all videos:")
print(all_diameters)


# Name of the output CSV file
output_csv = "diameters.csv"

# Write all diameters to the CSV file
with open(output_csv, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Video Name", "Diameters"])
    for video_name, diameters in zip(avi_files, all_diameters):
        writer.writerow([video_name, ", ".join(map(str, diameters))])

print(f"Diameters saved in {output_csv}")