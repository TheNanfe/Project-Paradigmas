%Autor: Hernan Lopez

%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%----Hechos----%%%%%

%hechos espacios_alquilables_y_tarifas por dia
normal(dia).
normal(mes).

sombra(dia).
sombra(mes).

extenso(dia).
extenso(mes).

sombra_extenso(dia).
sombra_extenso(mes).

%defino precio de los cajones segun el tipo del alquiler

precio(normal(dia),10000).
precio(normal(mes),192000).

precio(sombra(dia),25000).
precio(sombra(mes),207000).

precio(extenso(dia),30000).
precio(extenso(mes),212000).

precio(sombra_extenso(dia),50000).
precio(sombra_extenso(mes),250000).


%defino
cantidad(normal,5).
cantidad(sombra,5).
cantidad(extenso,3).
cantidad(sombra_extenso,0).

%hechos personas
cliente(hernan, lopez).
administrador(lopez, hernan).


%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%----Reglas----%%%%%

%regla disponibilidad_del_bien
    %N: nombre
    %C: cantidad
    esta_disponible(N):-(cantidad(normal(N),C), C > 0);(cantidad(sombra(N),C), C > 0);(cantidad(extenso(N),C), C > 0).

%regla comparar_precios
	%C: tipo_cajon_economico
	%X: tipo_cajon_caro
	%T: tipo_alquiler
	%P: Precio
	%mas_economico(T,C):- (precio(T(C),P), P < 1000).

%regla es persona
    %C: clasificacion
    %N: nombre
    %A: apellido
    es_persona(N, A):-cliente(N, A); administrador(N, A).

