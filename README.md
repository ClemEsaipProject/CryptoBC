# **Projet Blockchain**
*Description*
Ce projet implémente une blockchain simple en Python. 
Il permet de créer des transactions, de les vérifier, de les afficher, d'altérer des blocs et de valider la chaîne de blocs.
 Chaque fois que 10 transactions sont ajoutées, un nouveau bloc est créé dans la chaîne.
# **Fonctionnalités**
* Ajouter une transaction : Permet d'ajouter une nouvelle transaction à la blockchain.
* Vérifier une transaction : Vérifie l'existence d'une transaction dans la blockchain en utilisant son ID.
* Afficher les 10 dernières transactions : Affiche les 10 dernières transactions ajoutées à la blockchain.
* Altérer un bloc : Permet d'altérer une transaction existante dans un bloc.
* Valider la blockchain : Vérifie l'intégrité de la blockchain et s'assure qu'aucun bloc n'a été altéré.
# *Prérequis*
Python 3.x
Aucune bibliothèque externe n'est nécessaire pour ce projet.
# Installation
Clonez le dépôt :
* ``[git clone https://github.com/ClemEsaipProject/CryptoBC.git``
* ``cd CryptoBC``

(Facultatif) Créez un environnement virtuel :
Création de l'environnement virtuel
``python -m venv venv``


# Installation des dépendances
``pip install -r requirements.txt``

# Utilisation
Exécutez le programme principal :
``python main.py``
Suivez les instructions à l'écran pour interagir avec la blockchain.

*Structure du projet*
```
blockchain-project/
│
├── main.py            # Point d'entrée du programme
├── blockchain.py      # Classe Blockchain et gestion des blocs
├── block.py           # Classe Block pour gérer les blocs individuels
└── transaction.py     # Classe Transaction pour gérer les transactions
```

