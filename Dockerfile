# Utiliser l'image officielle légère de Python.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Permettre l'affichage immédiat des instructions et messages de log dans les journaux de Knative

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances nécessaires
RUN pip install -r requirements.txt

# Copier tout le contenu du répertoire local dans le conteneur
COPY . /app

# Exposer le port sur lequel l'application va fonctionner

# Définir la commande par défaut pour lancer l'application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000","--reload"]