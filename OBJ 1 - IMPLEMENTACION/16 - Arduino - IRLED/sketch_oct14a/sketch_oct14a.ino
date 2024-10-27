int led1 = 13;

void setup() {
  pinMode(led1, OUTPUT);
}

void loop() {
  // Turn the LED on for 10 seconds
  digitalWrite(led1, HIGH);
  delay(10000);  // 10 seconds (10,000 milliseconds)

  // Turn the LED off for 60 seconds
  digitalWrite(led1, LOW);
  delay(60000);  // 60 seconds (60,000 milliseconds)
}
