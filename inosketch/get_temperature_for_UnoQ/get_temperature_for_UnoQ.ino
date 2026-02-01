#include "Arduino_RouterBridge.h"
#include <math.h>

const int B = 4275000;            // サーミスタのB値
const int R0 = 100000;            // R0 = 100k
const int pinTempSensor = A0;     // Grove - Temperature SensorをA0に接続
float temperature = 0;

void setup() {
    Bridge.begin();
    Bridge.provide("get_temperature", get_temperature);
}

void loop() {
    int a = analogRead(pinTempSensor);
    float R = 1023.0/a-1.0;
    R = R0*R;

    temperature = 1.0/(log(R/R0)/B+1/298.15)-273.15; // データシートを基に温度に変換
    delay(100);
}

float get_temperature() {
    return temperature;
}