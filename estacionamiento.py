from zodb.mizodb import DataBaseManagment
from cajones import *
from persona import Cliente, Empleado
from view import View
from datetime import date
from random import choice
from documentos import *
import copy
class Estacionamiento:
	'''Clase abstracta de Empresa de estacionamiento.Su funcion pasa de realizar un intercambio de informacion
	entre los clientes y espacio a ser alquilados'''

	def	__init__(self):
		self.cajones = [\
		[CajonNormal(x) for x in range(0, CajonNormal.cant_max)],\
		[CajonSombra(x) for x in range(0, CajonSombra.cant_max)],\
		[CajonExtenso(x) for x in range(0, CajonExtenso.cant_max)],\
		[CajonSombraExtenso(x) for x in range(0, CajonSombraExtenso.cant_max)]]
		self.cajon_alquilable = None
		self.cliente = None
		self.database = DataBaseManagment()

	def obtenerEspacioLibre(self,tipo):
		'''Obtiene un espacio que esta libre para ser alquilado'''
		for x in range(0, len(self.cajones[tipo-1])):
			if  self.cajones[tipo-1][x].estado == 'libre':
				self.cajon_alquilable = self.cajones[tipo-1][x]
				return self.cajon_alquilable

	@staticmethod
	def generarPass(prefijo):
		'''Genera un pass para el cliente, para que pueda salir e ingresar del/al estacionamiento'''
		longitud = 3
		caracteres = 'qwertyuiopasdfghjklzxcvbnm'
		password = ''
		password = password.join([choice(caracteres) for x in range(longitud)])
		password = prefijo + password
		return password

	def encontrarCajon(self, pasw):
		'''Encuentra el cajon asignado a un cliente por medio de su password'''
		try:
			self.cajon_alquilable = self.cajones[int(pasw[0])-1][int(pasw[1])]
		except Exception as e:
			texto = 'From method: encontrarCajon(); line 38:\n'
			raise Exception(texto + str(e) + '; line 41')

	def alquilarCajon(self, cajon, tipo_aquiler, cliente):
		tipos_de_cajon = {\
		'normal':1,\
		'sombra':2,\
		'extenso':3,\
		'sombra_extenso': 4
		}
		'''Aqui se realizan los 'tramites' para que el cliente pueda alquilar su cajon'''
		self.cliente = cliente
		self.cajon_alquilable = cajon
		para_el_pass = str(tipos_de_cajon[self.cajon_alquilable.tipo])+str(self.cajon_alquilable.numero)
		self.cliente.password = self.__class__.generarPass(para_el_pass)
		self.cajon_alquilable.alquilar(self.cliente, tipo_aquiler, date.today())				
		self.cliente.alquilar(self.cajon_alquilable)
		self.cliente.factura = Factura(self.cliente, self.cajon_alquilable)
		self.database.guardarCajon(copy.deepcopy(self.cajon_alquilable))
		return self.cajon_alquilable

	def restauracion(self):
		'''restablece todos los datos guardados en caso de que el programa sea interrumpido'''
		numero_llaves = self.database.llaves()
		for key in numero_llaves:
			datos_a_restaurar = self.database.restaurarDatos(key)
			self.encontrarCajon(key)
			self.cliente = datos_a_restaurar[1]
			self.cajon_alquilable.tipo_alquiler = datos_a_restaurar[3]
			self.cajon_alquilable.alquilar(self.cliente, self.cajon_alquilable.tipo_alquiler, datos_a_restaurar[2])

	def multar(self):
		'''Verifica si el cliente excedio su tiempo de alquiler y de ser asi, es multado'''
		if self.cliente.estado == 'dentro':
			return self.cliente.multa()

	def liberarCajon(self,password):
		'''Permite que los clientes abandonen el estacionamiento'''
		try:
			self.encontrarCajon(password)
			self.cliente = self.cajon_alquilable.cliente
			if self.cliente.password == password:
				if (self.cajon_alquilable.fecha_fin) < (date.today()): 
					multa = self.multar()
					self.cliente.salirEstacionamiento()
					self.cajon_alquilable.liberar()
					self.database.eliminarCajon(self.cliente.password)
					return multa
				elif (self.cajon_alquilable.fecha_fin) == (date.today()):
					self.cliente.salirEstacionamiento()
					self.cajon_alquilable.liberar()
					self.database.eliminarCajon(self.cliente.password)
					return 'Que tenga un buen dia'
				else:
					self.cliente.salirEstacionamiento()
					self.database.guardarCajon(copy.deepcopy(self.cajon_alquilable))
					return 'Que tenga un buen dia'
			else:
				print('esto')
				return 'Pass incorrecto'
		except Exception as e:
			print('aquello')
			raise Exception('From method: liberarCajon, line 80:\n'+str(e))
			
	def ingresarEstacionamiento(self, password):
		'''Permite que los clientes con alquiler de mes puedan volver a ingresar al estacionamiento'''
		try:
			self.encontrarCajon(password)
			self.cliente = self.cajon_alquilable.cliente
			if self.cliente.password == password and self.cliente.estado == 'fuera':	
				if self.cajon_alquilable.fecha_fin < date.today():
					#self.database.eliminarCajon(copy.deepcopy(self.cliente.password))
					return 'Alquiler finalizado'
				else:
					self.cliente.ingresarConPass()
					#copia = copy.deepcopy(self.cajon_alquilable)
					#self.database.modificarCajon(copy.deepcopy(self.cliente.password))
					return 'Bien volvido estimado caballero caballeroso(No tuve en cuenta que pueda ser mujer D:)!'
			else:
				return 'Pass incorrecto'
		except:
			texto = 'Pass incorrecto o alquiler finalizado\n'
			return texto

	def controlarCajones(self):
		for x in range(0,len(self.cajones)):
			for y in range(0,len(self.cajones[x])):
				if self.cajones[x][y].fecha_fin != None:	
					if (self.cajones[x][y].fecha_fin) < (date.today() and self.cajones[x][y].cliente.estado == 'fuera'):
						self.database.eliminarCajon(self.cajones[x][y].cliente.password)

