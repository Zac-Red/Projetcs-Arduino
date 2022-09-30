#include <Stepper.h>
//revoluciones del motor
const int stepsPerRevolution = 2048;
Stepper myStepper(stepsPerRevolution, 8, 10, 9, 11);
int stepCount = 0;  // estdo del contador de pasos del motor. 
 
void setup() {
//puerto seril a 9600 baudios
  Serial.begin(9600);
}
 
void loop() {
//pin analogico para la señal del potenciometro
int sensorReading = analogRead(A0);
int motorSpeed = map(sensorReading, 0, 1023, 0, 20);
Serial.println(motorSpeed);
//variacion de velocidad en el caso de que el motor este a 0 
if (motorSpeed > 0) {
  myStepper.setSpeed(motorSpeed);
  //division de revoluciones del meotor entre 1000
  myStepper.step(stepsPerRevolution / 1000);
}
}