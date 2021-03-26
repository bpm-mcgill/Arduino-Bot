int ledpin = 3;
int buzzerpin = 5;
String val;
void setup() {
  Serial.begin(9600);
  pinMode(ledpin, OUTPUT);

}

void loop() {
  //digitalWrite(ledpin,HIGH);
  while(Serial.available()>0){}
  val = Serial.readString();
  Serial.println(val);
  
  if (val == "o"){
    Serial.println("LED Turned On");
    digitalWrite(ledpin,HIGH);
  }
  if (val == "f"){
    Serial.println("LED Turned Off");
    digitalWrite(ledpin,LOW);
  }

  // EXTRA CODE FOR BUZZER (Ignore if you aren't going to add a buzzer):
  
  if (val == "q"){
    for(int i=0;i<=3;i++){
      tone(buzzerpin,2500,1000);
      delay(200);
      tone(buzzerpin,1000,2000);
      delay(300);
    }
    noTone(buzzerpin);
    digitalWrite(buzzerpin,HIGH);
    Serial.println("ping finished");
  }
}
