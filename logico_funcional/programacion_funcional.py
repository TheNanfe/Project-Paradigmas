from zodb.mizodb import DataBaseManagment
from datetime import date
import functools

''' Codigo Original------Origen: estacionamiento.py
def controlarCajones(self):
		for x in range(0,len(self.cajones)):
			for y in range(0,len(self.cajones[x])):
				if self.cajones[x][y].fecha_fin != None:	
					if (self.cajones[x][y].fecha_fin) < (date.today() and self.cajones[x][y].cliente.estado == 'fuera'):
						self.database.eliminarCajon(self.cajones[x][y].cliente.password)'''

###Se encarga de eliminar a todos los clientes cuyos periodos de alquiler hayan finiquitado###
def eliminar(length, cajones):
	if length == -1:
		return
	if length == 0:
		database.eliminarCajon(cajones[length].cliente.password)
		return
	database.eliminarCajon(cajones[length].cliente.password)
	eliminar(length-1,cajones)

database = DataBaseManagment() 
all_Cajones_alquilados = database.traerTodo()
expired_time_cajones = [x for x in all_Cajones_alquilados if x.fecha_fin < date.today() and x.cliente.estado == 'fuera']
eliminar(len(expired_time_cajones)-1,expired_time_cajones)






