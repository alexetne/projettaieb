# Installation de l'environnement Python

Ce projet nécessite Python 3 et utilise un environnement virtuel pour la gestion des dépendances.

## Prérequis
- **Python 3** est installé sur la machine. On vérifie la version installée avec :
  ```sh
  python3 --version
  ```

## Création et activation de l'environnement virtuel

1. Créez un environnement virtuel :
   ```sh
   python3 -m venv env
   ```

2. Activez l'environnement virtuel :
   - **Sur Linux** :
     ```sh
     source env/bin/activate
     ```


## Installation des dépendances

Une fois l'environnement activé, installez les dépendances du projet :
```sh
pip install -r requirements.txt
```

## Désactivation de l'environnement virtuel

Pour quitter l'environnement virtuel, on execute :
```sh
deactivate
```

## Vérification des dépendances installées

on pe vérifier les packages installés avec :
```sh
pip list
```

## Exécution du projet

Pour lancer votre projet après l'installation des dépendances, utilisez la commande spécifique à votre projet.



