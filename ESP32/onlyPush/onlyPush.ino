const int pushPanic = 15;
const int pushLedAlarm = 2;

void setup() {
  Serial.begin(115200);
  pinMode(pushPanic, INPUT);
  pinMode(pushLedAlarm, INPUT);
}

void loop() {
  int pushPanicState = digitalRead(pushPanic);
  int pushLedAlarmState = digitalRead(pushLedAlarm);

  Serial.println("Esperando push");
  if (pushPanicState == HIGH)
  {
    Serial.println("Panico presionado");
  }
  else if (pushLedAlarmState == HIGH)
  {
    Serial.println("Alarma y leds presionado");
  }
  
  delay(1000);
}

// ESP32\\onlyPush\\onlyPush.ino