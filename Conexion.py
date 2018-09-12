import MySQLdb



USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
NAME_BD = 'BDInvernadero'

try:
	
	

        def mtdGuardarDatos(temperatura, fech, hor):
            print(fech+' '+ hor)
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "Insert INTO dato (Dato,Tipo,IdSensor,Fecha,Hora)VALUES({dato},'{tipo}',{idSensor},'{fecha}','{hora}')"
            queryTemperatura= sql.format(dato=temperatura,tipo='Temperatura',idSensor = 18, fecha = fech, hora = hor)
            cursor.execute(queryTemperatura)
            conexion.commit()
            conexion.close()

        def mtdGuardarDatosH(humedad,fech, hor):
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "Insert INTO dato (Dato,Tipo,IdSensor,Fecha,Hora)VALUES({dato},'{tipo}',{idSensor},'{fecha}','{hora}')"
            queryHumedad = sql.format(dato=humedad,tipo='Humedad',idSensor = 19, fecha = fech, hora = hor)
            cursor.execute(queryHumedad)
            conexion.commit()
            conexion.close()

	def mtdConsultarEstado():
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "SELECT Estado FROM actuador Where idActuador = {idActuador}"
            query = sql.format(idActuador=1)
            cursor.execute(query)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado

        def mtdConsultarEstadoR():
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "SELECT Estado FROM actuador Where idActuador = {idActuador}"
            query = sql.format(idActuador=2)
            cursor.execute(query)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        
        def mtdActualizarEstado(est):
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "UPDATE actuador SET Estado = '{estado}' Where idActuador = {idActuador}"
            query = sql.format(estado = est, idActuador=1)
            cursor.execute(query)
            conexion.commit()
            conexion.close()
            
        def mtdActualizarEstadoR(est):
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "UPDATE actuador SET Estado = '{estado}' Where idActuador = {idActuador}"
            query = sql.format(estado = est, idActuador=2)
            cursor.execute(query)
            conexion.commit()
            conexion.close()

        def mtdConsultarModificacion():
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "SELECT Accion,IdModificacion, Duracion FROM modificacion Where idActuador = {idActuador} and Estado = '{estado}'"
            query = sql.format(idActuador=1, estado = 'Pendiente')
            cursor.execute(query)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        def mtdConsultarModificacionR():
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "SELECT Accion,IdModificacion, Duracion FROM modificacion Where idActuador = {idActuador} and Estado = '{estado}'"
            query = sql.format(idActuador=2, estado = 'Pendiente')
            cursor.execute(query)
            resultado = cursor.fetchall()
            conexion.close()
            return resultado

        def mtdActualizarEstadoModi(IdModi):
            conexion = MySQLdb.connect(HOST,USER,PASSWORD,NAME_BD)
            cursor = conexion.cursor()
            sql= "UPDATE modificacion SET Estado = '{estado}' Where idModificacion = {idModificacion}"
            query = sql.format(estado = 'Realizada', idModificacion=IdModi)
            cursor.execute(query)
            conexion.commit()
            conexion.close()
            
	
except MySQLdb.Error as error:
	print(error)


	
	
