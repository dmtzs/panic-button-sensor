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
    ref = db.reference("/Coordinates/ESP_40:91:51:99:44:90/lectura")
    result = ref.order_by_key().limit_to_last(1).get()
    result = dict(result)
    for key in result.keys():
        result_key = key

    return result[result_key]

def get_email():
    ref = db.reference("/Coordinates/ESP_40:91:51:99:44:90")
    result = ref.order_by_key().limit_to_first(1).get()
    result = dict(result)
    for key in result.keys():
        result_key = key

    # print(result[result_key])
    return result[result_key]

def get_5_coordinates():
    ref = db.reference("/Coordinates/ESP_40:91:51:99:44:90/lectura")
    result = ref.order_by_key().limit_to_last(5).get()
    result = dict(result)
    
    results = []
    for key in result.keys():
        results.append(result[key])

    return results

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

# Method to update the google map
def create_map_instance(coordinates):
    mymap = Map(identifier="view-center",
    varname="mymap",
    style="height:1520px;width:1900px;margin:0;",
    lat=coordinates["lat"],
    lng=coordinates["lng"],
    zoom=19,
    markers=[(coordinates["lat"], coordinates["lng"])])

    return mymap

def update_map(map_to_use):#TODO: In local tests test if we can delete some code like only putting the get coordinates method inside the if and the rest outside the if`s`
    if map_to_use == "one":
        coordinates = get_coordinates()
        mymap = create_map_instance(coordinates)
        return mymap, coordinates
    else:
        coordinates = get_5_coordinates()
        mymap = create_map_instance(coordinates)
        return mymap, coordinates

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.now()
    }

# -------------Endpoints-------------
@app.route("/", methods=["GET"])# Map of google maps to show coordinates
def my_map():
    # try:
    coordinates = get_coordinates()
    mymap = Map(identifier="view-center",
    varname="mymap",
    style="height:1520px;width:1900px;margin:0;",
    lat=coordinates["lat"],
    lng=coordinates["lng"],
    zoom=19,
    markers=[(coordinates["lat"], coordinates["lng"])])

    return render_template("googlemap.html", pageTitle= "Map", mymap=mymap)
    # except Exception:
    #     abort(500)

@app.route("/lastlocations", methods=["GET"])# Map of google maps to show last 5 coordinates
def map_with_last_locations():
    try:
        coordinates = get_5_coordinates()
        # mymap = update_map("two")# TODO: Test this in locala after index tested
        mymap = Map(identifier="view-center",
        varname="mymap",
        style="height:1520px;width:1900px;margin:0;",
        lat=coordinates[4]["lat"],
        lng=coordinates[4]["lng"],
        zoom=18,
        markers=coordinates)

        return render_template("googlemap.html", pageTitle= "Map", mymap=mymap)
    except Exception:
        abort(500)

@app.route("/sendemail", methods=["POST"])# Endpoint to send an email
def send_email():
    try:
        email_from = get_email()
        email_send(email_from)
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

@app.route("/testMethods", methods=["POST"])
def tests_methods():
    try:
        coordinates = get_5_coordinates()
        respCode = 200
        respJSON = {
            "responseCode": respCode,
            "responseMessage": "Query done",
            "queryResult": coordinates
        }
        respJSON = json.dumps(respJSON)
    except Exception as ex:
        respCode = 200
        respJSON = {
            "responseCode": respCode,
            "responseMessage": str(ex),
            "queryResult": "Query not done"
        }
        respJSON = json.dumps(respJSON)

    return Response(respJSON, mimetype="application/json")