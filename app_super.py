from datetime import date
from estacionamiento import Estacionamiento
from persona import Cliente, Empleado
import cajones
from view import View
import os, os.path
from tkinter import *
import tkinter as tk
from gui_elementos import *
from functools import partial

class AplicacionSuper():

	def restablecimientoDatos():
		'''Realiza el backup de la base de datos.'''
		if os.path.isfile('./cajones.fs'):
			estacionamiento.restauracion()
			
	def main(w,h):
		'''Metodo que contiene las funcionaes vitales del estacionamiento'''
		paleta_bg = {'normal': 'pale green', 'sombra': 'OliveDrab2', 'extenso': 'goldenrod1', 'sombra_extenso': 'IndianRed1'}
		font_conf = {'dia':'Helvetica 8', 'mes':'Helvetica 8 bold'}
		def actualizar():
			w, h = child.winfo_screenwidth(), child.winfo_screenheight()
			child.destroy()
			AplicacionSuper.main(w,h)			
		try:	
			def borrarClientes(cliente):
				empleado.eliminarCliente(cliente.cliente.password, estacionamiento.database)
				actualizar()

			def editarCliente(cliente):
				
				def formatearFecha(fecha):
					fecha = [int(fecha[0:4]),int(fecha[5:7]),int(fecha[8:10])]
					fecha = date(fecha[0],fecha[1],fecha[2])
					return fecha

				def modificarAndSend():
					cliente.cliente.ci = int(entrada_cedula.get())
					cliente.fecha_inicio = formatearFecha(entrada_fecha_inicio.get())
					cliente.fecha_fin = formatearFecha(entrada_fecha_fin.get())
					cliente.numero = int(entrada_numero_cajon.get())
					empleado.modificarCliente(cliente, estacionamiento.database)
					nueva_ventana.destroy()
					actualizar()


				f_p = 300
				nueva_ventana = VentanaHija()
				nueva_ventana.title('modificar')
				MiEtiqueta(nueva_ventana, text = 'Cedula').place(x = f_p, y = 40)
				entrada_cedula = Entry(nueva_ventana)
				entrada_cedula.insert(0, cliente.cliente.ci)
				entrada_cedula.place(x = 400, y = 40)
				MiEtiqueta(nueva_ventana, text = 'fecha_inicio').place(x = f_p, y = 60)
				entrada_fecha_inicio = Entry(nueva_ventana)
				entrada_fecha_inicio.insert(0, cliente.fecha_inicio)
				entrada_fecha_inicio.place(x = 400, y = 60)
				MiEtiqueta(nueva_ventana, text = 'fecha_fin').place(x = f_p, y = 80)
				entrada_fecha_fin = Entry(nueva_ventana)
				entrada_fecha_fin.insert(0, cliente.fecha_fin)
				entrada_fecha_fin.place(x = 400, y = 80)
				MiEtiqueta(nueva_ventana, text = 'Numero_cajon').place(x = f_p, y = 100)
				entrada_numero_cajon = Entry(nueva_ventana)
				entrada_numero_cajon.insert(0, cliente.numero)
				entrada_numero_cajon.place(x = 400, y = 100)
				ok_button = MiBoton(nueva_ventana, text = 'OK', command = lambda: modificarAndSend()).pack()
				cancel_button = MiBoton(nueva_ventana, text = 'Cancelar')
				cancel_button['command'] = lambda: nueva_ventana.destroy()
				cancel_button.pack()

			child = VentanaHija()
			child.title('Control de estacionamiento')
			child.overrideredirect(0)
			child.geometry("%dx%d+0+0" % (w, h))
			child['bg'] = 'gray26'			
			todos_clientes = estacionamiento.database.traerTodo()
			f_p = 50
			c_p = 0
			nuevo_label = MiEtiqueta(child, text = 'Clientes', justify = LEFT ).place(x = 320, y = 10)
			actualilzar_button = MiBoton(child,text = 'Actualizar', command = lambda: actualizar() )
			actualilzar_button['bg'] = 	'SteelBlue1'
			actualilzar_button.place(x = 500, y = 10)
			for cliente in todos_clientes:
				c_p += 50
				if c_p >= 800:
					f_p += 200
					c_p = 50
				etiqueta_cliente = MiEtiqueta(child, text = cliente.cliente, justify = LEFT, font = font_conf[cliente.tipo_alquiler])
				etiqueta_cliente['bg'] = paleta_bg[cliente.tipo]
				etiqueta_cliente.place(x = f_p, y = c_p)
				parcial = partial(editarCliente, cliente)
				borrar_button = MiBoton(child, text = 'Borrar')
				borrar_button['command'] = lambda: borrarClientes(cliente)
				borrar_button['bg'] = 'light coral'
				borrar_button.place(x = f_p + 35, y = c_p + 185)
				modificar_button = MiBoton(child, text = 'Modificar', command = parcial)
				modificar_button['bg'] = 'light goldenrod'
				modificar_button.place(x = f_p + 35, y = c_p + 215)
				c_p += 200
		except Exception as e:
			print(e)

if __name__ == '__main__':
	estacionamiento = Estacionamiento()
	cajones = estacionamiento.cajones
	AplicacionSuper.restablecimientoDatos()
	try:
		empleado = Empleado(4820756, 'Zlatan Pepe','Dios Pogba')
		ventana = MiVentana()
		ventana.withdraw()
		AplicacionSuper.main(1920,1080)
		ventana.mainloop()
	except Exception as e:
		print(e)

	#Aplicacion.restablecimientoDatos()
