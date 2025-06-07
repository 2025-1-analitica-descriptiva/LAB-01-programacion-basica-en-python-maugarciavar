"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import os

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    """
    suma = 0
    # Obtiene la ruta absoluta del archivo actual
    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "../files/input/data.csv")
    print(data_path)
    print("Abriendo archivo:", os.path.abspath(data_path))
    with open(data_path, "r") as file:
        for line in file:
            columns = line.strip().split('\t')
            suma += int(columns[1])
    return suma

if __name__ == "__main__":
    print(pregunta_01())

    