# 📌 Projet de Détection d'Intrusions Réseau avec Random Forest

## 📖 Introduction
Ce projet vise à analyser un dataset de trafic réseau et à construire un modèle de machine learning basé sur **Random Forest** afin de détecter les attaques réseau. Le dataset utilisé contient diverses caractéristiques des paquets réseau ainsi qu'un label indiquant s'il s'agit d'un **trafic normal** ou d'une **attaque**.

---
## 📂 Structure du projet
```
├── .gitignore
├── 02-14-2018-2.csv
├── ex1.ipynb
├── ex2.ipynb
├── main.py
├── README.md
```

---
## 📊 Données
### 📥 Source des données
Le dataset utilisé est un ensemble de logs réseau capturés, contenant les caractéristiques des paquets et des connexions.

### 🏷️ En-têtes principales du dataset
- **Dst Port** : Port de destination
- **Protocol** : Protocole utilisé (TCP, UDP...)
- **Timestamp** : Horodatage du paquet
- **Flow Duration** : Durée totale du flux
- **Tot Fwd Pkts / Tot Bwd Pkts** : Nombre total de paquets envoyés/reçus
- **TotLen Fwd Pkts / TotLen Bwd Pkts** : Taille totale des paquets envoyés/reçus
- **Fwd Pkt Len Max/Min/Mean/Std** : Statistiques sur la taille des paquets en envoi
- **Bwd Pkt Len Max/Min/Mean/Std** : Statistiques sur la taille des paquets en réception
- **Flow Byts/s & Flow Pkts/s** : Débit en bytes et en paquets par seconde
- **Flags TCP (FIN, SYN, ACK, etc.)** : Indicateurs TCP
- **Idle Mean/Std/Max/Min** : Temps d'inactivité moyen et extrêmes
- **Label** : **0 = Normal**, **1 = Attaque**

---
## 🛠️ Prétraitement des données
1. **Chargement et exploration des données**
2. **Suppression des doublons**
3. **Gestion des valeurs manquantes** (remplacement par la médiane, suppression si nécessaire)
4. **Correction des types de données** (conversion des timestamps, normalisation des valeurs numériques)
5. **Encodage du label** (binarisation)
6. **Normalisation des caractéristiques** avec `StandardScaler`

---
## 🧠 Modèle de Machine Learning
### 📌 Modèle utilisé : **Random Forest Classifier**
**Hyperparamètres optimisés avec GridSearchCV** :
- `n_estimators = [50, 100, 200]`
- `max_depth = [10, 20, None]`
- `min_samples_split = [2, 5, 10]`

📊 **Séparation des données** : 80% Entraînement | 20% Test

**Évaluation du modèle** :
- **Accuracy**
- **Precision, Recall, F1-score**
- **Matrice de confusion**
- **ROC-AUC Score**
- **Feature Importance**

---
## 📈 Résultats et Visualisations
✅ **Performance du modèle optimisé** :
- **Accuracy** : `> 90%`
- **Recall** : `> 85%` (bonne capacité de détection des attaques)
- **Précision** : `> 80%` (faible taux de faux positifs)
- **AUC ROC** : `> 0.90` (bonne séparation des classes)

📌 **Visualisations :**
- Matrice de confusion normalisée
- Courbes ROC et Precision-Recall
- Analyse des Features les plus influentes (SHAP & Feature Importance)

---
## 🚀 Recommandations
🔹 **Optimisations possibles** :
- Tester d'autres modèles (**XGBoost, LightGBM, Deep Learning**)
- Ajouter de nouvelles données réseau pour enrichir l'entraînement
- Affiner l'équilibrage des classes (SMOTE, sous-échantillonnage)
- Déploiement en **temps réel** sur un SIEM (Splunk, ELK...)

---
## 📌 Comment utiliser ce projet ?
### 1️⃣ **Création de l'env**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2️⃣ **Installation des dép**
```bash
pip install -r requierment.txt
```

---
## 🔗 Auteurs et Contributions
Ce projet a été développé par [ETIENNE Alexandre].
Contributions et améliorations bienvenues ! 🚀

📩 **Contact** : [alex@etienne26.fr]

---
## 📜 Licence
Ce projet est sous licence **MIT** - Voir `LICENSE` pour plus d’informations.

