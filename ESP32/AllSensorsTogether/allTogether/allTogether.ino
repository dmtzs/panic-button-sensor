// Bibliotecas nativas
#include <Arduino.h>
#include <WiFi.h>

// Biblioteca que se debe de instalar
#include <WifiLocation.h>
#include <FirebaseESP32.h>

// const char* googleApiKey = "Api key";
// const char* ssid = "...";
// const char* passwd = "...";
#define googleApiKey "AIzaSyA6TDHaUUCPJ0qn0TwB8If3HNsOKh-sPDU"
#define ssid "Asus 2.4"
#define passwd "M_on_ky_3"

#define FIREBASE_HOST "https://geolocation-346122-default-rtdb.firebaseio.com/"
#define FIREBASE_Authorization_key "W26buUb20gAqTTzyex8MasvrmUa87zK7T4FRn2z0"

//Debajo para mq3
#define GAS_SENSOR A0
int val, control_request=0;
String lat, lng;

//Firebase objetos
FirebaseData firebaseData;
FirebaseJson json;

WifiLocation location (googleApiKey);

// Set time via NTP, as required for x.509 validation
void setClock () {
    configTime (0, 0, "pool.ntp.org", "time.nist.gov");

    Serial.print ("Waiting for NTP time sync: ");
    time_t now = time (nullptr);
    while (now < 8 * 3600 * 2) {
        delay (500);
        Serial.print (".");
        now = time (nullptr);
    }
    struct tm timeinfo;
    gmtime_r (&now, &timeinfo);
    Serial.print ("\n");
    Serial.print ("Current time: ");
    Serial.print (asctime (&timeinfo));
}

void connectToWifi() {
    //Connect to WPA/WPA2 network
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, passwd);
    while (WiFi.status() != WL_CONNECTED) {
        Serial.print("Attempting to connect to WPA SSID: ");
        Serial.println(ssid);
        // wait 5 seconds for connection:
        Serial.print("Status = ");
        Serial.println(WiFi.status());
        delay(500);
    }
    Serial.println ("Connected");
}

void getLocation() {
  setClock();
    
  location_t loc = location.getGeoFromWiFi();

  Serial.println("Location request data");
//   Serial.println(location.getSurroundingWiFiJson()+"\n");// Las macc adress que considero no es necesario mostrar
  Serial.println ("Location: " + String (loc.lat, 7) + "," + String (loc.lon, 7));
  Serial.println ("Accuracy: " + String (loc.accuracy));
  Serial.println ("Result: " + location.wlStatusStr (location.getStatus ()));
  lat = String (loc.lat, 7);
  lng = String (loc.lon, 7);
}

void setup() {
    Serial.begin(115200);
    connectToWifi();
    //Debajo de mq3
    delay(10);
    pinMode(GAS_SENSOR, INPUT);
}

void loop() {
    // String data = Serial.readStringUntil('\n');// En vez de esto será la lectura del sensor y/o push button
    val=analogRead(GAS_SENSOR);//Lectura sensor mq3 y debajo if de la lectura
    Serial.println(val);
    if(val >= 1200 && control_request == 0){
      Serial.println("Alcohol detected, sending geolocation");
      control_request=1;
      getLocation();
      Firebase.begin(FIREBASE_HOST,FIREBASE_Authorization_key);
      Firebase.setDouble(firebaseData, "/Coordinates/-N017k3urhCwePnWAAjX/latitude", lat.toFloat());
      Firebase.setDouble(firebaseData, "/Coordinates/-N017k3urhCwePnWAAjX/longitude", lng.toFloat());
    }
    else {
      control_request=0;
      Serial.println("No data received");
    }
    delay(1000);
}