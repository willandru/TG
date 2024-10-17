int led1=13;
int var1;

void setup() {
  Serial.begin(9600);
  pinMode(led1,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    var1=Serial.read();
    if(var1=='a'){
      digitalWrite(led1,HIGH);
    }
    else{
      digitalWrite(led1,LOW);
    }
  }
}
