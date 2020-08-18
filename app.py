from estacionamiento import Estacionamiento
from persona import Cliente
import cajones
from view import View
import os, os.path
from tkinter import *
import tkinter as tk
from gui_elementos import *
from functools import partial
class Aplicacion:
	'''Clase destinada a realizar las entradas y salidas'''

	def restablecimientoDatos():
		'''Realiza el backup de la base de datos.'''
		if os.path.isfile('./cajones.fs'):
			estacionamiento.restauracion()

	def registrarseEstacionamiento():
		'''Permite a los usuarios nuevos, registrare en el estacionamiento'''
		def funcion_combinada():
			try: 	
				cedula = int(atrapa_valor.get())
				entrada.config(state = 'disabled')
				ok_button.config(state = 'disabled')
				tipo_alquiler = StringVar()
				MiEtiqueta(nueva_ventana, text = 'Seleccione el tiempo que desea alquilar').place(x=220,y=80)
				radio_button = RadioBoton(nueva_ventana, variable = tipo_alquiler, text = 'Dia', value = 'dia').place(x=260,y=100)
				radio_button = RadioBoton(nueva_ventana, variable = tipo_alquiler, text = 'Mes', value = 'mes').place(x=300,y=100)
				operacion_parcial = partial(Aplicacion.mostrarBotones, nueva_ventana, tipo_alquiler, cedula)
				mostrar = MiBoton(nueva_ventana, text = 'Mostrar Estacionamientos disponibles')
				mostrar['command'] = lambda: Aplicacion.mostrarBotones(nueva_ventana, tipo_alquiler.get(), cedula)
				mostrar.place(x=200, y = 150)
				return 
			except:
				def mostrarVentanas():
					ventana_error.destroy()
					nueva_ventana.deiconify()

				nueva_ventana.withdraw()
				ventana_error = VentanaHija()
				ventana_error.title('error')
				ventana_error.geometry('580x180')
				MiEtiqueta(ventana_error, text = 'entrada incorrecta')	
				aceptar_button = MiBoton(ventana_error, text = 'Aceptar', command = mostrarVentanas).pack()

		nueva_ventana = VentanaHija()
		nueva_ventana.title('Registrarse')
		label_cedula = MiEtiqueta(nueva_ventana, text = 'Ingrese su cedula')
		atrapa_valor = StringVar()
		entrada = Entry(nueva_ventana, textvariable = atrapa_valor)
		entrada.pack()
		entrada.focus_set()
		ok_button = MiBoton(nueva_ventana, text = 'ok')
		ok_button['command'] = lambda : funcion_combinada()
		ok_button.pack()
		print('Everython went ok!')

	def salirEstacionamiento():
		'''Para los usuarios que deseen abandonar el estacionamiento'''
		Aplicacion.restablecimientoDatos()
		def estado_salida():
			def frameDestroyer():
				nueva_ventana.destroy()
				child.destroy()

			try:
				password = passw.get()	
				estado_salida = estacionamiento.liberarCajon(password)
				if estado_salida == 'Que tenga un buen dia':	
					nueva_ventana.destroy()
					child = VentanaHija()
					child.title('salida')
					MiEtiqueta(child, text = 'Que tenga un buen dia')
					child.after(1000, lambda: child.destroy())
				elif estado_salida == 'Pass incorrecto':
					child = VentanaHija()
					child.title('error')
					MiEtiqueta(child, text = 'PASS INCORRECTO!')
					MiBoton(child, text = 'Aceptar', command = frameDestroyer).pack()	
				else:
					child = VentanaHija()
					child.title('multa')
					print(estado_salida)
					MiEtiqueta(child, text = ('ATENCION!\nDebe pagar una multa de ',int(estado_salida)))
					MiBoton(child, text = 'Aceptar', command = frameDestroyer).pack()
			except Exception as e:	
				child = VentanaHija()
				child.title('error')
				MiEtiqueta(child, text = 'Entrada no valida ')
				MiBoton(child, text = 'Aceptar', command = child.destroy).pack()
				raise('Entrada incorrecta'+str(e))
			

		nueva_ventana = VentanaHija()
		nueva_ventana.title('Salir Estacionamiento')
		label_password = MiEtiqueta(nueva_ventana, text = 'Ingrese su Pass para salir del estacionamiento')
		passw = StringVar()
		entrada_pass = Entry(nueva_ventana, textvariable = passw)
		entrada_pass.pack()
		entrada_pass.focus_set()
		ok_button = MiBoton(nueva_ventana, text = 'ok', command = lambda: estado_salida())
		ok_button.pack()
		
	def ingresarEstacionamiento():
		'''Para los usuarios que alquilaron por mes. Permite volver a ingresar al estacionamiento'''
		def estado_entrada():
			def windowsDestroyer():
				nueva_ventana.destroy()
				child.destroy()

			Aplicacion.restablecimientoDatos()
			password = passw.get()	
			print(password)
			estado_entrada = estacionamiento.ingresarEstacionamiento(password)
			child = VentanaHija()
			MiEtiqueta(child, text = estado_entrada)
			child.after(1670, lambda: child.destroy())
			
		nueva_ventana = VentanaHija()
		label_password = MiEtiqueta(nueva_ventana, text = 'Ingrese su Pass para entrar al estacionamiento')
		passw = StringVar()
		entrada_pass = Entry(nueva_ventana, textvariable = passw)
		entrada_pass.pack()
		entrada_pass.focus_set()
		ok_button = MiBoton(nueva_ventana, text = 'ok', command = lambda: estado_entrada())
		ok_button.pack()

	def control():
		'''Controla interminablemente y da de baja todos los alquileres que hayan excedido la fecha de alquiler'''
		alquileres_terminados = estacionamiento.controlarCajones()
		for x in range(0, len(alquileres_terminados)):
			llave = alquileres_terminados[x]
			database.eliminarCajon(estacionamiento.liberarCajon(llave))

	@staticmethod
	def mostrarBotones(nueva_ventana, tipo_alquiler, cedula):
		'''Metodo utilizado solo como guia'''
		def funcion_combinada(x,y):
			def kill_windows():
				nueva_ventana.destroy()
				child.destroy()
				Aplicacion.registrarseEstacionamiento()	

			def killWindowsAndRestart():
				nueva_ventana.destroy()
				ventana_nieta.destroy()
				estacionamiento.database.eliminarCajon(cajones[x][y].cliente.password)
				cajones[x][y].liberar()
				Aplicacion.registrarseEstacionamiento()

			estacionamiento.alquilarCajon(cajones[x][y], tipo_alquiler, Cliente(cedula))
			child = VentanaHija()
			child.title('Detalle factura')
			MiEtiqueta(child, text = 'Detalle Factura: \n'+str(cajones[x][y].cliente.factura), justify = LEFT)
			aceptar_button = MiBoton(child, text = 'Aceptar', command = kill_windows).pack()
			cancelar_button = MiBoton(child, text = 'Cancelar', command = killWindowsAndRestart).pack()

		Aplicacion.restablecimientoDatos()
		f_p = 100
		c_p = 200
		nuevo_label = MiEtiqueta(nueva_ventana, text = 'Seleccione su estacionamiento' )
		for x in range(0, len(cajones)):
			f_p = 100
			c_p += 50
			MiEtiqueta(nueva_ventana, text = cajones[x][0].tipo).place(x=f_p,y=c_p)
			c_p += 50
			for y in range(0, len(cajones[x])):
				if cajones[x][y].cliente != None:
					
					def aviso_ocupado():
						ventana_aviso = VentanaHija()
						ventana_aviso.title('aviso')
						MiEtiqueta(ventana_aviso, text = 'Estacionamiento actualmente Ocupado')
						aceptar_button = MiBoton(ventana_aviso, text = 'Aceptar', command = ventana_aviso.destroy).pack()

					cajon_button = MiBoton(nueva_ventana,\
					 text = 'Cajon '+ cajones[x][y].tipo + ': ' + str(+cajones[x][y].numero))
					cajon_button['fg'] = 'red'
					cajon_button['command'] = aviso_ocupado
					cajon_button.place(x=f_p,y=c_p)
				else:
					cajon_button = MiBoton(nueva_ventana,\
					 text = 'Cajon '+ cajones[x][y].tipo + ': ' + str(+cajones[x][y].numero))
					cajon_button['bg'] = 'green'
					funcion_parcial = partial(funcion_combinada,x,y)
					cajon_button['command'] = funcion_parcial
					cajon_button.place(x=f_p,y=c_p)
				f_p = f_p + 150

	def main(ventana):
		'''Metodo que contiene las funcionaes vitales del estacionamiento'''
		def regSalEnt():
			Aplicacion.registrarseEstacionamiento()
			Aplicacion.salirEstacionamiento()
			Aplicacion.ingresarEstacionamiento()
		try:
			#regSalEnt()
			alquilar_button = MiBoton(ventana, text = 'Alquilar')
			alquilar_button['command'] = lambda : Aplicacion.registrarseEstacionamiento()
			salir_button = MiBoton(ventana, text = 'Salir')
			salir_button['command'] = lambda : Aplicacion.salirEstacionamiento()
			ingresar_button= MiBoton(ventana, text = 'Ingresar')
			ingresar_button['command'] = lambda : Aplicacion.ingresarEstacionamiento()
			alquilar_button.pack()
			salir_button.pack()
			ingresar_button.pack()
		except Exception as e:
			print(e)
if __name__ == '__main__':
	estacionamiento = Estacionamiento()
	cajones = estacionamiento.cajones
	#estacionamiento.controlarCajones()
	try:
		ventana = MiVentana()
		Aplicacion.main(ventana)
		ventana.mainloop()
	except Exception as e:
		print(e)

