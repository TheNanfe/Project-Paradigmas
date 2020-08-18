#Script de  objetos de tipo cajon.
#from view import View
import datetime as dt
from datetime import date
from alquilable import *
from abc import ABCMeta
import persistent

class Cajon(Alquilable, persistent.Persistent, metaclass = ABCMeta):
	'''Clase abstracta que representa a un espacio de estacionamiento alquilalbe'''
	costos_de_alquiler =  {'dia': 10000, 'mes': 192000, None: None}
	MAGIA_IDE = 1000
	
	def __init__ (self, numero, estado = 'libre', cliente = None, tipo = None):
	 	super().__init__()
	 	self.numero =  numero
	 	self.tipo = tipo
	 	self.estado = estado
	 	self.cliente = cliente

	def __str__(self):
		return '\nnum_Cajon:'+str(self.numero)+'\ntipo_cajon:'+self.tipo+'\nid_cajon:'+str(self.ide)+super().__str__()	
 	
	def alquilar(self, cliente, tipo_alquiler, fecha_inicio):
		'''Cambia el estado del cajon, dejandolo reservado por un cliente'''
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = (self.fecha_inicio) + dt.timedelta(self.__class__.tipos_de_alquiler[tipo_alquiler])
		self.tipo_alquiler = tipo_alquiler
		self.estado = 'ocupado'
		self.cliente = cliente
		self.cliente.monto_pagar = self.obtenerTarifa()
		self.__class__.cajones_ocupados = self.__class__.cajones_ocupados + 1

	def liberar(self):
		'''Cuando el periodo de alquiler termina, el cajon vuelve a ser liberado'''
		super().liberar()
		self.estado = 'libre'
		self.cliente = None
		self.tipo_alquiler = None
		self.__class__.cajones_ocupados = self.__class__.cajones_ocupados - 1

	def obtenerTarifa(self):
		'''Obtiene la tarifa que el cliente debera pagar'''
		tarifa_final = self.__class__.costos_de_alquiler[self.tipo_alquiler] + self.__class__.tarifa_extra
		return tarifa_final
	 	
	 	
class CajonNormal(Cajon):
	cajones_ocupados = 0
	cant_max = 5
	tarifa_extra = 0 

	def __init__(self, numero, estado = 'libre', cliente = None, tipo = 'normal'):
	 	super().__init__(numero, estado, cliente)
	 	self.tipo = tipo
	 	self.ide = self.__class__.MAGIA_IDE + self.numero

	@staticmethod
	def obtenerOcupados():
		return __class__.cajones_ocupados
	
	@staticmethod	
	def consultar():
		if __class__.cant_max <= __class__.cajones_ocupados:
			return 'No disponible'

		else:
			return 'disponible'
	 

class CajonSombra(Cajon):
	cant_max = 5
	cajones_ocupados = 0
	tarifa_extra = 15000

	def __init__(self, numero, estado = 'libre', cliente = None, tipo = 'sombra'):
	 	super().__init__(numero, estado, cliente)
	 	self.tipo = tipo
	 	self.ide = self.__class__.MAGIA_IDE*10 + self.numero

	@staticmethod
	def obtenerOcupados():
		return __class__.cajones_ocupados
	
	@staticmethod	
	def consultar():
		if __class__.cant_max <= __class__.cajones_ocupados:
			return 'No disponible'
		else:
			return 'disponible'
	

class CajonExtenso(Cajon):
	cant_max = 5
	cajones_ocupados = 0
	tarifa_extra =  20000

	def __init__(self, numero, estado = 'libre', cliente = None, tipo = 'extenso'):
	 	super().__init__(numero, estado, cliente)
	 	self.tipo = tipo
	 	self.ide = self.__class__.MAGIA_IDE*100 + self.numero

	@staticmethod
	def obtenerOcupados():
		return __class__.cajones_ocupados

	@staticmethod	
	def consultar():
		if __class__.cant_max <= __class__.cajones_ocupados:
			return 'No disponible'

		else:
			return 'disponible'
	

class CajonSombraExtenso(Cajon):
	cant_max = 5
	cajones_ocupados = 0
	tarifa_extra = 50000

	def __init__(self, numero, estado = 'libre', cliente = None, tipo = 'sombra_extenso'):
	 	super().__init__(numero, estado, cliente)
	 	self.tipo = tipo
	 	self.ide = self.__class__.MAGIA_IDE*1000 + self.numero

	@staticmethod
	def obtenerOcupados():
		return __class__.cajones_ocupados
	
	@staticmethod	
	def consultar():
		if __class__.cant_max <= __class__.cajones_ocupados:
			return 'no disponible'

		else:
			return 'disponible'


			