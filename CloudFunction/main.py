try:
    import base64
    import firebase_admin
    from firebase_admin import credentials, db
except ImportError as eImp:
    print(f"The following import error ocurred: {eImp}")

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """

    # Authentication to firebase
    cred = credentials.Certificate("geolocation.json")
    url_database = {"databaseURL": "url_of_my_database"}
    firebase_admin.initialize_app(cred, url_database)

    # Receive the message
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')#TODO: Necesito ver cómo recibo el mensaje primero para mandarlo, creo es un json pero aun así necesito verlo

    # Update field in the database
    ref = db.reference("/Coordinates")
    product_ref = ref.child("-N017k3urhCwePnWAAjX")
    product_ref.update({})# A dictionary, it could be the json that I think I receive in the message

    # Send the email

# This is the main script that should be in the cloud fucntion with the credentials json file generated
# For more instruction about this part I need to documentate the steps of the youtube video in the python list fo my profile