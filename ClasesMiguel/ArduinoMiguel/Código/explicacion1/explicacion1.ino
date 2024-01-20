
void setup() {
  pinMode(10, OUTPUT);
  pinMode(A0, INPUT);
}

void loop() {
    int valor = analogRead(A0);
    analogWrite(10, valor);
    delay(50);
  
}
