# Utilise une image Python officielle
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port (ex. : Flask par défaut = 5000)
EXPOSE 5000

# Démarrer l'application avec gunicorn
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000"]