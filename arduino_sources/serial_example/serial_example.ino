#include <Servo.h>
#include <string.h>

String var;
int sensor_pin = A0;
int servo_pin = 3;
Servo servo;

void setup() {
  // startup codes
  // serial begin, pinmode declaration, establishContact for establishing
  // servo attaches
  Serial.begin(9600);
  while (!Serial) {;} //waiting for serial to connect

  pinMode(servo_pin, OUTPUT);
  // Analog input need not be declared here
  Serial.println("serial started");
  establishContact();
  

}

void loop() {
  // repeated run
  if (Serial.available()>0){ // if input exists
    var = Serial.readString(); // available buffer cleared, 0 printed!!
    // char var = Serial.read(); -> use buffer, character input one by one
    // Serial.println(Serial.available()); //returns available number of bytes
    // Serial.println(var);
    Serial.write("received");
  }

}

void establishContact() {
  while (Serial.available() <= 0) {
    Serial.println(Serial.available());
    delay(300);
  }
}