try:
    import os
    import firebase_admin
    from flask import Flask
    from firebase_admin import credentials
    from flask_googlemaps import GoogleMaps
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

app= Flask(__name__)

cred = credentials.Certificate(os.path.realpath("geolocation.json"))# Importante, el archivo debe estar a la misma altura de runApp.py forzosamente y correr el app estando en ese directorio
url_database = {"databaseURL": "databaseURL"}#TODO: In prod change this part
firebase_admin.initialize_app(cred, url_database)

app.config['GOOGLEMAPS_KEY'] = "yourApiKey"# Se supone es la misma clave de API que me dan y que uso en el ESP32
GoogleMaps(app)

from app import routes, admin_routes, errorHandlers