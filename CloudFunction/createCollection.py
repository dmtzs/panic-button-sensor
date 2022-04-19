from typing import Collection


# A script only to create by first time the collection I need so later in th cloud function I can be able to only update the fields

try:
    import firebase_admin
    from firebase_admin import credentials, db
except ImportError as eImp:
    print(f"The following import error ocurred: {eImp}")

cred = credentials.Certificate("path_to_my_json_credentials_file")
url_database = {"databaseURL": "url_of_my_database"}
firebase_admin.initialize_app(cred, url_database)

ref = db.reference("/Coordinates")
collection = {
    "latitude": 19.362534,
    "longitude": -99.249061
}
ref.push(collection)