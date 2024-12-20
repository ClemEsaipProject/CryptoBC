# Utiliser une image Python officielle comme base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les dépendances
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application
COPY . .

# Exposer le port sur lequel votre application s'exécute
EXPOSE 8000

# Commande pour exécuter l'application
CMD ["python", "main.py"]
