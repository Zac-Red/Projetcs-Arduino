/* Pi4IoT 30.12.2018  */
 
void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    if (Serial.read() == 'p'){
      Serial.print(analogRead(2));
      Serial.print("\n");
    }
  }
}
