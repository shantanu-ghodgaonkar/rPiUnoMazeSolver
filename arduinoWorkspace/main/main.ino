#include <Servo.h>

Servo botServo;
Servo topServo;

const int botHome = 84;
const int topHome = 86;
const int botOffset = 15; //13
const int topOffset = 15;
const int delayTime1 = 50; //2
const int delayTime2 = 2000; //2000
const int botSpeed = 30; //30
const int botSpeedReturn = 5;
const int topSpeed = 30;
int i = 0;
int p = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  botServo.attach(9);
  topServo.attach(10);
  botServo.write(botHome);
  topServo.write(topHome);
}

void rotateServo(char servo, char dir) {

  if ((servo == 'b') && (dir == 'u')) {
    for (i = botHome; i < botHome + botOffset; i++) {
      delay(botSpeed);
      botServo.write(i);
    }
    delay(delayTime1);
    for (i = botHome + botOffset; i > botHome; i--) {
      botServo.write(i);
      delay(botSpeed);
    }
    botServo.write(botHome);
  } else if ((servo == 'b') && (dir == 'd')) {
    for (i = botHome; i > botHome - botOffset; i--) {
      delay(botSpeed);
      botServo.write(i);

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


void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available()) {
    p = (unsigned int) Serial.read() - 48;

    switch (p) {
      case 0:  botServo.write(botHome);
        topServo.write(topHome);
        Serial.println("Bringing both servos to home location");
        break;
      // Case to rotate the bottom servo by 15 degrees clockwise
      case 1:  rotateServo('b', 'u');
        Serial.println("Rotating the bottom servo UP");
        break;
      // Case to rotate the bottom servo by 15 degrees counterclockwise
      case 2:  rotateServo('b', 'd');
        Serial.println("Rotating the bottom servo DOWN");
        break;
      // Case to rotate the top servo by 15 degrees clockwise
      case 3:  rotateServo('t', 'u');
        Serial.println("Rotating the top servo by UP");
        break;
      // Case to rotate the top servo by 15 degrees counterclockwise
      case 4:  rotateServo('t', 'd');
        Serial.println("Rotating the top servo by DOWN");
        break;

      case 5:
        // Bottom Servo downward Jerk
        for (i = botHome; i < botHome + 11; i++) {
          delay(50);  //50
          botServo.write(i);
        }
        delay(45);  //50
        botServo.write(botHome - 12); //12
        delay(65);  //65
        botServo.write(botHome);
        // Bottom Servo downward Jerk End
        break;

      case 6:
        //Bottom Servo Upward Jerk
        botServo.write(botHome);
        delay(1000);
        for (i = botHome; i > botHome - 11; i--) {
          delay(50);  //50
          botServo.write(i);
        }
        delay(45);  //50
        botServo.write(botHome + 12); //12
        delay(65);  //65
        botServo.write(botHome);
        //Bottom Servo Upward Jerk End
        break;

      case 7:
        // Top servo right jerk
        for (i = topHome; i > topHome - 10; i--) {
          delay(35);  //50
          topServo.write(i);
        }
        delay(45);  //50
        topServo.write(topHome + 11); //12
        delay(65);  //65
        topServo.write(topHome);
        break;
      // Top servo right jerk End
      case 8:
        // Top servo left jerk
        for (i = topHome; i < topHome + 10; i++) {
          delay(35);  //50
          topServo.write(i);
        }
        delay(45);  //50
        topServo.write(topHome - 11); //12
        delay(65);  //65
        topServo.write(topHome);
        break;
      // Top servo left jerk End
      // Default case to bring both servos to home angle
      default:  botServo.write(botHome);
        topServo.write(topHome);
        Serial.println("DEF Bringing both servos to home location");
        break;

    }
  }
}
