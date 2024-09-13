#include <Servo.h>

Servo base;
Servo brazoIzquiero;
Servo brazoDerecho;
Servo pinza;

void setup() {
  base.attach(11);
  brazoIzquiero.attach(10);
  brazoDerecho.attach(9);
  pinza.attach(5);
 
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  
  Serial.begin(9600);

}

void loop() {
  // LIMITES

  // Pinza 100-115
  // Brazo Izquierdo 60-150
  // Brazo Derecho 40-145
  // Base 0-180
  
  // A0 -> IzquierdaX
  // A1 -> IzquierdaY
  // A2 -> DerechaY
  // A3 -> DerechaX
  
  int IzquierdaX = analogRead(A0);
  int IzquierdaY = analogRead(A1);
  int DerechaY = analogRead(A2);
  int DerechaX = analogRead(A3);

  
  int anguloBase = map (DerechaX, 0, 1023, 0, 180);
  int anguloBrazoIzquierdo = map (IzquierdaY, 0, 1023, 60, 150);
  int anguloBrazoDerecho = map (DerechaY, 0, 1023, 40, 145);
  int anguloPinza = map (IzquierdaX, 0, 1023, 100, 115);

  
  base.write(anguloBase);
  brazoIzquiero.write(anguloBrazoIzquierdo);
  brazoDerecho.write(anguloBrazoDerecho);
  pinza.write(anguloPinza);

  delay(100);
  
}
