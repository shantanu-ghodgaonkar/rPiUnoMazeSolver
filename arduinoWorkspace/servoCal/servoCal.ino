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

// const int botHome = 92;
// const int topHome = 83;

const int botHome = 83;
const int topHome = 90;
const int botOffset = 12;
const int topOffset = 8;
const int delayTime1 = 20;
const int delayTime2 = 2000;
const int botSpeed = 32;
const int topSpeed = 15;
int i = 0;


void setup() {
  botServo.attach(9);
  topServo.attach(10);
  botServo.write(botHome);  // HOME
  topServo.write(topHome);  // HOME
}

void rotateServo(char servo, char dir) {

  if ((servo == 'b') && (dir == 'u')) {
    for (i = botHome; i < botHome + botOffset; i++) {
      botServo.write(i);
      delay(botSpeed);
    }
    delay(delayTime1);
    for (i = botHome + botOffset; i > botHome; i--) {
      botServo.write(i);
      // delay(botSpeed);
    }
  } else if ((servo == 'b') && (dir == 'd')) {
    for (i = botHome; i > botHome - botOffset; i--) {
      botServo.write(i);
      delay(botSpeed);
    }
    delay(delayTime1);
    for (i = botHome - botOffset; i < botHome; i++) {
      botServo.write(i);
      // delay(botSpeed);
    }
  } else if ((servo == 't') && (dir == 'u')) {
     for (i = topHome; i < topHome + topOffset; i++) {
      topServo.write(i);
      delay(topSpeed);
    }
    delay(delayTime1);
    for (i = topHome + topOffset; i > topHome; i--) {
      topServo.write(i);
      delay(topSpeed);
    }
  } else if ((servo == 't') && (dir == 'd')) {
    for (i = topHome; i > topHome - topOffset; i--) {
      topServo.write(i);
      delay(topSpeed);
    }
    delay(delayTime1);
    for (i = topHome - topOffset; i < topHome; i++) {
      topServo.write(i);
      delay(topSpeed);
    }
  }
}
void loop() {

  
  delay(delayTime2);
  rotateServo('b', 'u');
  delay(delayTime2);
  rotateServo('b', 'd');
  delay(delayTime2);
  rotateServo('t', 'u');
  delay(delayTime2);
  rotateServo('t', 'd');
}
