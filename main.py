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

# 🔹 3. Suppression des valeurs infinies et aberrantes
num_cols = df.select_dtypes(include=['float64', 'float32', 'int64']).columns

# Remplacement des valeurs infinies par la valeur maximale de la colonne
for col in num_cols:
    df[col] = df[col].replace([np.inf, -np.inf], np.nan)  # Transformer inf en NaN
    df[col] = df[col].fillna(df[col].median())  # Remplacer NaN par la médiane

# Suppression des valeurs aberrantes (IQR method)
Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[~((df[num_cols] < lower_bound) | (df[num_cols] > upper_bound)).any(axis=1)]

print("\n✅ Suppression des valeurs infinies et des outliers effectuée.")

# 🔹 4. Conversion des types de données (float64 → float32 pour économiser de la mémoire)
df[num_cols] = df[num_cols].astype('float32')

print("\n✅ Conversion des types de données effectuée.")

# 🔹 5. Encodage des labels (trafic normal vs attaques)
if 'Label' in df.columns:
    encoder = LabelEncoder()
    df['Label'] = encoder.fit_transform(df['Label'])  # Normal (0) / Attaque (1+ pour plusieurs types)

print("\n✅ Encodage des labels effectué.")

# 🔹 6. Normalisation des valeurs numériques
scaler = StandardScaler()

# Vérification que les valeurs sont finies avant normalisation
if np.isfinite(df[num_cols]).all().all():
    df[num_cols] = scaler.fit_transform(df[num_cols])
    print("\n✅ Normalisation des valeurs numériques effectuée.")
else:
    print("\n⚠️ Attention : Certaines valeurs sont encore infinies ou NaN après nettoyage.")

# 🔹 7. Vérification après nettoyage
print("\n📌 Après nettoyage :")
print(df.info())

# 🔹 8. Sauvegarde du dataset nettoyé
df.to_csv("CSE-CIC-IDS2018_cleaned.csv", index=False)
print("\n✅ Dataset nettoyé enregistré sous 'CSE-CIC-IDS2018_cleaned.csv'.")
