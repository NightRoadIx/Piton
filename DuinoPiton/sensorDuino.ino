// Ejemplo de prueba para varios sensores de humedad/temperatura DHT

// REQUIERE las siguientes bibliotecas de Arduino:
// - Biblioteca del sensor DHT: https://github.com/adafruit/DHT-sensor-library
// - Biblioteca Adafruit Unified Sensor: https://github.com/adafruit/Adafruit_Sensor

#include "DHT.h"

#define DHTPIN 2     // Pin digital conectado al sensor DHT
// Nota para Feather HUZZAH ESP8266: usa los pines 3, 4, 5, 12, 13 o 14 --
// El pin 15 puede funcionar, pero el DHT debe estar desconectado durante la carga del programa.

// Descomenta el tipo de sensor que estés usando:
#define DHTTYPE DHT11   // DHT 11
//#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321
//#define DHTTYPE DHT21   // DHT 21 (AM2301)

// Conecta el pin 1 (a la izquierda) del sensor a +5V
// NOTA: Si estás usando una placa con lógica de 3.3V como el Arduino Due, conecta el pin 1
// a 3.3V en lugar de 5V!
// Conecta el pin 2 del sensor al pin DHTPIN
// Conecta el pin 3 (a la derecha) del sensor a GND (si tu sensor tiene 3 pines)
// Conecta el pin 4 (a la derecha) del sensor a GND y deja el pin 3 VACÍO (si tu sensor tiene 4 pines)
// Conecta una resistencia de 10K entre el pin 2 (datos) y el pin 1 (alimentación) del sensor

// Inicializa el sensor DHT.
// Ten en cuenta que las versiones antiguas de esta biblioteca requerían un tercer parámetro opcional para
// ajustar los tiempos para procesadores más rápidos. Este parámetro ya no es necesario
// ya que el algoritmo actual de lectura de DHT se ajusta automáticamente para trabajar en procesadores más rápidos.
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("¡Prueba DHTxx!"));

  dht.begin();
}

void loop() {
  // Espera unos segundos entre mediciones.
  delay(2000);

  // ¡Leer la temperatura o humedad tarda aproximadamente 250 milisegundos!
  // Las lecturas del sensor también pueden estar hasta 2 segundos "antiguas" (es un sensor muy lento)
  float h = dht.readHumidity();
  // Leer la temperatura en Celsius (por defecto)
  float t = dht.readTemperature();
  // Leer la temperatura en Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Verifica si alguna lectura falló y sale temprano (para intentar de nuevo).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Fallo la lectura del sensor DHT"));
    return;
  }

  // Calcular el índice de calor en Fahrenheit (por defecto)
  float hif = dht.computeHeatIndex(f, h);
  // Calcular el índice de calor en Celsius (isFahrenheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humedad: "));
  Serial.print(h);
  Serial.print(F("%  Temperatura: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Índice de temperatura: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
}
