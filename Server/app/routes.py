try:
    from app import app
    from firebase_admin import db
    from flask_googlemaps import Map
    from datetime import datetime as dt
    from flask import render_template, Response, abort
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# Firebase methods
def get_coordinates():
    ref = db.reference("/Coordinates")
    result = ref.get()
    for key in result.keys():
        result_key = key

    print(result[result_key])
    return result[result_key]# Returns dicctionary {'latitude': 19.362534, 'longitude': -99.249061}

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.now()
    }

# -------------Endpoints-------------
@app.route("/", methods=["GET"])# Mapa de google maps para las coordenadas
def my_map():
    try:
        coordinates = get_coordinates()
        mymap = Map(identifier="view-center",
        varname="mymap",
        style="height:1520px;width:1900px;margin:0;",
        lat=coordinates["latitude"],
        lng=coordinates["longitude"],
        zoom=19,
        markers=[(coordinates["latitude"], coordinates["longitude"])])

        return render_template("googlemap.html", pageTitle= "Map", mymap=mymap)
    except Exception:
        abort(500)

@app.route("/sendemail", methods=["POST"])# Endpoint para mandar el correo que se llamará desde otro lado
def send_email():
    respCode = 200
    respJSON = {}

    return Response(respJSON, mimetype="application/json"), respCode