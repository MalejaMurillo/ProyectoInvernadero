

import RPi.GPIO as GPIO
from time import sleep



def mtdActivarMotorArriba():
    GPIO.setmode(GPIO.BCM)
    Motor1A = 23
    Motor1B = 24
    Motor1E = 25
 
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    
    pwm = GPIO.PWM(25,100)
    pwm.start(12)
    print "GIRO ARRIBA"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
     
    sleep(3)

     
    print "MOTOR DETENIDO"
    GPIO.output(Motor1E,GPIO.LOW)
    pwm.stop() 
    GPIO.cleanup()
mtdActivarMotorArriba()
