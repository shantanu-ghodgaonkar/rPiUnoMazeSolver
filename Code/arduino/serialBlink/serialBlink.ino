const int ledPin = 13;
byte data = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
pinMode(ledPin, OUTPUT);
}
void types(String a) {Serial.println("Data is a string");}
void types(int a) {Serial.println("Data is a int");}
void types(char *a) {Serial.println("Data is a char*");}
void types(float a) {Serial.println("Data is a float");}
void types(unsigned int a) {Serial.println("Data is a unsigned int");}
void types(byte a) {Serial.println("Data is a byte");}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()){
  data = Serial.read();
  Serial.println(data - '0');
 switch(data) {
    case 48: Serial.println("ASCII 0 detected");
    break;
    case 49: Serial.println("ASCII 1 detected");
    break;
  }
  types(data);
  blink(data - '0');
}
}

void blink(int n)
{
  for(int i = 0; i < n; i++) {
    digitalWrite(ledPin,HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }
  }
