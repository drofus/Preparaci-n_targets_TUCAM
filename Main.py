import os
from Dummys.Archivos_dummy import dummy
from Dummys.Archivos_Target import Archivos_Target
from Dummys.Archivos_Flat import Archivos_Flat
from Dummys.Archivos_Dark import Archivos_Dark

#Acá creamos los dummy para reemplazar los archivos
dummy()

#NOMBRE DE LOS TARGETS
Target_name = "Target_name"
Target_text = input('escribe el nombre de tu target:')

#filtro
filtro_name = "filtro"
filtro_text = input("elige el tipo de filtro (R,B,V):")

#Cantidad de imagenes
Cantidad_imagenes = "cantidad_imagenes"
Cantidad_imagenes_text = input('¿cuantas imagenes van a tomar?:')

#TIEMPO DE EXPOSICIÓN
Exp_name = "tiempo_exp"
Exp_text = input('escribe el tiempo de exposición en segundos:')

Archivos_Target(Target_name, Target_text, filtro_name, filtro_text, Cantidad_imagenes, Cantidad_imagenes_text, Exp_name, Exp_text)

Archivos_Flat(filtro_name, filtro_text,Exp_name, Exp_text)

Archivos_Dark(Exp_name, Exp_text)


os.mkdir(f'Esquema de OBS para {Target_text}')

#nombre del target
os.rename('Target_dummy_4.esq',f'Esquema de OBS para {Target_text}/{Target_text}_{filtro_text}_{Exp_text}_sec.esq')

#Nombre para el FLAT
os.rename('Flat_dummy_2.esq',f'Esquema de OBS para {Target_text}/Flat_{filtro_text}_{Exp_text}_sec.esq')

#nombre para Darks
os.rename('Dark_dummy.esq',f'Esquema de OBS para {Target_text}/Dark_{Exp_text}_sec.esq')




print("Tabla de observación creada") 