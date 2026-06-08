# Pruebas realizadas al componente desarrollado

## 1. Prueba de carga del dataset
Se ejecuto el archivo `modelo_kmeans_transporte.py` para validar que el dataset `dataset_transporte_no_supervisado.csv` cargara correctamente con pandas.

Resultado esperado: que el programa muestre las primeras filas del dataset y la cantidad de registros y columnas.

Resultado obtenido: el dataset se cargo correctamente con 150 registros y 12 columnas antes de asignar el cluster.

## 2. Prueba de preprocesamiento
Se verifico que las columnas categoricas fueran transformadas con OneHotEncoder y las columnas numericas fueran escaladas con StandardScaler.

Resultado esperado: que el modelo pudiera usar variables categoricas y numericas sin errores.

Resultado obtenido: el preprocesamiento se ejecuto correctamente.

## 3. Prueba de seleccion de numero de grupos
Se evaluaron valores de k entre 2 y 7 usando el metodo del codo y el puntaje de silueta.

Resultado esperado: generar las imagenes `metodo_codo.png` y `puntaje_silueta.png`.

Resultado obtenido: ambas graficas fueron generadas correctamente.

## 4. Prueba de entrenamiento del modelo
Se entreno un modelo K-Means con k = 3 para agrupar los registros del sistema de transporte.

Resultado esperado: que cada registro recibiera un numero de cluster.

Resultado obtenido: el modelo asigno los siguientes registros por cluster:

cluster
0    53
1    71
2    26

## 5. Prueba de resultados
Se genero un archivo `resultados_clusters_transporte.csv` con el cluster asignado a cada registro y una grafica `clusters_pca.png` para visualizar los grupos en dos dimensiones.

Resultado esperado: obtener una salida interpretable para analizar patrones de operacion.

Resultado obtenido: los archivos se generaron correctamente y se pudieron identificar grupos con diferentes niveles de demanda, ocupacion, retraso y velocidad.

## Conclusion de las pruebas
El componente desarrollado funciona correctamente porque carga los datos, los transforma, entrena el modelo no supervisado, asigna clusters y genera resultados visuales para su interpretacion.
