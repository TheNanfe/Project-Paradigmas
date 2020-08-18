from tkinter import Button, Label, Tk, Toplevel, Radiobutton


class MiBoton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.configuracion()

    def configuracion(self):
        # self.config(fg='red', bg='black',cursor='hand2')
        self.config(fg='black', bg='white', cursor='hand1')


class MiEtiqueta(Label):
    def __init__(self, parent=None, **config):
        Label.__init__(self, parent, **config)
        self.configuracion()

    def configuracion(self):
        self.config(bg='white')
        self.pack()


class MiVentana(Tk):
    """Configuracion basica de la ventana principal"""

    def __init__(self):
        Tk.__init__(self)
        self.configuracion()

    def configuracion(self):
        self.title('Estacionamiento')
        self.config(bg='white')  # Fondo de la pantalla
        self.geometry('480x300')

class VentanaHija(Toplevel):
    """Standar basica para las ventanas mostradas al usuario"""

    def __init__(self, parent=None, **config):
        Toplevel.__init__(self, parent, **config)
        self.configuracion()

    def configuracion(self):
        self.title('Hija')
        self.config(bg='white')
        self.geometry('580x380')
        self.geometry("+%d+%d" % (380, 150))
        #self.resizable(0, 0)


class RadioBoton(Radiobutton):
    """Cambio de detalle de los botones para presentar al usuario"""

    def __init__(self, master=None, **kw):
        Radiobutton.__init__(self, master, **kw)
        self.configuracion()

    def configuracion(self):
        self.config(bg='white', indicatoron=0,
                    activebackground='tan',
                    highlightbackground='slate gray',
                    activeforeground='blue4')
        self.config(font=10)
        self.anchor('center')
