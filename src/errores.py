import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import cargar_datos

def redondear_sig(x, cifras):
    if x == 0:
        return 0
    return round(x, cifras - int(np.floor(np.log10(abs(x)))) - 1)

datos = cargar_datos()

anio = datos["anio"]
mes = datos["mes"]
mes_num = datos["mes_num"]
precio_real = datos["dolar_observado_promedio_clp"]


# A1 con 2 cifras significativas
vred2 = np.vectorize(lambda x: redondear_sig(x, 2))

precio_aprox = vred2(precio_real)

error_abs = np.abs(precio_real - precio_aprox)
error_rel = error_abs / precio_real * 100

indice_max = np.argmax(error_rel)

print("\nA1")
print("Mes con mayor error relativo:")
print(mes[indice_max], anio[indice_max])
print("Valor real:", round(precio_real[indice_max], 2))
print("Valor aproximado:", round(precio_aprox[indice_max], 2))
print("Error relativo:", round(error_rel[indice_max], 4), "%")


# CSV
salida = np.column_stack([
    anio,
    mes,
    np.round(precio_real, 2),
    np.round(precio_aprox, 2),
    np.round(error_abs, 2),
    np.round(error_rel, 4)
])


np.savetxt(
    "error_representacion.csv",
    salida,
    delimiter=",",
    fmt="%s",
    header="anio,mes,valor_real,valor_aprox,error_absoluto,error_relativo",
    comments=""
)

print("error_representacion.csv generado")


# Gráfico 1
plt.figure(figsize=(10, 5))
plt.plot(precio_real, marker="o")
plt.title("Serie mensual del dólar observado")
plt.xlabel("Mes")
plt.ylabel("CLP")
plt.grid(True)
plt.tight_layout()
plt.savefig("graficos/grafico1_serie_temporal.png")
plt.close()


# Gráfico 2
delta_p = np.diff(precio_real)

plt.figure(figsize=(10, 5))
plt.bar(range(len(delta_p)), delta_p)
plt.axhline(0, color="red", linestyle="--")
plt.title("Variación mensual ΔP")
plt.xlabel("Mes")
plt.ylabel("ΔP")
plt.tight_layout()
plt.savefig("graficos/grafico2_variacion.png")
plt.close()


# Gráfico 3
plt.figure(figsize=(10, 5))
plt.bar(range(len(error_rel)), error_rel)
plt.title("Error relativo de representación")
plt.xlabel("Mes")
plt.ylabel("Error relativo (%)")
plt.tight_layout()
plt.savefig("graficos/grafico3_error_representacion.png")
plt.close()

print("Gráficos 1, 2 y 3 generados")