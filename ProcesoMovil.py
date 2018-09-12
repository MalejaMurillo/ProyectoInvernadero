import Conexion
import threading
import time
import GiroArriba
import GiroAbajo

def consultarEstado():
    
    while True:
        
        resultado = Conexion.mtdConsultarModificacion()
        if resultado:
            if resultado[0][0] == "Bajar":
                 print "Bajando..."
                 GiroAbajo.mtdActivarMotorAbajo()
                 Conexion.mtdActualizarEstadoModi(resultado[0][1])
            elif resultado[0][0] == "Subir":
                 print "Subiendo..."
                 GiroArriba.mtdActivarMotorArriba()
                 Conexion.mtdActualizarEstadoModi(resultado[0][1])
       
        time.sleep(3)
        

hilo1 = threading.Thread(target=consultarEstado)
hilo1.start()

