# Mon Portfolio Django (Monolithe Modulaire)

🛠️Architecture du ProjetLe projet respecte une séparation stricte des fonctionnalités. Voici la structure réelle du dépôt :
📂 portfolio_root/
 ┃
 ┣ 📂 contact/                 # Application Django : Gestion des messages des visiteurs
 ┣ 📂 portfolio électronique/   # Application Django : Vitrine des projets et compétences
 ┣ 📂 pages/                   # Application Django : Gestion des pages statiques/principales
 ┃
 ┣ 📂 médias/                  # Stockage des fichiers médias téléversés (images, pdf)
 ┣ 📂 fichiers statiques/       # Fichiers CSS, JS et images globaux du projet
 ┣ 📂 ressources statiques/     # Sources ou assets bruts du projet
 ┣ 📂 modules Node/            # Dépendances Node.js (npm) pour le frontend
 ┃
 ┣ 📄 .env.exemple             # Modèle de configuration des variables d'environnement
 ┣ 📄 .gitignore               # Fichiers à exclure du suivi Git
 ┣ 📄 db.sqlite3               # Base de données locale de développement
 ┣ 📄 gérer.py                 # Script de gestion Django (manage.py)
 ┣ 📄 package.json             # Configuration des scripts et dépendances npm
 ┣ 📄 package-lock.json        # Verrouillage des versions npm
 ┗ 📄 requirements.txt         # Dépendances Python/Django du projet

  # Architecture des Modules DjangoChaque application (contact, portfolio électronique, pages) 
 est totalement autonome et contient :Ses propres modèles (models.py) pour la gestion des données.
 Ses propres routes (urls.py) pour l'isolation des URLs.Ses propres tests (tests.py) pour garantir la robustesse de chaque module de manière indépendante.

 # Installation et Lancement Local1. Prérequis Python & DjangoClonez le dépôt, créez votre environnement virtuel, puis installez les dépendances :

 # Installer les paquets Python
pip install -r requirements.txt

# Configurer vos variables d'environnement
cp .env.exemple .env

# Appliquer les migrations de la base de données
python gérer.py migrate

# Lancer le serveur de développement
python gérer.py runserver

