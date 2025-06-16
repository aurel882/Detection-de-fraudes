# Détection de Fraudes sur Transactions Bancaires

## Description du projet

Ce projet vise à détecter des transactions financières frauduleuses ou anormales à partir d’un jeu de données de transactions bancaires. Plusieurs méthodes d'analyse des anomalies sont appliquées pour identifier des transactions suspectes.

Le script Python traite un fichier Excel contenant des transactions, analyse la distribution des montants, et utilise différentes techniques de détection d'anomalies :

- Méthode statistique : Z-Score
- Algorithmes d’apprentissage automatique non supervisés :
  - Isolation Forest
  - DBSCAN (clustering)
  - Local Outlier Factor (LOF)
  - One-Class SVM

Le but est d’identifier des transactions qui pourraient indiquer une fraude, avec une approche robuste combinant plusieurs méthodes.

---

## Fonctionnalités principales

- Chargement et prétraitement des données (formatage des dates, encodage des variables catégorielles)
- Visualisation des données (histogramme et boxplot des montants)
- Détection d’anomalies via 5 méthodes différentes
- Visualisation des anomalies détectées (exemple avec Isolation Forest)
- Synthèse et comparaison des résultats
- Identification des transactions anormales détectées par **toutes** les méthodes (intersection)

---

## Résultats

- Le script affiche les transactions considérées comme anormales selon chaque méthode.
- Un graphique montre la répartition des anomalies détectées par Isolation Forest dans le temps.
- En sortie finale, il affiche la liste des transactions considérées anormales par **toutes les méthodes** (intersection des résultats), pour un niveau de confiance plus élevé.

---

## Structure du code

- Import des librairies
- Chargement et prétraitement des données
- Visualisation exploratoire
- Implémentation et exécution des 5 méthodes de détection d’anomalies
- Affichage et comparaison des anomalies détectées
- Extraction des anomalies communes aux 5 méthodes

---

## Améliorations possibles

- Ajouter plus de variables/features (ex : localisation GPS, moyen de paiement)
- Automatiser la recherche de paramètres optimaux pour chaque méthode (ex : `eps` pour DBSCAN)
- Intégrer une méthode de fusion ou de vote pondéré des anomalies détectées
- Mettre en place une interface utilisateur ou une API pour faciliter l’analyse

---

## Licence

Ce projet est libre d'utilisation et de modification sous licence MIT.
