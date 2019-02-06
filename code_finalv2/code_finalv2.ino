
#include <Servo.h>

Servo q1;  // create servo object to control a servo
Servo q2;  // create servo object to control a servo

float q1_angle;
float q2_angle;
int joint;

bool q1_ready;
bool q2_ready;
int delay_time;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  q1.attach(9);  // attaches the servo on pin 9 to the servo object
  q2.attach(10); 
  q1_angle = 0;
  q2_angle = 0;
  q1_ready = false;
  q2_ready = false;
  delay_time = 10;
  joint = 1; //everytime you read a new line or a command, iterate the loop. mod 2
}

//make delay propotional to distance

void loop() {
    static char buffer[32];
    static size_t pos; 

    if (Serial.available()) {
        char c = Serial.read();
        if ((c == '\n') || (c == ','))  {  // on end of line, parse the number
   
            buffer[pos] = '\0';
            float value = atof(buffer);
     

            if (joint == 1){
               q1_angle = value;
               q1_ready = false;
            }
             if (joint == 2){
               q2_angle = value;
               q2_ready = false;
            }
            pos = 0;
            
            joint = joint%2 + 1;
            Serial.print("q1: ");
            Serial.print(q1_angle);
            Serial.print(" q2: ");
            Serial.println(q2_angle);
            q1.write(q1_angle);
            q2.write(q2_angle);
            
//            delay(delay_time);   
            
        } else if (pos < sizeof buffer - 1) {  // otherwise, buffer it
            buffer[pos++] = c;
        }
    }

if (!q1_ready && !q2_ready){
    q1_ready = true;
    Serial.println("q1_ready"); 
    q2_ready = true;
    Serial.println("q2_ready"); 
}
}
