/*
 * Radar
 *
 * ----------------------------------
 * Author: e.yllanescucho@ieee.org
 * Date: 2015-04-10
 * ----------------------------------
 */

#include <Servo.h>
#include <Ultrasonic.h>

#define TRIGGER_PIN  12
#define ECHO_PIN     13
#define SERVO_PIN    9

Servo myservo;  // create servo object to control a servo
Ultrasonic ultrasonic(TRIGGER_PIN, ECHO_PIN, 6000);

// this constant won't change.  It's the pin number
// of the sensor's output:
int angle = 1;
long time;
int val;
int tick =   1;
char mode = 't';
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  myservo.attach(SERVO_PIN);  // attaches the servo on SERVO_PIN to the servo object
  char s = 'n';
  Serial.println('s');
  while (s != 's')
    s = Serial.read();
}

void loop()
{
  if (Serial.available() > 0) {
    mode = Serial.read();
    switch (mode) {
      case 'r':
        time = ultrasonic.Timing();
        if (angle > 180) {
          angle = 180;
          tick = -1;
        }
        if (angle <= 0)
        {
          angle = 1;
          tick = 1;
        }
        Serial.print(time);
        Serial.print(" ");
        Serial.println(angle);
        val = map(angle, 0, 180, 0, 179);
        myservo.write(val);
        angle += tick;
        break;
    }
    delay(10);
  }
}
