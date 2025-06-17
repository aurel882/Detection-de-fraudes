# Détection d'Anomalies sur des Transactions Bancaires

## Description du projet

Ce projet Python vise à détecter des transactions bancaires potentiellement frauduleuses à l’aide de méthodes de détection d’anomalies. En combinant plusieurs approches statistiques et algorithmiques, on identifie les transactions les plus suspectes à partir d’un fichier Excel de données financières.

L’objectif final est d’isoler les transactions considérées comme anormales par toutes les méthodes utilisées, pour maximiser la fiabilité de la détection.

---

## Méthodes utilisées

Le script applique cinq techniques différentes de détection d’anomalies :

- Z-Score (approche statistique)
- Isolation Forest (apprentissage non supervisé)
- DBSCAN (clustering basé sur la densité)
- Local Outlier Factor (LOF)
- One-Class SVM

---

## Fonctionnalités principales

- Chargement et prétraitement des données :
  - Formatage de la date
  - Encodage de la variable `type_operation`
- Analyse statistique et visualisations :
  - Histogramme et boxplot des montants
- Détection d’anomalies via cinq méthodes
- Identification des transactions détectées comme anormales par toutes les méthodes
- Export automatique du résultat final en CSV
- Suppression de la colonne `is_fraud` si elle existe (nettoyage)

---

## Structure du code

1. Import des bibliothèques
2. Chargement des données Excel
3. Prétraitement :
   - Formatage des dates
   - Encodage des variables catégorielles
4. Visualisation des montants
5. Détection des anomalies :
   - Z-Score
   - Isolation Forest
   - DBSCAN
   - LOF
   - One-Class SVM
6. Fusion des résultats : intersection des indices anormaux
7. Nettoyage (suppression éventuelle de `is_fraud`)
8. Export des anomalies finales en `.csv`

---

## Résultats

- Liste des transactions détectées comme anormales pour chaque méthode
- Visualisation temporelle des anomalies (exemple : Isolation Forest)
- Intersection des cinq méthodes pour une détection de haute confiance
- Export final dans un fichier :  
  `anomalies_finales.csv`

---

## Améliorations possibles

- Ajouter de nouvelles features (moyen de paiement, localisation, etc.)
- Automatiser l’optimisation des hyperparamètres (par exemple `eps` pour DBSCAN)
- Implémenter un système de vote pondéré entre les méthodes
- Créer une interface utilisateur ou une API REST pour faciliter l'utilisation

---

## Licence

Ce projet est libre d’utilisation et de modification sous licence MIT.
