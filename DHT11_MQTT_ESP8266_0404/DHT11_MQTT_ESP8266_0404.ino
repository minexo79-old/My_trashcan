#include "EspMQTTClient.h" // mqtt library
#include <SimpleDHT.h> // dht library 

// create MQTT object
EspMQTTClient client{
  "", // Wifi SSID
  "", //Wifi password
  "", // MQTT server address
  "", // mqtt username
  "", //mqtt password
  "" //client name
};

int pinDHT11 = 16; // D0
int led = 5; // D1
SimpleDHT11 dht11(pinDHT11);

void setup() {
  pinMode(led,OUTPUT);
}

void onConnectionEstablished() {
  client.publish("Test/DHT11", "Done!");
}

void ledsw(int sw) {
  digitalWrite(led,sw);
}

void loop() {
  client.loop();
  byte temp = 0,humi = 0;
  int err = dht11.read(pinDHT11, &temp, &humi, NULL);
  if (err == 0) {
    String send_data = (String)temp + ',' + (String)humi + ',' + (String)err;
    ledsw(1);
    client.publish("Test/DHT11",send_data);
  }
  else ledsw(0);
  delay(1000);
}
