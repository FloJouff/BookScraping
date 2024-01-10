## Etapes à suivre pour l'installation et l'utilisation du script d'extraction de "Books_to_scrap"

### Etapes d'installation:

#### Faire une copie du repository.

A partir du lien GitHub: https://github.com/FloJouff/BookScraping.git, créer un clone du projet en local sur votre ordinateur


#### Création de l'environnement virtuel 

Depuis votre terminal, à la racine du projet, créer un environnement virtuel, afin d'y installer uniquement les paquets Python nécessaires à l'exécution du script.

    $ python -m venv env
    $ ls
    all_books_scrap.py      env      requirements.txt       README.md

#### Créer les dossiers /images et /fichiers_csv 

A la racine du projet, créer ces deux dossiers, qui permettront d'y enregistrer les données extraites

#### Activation de l'environnement virtuel

A partir du terminal, taper la commande suivante:

    $ source env/bin/activate (pour MacOs, Linux)
    $ env\scripts\activate (pour Windows)

#### Installation des paquets Python nécessaires à l'execution du code: 

le fichier --requirements.txt-- été cloné à partir du repository GitHub.
A partir du terminal, taper la commande suivante:
   
    $ pip install -r requirements.txt

Une fois l'installation terminée, taper la commande suivante pour vous assurer de l'installation correcte des modules requis:

    $ pip freeze

Les paquets, ainsi que leurs dépendances doivent apparaitre (les versions peuvent être différentes):

    beautifulsoup4==4.12.2
    certifi==2023.11.17
    charset-normalizer==3.3.2
    idna==3.6
    requests==2.31.0
    soupsieve==2.5
    urllib3==2.1.0


### Exécution du code d'application:

#### Lancer le script à partir du terminal: 

Vous pouvez enfin exécuter le script all_books_scrap.py correctement, à partir d'un terminal:

    $ Python all_books_scrap.py

Une fois le script lancé, il faut entre 25 et 30 min pour extraire toutes les données, qui seront automatiquement enregistrées dans les dossiers créés : /images et /fichiers_csv

### Consultation des données:

Le dossier /images contient les images de toutes les pages de couvertures, de chaque livre, classées par catégories.

le dossier /fichiers_csv contient les données extraites pour chaque livre, classées par catégories.

Pour consulter les fichiers csv, il faut les ouvrir avec Excel ou équivalent:
    Sur Excel:
    - "Data" (ou données)
        - "From Text"
            - Sélectionner le fichier à consulter --> "get-data"
                - "Delimited" --> "Next"
                    - "Comma" (ou virgules) --> "next"
                        - "Finish" puis "ok"