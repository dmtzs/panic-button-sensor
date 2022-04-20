#include <FirebaseESP32.h>
#include  <WiFi.h>

#define FIREBASE_HOST "https://geolocation-346122-default-rtdb.firebaseio.com/"
#define WIFI_SSID "Asus 2.4" // Change the name of your WIFI
#define WIFI_PASSWORD "M_on_ky_3" // Change the password of your WIFI
#define FIREBASE_Authorization_key "W26buUb20gAqTTzyex8MasvrmUa87zK7T4FRn2z0"

FirebaseData firebaseData;
FirebaseJson json;

void setup() {
  Serial.begin(115200);
  WiFi.begin (WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting...");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println("IP Address: ");
  //Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST,FIREBASE_Authorization_key);
  Firebase.setFloat(firebaseData, "/-N017k3urhCwePnWAAjX/latitude", 19.362534);
  Firebase.setFloat(firebaseData, "/-N017k3urhCwePnWAAjX/longitude", -99.249061);
}

void loop() {

}
