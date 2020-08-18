from abc import ABCMeta
class Documento(metaclass = ABCMeta):
	cantidad_documentos = 0
	prefijo_sucursal = '001'

	def __init__(self, num_documento, cliente, nombre_empresa):
		self.num_documento = self.__class__.prefijo_sucursal +  '-' + str(num_documento)
		self.cliente = cliente
		self.nombre_empresa = nombre_empresa
		self.__class__.cantidad_documentos = self.__class__.cantidad_documentos + 1

	def __str__(self):
		texto =\
		 'num_documento :'+self.num_documento+'\n'+self.nombre_empresa+'\nDatos del cliente\n'+str(self.cliente)+'\n' 
		return texto

	@staticmethod
	def obtenerCantDocumentos():
		return self.__class__.cantidad_documentos

class Factura(Documento):
	cantidad_facturas = 0

	def __init__(self, cliente, cajon, nombre_empresa = 'SuperEstacionamiento',  num_documento = cantidad_facturas ):
		super().__init__(num_documento, cliente, nombre_empresa)
		self.cajon = cajon
		self.__class__.cantidad_facturas = self.__class__.cantidad_facturas + 1

	def __str__(self):
		return super().__str__() +'\nDatos del SuperEstacionamiento y alquiler\n'

	@staticmethod
	def obtenerCantFacturas():
		return __class__.cantidad_facturas

	



