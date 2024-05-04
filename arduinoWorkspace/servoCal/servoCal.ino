/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>

Servo botServo;
Servo topServo;



void setup() {
  botServo.attach(9);  
  topServo.attach(10);

}
const float botHome = 102.5;
const int topHome = 97;
const int offset = 7;
const int delayTime1 = 100;
const int delayTime2= 2500;

void loop() {

  botServo.write(botHome); // HOME
  topServo.write(topHome); // HOME
  
  delay(delayTime2);

  // botServo.write(botHome-offset);

  // delay(delayTime1);

  // botServo.write(botHome); // HOME

  // delay(delayTime2);

  // botServo.write(botHome+offset);

  // delay(delayTime1);

  // botServo.write(botHome); // HOME

  // delay(delayTime2);

  topServo.write(topHome-offset);

  delay(delayTime1);

  topServo.write(topHome); // HOME

  delay(delayTime2);

  topServo.write(topHome+offset);

  delay(delayTime1);

  topServo.write(topHome);
}
