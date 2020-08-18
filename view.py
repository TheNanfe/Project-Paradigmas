# vista UCLI
import os
from datetime import date


class View:
	############CAJONES###############
	@staticmethod
	def consultarCajon(fecha_liberacion):
		if fecha_liberacion == None:
			print('El cajon esta libre')
		else:
			print('El cajon estara despues del %s' %(str(fecha_liberacion)))

	#############APP##################
	@staticmethod
	def mainMenu():
		return input('\
			1. Alquilar Estacionamiento\n\
			2. Abandonar Estacionamiento\n\
			3. Ingresar Estacionamiento\n \
			4. Listar clientes con sus cajone(Solo para guia)\n\
			\nEscoja una opcion: ')


	############OPERACIONES#############
	@staticmethod
	def obtenerCedula():
		while True:
			try:
				x = int(input('Ingrese su numero de Cedula: '))
				return str(x)
			except ValueError as e:
				print(str(e)+'\nEntrada No Valida, por favor vuelva a ingresar su numero de cedula')

	@staticmethod
	def obtenerTipoCajon():
		while True:
			try:
				x = int(input('\n\n\
				1: Estacionamiento Normal\n\
				2: Estacionamiento con Sombra\n\
				3: Estacionamiento Extenso\n\
				4: Estacionamiento Extenso con Sombra\n\n\
				Ingrese tipo de estacionamiento que desea:'))
				return x
			except Exception:
				print('Entrada no valida')

	@staticmethod
	def mensaje (tipo_mensaje):
		print(tipo_mensaje)
			
	@staticmethod
	def obtenerTipoAlquiler():
		diccionario = {'1':'dia', '2':'mes' }
		while True:
				try:
					x = diccionario[input('\
					1: Alquilar por hoy\n\
					2: Alquilar por el Mes\n\n\
					Por cuanto tiempo desea alquilarlo?: ')]
					break
				except KeyError:
					print('Entrada incorrecta, por favor, vuelva a ingresar')
		return x

	@staticmethod
	def obtenerTicket(cajon):
		print('\nCliente:\t%s' %cajon.cliente.ci)
		print('\nTipo de Estacionamiento:\t%s' %cajon.tipo)
		print('\nFecha de Entrada:\t%s' %str(cajon.fecha_inicio))
		print('\nFecha de Salida:\t%s' %str(cajon.fecha_fin))
		print('\nTotal a Pagar: \t%s' %str(cajon.cliente.monto_pagar)+'Gs')
		print('\nNumero Estacionamiento:\t%s' %str(cajon.ide))
		print('\n Password: %s' %cajon.cliente.password)
		i = ''
		while i != 's':
			i = str.lower(input('\n Proseguir?(S): '))
		else: 
			print('Operacion Exitosa!')
			i = 0
			while i < 10000000:
				i = i + 1
			os.system("cls")
			return 0

	@staticmethod
	def introducirPass():
		try:
			i = input('Por favor, introduzca su pass: ')
			return i
		except NameError :
			print('Password invalido.')
		except ValueError :
			print('Password invalido.')
	
	@staticmethod
	def mostrarMulta(multa):
		print('Tiene una multa de %igs' %multa)
		i = ''
		while i != 's':
			i = str.lower(input('\n Proseguir?(S \ N): '))
		if i == 's':
			print('Que tenga un buen dia')
			os.system("clear")
			return

	@staticmethod
	def menuSuper():
		try:	
			x = input('\
				1: Eliminar Cliente\n\
				2: Agregar Cliente\n\
				3: Modificar Clientes\n\
				4: Obtener Lista Clientes\n\
				5: Volver Al Menu Inicial\n\
				\nSeleccione una opcion: ')
			return x
		except KeyError:
			print('Entrada no valida')

	@staticmethod
	def listarClientes(tipo, estado):
		c = 0
		c1 = 0
		for y in range(0, len(tipo)):
			for x in range(0, len(tipo[y])):
				c = c + 1
				if tipo[y][x].estado == estado:
					c1  = c1 + 1
					print(c, tipo[y][x])
		if c1 == 0:
			print('No hay espacios '+estado+'s')

	@staticmethod
	def posicion_cliente():
		return input('Ingrese el cliente que desee eliminar: ')

	@staticmethod
	def obtenerFecha(mensaje):
		while True:
			try:
				x = date(date.today().year,int(input('\tMes: ')), int(input('dia: ')))
				print(x, ' misteriosamente no entra en la excepcion. Why')
				return x
			except TypeError:
				print('Formato de fecha no valido')

	@staticmethod
	def obtenerModificacion():
		return input('\
			1: Modificar Cedula Cliente\n\
			2: Modificar Password del Cliente\n\
			3: Modificar Fecha de entrada\n\
			4: Modificar Fecha de Salida\n\
			\nIngrese una opcion: ')

