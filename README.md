

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


