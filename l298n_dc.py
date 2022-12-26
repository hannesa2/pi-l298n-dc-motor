# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

from getch import getch, pause
import RPi.GPIO as GPIO          
from time import sleep

in1 = 21
in2 = 25
in3 = 24
in4 = 23
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in1,GPIO.LOW)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-rightmotor l-leftmotor s-stop f-forward b-backward")
print("\n")    
print("push 'e' to exit")
print("\n")

while(1):

    x=getch()
    
    if x=='r':
        print("right motor")
        if(temp1==1):
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.LOW)
         print("backward")
         x='z'
    
    elif x=='l':
       print("left motor")
       if(temp1==1):
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        print("forward")
        x='z'
       else:
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        print("backward")
        x='z'

    elif x=='s':
       print("stop")
       GPIO.output(in3,GPIO.LOW)
       GPIO.output(in4,GPIO.LOW)
       GPIO.output(in1,GPIO.LOW)
       GPIO.output(in2,GPIO.LOW)
       x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'
       
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

