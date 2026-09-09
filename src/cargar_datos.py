import numpy as np

def cargar_datos():
    return np.genfromtxt(
        "data/dolar_observado_sii_2022_2025.csv",
        delimiter=",",
        names=True,
        dtype=None,
        encoding="utf-8"
    )

if __name__ == "__main__":
    datos = cargar_datos()

    print("Registros:", len(datos))
    print("Columnas:", datos.dtype.names)
    print(datos[:3])