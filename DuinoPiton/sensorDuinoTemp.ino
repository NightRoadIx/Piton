// Ejemplo de prueba para sensor DHT (solo temperatura)

#include "DHT.h"

#define DHTPIN 2     // Pin digital conectado al sensor DHT
#define DHTTYPE DHT11   // DHT 11 (puedes cambiar a DHT22 si es tu caso)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("Prueba DHTxx - Solo Temperatura!"));

  dht.begin();
}

void loop() {
  delay(2000);  // Espera de 2 segundos entre mediciones

  // Leer la temperatura en Celsius
  float t = dht.readTemperature();  

  // Verificar si la lectura falló
  if (isnan(t)) {
    Serial.println(F("Fallo la lectura del sensor DHT"));
    return;
  }

  // Enviar solo la temperatura por el puerto serial
  Serial.println(t);  // Solo se envía la temperatura

}
