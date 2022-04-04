try:
    from app import app
    from flask_googlemaps import Map
    from datetime import datetime as dt
    from flask import render_template, Response, request, abort
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

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
        mymap = Map(identifier="view-center",
        varname="mymap",
        style="height:1520px;width:1900px;margin:0;",
        lat=19.362534,
        lng=-99.249061,
        zoom=19,
        markers=[(19.362534, -99.249061)])

        return render_template("googlemap.html", pageTitle= "Map", mymap=mymap)
    except Exception:
        abort(500)

@app.route("/sendemail", methods=["POST"])# Endpoint para mandar el correo que se llamará desde otro lado
def send_email():
    respCode = 200
    respJSON = {}

    return Response(respJSON, mimetype="application/json"), respCode