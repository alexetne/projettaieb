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

# -----------------------------------
# 🔹 9. ANALYSE STATISTIQUE DESCRIPTIVE
# -----------------------------------

print("\n📊 ANALYSE STATISTIQUE DESCRIPTIVE")

# 🔹 Statistiques générales des variables numériques
print("\n📌 Statistiques générales des variables numériques :")
print(df.describe())

# 🔹 Distribution des classes (trafic normal vs attaques)
plt.figure(figsize=(8, 4))
sns.countplot(y=df['Label'], order=df['Label'].value_counts().index, palette="coolwarm")
plt.title("📊 Distribution des classes (trafic normal vs attaques)")
plt.xlabel("Nombre d'échantillons")
plt.ylabel("Classes")
plt.show()

# 🔹 Histogramme des variables clés
key_features = ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'Fwd Packet Length Max']
key_features = [col for col in key_features if col in df.columns]  # Vérification que les colonnes existent

if key_features:
    df[key_features].hist(figsize=(12, 8), bins=50, color='skyblue')
    plt.suptitle("📊 Histogrammes des variables clés")
    plt.show()

# 🔹 Matrice de corrélation des 10 premières variables
plt.figure(figsize=(12, 8))
corr_matrix = df[num_cols].corr()
sns.heatmap(corr_matrix.iloc[:10, :10], annot=True, cmap='coolwarm', fmt=".2f")
plt.title("🔍 Matrice de Corrélation (10 premières variables)")
plt.show()

print("\n✅ Analyse statistique descriptive terminée !")


# 📌 Charger le dataset nettoyé
file_path = "CSE-CIC-IDS2018_cleaned.csv"
df = pd.read_csv(file_path)

print("\n📊 ANALYSE VISUELLE DES DONNÉES")

# 🔹 Vérifier si les données sont déjà normalisées
if df.select_dtypes(include=[np.number]).apply(lambda x: x.mean()).abs().max() < 1:
    print("\n⚠️ Attention : Les données semblent déjà normalisées (mean ≈ 0, std ≈ 1). Vérification requise avant toute normalisation.")
    
# 🔹 1. Distribution des classes (trafic normal vs attaques)
plt.figure(figsize=(8, 4))
sns.countplot(y=df['Label'], order=df['Label'].value_counts().index, hue=df['Label'], palette="coolwarm", legend=False)
plt.title("📊 Distribution des classes (trafic normal vs attaques)")
plt.xlabel("Nombre d'échantillons")
plt.ylabel("Classes")
plt.savefig("distribution_classes.png")  # Sauvegarde l'image
plt.close()

# 🔹 2. Histogrammes des principales caractéristiques
key_features = ['Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'Fwd Packet Length Max']
key_features = [col for col in key_features if col in df.columns]  # Vérification que les colonnes existent

if key_features:
    df[key_features].hist(figsize=(12, 8), bins=50, color='skyblue')
    plt.suptitle("📊 Histogrammes des principales variables")
    plt.savefig("histogrammes_variables.png")
    plt.close()

# 🔹 3. Boxplots pour identifier les valeurs aberrantes
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[key_features], palette="coolwarm")
plt.title("📊 Boxplots des principales variables pour détecter les outliers")
plt.xticks(rotation=45)
plt.savefig("boxplots_outliers.png")
plt.close()

# 🔹 4. Matrice de corrélation des 10 premières variables
plt.figure(figsize=(12, 8))
corr_matrix = df.select_dtypes(include=[np.number]).corr()
sns.heatmap(corr_matrix.iloc[:10, :10], annot=True, cmap='coolwarm', fmt=".2f")
plt.title("🔍 Matrice de Corrélation (10 premières variables)")
plt.savefig("matrice_correlation.png")
plt.close()

# 🔹 5. Pairplot des principales features (échantillonnage si trop grand)
sample_df = df.sample(n=5000, random_state=42) if df.shape[0] > 5000 else df

if len(key_features) > 1:
    sns.pairplot(sample_df[key_features + ['Label']], hue='Label', palette="coolwarm", diag_kind="kde")
    plt.suptitle("📊 Pairplot des principales variables en fonction des classes", y=1.02)
    plt.savefig("pairplot_variables.png")
    plt.close()

print("\n✅ Visualisation des données terminée ! Toutes les figures sont enregistrées.")
