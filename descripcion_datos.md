# Descripcion de los datos

La fuente de datos corresponde a una muestra creada para representar registros operativos de un sistema de transporte masivo tipo TransMilenio. Como no se conto con una base de datos real, se desarrollo un dataset propio con informacion simulada pero coherente con el problema planteado.

## Archivo
`dataset_transporte_no_supervisado.csv`

## Columnas

| Columna | Descripcion |
|---|---|
| id_registro | Identificador unico del registro. |
| ruta | Ruta troncal o servicio del sistema de transporte. |
| dia_semana | Dia en que se registra la operacion. |
| franja_horaria | Momento del dia: madrugada, hora pico, hora valle o noche. |
| clima | Condicion climatica aproximada. |
| pasajeros_estimados | Cantidad estimada de pasajeros movilizados en la ruta. |
| frecuencia_buses_min | Tiempo promedio entre buses, en minutos. |
| tiempo_espera_prom_min | Tiempo promedio de espera del usuario. |
| retraso_prom_min | Retraso promedio estimado de la ruta. |
| ocupacion_promedio_pct | Porcentaje promedio de ocupacion del bus o estacion. |
| velocidad_prom_kmh | Velocidad promedio de operacion. |
| incidentes_reportados | Numero de incidentes reportados en la franja observada. |

## Uso en aprendizaje no supervisado

En esta actividad no existe una variable objetivo como congestion alta o baja. El objetivo es encontrar patrones ocultos en los datos. Por esta razon, se utilizan las columnas del dataset para que el algoritmo K-Means agrupe registros similares. Los grupos obtenidos pueden interpretarse como comportamientos operativos, por ejemplo rutas con alta demanda, rutas con tiempos de espera altos o registros con operacion mas estable.
