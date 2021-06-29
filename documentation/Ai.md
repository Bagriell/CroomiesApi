# Doormate AI documentation

## General

L'IA au sein de l'API est utilisée sur la "/route register_seeker" afin de d'attribuer un cluster à chaque utilisateur s'inscrivant sur l'application mobile **Doormate** en fonction des informations renseignée par ce dernier.

## Fichiers

Les modèles et scripts nécessaires au bon fonctionnement de l'IA de situe dans le répertoire: "/croomies_api/IA/".

### Modèles
- cluster_model.pkl: modèle de clusterisation provenant d'un Kmeans de la librairie scikit-learn. Il est le résultat d'un entrainnement avec les données du site de rencontre Okcupid.
- pipeline_model.pkl: modèle pipeline permettant de préparer les données; notamment à encoder en vue d'une prédiction avec le modèle de clusterisation.

### Scripts
- ai-doormate-mvp.ipynb: jupyter notebook créant les modèles à partir des données Okcupid.
- format_data.py: script utilisé pour nettoyer la donnée et renvoyer une prédiction.

## Evolutions

Le modèle de clusterisation utilisé pour la prediction sera amené à évoluer lorsque sufisemment d'utilisateur seront inscrits sur la plateforme.
Pour des questions d'optimisation il serait judicieux de charger en mémoire les modèles dès l'instanciation du l'API.
Le scripts permettant la prediction propose pour le moment une utilisatin assez rigide, il serait interessant de l'optimiser et de le rendre plus souple d'utilisation.
Une version experimentale de detection de harcèlement n'est pas utilisée car pas assez aboutie mais sera cruciale afin de proposer une fonctionnalité de messagerie saine.