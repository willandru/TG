import numpy as np
import time

def generar_matriz_aleatoria(filas, columnas):
    """
    Genera una matriz de datos aleatorios entre 0 y 1 de tamaño (filas, columnas).
    
    Args:
    - filas (int): Número de filas de la matriz.
    - columnas (int): Número de columnas de la matriz.
    
    Returns:
    - matriz_aleatoria (numpy.ndarray): La matriz de datos aleatorios generada.
    """
    return np.random.rand(filas, columnas)


