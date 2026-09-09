import numpy as np
import matplotlib.pyplot as plt

def redondear_sig(x, cifras):
    if x == 0:
        return 0
    return round(x, cifras - int(np.floor(np.log10(abs(x)))) - 1)

datos = np.genfromtxt(
    "error_representacion.csv",
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8"
)

precio_real = datos["valor_real"]

capital = 1000000


# A3 Cancelación
print("\nA3")

valor_2022 = 875.66
valor_2023 = 874.67

aprox_2022 = redondear_sig(valor_2022, 3)
aprox_2023 = redondear_sig(valor_2023, 3)

delta = aprox_2023 - aprox_2022

error_2022 = abs(valor_2022 - aprox_2022)
error_2023 = abs(valor_2023 - aprox_2023)

error_propagado = error_2022 + error_2023

if delta != 0:
    error_relativo = error_propagado / abs(delta) * 100
else:
    error_relativo = np.inf

print("ΔP =",round(delta, 2),"±",round(error_propagado, 2))
print("Error relativo =",round(error_relativo, 2),"%")

if error_propagado > abs(delta):
    print("Resultado NO confiable por cancelación.")
else:
    print("Resultado confiable.")


# Agregar A3 al CSV
tabla = np.atleast_2d(
    np.genfromtxt(
        "resultados_error.csv",
        delimiter=",",
        dtype=str,
        skip_header=1
    )
)

nueva_fila = np.array([[
    "A3",
    str(round(error_propagado, 2)),
    str(round(error_relativo, 4)),
    str(round(error_propagado, 2))
]])

tabla = np.vstack([tabla, nueva_fila])

np.savetxt(
    "resultados_error.csv",
    tabla,
    delimiter=",",
    fmt="%s",
    header="caso,error_absoluto,error_relativo,error_propagado",
    comments=""
)

print("A3 agregado a resultados_error.csv")


# B2 Ida y vuelta
print("\nB2")

usd = np.float32(capital / precio_real)
clp = np.float32(usd * precio_real)

deriva = clp - capital

print("Mayor deriva:",round(np.max(np.abs(deriva)), 4))

# B4 float32 vs float64
print("\nB4")

valor_exacto = 874.67 - 875.66

resultado32 = np.float32(874.67) - np.float32(875.66)
resultado64 = np.float64(874.67) - np.float64(875.66)

error32 = abs(resultado32 - valor_exacto)
error64 = abs(resultado64 - valor_exacto)

print(f"float32 = {resultado32}")
print(f"float64 = {resultado64}")

print(f"Error float32 = {error32}")
print(f"Error float64 = {error64}")


# Gráfico 5
plt.figure(figsize=(10, 5))

plt.plot(deriva, marker="o")

plt.title("Deriva CLP → USD → CLP")
plt.xlabel("Mes")
plt.ylabel("Error (CLP)")

plt.grid(True)
plt.tight_layout()

plt.savefig("graficos/grafico5_deriva.png")
plt.close()

print("Gráfico 5 generado")