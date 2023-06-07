int datos = 0;
char entrada;

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop() 
{
  if(Serial.available() > 0)
  {
    entrada = Serial.read();
    if(entrada == 'g')
    {
      datos = analogRead(A0);
      Serial.println(datos);
    }
  }
}
