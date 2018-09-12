#!/usr/bin/python
import RPi.GPIO as GPIO
import time, Conexion,datetime

def tomarDatos():
        #GPIO SETUP
        try:
                channel = 21
                #global dato 
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(channel, GPIO.IN)
                 
                def callback(channel):
                        actual = datetime.datetime.now()
                        fecha =  actual.strftime("%Y-%m-%d")
                        if GPIO.input(channel):
                                
                                print "NO Water Detected!"
                                #dato = 0 
                                #Conexion.mtdGuardarDatosH(0,fecha,time.strftime("%X"))
                        else:
                                print "Water Detected!"
                                #dato = 100
                                #Conexion.mtdGuardarDatosH(100,fecha,time.strftime("%X"))
                 
                GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us knw when the pin goes HIGH or LOW
                GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

                        
                #return dato;
        except KeyboardInterrupt:
                GPIO.cleanup()

tomarDatos()
