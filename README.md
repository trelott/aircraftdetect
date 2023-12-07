# Aircraft detect API

## Initialisation:

Pour télécharger le projet: ```git clone https://github.com/trelott/aircraftdetect.git```

Pour lancer le projet: ```docker compose up -d```

## Utilisation:

### POST /image

Pour traiter et stocker une image, il faut effectuer une requête POST sur http://localhost:8000/image. Cette requête devra contenir un champ "file" contenant l'image.

### GET /image/{id}

Pour récupérer une image, il faut effectuer une requête GET sur http://localhost:8000/image/{id} avec "{id}" remplacé par l'id de l'image.

### GET /search

Pour récupérer l'ensemble des informations de la base, il faut effectuer une requête GET sur http://localhost:8000/search.

### GET /search/type/{type}

Pour récupérer l'ensemble des informations concernant un type d'appareil en particulier, il faut effectuer une requête GET sur http://localhost:8000/search/type/{type} avec "{type}" le type d'appareil recherché.

### GET /search/image_id/{image_id}

Pour récupérer l'ensemble des informations concernant une image en particulier, il faut effectuer une requête GET sur http://localhost:8000/search/image_id/{image_id} avec "{image_id}" l'id de l'image concernée.