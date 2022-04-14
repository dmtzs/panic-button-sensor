#define GAS_SENSOR A0
int val;

void setup(){
  Serial.begin(115200);
  delay(10);
  pinMode(GAS_SENSOR, INPUT);
}

void loop(){
  val=analogRead(GAS_SENSOR);
  if(val >= 2000){
    Serial.println("Nivel de alcohol detectado");
    Serial.print(val);
  }
  else{
    Serial.println("No hay alcohol");
    Serial.print(val);
  }
  delay(500);
}
