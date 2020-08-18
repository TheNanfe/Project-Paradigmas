import datetime as dt
from datetime import date
from abc import ABCMeta

class Alquilable(metaclass = ABCMeta):
	'''Super Clase a ser heredada por la clase cajon'''
	tipos_de_alquiler = {'dia': 0, 'mes': 30, None: 0}
	multaXdia = 10000 

	def __init__(self, fecha_inicio = None, fecha_fin = None, tipo_alquiler = None):
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin
		self.tipo_alquiler = tipo_alquiler
		
	def __str__(self):	
		return '\nfecha_inicio:'+str(self.fecha_inicio)+'\nfecha_fin:'+str(self.fecha_fin)+'\ntipo_alquiler:'+str(self.tipo_alquiler)

	def alquilar():
		pass

	def liberar(self):
		self.fecha_inicio = None
		self.fecha_fin = None
		self.tipo_alquiler = None

	def obtenerTarifa(self):
		pass
