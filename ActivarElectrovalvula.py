#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
def activar():
    RelayPin = 27    # pin11

    try:
        GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
        GPIO.setup(RelayPin, GPIO.OUT)
        GPIO.output(RelayPin, GPIO.HIGH)


        print 'Se ha ACTIVADO el riego'
        GPIO.output(RelayPin, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.output(RelayPin, GPIO.HIGH)
        GPIO.cleanup()
