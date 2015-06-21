/*
 * belt
 *
 * ----------------------------------
 * Author: e.yllanescucho@ieee.org
 * Date: 2015-04-10
 * ----------------------------------
 */


#include <Ultrasonic.h>

#define TRIGGER_PIN  12
#define ECHO_PIN     13

Ultrasonic ultrasonic(TRIGGER_PIN, ECHO_PIN, 6000);

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
}
int time;
void loop()
{
  time = ultrasonic.Timing();
  Serial.println(time);
  delay(10);  
}
