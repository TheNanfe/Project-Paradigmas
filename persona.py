import datetime as dt
from abc import ABCMeta
from datetime import date
from zodb.mizodb import DataBaseManagment

class Persona(metaclass = ABCMeta):
	'''Clase abstracta de persona'''
	def __init__(self, nombre, apellido, ci):
		self.nombre = nombre
		self.apellido = apellido
		self.ci = ci

	def salir_estacionamiento(self):
		pass


class Cliente(Persona):
	'''Clase abstracta de un cliente'''
	cantidad_clientes = 0
	def __init__ (self, ci, nombre= None, estado = None, apellido = None, cajon = None, monto_pagar = None, password = None, factura = None):
		
		super().__init__(nombre, apellido, ci)
		self.cajon = cajon
		self.estado = estado
		self.monto_pagar = monto_pagar
		self.password = password	
		self.factura = factura	

	def __str__(self):
		return '\npass_cliente: '+str(self.password)+'\nci_cliente:'+str(self.ci)+'\nmonto_pagar:'+str(self.monto_pagar)+'\nestado_cliente:'+str(self.estado)\
		+' \n'+str(self.cajon)

	def multa(self):	
		'''En caso de exceder su tiempo de alquiler, es multado'''
		multa = 10000*(int((date.today() - self.cajon.fecha_fin).days))
		return multa	

	def alquilar(self, cajon):
		'''Cambia el estado y brinda un espacio de estacionamiento al cliente(cajon)'''
		self.estado = 'dentro'
		self.cajon = cajon
		self.__class__.cantidad_clientes = self.__class__.cantidad_clientes + 1

	def ingresarConPass(self):
		'''Permite su re-ingreso al estacionamiento y cambia su estado a dentro'''
		self.estado = 'dentro'

	def salirEstacionamiento(self):
		'''cambia su estado a fuera'''
		self.estado = 'fuera'
		self.__class__.cantidad_clientes = self.__class__.cantidad_clientes - 1


class Empleado(Persona):
	'''Clase a ser implementada'''
	def __init__(self, ci, nombre, apellido):
		super().__init__(ci, nombre, apellido)
		self.pass_empleado = str(ci) + '_' + nombre[0] + apellido [0]


	def controlEmpleado(self, password):
		if password == self.password:
			return True


	def eliminarCliente(self, cajon_eliminar, database):#, password):
		#if self.controlEmpleado(password) == True:
		database.eliminarCajon(cajon_eliminar)


	def modificarCliente(self, cajon_modificar, database):#, password):
		#if self.controlEmpleado(password) == True:
		database.guardarCajon(cajon_modificar)
		
