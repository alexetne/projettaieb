# Installation de l'environnement Python

Ce projet nécessite Python 3 et utilise un environnement virtuel pour la gestion des dépendances. L'utilisation d'un environnement virtuel garantit l'isolation des packages, évitant ainsi les conflits avec d'autres projets et maintenant un environnement stable.

## Prérequis
- **Python 3** est installé sur la machine. On vérifie la version installée avec :
  ```sh
  python3 --version
  ```

## Création et activation de l'environnement virtuel

Nous avons choisi d'utiliser `venv` car il est intégré à Python et permet une gestion simplifiée des dépendances sans nécessiter d'outils supplémentaires.

1. Créez un environnement virtuel :
   ```sh
   python3 -m venv env
   ```
   Cette commande crée un répertoire `env` contenant une copie indépendante de l'interpréteur Python et des bibliothèques standard.

2. Activez l'environnement virtuel :
   - **Sur Linux** :
     ```sh
     source env/bin/activate
     ```
   Une fois activé, les dépendances installées seront isolées dans cet environnement, évitant toute interférence avec d'autres projets.

## Installation des dépendances

Les dépendances du projet sont répertoriées dans le fichier `requirements.txt` pour assurer une installation cohérente sur toutes les machines de développement.

Une fois l'environnement activé, installez les dépendances du projet :
```sh
pip install -r requirements.txt
```
Cette commande installe toutes les bibliothèques listées dans `requirements.txt`, garantissant une compatibilité et une reproductibilité du projet.

## Désactivation de l'environnement virtuel

Pour quitter l'environnement virtuel, on exécute :
```sh
deactivate
```
Cette commande désactive l'environnement et vous ramène à votre installation globale de Python.

## Vérification des dépendances installées

On peut vérifier les packages installés avec :
```sh
pip list
```
Cela permet de s'assurer que toutes les bibliothèques nécessaires sont bien en place.

## Nettoyage et Préparation des Données

Après l'installation des dépendances, nous effectuons une **évaluation et un nettoyage des données** afin de garantir leur qualité et d'éviter les biais dans le modèle de Machine Learning.

### Évaluation de la qualité et de la quantité des données
Nous procédons à plusieurs analyses pour comprendre le dataset :
- **Structure des données** : Nombre de lignes, colonnes et types de données.
- **Présence de valeurs manquantes** : Identification des colonnes à nettoyer.
- **Distribution des classes** : Vérification de l'équilibre entre les attaques et le trafic normal.
- **Corrélation entre les variables** : Identification des caractéristiques influentes.

### Nettoyage des données
Nous effectuons plusieurs étapes pour améliorer la qualité des données :
- **Suppression des doublons** : Élimination des lignes identiques pour éviter des biais.
- **Gestion des valeurs manquantes** : Suppression des colonnes avec trop de valeurs nulles et remplacement des autres par la médiane.
- **Optimisation des types de données** : Conversion des valeurs float64 en float32 pour économiser de la mémoire.
- **Encodage des labels** : Transformation des valeurs catégoriques (`Label`) en valeurs numériques exploitables par le modèle.
- **Normalisation des valeurs numériques** : Mise à l'échelle des caractéristiques pour éviter que certaines variables ne dominent les autres dans l'apprentissage du modèle.

Un fichier nettoyé est ensuite généré sous le nom **`CSE-CIC-IDS2018_cleaned.csv`**, prêt à être utilisé pour l'entraînement d'un modèle de Machine Learning.

## Exécution du projet

Pour lancer votre projet après l'installation des dépendances et la préparation des données, utilisez la commande spécifique à votre projet.

---

Ce fichier peut être modifié en fonction des besoins spécifiques du projet.

