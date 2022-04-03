try:
    import json
    from app import app
    from flask import Response
except ImportError as eImp:
    print(f"The following import ERROR occurred in {__file__}: {eImp}")

def response_method(resCode, resTitle, resDes):
    respJSON = {
        "responseCode": resCode,
        "responseCodeTitle": resTitle,
        "responseMessage": resDes
        }

    respJSON= json.dumps(respJSON)
    return respJSON

# -----------------------------App errors-----------------------------
@app.errorhandler(405)
def access_error(error):
    respJSON = response_method(error.code, error.name, error.description)
    return Response(respJSON, mimetype="application/json"), error.code

@app.errorhandler(404)
def access_error(error):
    respJSON = response_method(error.code, error.name, error.description)
    return Response(respJSON, mimetype="application/json"), error.code

@app.errorhandler(400)
def access_error(error):
    message = f"The neccessary header is not in the request or is not the raspberry registered in our database or {error.description.lower()}"
    respJSON = response_method(error.code, error.name, message)
    return Response(respJSON, mimetype="application/json"), error.code

@app.errorhandler(500)
def access_error(error):
    respJSON = response_method(error.code, error.name, error.description)
    return Response(respJSON, mimetype="application/json"), error.code