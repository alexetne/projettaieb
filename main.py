import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 📌 Charger un fichier CSV (ajuster le chemin selon l'emplacement du fichier)
file_path = "02-14-2018.csv"
df = pd.read_csv(file_path)

print("\n📌 Avant le nettoyage :")
print(df.info())

# 🔹 1. Suppression des doublons
initial_rows = df.shape[0]
df = df.drop_duplicates()
print(f"\n✅ Suppression des doublons : {initial_rows - df.shape[0]} lignes supprimées.")

# 🔹 2. Gestion des valeurs manquantes
missing_values = df.isnull().sum()
missing_cols = missing_values[missing_values > 0].index.tolist()

# Suppression des colonnes avec trop de valeurs manquantes (>30%)
threshold = 0.3 * df.shape[0]
cols_to_drop = [col for col in missing_cols if missing_values[col] > threshold]
df = df.drop(columns=cols_to_drop)
print(f"✅ Colonnes supprimées à cause de valeurs manquantes : {cols_to_drop}")

# Remplacement des valeurs manquantes restantes par la médiane
for col in missing_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

print("\n✅ Valeurs manquantes traitées.")

# 🔹 3. Conversion des types de données (float64 → float32 pour économiser de la mémoire)
num_cols = df.select_dtypes(include=['float64']).columns
df[num_cols] = df[num_cols].astype('float32')

print("\n✅ Conversion des types de données effectuée.")

# 🔹 4. Encodage des labels (trafic normal vs attaques)
if 'Label' in df.columns:
    encoder = LabelEncoder()
    df['Label'] = encoder.fit_transform(df['Label'])  # Normal (0) / Attaque (1+ pour plusieurs types)

print("\n✅ Encodage des labels effectué.")

# 🔹 5. Normalisation des valeurs numériques
scaler = StandardScaler()
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

print("\n✅ Normalisation des valeurs numériques effectuée.")

# 🔹 6. Vérification après nettoyage
print("\n📌 Après nettoyage :")
print(df.info())
print("\n✅ Nettoyage des données terminé !")

# 🔹 7. Sauvegarde du dataset nettoyé
df.to_csv("CSE-CIC-IDS2018_cleaned.csv", index=False)
print("\n✅ Dataset nettoyé enregistré sous 'CSE-CIC-IDS2018_cleaned.csv'.")
