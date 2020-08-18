# mizodb.py
from ZODB import FileStorage, DB
import transaction
import copy

class MiZODB(object):
	'''clase  que inicializa el archivo que se encarga de la perscistencia del objeto'''	
	def __init__(self, archivo):
		self.storage = FileStorage.FileStorage(archivo)
		self.db = DB(self.storage)
		self.conexion = self.db.open()
		self.raiz = self.conexion.root()

	def close(self):
		self.conexion.close()
		self.db.close()
		self.storage.close()
		

class DataBaseManagment():

	@staticmethod
	def close():
		db = MiZODB('./cajones.fs')
		db.close()

	@staticmethod
	def guardarCajon(cajon):
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		dbroot[cajon.cliente.password] = cajon
		print('guardarCajon: ',dbroot[cajon.cliente.password])
		transaction.commit()
		db.close()

	@staticmethod
	def modificarEstado(password):
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		dbroot[password].estado = 'dentro'
		transaction.commit()
		db.close()


	@staticmethod
	def eliminarCajon(key):
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		del dbroot[key]
		transaction.commit()
		db.close()

	@staticmethod
	def guardarFactura(factura):
		db = MiZODB('./facturas.fs')
		dbroot = db.raiz
		dbroot[cajon.cliente.password] = factura
		transaction.commit()
		db.close()

	@staticmethod
	def llaves():
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		llaves = dbroot.keys()
		db.close()
		return llaves

	@staticmethod
	def consultar(llave):
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		objetoConsulta = dbroot[llave]
		db.close()
		return objetoConsulta

	@staticmethod
	def traerTodo():
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		objetosConsulta = []
		for key in dbroot.keys():
			#print(key)
			objetosConsulta.append(copy.deepcopy(dbroot[key]))
			#print(objetosConsulta)
		
		db.close()
		#print(objetosConsulta)
		return objetosConsulta


	@staticmethod
	def restaurarDatos(key):
		datos_a_restaurar = [] 
		db = MiZODB('./cajones.fs')
		dbroot = db.raiz
		datos_a_restaurar.append(dbroot[key].tipo)
		datos_a_restaurar.append(dbroot[key].cliente)
		datos_a_restaurar.append(dbroot[key].fecha_inicio)
		datos_a_restaurar.append(dbroot[key].tipo_alquiler)
		transaction.commit()
		db.close()
		return datos_a_restaurar