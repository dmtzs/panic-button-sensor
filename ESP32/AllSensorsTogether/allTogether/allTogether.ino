// Native libraries
#include <Arduino.h>
#include <WiFi.h>

// Libraries that should be installed
#include <WifiLocation.h>
#include <FirebaseESP32.h>

//---------------------------------------Credentials---------------------------------------
#define googleApiKey "googleApiKey"
#define ssid "ssid"
#define passwd "passwd"

#define FIREBASE_HOST "FIREBASE_HOST"
#define FIREBASE_Authorization_key "FIREBASE_Authorization_key"
// ----------------------------------------------------------------------------------------

//For mq3
#define GAS_SENSOR A0
int val, control_request=0, control_alarm_led=0;
String lat, lng, time_stamp;

//push button pins and out pins
const int pushPanic = 15;
const int pushLedAlarm = 19;
const int ledRojo = 4;
const int ledAzul = 5;
const int alarma = 18;

//Firebase objects
FirebaseData firebaseData;
FirebaseJson json;

WifiLocation location (googleApiKey);
String ESP_serie;

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
    struct tm timeinfo2;//temporal
    localtime_r(&now, &timeinfo2);
    Serial.println("Other time stamp");
    Serial.print (asctime (&timeinfo2));
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
    pinMode(pushPanic, INPUT);
    pinMode(pushLedAlarm, INPUT);

    pinMode(ledRojo, OUTPUT);
    pinMode(ledAzul, OUTPUT);
    pinMode(alarma, OUTPUT);

    digitalWrite(ledRojo, LOW);
    digitalWrite(ledAzul, LOW);
    digitalWrite(alarma, LOW);

    Firebase.begin(FIREBASE_HOST,FIREBASE_Authorization_key);
    ESP_serie = WiFi.macAddress();
    // FirebaseJson json_value;// A variable to set the key and content I want
    // json_value.set("email-dest", "mmicros717@gmail.com");
    // Firebase.pushJSON(firebaseData, "/Coordinates/ESP_" + ESP_serie + "/lectura", json_value);
}

void loop() {
    int pushPanicState = digitalRead(pushPanic);
    int pushLedAlarmState = digitalRead(pushLedAlarm);
    val=analogRead(GAS_SENSOR);//Lectura sensor mq3 y debajo if de la lectura
    Serial.print("MQ3: ");
    Serial.println(val);

    if(val >= 1200 && control_request == 0) {
      Serial.println("Alcohol detected, sending geolocation");
      control_request=1;
      getLocation();
      FirebaseJson json_value;// A variable to set the key and content I want
      json_value.set("latitude", lat.toFloat());
      json_value.set("longitude", lng.toFloat());

      Firebase.pushJSON(firebaseData, "/Coordinates/ESP_" + ESP_serie + "/lectura", json_value);
    }
    else if(pushPanicState == HIGH && control_request == 0) {
      Serial.println("Panic button detected");
      control_request=1;
      getLocation();
      FirebaseJson json_value;// A variable to set the key and content I want
      json_value.set("latitude", lat.toFloat());
      json_value.set("longitude", lng.toFloat());

      Firebase.pushJSON(firebaseData, "/Coordinates/ESP_" + ESP_serie + "/lectura", json_value);
    }
    else if(pushLedAlarmState == HIGH && control_alarm_led == 0) {
      Serial.println("Encender alarma");
      control_alarm_led = 1;
      digitalWrite(ledRojo, HIGH);
      digitalWrite(ledAzul, HIGH);
      digitalWrite(alarma, HIGH);
    }
    else if(pushLedAlarmState == HIGH && control_alarm_led == 1) {
      control_alarm_led = 0;
      Serial.println("Apagar alarma");
      digitalWrite(ledRojo, LOW);
      digitalWrite(ledAzul, LOW);
      digitalWrite(alarma, LOW);
    }
    else {
      control_request=0;
      Serial.println("No data received");
    }
    delay(2000);
}

// For arduino.json: ESP32\\AllSensorsTogether\\allTogether\\allTogether.ino