try:
    import json
    import smtplib
    from app import app
    from firebase_admin import db
    from flask_googlemaps import Map
    from datetime import datetime as dt
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
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

# Method to send email
def email_send(destiny_email):
    #send email 
    toaddr = destiny_email
    # fromaddr = "mmicros717@gmail.com"
    fromaddr = "eder1354684@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alarm geolocation"
    body="--------------------------------------------------------------------------- \n" + "Go and visit the next IP address: http://137.184.131.234/" + "\n--------------------------------------------------------------------------- "
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "passwd")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("Successfully sent mail ")

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

@app.route("/lastlocations", methods=["GET"])# Mapa de google maps para las coordenadas
def map_with_last_locations():
    pass

@app.route("/sendemail", methods=["POST"])# Endpoint para mandar el correo que se llamará desde otro lado
def send_email():
    try:
        coordinates = get_coordinates()
        email_send(coordinates["email-dest"])
        respCode = 200
        respJSON = {
            "responseCode": respCode,
            "responseMessage": "Email sent successfully"
        }
        respJSON = json.dumps(respJSON)
    except Exception as ex:
        respCode = 200
        respJSON = {
            "responseCode": respCode,
            "responseMessage": str(ex)
        }
        respJSON = json.dumps(respJSON)

    return Response(respJSON, mimetype="application/json")