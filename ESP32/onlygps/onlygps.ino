// Bibliotecas nativas
#include <Arduino.h>
#include <WiFi.h>

// Biblioteca que se debe de instalar
#include <WifiLocation.h>

const char* googleApiKey = "AIzaSyBgcSZMRzZZS-fBlkFQGqYY4eqg46XSWM8";
const char* ssid = "Asus 2.4";
const char* passwd = "M_on_ky_3";

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
}

void setup() {
    Serial.begin(115200);
    connectToWifi();
}

void loop() {
    if (Serial.available())
    {
        String data = Serial.readStringUntil('\n');// En vez de esto será la lectura del sensor y/o push button
        if(data == "eder") {//Validar el valor del sensor y del push button. Preguntar a David cómo evitar el debounce del push button.
          Serial.print("Data received: ");
          Serial.println(data);
          Serial.println("Showing now data of geolocation:");
          getLocation();
        }
        else {
          Serial.println("No data received");
        }
    }
    delay(1000);
}