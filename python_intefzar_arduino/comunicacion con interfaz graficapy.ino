const int pinLed1 = 8;
const int pinLed2 = 9;
const int pinpush1 = 2;
const int pinpush2 = 4;
int input;


void setup() {
  Serial.begin(9600);
  pinMode(pinLed1, OUTPUT);
  pinMode(pinLed2, OUTPUT);
  pinMode(pinpush1, INPUT);
  pinMode(pinpush2, INPUT);
  digitalWrite(pinLed1, 1);
  digitalWrite(pinLed2, 1);
}

int contadorpush1 = 0;
int contadorpush2 = 0;

void loop() {  
  //contador de pulsos 1
  if(digitalRead(pinpush1) == HIGH){
    if(digitalRead(pinpush1) == LOW){
       contadorpush1++;
       delay(1);
      }
   }
  //contador de pulsos 2
   if(digitalRead(pinpush2) == HIGH){
    if(digitalRead(pinpush2) == LOW){
       contadorpush2++;
       delay(1);
      }
   }
  //encendiendo leds de forma analoga 
  if(contadorpush1 == 2){
      Serial.println(contadorpush1);
      digitalWrite(pinLed1, 0);
      delay(5000);
      digitalWrite(pinLed1, 1);
      contadorpush1++;
      Serial.println(contadorpush1);
   }
   if(contadorpush1 == 5){
      Serial.println(contadorpush1);
      digitalWrite(pinLed2, 0);
      delay(5000);
      digitalWrite(pinLed2, 1);
      contadorpush1 = 0;
      Serial.println(contadorpush1);
   }

   if(contadorpush2 == 2){
      Serial.println(contadorpush2);
      digitalWrite(pinLed1, 0);
      delay(5000);
      digitalWrite(pinLed1, 1);
      contadorpush2++;
      Serial.println(contadorpush2);
   }
   if(contadorpush2 == 5){
      Serial.println(contadorpush2);
      digitalWrite(pinLed2, 0);
      delay(5000);
      digitalWrite(pinLed2, 1);
      contadorpush2 = 0;
      Serial.println(contadorpush2);
   }
  //prender leds con teclado 

  //pendiendo led de forma logica     
  if(Serial.available() > 0){
      char serialData = Serial.read();
    if(serialData == '1'){
      digitalWrite(pinLed1, 0);
      delay(10000);
      digitalWrite(pinLed1, 1);
    }
    if(serialData == '2'){
      digitalWrite(pinLed2, 0);
      delay(10000);
      digitalWrite(pinLed2, 1);
    }
    if(serialData=='a'){
    digitalWrite(pinLed1,0);
    digitalWrite(pinLed2,0);
    }
    if(serialData=='b'){
    digitalWrite(pinLed1,1);
    digitalWrite(pinLed2,1);
    }
}
}
