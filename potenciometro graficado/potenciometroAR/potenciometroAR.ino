//señal del potenciometro 
int POTpin = 2;
int val,lectura = 0;
int led = 8;
void setup() {
 Serial.begin(9600);
 pinMode(led, OUTPUT);
}

void loop() {
  val = analogRead(POTpin);
  lectura = analogRead(POTpin);
  
  float volt = val * (5.0/ 1023.0); 
  Serial.println(volt);
  int porcentaje = map(lectura, 0, 1023, 0, 100);
  delay(20);
  
  if(porcentaje == 0){
      digitalWrite(led, HIGH);
   }
   if(porcentaje == 50){
      digitalWrite(led, LOW);
   }
   if(porcentaje == 99){
      digitalWrite(led, HIGH);
      delay(100);
      digitalWrite(led, LOW); 
   }
}
