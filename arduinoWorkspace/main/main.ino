#include <Servo.h>

#define SERVOBOTPIN 9    // Pin to which the bottom servo is attached
#define SERVOTOPPIN 10   // Pin to which the top servo is attached
#define BAUDRATE 115200  // Baud Rate

Servo servoBot;                          // Bottom Servo denoted by number 0
Servo servoTop;                          // Top Servo denoted by number 1
const unsigned int servoHomeAngle = 90;  // The home angles for both servos
const unsigned int servoRotAngle = 15;   // The rotation offset for both servos
unsigned int servoBotStatus = 48;        // Status of bottom servo based on command from RPi
unsigned int servoTopStatus = 48;        // Status of top servo based on command from RPi
const unsigned int servoRotSpeed = 50;   // Delay in for loops that rotate the servos thus deciding the speed of rotation (needs to be tuned)

void rotateServoSwitch(unsigned int servoDir) { /* Switch case that takes a command from the RPi as an input and accordingly decides which servo to rotate in which direction */
  switch (servoDir) {                           // Switch Case to rotate servos according to the signal from the RPi
    // Case to bring both servos to home location
    case 48:  //servoBot.write(servoHomeAngle);
      //servoTop.write(servoHomeAngle);
      rotateServo('h', 'h');
      servoBotStatus = servoDir;
      servoTopStatus = servoDir;
      Serial.println("Bringing both servos to home location");
      break;
    // Case to rotate the bottom servo by 15 degrees clockwise
    case 49:  // servoBot.write(servoHomeAngle-servoRotAngle);
      rotateServo('b', 'd');
      servoBotStatus = servoDir;
      Serial.println("Rotating the bottom servo by 15 degrees clockwise");
      break;
    // Case to rotate the bottom servo by 15 degrees counterclockwise
    case 50:  //servoBot.write(servoHomeAngle+servoRotAngle);
      rotateServo('b', 'u');
      servoBotStatus = servoDir;
      Serial.println("Rotating the bottom servo by 15 degrees counterclockwise");
      break;
    // Case to rotate the top servo by 15 degrees clockwise
    case 51:  //servoTop.write(servoHomeAngle-servoRotAngle);
      rotateServo('t', 'd');
      servoTopStatus = servoDir;
      Serial.println("Rotating the top servo by 15 degrees clockwise");
      break;
    // Case to rotate the top servo by 15 degrees counterclockwise
    case 52:  //servoTop.write(servoHomeAngle+servoRotAngle);
      rotateServo('t', 'u');
      servoTopStatus = servoDir;
      Serial.println("Rotating the top servo by 15 degrees counterclockwise");
      break;
    // Default case to bring both servos to home angle
    default:
      servoBot.write(servoHomeAngle);
      servoTop.write(servoHomeAngle);
      servoBotStatus = 48;
      servoTopStatus = 48;
      Serial.println("Bringing both servos to home location");
      break;
  }
}

void rotateServo(char servo, char dir) {
  unsigned int i = 0;
  if ((servo == 'h') & (dir == 'h')) {
    unsigned int j = 0;
    if (servoBotStatus == servoTopStatus) {
    } else if (servoTopStatus = 48) {
      switch (servoBotStatus) {
        case 48: break;
        case 49:
          for (i = servoHomeAngle - servoRotAngle; i < servoHomeAngle; i++) {
            servoBot.write(i);
            delay(servoRotSpeed);
          }
          break;
        case 50:
          for (i = servoHomeAngle + servoRotAngle; i > servoHomeAngle; i--) {
            servoBot.write(i);
            delay(servoRotSpeed);
          }
          break;
        default: servoBot.write(servoHomeAngle);
      }
    } else if (servoBotStatus = 48) {
      switch (servoTopStatus) {
        case 48: break;
        case 51:
          for (i = servoHomeAngle - servoRotAngle; i < servoHomeAngle; i++) {
            servoTop.write(i);
            delay(servoRotSpeed);
          }
          break;
        case 52:
          for (i = servoHomeAngle + servoRotAngle; i > servoHomeAngle; i--) {
            servoTop.write(i);
            delay(servoRotSpeed);
          }
          break;
        default: servoTop.write(servoHomeAngle);
      }
    } else if ((servoBotStatus == 49) && (servoTopStatus = 51)) {
      for (i = servoHomeAngle - servoRotAngle, j = servoHomeAngle - servoRotAngle; i < servoHomeAngle, j < servoHomeAngle; i++, j++) {
        servoBot.write(i);
        servoTop.write(i);
        delay(servoRotSpeed);
      }
    } else if ((servoBotStatus == 49) && (servoTopStatus = 52)) {
      for (i = servoHomeAngle - servoRotAngle, j = servoHomeAngle + servoRotAngle; i<servoHomeAngle, j> servoHomeAngle; i++, j--) {
        servoBot.write(i);
        servoTop.write(i);
        delay(servoRotSpeed);
      }
    } else if ((servoBotStatus == 50) && (servoTopStatus = 51)) {
      for (i = servoHomeAngle + servoRotAngle, j = servoHomeAngle - servoRotAngle; i > servoHomeAngle, j < servoHomeAngle; i--, j++) {
        servoBot.write(i);
        servoTop.write(i);
        delay(servoRotSpeed);
      }
    } else if ((servoBotStatus == 50) && (servoTopStatus = 52)) {
      for (i = servoHomeAngle + servoRotAngle, j = servoHomeAngle + servoRotAngle; i > servoHomeAngle, j > servoHomeAngle; i--, j--) {
        servoBot.write(i);
        servoTop.write(i);
        delay(servoRotSpeed);
      }
    }
  } else if ((servo == 'b') & (dir == 'u')) {
    for (i = servoHomeAngle; i < servoHomeAngle + servoRotAngle; i++) {
      servoBot.write(i);
      delay(servoRotSpeed);
    }
  } else if ((servo == 'b') & (dir == 'd')) {
    for (i = servoHomeAngle; i > servoHomeAngle - servoRotAngle; i--) {
      servoBot.write(i);
      delay(servoRotSpeed);
    }
  } else if ((servo == 't') & (dir == 'u')) {
    for (i = servoHomeAngle; i < servoHomeAngle + servoRotAngle; i++) {
      servoTop.write(i);
      delay(servoRotSpeed);
    }
  } else if ((servo == 't') & (dir == 'd')) {
    for (i = servoHomeAngle; i > servoHomeAngle - servoRotAngle; i--) {
      servoTop.write(i);
      delay(servoRotSpeed);
    }
  }
}


void setup() {
  servoBot.attach(SERVOBOTPIN);  // Attach bottom servo to its pin
  servoTop.attach(SERVOTOPPIN);  // Attach top servo to its pin
  Serial.begin(BAUDRATE);        // Set baudrate and begin serial communication
}
void loop() {
  if (Serial.available()) {                          // Check if a byte of data has been received
    rotateServoSwitch((unsigned int)Serial.read());  // When a byte of data has been received, pass it on to the rotateServo() function
  }
}
