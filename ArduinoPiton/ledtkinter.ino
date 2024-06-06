int led=13;
void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
//lectura 
  if(Serial.available()>0){
    char valor=Serial.read();
    if(valor=='e'){
      digitalWrite(led,HIGH);
    }
    else if(valor=='a'){
      digitalWrite(led,LOW);
    }
  }
}
