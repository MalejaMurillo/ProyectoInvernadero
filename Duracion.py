import time, datetime
import Conexion, threading

def cuentaRegresiva(duracion):
        estado = True
        try:                 
                while estado == True:
                        
                        print "Quedan %s seg para volver a evaluar los datos del sensor de temperatura"%duracion
                        if duracion == 0:
                                estado = False
                        else:                
                                duracion = duracion - 1
                                time.sleep(1)

        except Exception as e:
                print e
                estado = False
                
