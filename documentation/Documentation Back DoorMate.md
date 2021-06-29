
# Documentation Back DoorMate

Le back est codé en python et utilise le framework Django Rest


## Architecture :

![enter image description here](https://bezkoder.com/wp-content/uploads/2020/04/django-rest-api-tutorial-example-architecture.png)


- Les requêtes HTTP seront mises en correspondance avec les modèles d'URL et transmises aux vues

- Views traite les requêtes HTTP et renvoie les réponses HTTP (à l'aide de Serializer)

- Les serializers sérialise/désérialise les objets du modèle de données (la sérialisation est le codage d'une information sous la forme d'une suite d'informations plus petites)

- Les modèles contiennent des champs et des comportements essentiels pour les opérations CRUD avec base de données

## Structure du back :

![enter image description here](https://cdn.discordapp.com/attachments/710948740319674368/859424045736001547/Capture_decran_2021-06-29_a_01.21.22.png)

- croomies_api/**apps.py** : Contient le AppConfig (django.apps.AppConfig) qui définit le nom et la configuration de l’application.

- croomies/settings/**development.py & production.py :** Contient les paramètres de notre projet Django : moteur de base de données, liste des INSTALLED_APPS avec le framework Django REST, CORS et MIDDLEWARE, il y’a deux configurations différentes, une pour les tests en local (development.py) et une pour la production c’est-à-dire la « vrai » configuration (production.py)

- croomies_api/**models.py** : définit la classe de modèle de données (sous-classe de django.db.models.Model)

- croomies_api/**migrations** : est créé lorsque nous effectuons des migrations pour le modèle de données et sera utilisé pour générer la table de base de données.

- croomies_api/**serializers.py** : gère la sérialisation et la désérialisation avec la classe rest_framework.serializers.ModelSerializer).

- croomies_api/**views.py** : contient des fonctions pour traiter les requêtes HTTP et produire des réponses HTTP (à l'aide de django.db.models).

- croomies/**urls.py :** définit les modèles d'URL ainsi que les fonctions de request dans les vues.c’est le fichier root urls

## Listes des routes dans urls.py :

'admin/' Donne accès au panel admin en ligne django.

'api/' Racine des urls de l’application.

'api/register/' Route d’inscription

'api/login_croomies/<str:email>/<str:mdp>' Route de login prenant en param email et mdp.

'api/logout/' route de logout.

'api/logoutall/' route pour logout tous les users.

'api/habitation/' Route pour ajouter des habitations et les listées.

'api/habitation/<int:habitation_id>/' Route pour obtenir une habitation par ID.

'api/habitation/withuser/' Route qui liste les habitations avec les users dedans.

'api/habitation/geo/<str:param>/' Filtre prenant l’adresse en paramètre pour afficher les habitations correspondantes.

'api/habitation/prices/<int:priceMin>/<int:priceMax>/' Filtre prenant le budget min et max pour afficher les habitations correspondantes.

'api/habitation/dates/<str:datebegin>/<str:dateending>/' Filtre prenant la date de début et de fin pour afficher les habitations correspondantes.

'api/habitation/filters/<str:param>/<int:priceMin>/<int:priceMax>/<str:datebegin>/<str:dateending>/' Filtre combinant le filtre geo, prices et dates.

'api/sport/' Route pour ajouter des sports et les listés.

'api/film/' Route pour ajouter des films et les listés.

'api/music/' Route pour ajouter des genres musicaux et les listés.

'api/sport_user/' Table de liaison sport -> user.

'api/film_user/' Table de liaison film -> user.

'api/music_user/' Table de liaison musique -> user.

'api/media/' Route permettant d’ajouter des images de profil / image de colocation et les listées.

'api/address/' Route permettant d’ajouter des adresses d’habitation et les listées.

'api/croomiesuser/' Route permettant d’ajouter des users et les listés.

'api/croomiesuser/<int:croomieuser_id>/' Route pour obtenir un user par ID.

'api/seeker/' Route permettant d’ajouter des seeker (manuellement) et les listés.

'api/matching/' Route permettant d’ajouter des matching et les listés.

'api/roomate_in_habitation/' Route permettant d’ajouter des relations entre user et habitation et les listés.

'api/media_habitation/' Route permettant d’ajouter des relations entre media et habitation et les listés.

'api/time_slots/' Route permettant d’ajouter des heures de RDV et les listés.

'api/date_slots/' Route permettant d’ajouter des dates de RDV et les listés.

'api/visite/' Route permettant d’ajouter des visites et les listés.

'api/application/' Route permettant d’ajouter des demandes et les listés.

'api/register_seeker/' Route permettant d’ajouter des seekers et les listés.

## La BDD
![enter image description here](https://cdn.discordapp.com/attachments/819251742553931799/859037010542329907/myapp_models.png)
