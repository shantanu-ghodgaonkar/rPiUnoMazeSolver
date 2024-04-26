#include<Servo.h>

#define SERVOBOTPIN 9 // Pin to which the bottom servo is attached
#define SERVOTOPPIN 10 // Pin to which the top servo is attached
#define BAUDRATE 115200 // Baud Rate

Servo servoBot; // Bottom Servo denoted by number 0
Servo servoTop; // Top Servo denoted by number 1
const unsigned int servoHomeAngle = 90; // The home angles for both servos
const unsigned int servoRotAngle = 15; // The rotation offset for both servos

void rotateServo(unsigned int servoDir){
  switch(servoDir) { // Switch Case to rotate servos according to the signal from the RPi
    // Case to bring both servos to home location
    case 48:  servoBot.write(servoHomeAngle);
              servoTop.write(servoHomeAngle);
              break;
    // Case to rotate the bottom servo by 15 degrees clockwise
    case 49:  servoBot.write(servoHomeAngle-servoRotAngle);
              break;
    // Case to rotate the bottom servo by 15 degrees counterclockwise
    case 50:  servoBot.write(servoHomeAngle+servoRotAngle);
              break;
    // Case to rotate the top servo by 15 degrees clockwise
    case 51:  servoTop.write(servoHomeAngle-servoRotAngle);
              break;
    // Case to rotate the top servo by 15 degrees counterclockwise
    case 52:  servoTop.write(servoHomeAngle+servoRotAngle);
              break;
    // Default case to bring both servos to home angle
    default:  servoBot.write(servoHomeAngle);
              servoTop.write(servoHomeAngle);
              break;
  }
}

void setup() {
  servoBot.attach(SERVOBOTPIN); // Attach bottom servo to its pin
  servoTop.attach(SERVOTOPPIN); // Attach top servo to its pin
  Serial.begin(BAUDRATE); // Set baudrate and begin serial communication
}
void loop() {
  if(Serial.available()){ // Check if a byte of data has been received
    rotateServo((unsigned int) Serial.read()); // When a byte of data has been received, pass it on to the rotateServo() function
  }
}
