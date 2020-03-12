#include <LiquidCrystal_I2C.h> // I2C include
#include <Wire.h> // Arduino include
#include <SimpleDHT.h> // DHT include

LiquidCrystal_I2C lcd(0x27, 16, 2);
int pinDHT = 2;
SimpleDHT11 dht11;
byte temperature = 0,humidity = 0;

void setup() {
    // put your setup code here, to run once:
    lcd.begin();
}

int i2c_error(int code) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("DHT11 failed!");
    lcd.setCursor(0, 1);
    lcd.print(code);
    delay(500);  
}

int i2c_display(byte temp,byte humi) {
    lcd.setCursor(0, 0);
    lcd.print("Humidity: ");
    lcd.print((int)humi);
    lcd.print("%");
    lcd.setCursor(0, 1);
    lcd.print("Temp: ");
    lcd.print((int)temp);
    lcd.print("C");    
}

void loop() {
    // put your main code here, to run repeatedly:
    int err = SimpleDHTErrSuccess;
    // Check DHT11 error
    if ((err = dht11.read(pinDHT,&temperature,&humidity,NULL))!= SimpleDHTErrSuccess) {
        // Send infomation to LCD.
        i2c_error(err);
        return;
    }
    // Send infomation to LCD.
    i2c_display(temperature,humidity);
    delay(1500);  
}
