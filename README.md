# Problema: La ganancia que se evapora

## Integrantes

Jeremy Orellana

## Descripción

Laboratorio de Computación Numérica centrado en el análisis de errores numéricos utilizando datos históricos del dólar observado del Servicio de Impuestos Internos (SII) entre los años 2022 y 2025.

El trabajo considera:
- Error absoluto
- Error relativo
- Propagación de errores
- Cancelación numérica
- Representación con pocas cifras significativas
- Comparación entre float32 y float64
- Conversión CLP -> USD -> CLP

## Estructura del repositorio

problema2-dolar-sii/
- README.md
- INFORME.md
- requirements.txt
 
data/
- dolar_observado_sii_2022_2025.csv
 
src/
- cargar_datos.py
- errores.py
- anualidad.py
- punto_flotante.py
 
graficos/
- grafico1_serie_temporal.png
- grafico2_variacion.png
- grafico3_error_representacion.png
- grafico4_rentabilidad.png
- grafico5_deriva.png
- error_representacion.csv
- resultados_error.csv    

## Requisitos

Instalar las dependencias:
- pip install -r requirements.txt

## Ejecución

Los programas deben ejecutarse en el siguiente orden:
python src/errores.py
python src/anualidad.py
python src/punto_flotante.py

## Archivos generados

### Gráficos

1. Serie mensual del dólar observado.
2. Variación mensual del dólar.
3. Error de representación por mes.
4. Rentabilidad con barras de error.
5. Deriva de la conversión CLP → USD → CLP.

### CSV

1. error_representacion.csv
Contiene para cada mes:
- Valor real.
- Valor aproximado.
- Error absoluto.
- Error relativo.

2. resultados_error.csv
Contiene:
- A2: compra y venta.
- A3: cancelación.
- A4: variaciones anuales.
- A5: mejor compra y venta.

Incluye:
- Error absoluto.
- Error relativo.
- Error propagado.

## Bibliotecas utilizadas

- NumPy
- Matplotlib

## Fuente de datos

Servicio de Impuestos Internos (SII).

Archivo utilizado:
- dolar_observado_sii_2022_2025.csv
