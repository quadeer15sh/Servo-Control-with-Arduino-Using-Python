#include <Servo.h>

Servo myservo1;
// create servo object to control a servo
// twelve servo objects can be created on most boards

int pos1;    // variable to store the servo position

char data;
void setup() {
  Serial.begin(9600);
  myservo1.attach(2);
  pos1 = 60;
}

void loop() {

  if(Serial.available()==0){}
  data = Serial.read(); // reading the data received from the bluetooth module
  switch (data) {
    case '6': 
    if (pos1<=180){
      pos1 = pos1 + 1;
      Serial.println(pos1);
      myservo1.write(pos1); 
      }
    break;
    case '4':
    if (pos1>=60){
      pos1 = pos1 - 1;
      Serial.println(pos1);
      myservo1.write(pos1); 
      }
    break;
    default: break;
    }
  }
