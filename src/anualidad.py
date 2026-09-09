import numpy as np
import matplotlib.pyplot as plt

datos = np.genfromtxt(
    "error_representacion.csv",
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8"
)

anio = datos["anio"]
mes = datos["mes"]

precio_real = datos["valor_real"]
precio_aprox = datos["valor_aprox"]

error_abs = datos["error_absoluto"]
error_rel = datos["error_relativo"]

capital = 1000000

resultados = []


# A2
print("\nA2")

idx_compra = 0
idx_venta = 9

p_compra = precio_aprox[idx_compra]
p_venta = precio_aprox[idx_venta]

usd = capital / p_compra
pesos_final = usd * p_venta

ganancia = pesos_final - capital

error_rel_total = error_rel[idx_compra] + error_rel[idx_venta]
error_propagado = abs(ganancia) * error_rel_total / 100

print("Ganancia =",round(ganancia, 2),"±",round(error_propagado, 2))
print("Error porcentual =",round(error_rel_total, 4), "%")

resultados.append([
    "A2",
    round(error_abs[idx_compra] + error_abs[idx_venta], 2),
    round(error_rel_total, 4),
    round(error_propagado, 2)
])


# A4
print("\nA4")

ranking = []

for anio_actual in [2022, 2023, 2024, 2025]:
    idx = np.where(anio == anio_actual)[0]

    enero = idx[0]
    diciembre = idx[-1]

    variacion = precio_aprox[diciembre] - precio_aprox[enero]

    ea = error_abs[enero] + error_abs[diciembre]

    if variacion == 0:
        er = np.inf
    else:
        er = ea / abs(variacion) * 100

    print(anio_actual,": Variación =",round(variacion, 2),"Error =",round(er, 2),"%")

    ranking.append((anio_actual, er))

    resultados.append([
        f"A4_{anio_actual}",
        round(ea, 2),
        round(er, 4),
        round(ea, 2)
    ])

print("\nRanking de confiabilidad")

ranking.sort(key=lambda x: x[1])

for posicion, dato in enumerate(ranking, start=1):
    print(posicion,dato[0],round(dato[1], 2),"%")


# A5
print("\nA5")

idx_min = np.argmin(precio_real)
idx_max = np.argmax(precio_real)

precio_min = precio_aprox[idx_min]
precio_max = precio_aprox[idx_max]

usd = capital / precio_min
final = usd * precio_max

ganancia = final - capital

rentabilidad = ganancia / capital * 100

error_rel_total = error_rel[idx_min] + error_rel[idx_max]
error_propagado = abs(rentabilidad) * error_rel_total / 100

print("Comprar:", mes[idx_min], anio[idx_min])
print("Vender:", mes[idx_max], anio[idx_max])
print("Rentabilidad =",round(rentabilidad, 2),"% ±",round(error_propagado, 2),"%")

resultados.append([
    "A5",
    round(error_abs[idx_min] + error_abs[idx_max], 2),
    round(error_rel_total, 4),
    round(error_propagado, 2)
])

# CSV obligatorio

np.savetxt(
    "resultados_error.csv",
    np.array(resultados, dtype=object),
    delimiter=",",
    fmt="%s",
    header="caso,error_absoluto,error_relativo,error_propagado",
    comments=""
)

print("\nresultados_error.csv generado")


# Gráfico 4
rentabilidades = []
errores = []

for p in precio_aprox:
    usd = capital / precio_min
    final = usd * p

    rent = (final - capital) / capital * 100

    rentabilidades.append(rent)
    errores.append(abs(rent) * error_rel_total / 100)

plt.figure(figsize=(10, 5))

plt.errorbar(
    range(len(rentabilidades)),
    rentabilidades,
    yerr=errores,
    fmt="o-",
    capsize=4
)

plt.title("Rentabilidad desde el mínimo")
plt.xlabel("Mes")
plt.ylabel("Rentabilidad (%)")

plt.grid(True)
plt.tight_layout()

plt.savefig("graficos/grafico4_rentabilidad.png")
plt.close()

print("Gráfico 4 generado")