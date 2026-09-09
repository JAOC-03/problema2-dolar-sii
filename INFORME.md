# Problema 2 - La ganancia que se evapora

## Introducción

En este laboratorio se trabajó con los datos del dólar observado del Servicio de Impuestos Internos (SII) entre los años 2022 y 2025.
El objetivo fue estudiar cómo los errores numéricos afectan los resultados cuando los valores se almacenan utilizando pocas cifras significativas,
simulando el comportamiento de los números en punto flotante.

A lo largo del trabajo se analizaron errores de representación, propagación de errores, cancelación numérica y diferencias entre los tipos de dato
float32 y float64. También se evaluó una estrategia de compra y venta de dólares para determinar si las conclusiones obtenidas eran confiables considerando los errores asociados.

## A1. Error de representación

Para cada valor del dólar se realizó una aproximación a dos cifras significativas. Posteriormente se calculó el error absoluto y el error
 relativo de cada dato.

El mes que presentó el mayor error relativo fue abril de 2022. En ese caso el valor real fue 815.12 CLP, mientras que el valor aproximado 
fue 820 CLP. El error relativo obtenido fue de 0.5987%.

Aunque este porcentaje es bajo, demuestra que cada aproximación introduce una pequeña pérdida de precisión. Esta pérdida puede propagarse
 posteriormente cuando se realizan operaciones matemáticas más complejas.

## A2. Evaluación entre dos puntos

Se simuló una operación de compra y venta utilizando un capital inicial de 1.000.000 de pesos.

La ganancia obtenida fue de 170731.71 CLP y el error propagado asociado fue de 1159.95 CLP. Esto corresponde a un error porcentual de 0.68%.

Al comparar ambos valores se observa que la incertidumbre representa una fracción pequeña de la ganancia total. Por esta razón se puede concluir que el resultado es confiable y que la propagación de errores no altera significativamente la conclusión obtenida.

## A3. Cancelación

Para analizar el fenómeno de cancelación se compararon los valores de diciembre de 2022 y diciembre de 2023 utilizando tres cifras significativas.

La diferencia calculada fue:

ΔP = -1.00 ± 0.67

El error relativo obtenido fue de 67%.

Aunque la diferencia sigue siendo mayor que el error propagado, el porcentaje de error es muy alto. Esto significa que una parte importante del resultado está afectada por la pérdida de precisión producida al restar dos valores muy semejantes.

Este ejercicio muestra claramente el problema de la cancelación numérica. Cuando se restan números grandes y muy parecidos, una pequeña incertidumbre puede transformarse en una parte importante del resultado final.

## A4. Variación anual

Para cada año se calculó la diferencia entre el valor del dólar en diciembre y el valor del dólar en enero. Después se propagaron los errores correspondientes y se calculó el error relativo de cada resultado.

Los errores relativos obtenidos fueron:

- 2025: 5.75%
- 2024: 6.16%
- 2022: 10.65%
- 2023: 20.82%

El ranking de confiabilidad obtenido fue:

1. 2025
2. 2024
3. 2022
4. 2023

Los años menos confiables tienen en común que la diferencia entre enero y diciembre es relativamente pequeña en comparación con el error propagado. Cuando esto ocurre, el error relativo aumenta y la confianza en el resultado disminuye.

## A5. Mejor compra y mejor venta

El precio mínimo del dólar durante todo el período analizado ocurrió en febrero de 2023. El precio máximo ocurrió en enero de 2025.

La estrategia de comprar en febrero de 2023 y vender en enero de 2025 produjo una rentabilidad de 25% con una incertidumbre aproximada de 0.07%.

La diferencia entre ambos valores es mucho mayor que el error asociado, por lo que la conclusión es sólida. El error tiene una influencia muy pequeña sobre el resultado final y no modifica la recomendación obtenida.

## B1. Cifras significativas y mantisa corta

Utilizar pocas cifras significativas es equivalente a almacenar un número utilizando una mantisa reducida.

Por ejemplo, el valor 1000.76 puede representarse como 1000 cuando se trabaja con pocas cifras significativas. La diferencia entre ambos valores corresponde al error de representación.

Este fenómeno es similar a lo que ocurre dentro del computador cuando los números se almacenan utilizando una cantidad limitada de bits. Mientras menor sea la precisión disponible, mayor será el error introducido en cada cálculo.

## B2. La ida y vuelta que no vuelve

En esta actividad se realizó una conversión desde pesos chilenos a dólares y posteriormente se volvió a convertir el resultado a pesos utilizando el mismo valor del dólar.

Teóricamente debería recuperarse exactamente el monto inicial. Sin embargo, debido a las limitaciones del punto flotante aparece una pequeña diferencia.

La mayor deriva observada fue de 0.0625 pesos.

Aunque este error es muy pequeño, demuestra que las operaciones realizadas por un computador no siempre recuperan exactamente el valor original debido a los errores de representación internos.

## B4. Cancelación en la máquina

Se calculó la operación 874.67 − 875.66 utilizando los tipos de dato float32 y float64.

Los resultados mostraron que float64 conserva una precisión superior a float32.

Los errores obtenidos fueron:

- float32: aproximadamente 0.0000098
- float64: 0

Esto demuestra que float64 permite representar los números con una mayor precisión y reduce considerablemente el efecto de la cancelación numérica.

Los resultados coinciden con lo observado en el ejercicio A3, donde pequeñas diferencias entre números muy parecidos generan pérdida de precisión.

## Conclusión

El mejor momento para comprar dólares dentro del período analizado fue febrero de 2023, mientras que el mejor momento para vender fue enero de 2025.

La estrategia completa produjo una rentabilidad aproximada de 25% con una incertidumbre de sólo 0.07%, por lo que la recomendación puede considerarse confiable y suficientemente respaldada por los cálculos realizados.

Por otro lado, el análisis de cancelación mostró que las diferencias pequeñas pueden verse fuertemente afectadas por los errores numéricos. El caso más representativo fue la comparación entre diciembre de 2022 y diciembre de 2023, donde el error relativo alcanzó un 67%.

También se observó que los resultados más confiables corresponden a situaciones donde la diferencia calculada es considerablemente mayor que el error asociado. Cuando ambos valores son similares, la capacidad para interpretar correctamente el resultado disminuye.

La principal lección aprendida en este laboratorio es que no basta con observar un resultado numérico. Siempre es necesario analizar el error asociado, especialmente cuando se trabaja con diferencias obtenidas a partir de números grandes y muy parecidos.
