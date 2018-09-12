import RPi.GPIO as GPIO
from time import sleep



def mtdActivarMotorAbajo():
    GPIO.setmode(GPIO.BCM)
    Motor1A = 23
    Motor1B = 24
    Motor1E = 25
 
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)

    pwm = GPIO.PWM(18,100)
    pwm.start(32)

    print "GIRO ABAJO"
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
     
    sleep(0.9)
     
    print "MOTOR DETENIDO"
    GPIO.output(Motor1E,GPIO.LOW)
    pwm.stop()
     
    GPIO.cleanup()
mtdActivarMotorAbajo()
