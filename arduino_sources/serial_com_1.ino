#include <Servo.h>

// define pin number
int sensor_pin = A0;
int servo_pin = 3;

// make servo motor object
Servo servo;

void setup() {

  // attach servo object to servo pin
  servo.attach(servo_pin);

  // set serial timeout & begin serial
  Serial.setTimeout(100);
  Serial.begin(9600);
  
  while (!Serial) {;} //waiting for serial to connect

  // set digital pin mode
  pinMode(servo_pin, OUTPUT);

  // Analog input need not be declared here
  Serial.println("serial started");
  establishContact();
  

}

void loop() { // repeated run

  // 1. get serial input & servo write

  if (Serial.available()>0){ // if input exists
    Serial.println(Serial.available());

    // parse integer data
    int data = Serial.parseInt();
    Serial.print("your input is:");
    Serial.println(data);

    // function: get data & servo object, execute servo motor control
    controlServo(data, servo);

    // 2. get sensor input & serial write
    readSensor();
  }
}

// contact establishment
void establishContact() {
  while (Serial.available() <= 0) {
    delay(100);
  }
}

// servo motor control
void controlServo(int data, Servo &servo) { // get servo object by reference

  // clip data
  if (data < 10) data = 10;
  else if (data > 170) data = 170;

  // write servo
  servo.write(data);
  delay(1000);
}

// read sensor & serial write
int readSensor(){

  // read analog data, serial write
  int data = analogRead(sensor_pin);
  Serial.write(data);
  // Serial.print("sensor input is: ");
  // Serial.println(data);
  
  delay (100);
}