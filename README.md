Vous trouverez ici différents scripts vous permettant d'extraire les données des articles du site https://books.toscrape.com/.

Veuillez lire les instructions qui suivent. Elles vous permettront de paramétrer le projet et d'exécuter les différents scripts.

## Paramétrage 

- Cloner le repository 
- Créer un environnement virtuel à la racine du projet
- Utiliser la commande *$ pip install -r requirements.txt* pour installer les modules et paquets nécessaires automatiquement

## Exécution des différents scripts
Lors de l'exécution de chaque script, un dossier *data* sera créé à la racine du projet s'il n'existe pas. Vous trouverez à l'intérieur un dossier portant le nom du script correspondant qui contiendra les données extraites.
### Script 1 : récupérer les données d'un article

- Ouvrir *script_1.py* dans un éditeur
- Renseigner l'URL de la page voulue dans la variable *url* de la section *Setup* 
- Exécuter le script

### Script 2 : récupérer les données des articles d'une catégorie

- Ouvrir *script_2.py* dans un éditeur
- Renseigner l'URL de la catégorie dans la variable *category_url* de la section *Setup*
- Exécuter le script

*Si vous souhaitez relancer le script plusieurs fois pour la même catégorie, il est préférable de supprimer le dossier **script_2** dans le dossier **data** avant de le relancer. Dans le cas contraire, les données seront ajoutées une nouvelle fois à la suite du fichier CSV existant.*

### Script 3 : récupérer les données de tous les articles du site par catégorie

- Exécuter le script tel quel, l'URL du site est déjà renseignée dans le script

*Si vous souhaitez relancer le script plusieurs fois, il est préférable de supprimer le dossier **script_3** dans le dossier **data** avant de le relancer. Dans le cas contraire, les données seront ajoutées une nouvelle fois à la suite des fichiers CSV existants pour chaque catégorie.*