#include <SoftwareSerial.h>
#include <TinyGPS++.h>

static const uint32_t GPSBaud = 9600;
TinyGPSPlus gps; // The TinyGPS++ object
SoftwareSerial ss(RXPin, TXPin); // The serial connection to the GPS device
const unsigned int writeInterval = 25000; // write interval (in ms)

void setup(){
  ss.begin();
}

void loop() {
  if (!client.connected()) 
  reconnect();
  client.loop();
  // This sketch displays information every time a new sentence is correctly encoded.
  while (ss.available() > 0)
  if (gps.encode(ss.read()))
  displayInfo();

  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println(F("No GPS detected: check wiring."));
    while(true);
  }
}

// GPS displayInfo
void displayInfo() {
  if (gps.location.isValid()) {
    double latitude = (gps.location.lat());
    double longitude = (gps.location.lng());

    Serial.println("Latitude: " + latitude);
    Serial.println("Longitude: " + longitude);
    delay(writeInterval);// delay
  } else {
    Serial.println(F("INVALID"));
  }
}