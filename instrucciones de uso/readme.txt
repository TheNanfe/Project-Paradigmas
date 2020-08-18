usuario del estacionamiento:

Antes de ejecutar el programa, se debe contar con un interprete de PYTHON3 y tener descargada una
libreria llamada ZODB(para persistencia de objetos).
Para ejecutar el programa, debe abrir la consola en el directorio donde se encuentre el proyecto y ejecutar el 
script "app.py" o "app_super.py", dependiendo del tipo de uso que quieras.

------------------------------------------------------------------------------------------------------------------------------------------
app.py: Interfaz para los clientes

Una vez dentro, el usuario tiene tres opciones:
1.Ingresa al estacionamiento: Permite a todos los nuevos clientes, ingresar al estacionamiento, les genera un PIN de acceso y salida.
2.Salir Estacionamiento: Para todos los clientes que quieran salir del estacionamiento, tienen que ingresar aqui su PIN y dependiendo del
tipo del alquiler se borrara o no al cliente de la base de datos.
3.Ingresar Estacionamiento: Solo para aquellos clientes que hayan alquilado por mes. Deben ingresar su PIN e ingresan!


--------------------------------------------------------------------------
app_super.py: Interfaz para los empleados del lugar

El "super usuario" podra modificar, eliminar o agregar atributos a los clientes.
El "super usuario" podra modificar, eliminar o agregar clientes.