# Problema: La ganancia que se evapora

## Introducción

El objetivo de este laboratorio fue estudiar los errores numéricos producidos por la representación limitada de números reales en computadores utilizando los valores del dólar observado del Servicio de Impuestos Internos (SII) entre los años 2022 y 2025.

Para ello se utilizaron aproximaciones con pocas cifras significativas, simulando una mantisa corta similar a la utilizada en representaciones de punto flotante. Posteriormente se analizaron los errores absolutos, errores relativos, propagación de errores y fenómenos de cancelación.


# A1. Error de representación

Todos los valores del dólar fueron aproximados a dos cifras significativas.

Para cada mes se calcularon:

## Error absoluto

- Error absoluto:  Ea = | valor verdadero − valor aproximado |  (en pesos). 

## Error relativo

- Error relativo (porcentual):  Er = ( Ea / valor verdadero ) × 100. 

El mayor error relativo fue observado en:

- Mes: Abril 2022
- Valor real: 815.12 CLP
- Valor aproximado: 820 CLP
- Error relativo: 0.5987 %

Aunque el error individual es pequeño, este puede propagarse durante operaciones posteriores y afectar los resultados finales.

---

# A2. Evaluación entre dos puntos

Se simuló una operación de compra y venta utilizando un capital inicial de:

\[
1.000.000\ CLP
\]

La cantidad de dólares comprada se calculó mediante:

\[
USD=\frac{Monto}{Precio_{compra}}
\]

Luego se obtuvo el monto recuperado:

\[
Pesos_{finales}=USD\times Precio_{venta}
\]

Finalmente:

\[
Ganancia = Pesos_{finales} - Monto
\]

La ganancia obtenida fue:

\[
170731.71 \pm 1159.95
\]

con un error porcentual de:

\[
0.68\%
\]

El error asociado resulta pequeño en comparación con la ganancia obtenida, por lo que el resultado puede considerarse confiable.

---

# A3. Cancelación

Se estudió la diferencia entre los valores de diciembre de 2022 y diciembre de 2023 utilizando tres cifras significativas.

Valores originales:

\[
875.66
\]

y

\[
874.67
\]

Valores aproximados:

\[
876
\]

y

\[
875
\]

La diferencia obtenida fue:

\[
\Delta P = -1.00 \pm 0.67
\]

con un error relativo de:

\[
67\%
\]

La diferencia observada es mayor que el error propagado, por lo que existe evidencia de una disminución del valor del dólar.

Sin embargo, el error relativo es extremadamente elevado, lo que indica una pérdida importante de precisión causada por cancelación numérica.

Por esta razón, aunque la disminución parece real, la conclusión debe considerarse poco robusta.

---

# A4. Variación anual

Para cada año se calculó:

\[
Variación = Precio_{diciembre} - Precio_{enero}
\]

y posteriormente se propagó el error absoluto asociado a ambas mediciones.

Los resultados obtenidos fueron:

| Año | Error relativo |
|------|------:|
| 2025 | 5.75 % |
| 2024 | 6.16 % |
| 2022 | 10.65 % |
| 2023 | 20.82 % |

Ranking de confiabilidad:

1. 2025
2. 2024
3. 2022
4. 2023

Los años menos confiables presentan una característica común: la diferencia observada entre enero y diciembre es relativamente pequeña respecto al error propagado.

A medida que la diferencia disminuye, el error relativo aumenta y la confiabilidad de la conclusión se reduce.

---

# A5. Mejor compra y mejor venta

Se identificó el valor mínimo y el valor máximo de todo el período analizado.

El mejor momento para comprar fue:

- Febrero 2023

El mejor momento para vender fue:

- Enero 2025

La rentabilidad obtenida fue:

\[
25\% \pm 0.07\%
\]

La incertidumbre es muy pequeña respecto de la rentabilidad obtenida.

Por lo tanto, la conclusión sobrevive claramente al error propagado y corresponde a la estrategia más sólida encontrada en los datos.

---

# B1. Cifras significativas y mantisa corta

La representación en punto flotante almacena los números utilizando una cantidad limitada de información.

Reducir un número a pocas cifras significativas equivale a utilizar una mantisa corta, ya que se descarta parte de la precisión original.

Por ejemplo:

\[
1000.76
\]

aproximado a tres cifras significativas se representa como:

\[
1000
\]

La diferencia entre ambos valores constituye un error de representación.

Este mismo fenómeno ocurre cuando una computadora almacena números utilizando una mantisa limitada.

---

# B2. La ida y vuelta que no vuelve

Se realizó la conversión:

\[
CLP \rightarrow USD \rightarrow CLP
\]

utilizando aritmética de punto flotante.

Teóricamente debería recuperarse exactamente el monto inicial.

Sin embargo, debido a las limitaciones de representación del computador, aparece una pequeña deriva acumulada.

La mayor deriva observada fue:

\[
0.0625\ CLP
\]

Aunque la magnitud del error es reducida, demuestra que las operaciones realizadas con punto flotante no recuperan exactamente el valor original.

---

# B4. Cancelación en la máquina

Se calculó la operación:

\[
874.67 - 875.66
\]

utilizando los tipos de dato `float32` y `float64`.

Resultados:

- float32 ≈ -0.98999
- float64 ≈ -0.99

Errores obtenidos:

- float32 ≈ 0.0000098
- float64 ≈ 0

Se observa que `float64` conserva una precisión superior debido a que dispone de una mantisa más grande.

Este comportamiento coincide con lo observado en A3, donde las diferencias pequeñas entre números grandes provocan pérdida de precisión y cancelación numérica.

---

# Conclusión

La mejor estrategia observada consiste en comprar dólares durante febrero de 2023 y venderlos durante enero de 2025.

Esta operación genera una rentabilidad aproximada de:

\[
25\% \pm 0.07\%
\]

por lo que la recomendación es sólida y la conclusión sobrevive claramente al error propagado.

En contraste, existen situaciones donde el error tiene una influencia relevante sobre el resultado. El caso más representativo corresponde a la comparación entre diciembre de 2022 y diciembre de 2023, donde el error relativo alcanzó un 67 %. Aunque la diferencia observada sugiere una disminución del dólar, la precisión de la conclusión es limitada debido al fenómeno de cancelación.

Los años menos confiables también corresponden a aquellos donde la diferencia observada es pequeña respecto al error propagado, destacando especialmente el año 2023.

La principal lección aprendida en este laboratorio es que no basta con observar el resultado de una diferencia. Cuando se restan números grandes y muy parecidos, una pequeña incertidumbre puede representar una fracción importante del resultado final, haciendo que la interpretación sea mucho menos confiable.

Por esta razón, toda conclusión numérica debe analizarse junto con el error asociado y no únicamente a partir del valor calculado.
