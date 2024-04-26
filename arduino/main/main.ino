const int ledPin = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hello Pi from UNO");
  delay(1000);
  if(Serial.available())
  {
    blink(Serial.read() - '0');
  }
}

void blink(int n) {
  for (int i = 0; i < n; i++) {
    digitalWrite(ledPin, HIGH);
    delay(1000);
    digitalWrite(ledPin, LOW);
    delay(1000);
  }
}
