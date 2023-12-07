# Docker-test

Pour lancer l'API aircraftdetector: ```docker compose up```

Pour obtenir le résultat de l'analyse d'une image, il faut ensuite effectuer une requête POST à l'adresse http://localhost:8000/ avec un champ "file" contenant le fichier à analyser.

Exemple de la requête en python: ```requests.post("http://localhost:8000/", files={"file": open(imagePath, "rb")})```

