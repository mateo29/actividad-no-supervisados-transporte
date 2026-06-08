# Actividad - Metodos no supervisados en inteligencia artificial

## Proyecto
Agrupamiento de patrones operativos en un sistema de transporte masivo colombiano tipo TransMilenio.

## Integrante
Daniel Mateo Aguilar Perez - trabajo individual.

## Objetivo
Aplicar un metodo de aprendizaje no supervisado para identificar grupos o patrones en registros de operacion del transporte masivo. El modelo no predice una etiqueta, sino que agrupa registros parecidos segun variables como pasajeros, tiempo de espera, retraso, ocupacion, velocidad, clima, ruta y franja horaria.

## Archivos incluidos
- `dataset_transporte_no_supervisado.csv`: fuente de datos creada para la actividad.
- `modelo_kmeans_transporte.py`: codigo fuente en Python.
- `descripcion_datos.md`: descripcion de las columnas del dataset.
- `pruebas_componente.md`: pruebas realizadas al componente desarrollado.
- `metodo_codo.png`: grafica usada para analizar el numero de clusters.
- `puntaje_silueta.png`: grafica de evaluacion de los grupos.
- `clusters_pca.png`: visualizacion de los clusters en dos dimensiones.
- `resultados_clusters_transporte.csv`: dataset con el cluster asignado a cada registro.
- `mapa_conceptual_no_supervisados.png`: mapa conceptual.
- `actividad_no_supervisados_transporte_masivo.pdf`: documento principal de entrega.

## Librerias utilizadas
```bash
pip install pandas scikit-learn matplotlib
```

## Ejecucion
```bash
py modelo_kmeans_transporte.py
```

## Links de entrega
Repositorio Git/GitLab: https://github.com/mateo29/actividad-no-supervisados-transporte
Video explicativo: PONGO EL VIDEO AQUI

## Nota
El trabajo fue realizado de forma individual, por lo tanto el log del repositorio corresponde a un solo integrante.
