import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import LocalOutlierFactor
from sklearn.cluster import DBSCAN
from sklearn.svm import OneClassSVM

# On lit le fichier Excel contenant les transactions
df = pd.read_excel("C:/Users/bress/DOCUMENTS/Projet pythoon/transactions.xlsx")

# On s'assure que la colonne 'date' est bien au format datetime
df['date'] = pd.to_datetime(df['date'])

# Aperçu rapide du dataset
print(df.head())
print(df.info())
print(df.describe())
print(df['pays'].value_counts())
print(df['type_operation'].value_counts())

# Visualisation de la distribution des montants
plt.figure(figsize=(10, 5))
sns.histplot(df['montant'], bins=50, kde=True)
plt.title("Distribution des montants")
plt.show()

# Boxplot pour repérer les valeurs extrêmes visuellement
plt.figure(figsize=(10, 2))
sns.boxplot(x=df['montant'])
plt.title("Boxplot des montants")
plt.show()


# MÉTHODE 1 : Z-SCORE
df['zscore'] = zscore(df['montant'])
outliers_z = df[abs(df['zscore']) > 3]
print("Anomalies détectées avec Z-Score :")
print(outliers_z[['transaction_id', 'montant', 'zscore']])


# Encodage de la variable catégorielle 'type_operation' pour les modèles

df_encoded = df.copy()
le_type = LabelEncoder()
df_encoded['type_operation_encoded'] = le_type.fit_transform(df['type_operation'])


# MÉTHODE 2 : Isolation Forest

features_if = df_encoded[['montant', 'type_operation_encoded']]
model_iforest = IsolationForest(contamination=0.05, random_state=42)
df_encoded['anomaly_iforest'] = model_iforest.fit_predict(features_if)

print("\nAnomalies Isolation Forest :")
print(df_encoded[df_encoded['anomaly_iforest'] == -1][['transaction_id', 'montant', 'anomaly_iforest']])

# Affichage des anomalies sur un graphique temporel
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_encoded, x='date', y='montant', hue='anomaly_iforest', palette={1: 'blue', -1: 'red'})
plt.title("Isolation Forest : Anomalies")
plt.show()


# MÉTHODE 3 : DBSCAN

features_db = StandardScaler().fit_transform(features_if)
dbscan = DBSCAN(eps=0.5, min_samples=5)
df_encoded['anomaly_dbscan'] = dbscan.fit_predict(features_db)

# Les points avec le label -1 sont considérés comme des anomalies
print("\nAnomalies DBSCAN :")
print(df_encoded[df_encoded['anomaly_dbscan'] == -1][['transaction_id', 'montant', 'type_operation']])


# MÉTHODE 4 : Local Outlier Factor

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
df_encoded['anomaly_lof'] = lof.fit_predict(features_if)

print("\nAnomalies LOF :")
print(df_encoded[df_encoded['anomaly_lof'] == -1][['transaction_id', 'montant', 'type_operation']])


# MÉTHODE 5 : One-Class SVM
svm = OneClassSVM(kernel='rbf', nu=0.05, gamma='auto')
df_encoded['anomaly_ocsvm'] = svm.fit_predict(features_db)

# Ici aussi, les -1 représentent les transactions suspectes
print("\nAnomalies One-Class SVM :")
print(df_encoded[df_encoded['anomaly_ocsvm'] == -1][['transaction_id', 'montant', 'type_operation']])


# Résumé du nombre d'anomalies détectées par chaque méthode

print("\nRésumé des anomalies détectées :")
print("Z-Score (>3) :", outliers_z.shape[0])
print("Isolation Forest :", (df_encoded['anomaly_iforest'] == -1).sum())
print("DBSCAN :", (df_encoded['anomaly_dbscan'] == -1).sum())
print("LOF :", (df_encoded['anomaly_lof'] == -1).sum())
print("One-Class SVM :", (df_encoded['anomaly_ocsvm'] == -1).sum())



# Détection des anomalies détectées par les 5 méthodes


# On récupère les indices des anomalies pour chaque méthode
idx_zscore = set(outliers_z.index)
idx_iforest = set(df_encoded[df_encoded['anomaly_iforest'] == -1].index)
idx_dbscan = set(df_encoded[df_encoded['anomaly_dbscan'] == -1].index)
idx_lof = set(df_encoded[df_encoded['anomaly_lof'] == -1].index)
idx_ocsvm = set(df_encoded[df_encoded['anomaly_ocsvm'] == -1].index)

# Intersection : anomalies communes aux 5 approches
idx_communs = idx_zscore & idx_iforest & idx_dbscan & idx_lof & idx_ocsvm

# On extrait ces transactions du DataFrame initial
anomalies_finales = df.loc[list(idx_communs)]

print("\n=== Transactions considérées comme RÉELLEMENT ANORMALES (détectées par les 5 méthodes) ===")
print(anomalies_finales[['transaction_id', 'date', 'montant', 'type_operation', 'pays']])
print(f"\nNombre total de transactions réellement anormales : {len(anomalies_finales)}")
