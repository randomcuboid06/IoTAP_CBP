void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(4, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  int counter = 3;
  int c = 0;
  while(c < counter){
    int isOn = digitalRead(8);
    //Serial.println(isOn);
    if(isOn == 0){
      c += 1;
      delay(2000);
    }
    delay(100);
  }  
  if(c >= counter){
    digitalWrite(4, LOW);
    digitalWrite(LED_BUILTIN, HIGH);
    //Serial.println("ON");
    delay(3000);
    digitalWrite(4, HIGH);
    digitalWrite(LED_BUILTIN, LOW);
    //Serial.println("OFF");
  }
}

void loop() {}
