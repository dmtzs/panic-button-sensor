try:
    from flask import Flask
    from flask_googlemaps import GoogleMaps
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

app= Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyA6TDHaUUCPJ0qn0TwB8If3HNsOKh-sPDU"# Se supone es la misma clave de API que me dan y que uso en el ESP32
# app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"
GoogleMaps(app)

from app import routes, admin_routes, errorHandlers