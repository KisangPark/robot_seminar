#include <Servo.h>

// define pin number
int sensor_pin = A0;
int servo_pin = 3;

// make servo motor object
Servo servo;

// setup function
void setup() {

  // attach servo object to servo pin
  servo.attach(servo_pin);

  // set serial timeout & begin serial
  Serial.setTimeout(100);
  Serial.begin(9600);
  
  while (!Serial) {;} //waiting for serial to connect

  // set digital pin mode
  pinMode(servo_pin, OUTPUT);

  Serial.println("1025"); // serial connection started flag
  establishContact(); // when input, move to loop function
  
}

// loop function: receive serial data, move servo, get sensor data
void loop() { 

  // 1. if serial input received, execute followings

  if (Serial.available()>0){ // if input exists

    // parse received character into integer data & saving
    int data = Serial.parseInt();

    // 2. function: get data & servo object, execute servo motor control
    controlServo(data, servo);

    // 3. get sensor input & serial write
    readSensor();
  }

  // total delay: 200
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
  delay(100);
}

// read sensor & serial write
int readSensor(){

  // read analog data, serial write
  int data = analogRead(sensor_pin);

  // convert into string, write to serial monitor
  String output = String(data);
  Serial.println(output);
  
  delay (100);
}