#include<Servo.h>

#define SERVOBOTPIN 9 // Pin to which the bottom servo is attached
#define SERVOTOPPIN 10 // Pin to which the top servo is attached
#define BAUDRATE 115200 // Baud Rate

Servo botServo; // Bottom Servo denoted by number 0
Servo topServo; // Top Servo denoted by number 1
const float botHome = 83;
const int topHome = 92;
const int botOffset = 6;
const int topOffset = 8;
const int delayTime1 = 30;
const int delayTime2 = 2000;
const int botSpeed = 18;
const int topSpeed = 15;
int i = 0;

void rotateServo(char servo, char dir) {

  if ((servo == 'b') && (dir == 'u')) {
    for (i = botHome; i < botHome + botOffset; i++) {
      botServo.write(i);
      delay(botSpeed);
    }
    delay(delayTime1);
    for (i = botHome + botOffset; i > botHome; i--) {
      botServo.write(i);
      delay(botSpeed);
    }
  } else if ((servo == 'b') && (dir == 'd')) {
    for (i = botHome; i > botHome - botOffset; i--) {
      botServo.write(i);
      delay(botSpeed);
    }
    delay(delayTime1);
    for (i = botHome - botOffset; i < botHome; i++) {
      botServo.write(i);
      delay(botSpeed);
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

void rotateServoSwitch(unsigned int servoDir){
  switch(servoDir) { // Switch Case to rotate servos according to the signal from the RPi
    // Case to bring both servos to home location
    case 48:  botServo.write(botHome);
              topServo.write(topHome);
              Serial.println("Bringing both servos to home location");
              break;
    // Case to rotate the bottom servo by 15 degrees clockwise
    case 49:  rotateServo('b', 'u');
              Serial.println("Rotating the bottom servo UP");
              break;
    // Case to rotate the bottom servo by 15 degrees counterclockwise
    case 50:  rotateServo('b', 'd');
              Serial.println("Rotating the bottom servo DOWN");
              break;
    // Case to rotate the top servo by 15 degrees clockwise
    case 51:  rotateServo('t', 'u');
              Serial.println("Rotating the top servo by UP");
              break;
    // Case to rotate the top servo by 15 degrees counterclockwise
    case 52:  rotateServo('t', 'd');
              Serial.println("Rotating the top servo by DOWN");
              break;
    // Default case to bring both servos to home angle
    default:  botServo.write(botHome);
              topServo.write(topHome);
              Serial.println("Bringing both servos to home location");
              break;
  }
}

void setup() {
  botServo.attach(SERVOBOTPIN); // Attach bottom servo to its pin
  topServo.attach(SERVOTOPPIN); // Attach top servo to its pin
  Serial.begin(BAUDRATE); // Set baudrate and begin serial communication
}
void loop() {
  if(Serial.available()){ // Check if a byte of data has been received
    rotateServoSwitch((unsigned int) Serial.read()); // When a byte of data has been received, pass it on to the rotateServo() function
  }
}
