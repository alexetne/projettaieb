import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 📌 Charger un fichier CSV (ajuster le chemin selon l'emplacement du fichier)
file_path = "02-14-2018.csv"
df = pd.read_csv(file_path)

# 🔹 1. Aperçu du dataset
print("\n📌 Aperçu des premières lignes du dataset :")
print(df.head())

# 🔹 2. Informations générales sur le dataset
print("\n📌 Informations générales :")
print(df.info())

# 🔹 3. Nombre de lignes et de colonnes
print(f"\n📌 Nombre de lignes : {df.shape[0]}  |  Nombre de colonnes : {df.shape[1]}")

# 🔹 4. Vérification des valeurs manquantes
missing_values = df.isnull().sum()
missing_values = missing_values[missing_values > 0]  # On garde uniquement les colonnes avec des valeurs nulles
print("\n📌 Colonnes avec valeurs manquantes :")
print(missing_values)

# 🔹 5. Distribution des classes (trafic normal vs attaques)
plt.figure(figsize=(10, 5))
sns.countplot(y=df['Label'], order=df['Label'].value_counts().index)
plt.title("📊 Distribution des attaques et du trafic normal")
plt.show()

# 🔹 6. Statistiques descriptives des variables numériques
print("\n📌 Statistiques descriptives des variables numériques :")
print(df.describe())

# 🔹 7. Vérification des valeurs dupliquées
duplicates = df.duplicated().sum()
print(f"\n📌 Nombre de lignes dupliquées : {duplicates}")

# 🔹 8. Matrice de corrélation des 10 premières variables
plt.figure(figsize=(12, 8))
corr_matrix = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr_matrix.iloc[:10, :10], annot=True, cmap='coolwarm', fmt=".2f")
plt.title("🔍 Matrice de Corrélation (10 premières variables)")
plt.show()

print("\n✅ Évaluation des données terminée !")
