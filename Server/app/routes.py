try:
    from app import app
    import datetime as dt
    from flask import render_template, Response, request, abort
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.datetime.now()
    }

# -------------Endpoints-------------
@app.route("/", methods=["GET"])# Mapa de google maps para las coordenadas
def index():
    return render_template("googlemap.html", pageTitle= "Map")

@app.route("/sendemail", methods=["POST"])# Endpoint para mandar el correo que se llamará desde otro lado
def send_email():
    respCode = 200
    respJSON = {}

    return Response(respJSON, mimetype="application/json"), respCode