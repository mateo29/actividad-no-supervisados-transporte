# Actividad - Metodos no supervisados en IA
# Proyecto: Agrupamiento de comportamientos en transporte masivo
# Autor: Daniel Mateo Aguilar Perez - trabajo individual

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# 1. Cargar fuente de datos
archivo = "dataset_transporte_no_supervisado.csv"
datos = pd.read_csv(archivo)
print("Primeras filas del dataset:")
print(datos.head())
print("\nCantidad de registros y columnas:", datos.shape)

# 2. Seleccionar variables para agrupamiento
columnas_categoricas = ["ruta", "dia_semana", "franja_horaria", "clima"]
columnas_numericas = [
    "pasajeros_estimados",
    "frecuencia_buses_min",
    "tiempo_espera_prom_min",
    "retraso_prom_min",
    "ocupacion_promedio_pct",
    "velocidad_prom_kmh",
    "incidentes_reportados"
]

X = datos[columnas_categoricas + columnas_numericas]

# 3. Transformar datos: codificar categorias y escalar variables numericas
preprocesador = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), columnas_categoricas),
        ("num", StandardScaler(), columnas_numericas)
    ]
)

X_procesado = preprocesador.fit_transform(X)

# 4. Buscar un numero adecuado de grupos con metodo del codo y silueta
inercias = []
siluetas = []
rango_k = range(2, 8)

for k in rango_k:
    modelo_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    etiquetas_temp = modelo_temp.fit_predict(X_procesado)
    inercias.append(modelo_temp.inertia_)
    siluetas.append(silhouette_score(X_procesado, etiquetas_temp))

plt.figure(figsize=(7, 4))
plt.plot(list(rango_k), inercias, marker="o")
plt.title("Metodo del codo para seleccionar k")
plt.xlabel("Numero de grupos k")
plt.ylabel("Inercia")
plt.tight_layout()
plt.savefig("metodo_codo.png")

plt.figure(figsize=(7, 4))
plt.plot(list(rango_k), siluetas, marker="o")
plt.title("Puntaje de silueta por numero de grupos")
plt.xlabel("Numero de grupos k")
plt.ylabel("Silhouette score")
plt.tight_layout()
plt.savefig("puntaje_silueta.png")

# 5. Entrenar modelo final de agrupamiento no supervisado
k_final = 3
modelo = KMeans(n_clusters=k_final, random_state=42, n_init=10)
datos["cluster"] = modelo.fit_predict(X_procesado)

# 6. Guardar dataset con grupo asignado
datos.to_csv("resultados_clusters_transporte.csv", index=False, encoding="utf-8-sig")

# 7. Resumen de cada grupo
resumen = datos.groupby("cluster")[columnas_numericas].mean().round(2)
conteo = datos["cluster"].value_counts().sort_index()
print("\nCantidad de registros por cluster:")
print(conteo)
print("\nResumen promedio por cluster:")
print(resumen)

# 8. Visualizacion en 2 dimensiones usando PCA
pca = PCA(n_components=2, random_state=42)
componentes = pca.fit_transform(X_procesado.toarray() if hasattr(X_procesado, "toarray") else X_procesado)

plt.figure(figsize=(7, 5))
plt.scatter(componentes[:, 0], componentes[:, 1], c=datos["cluster"], s=45)
plt.title("Agrupamiento de rutas usando K-Means")
plt.xlabel("Componente principal 1")
plt.ylabel("Componente principal 2")
plt.tight_layout()
plt.savefig("clusters_pca.png")

print("\nArchivos generados:")
print("- metodo_codo.png")
print("- puntaje_silueta.png")
print("- clusters_pca.png")
print("- resultados_clusters_transporte.csv")
print("\nProceso finalizado correctamente.")
