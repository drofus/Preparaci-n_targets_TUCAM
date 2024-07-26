import os
from Archivos_dummy import dummy

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


#lectura de los archivos
with open(r'Target_dummy.esq', 'r') as file: 
  
    #Target
    data_target = file.read() 
    data_target = data_target.replace(Target_name, Target_text)
    
    #filtro
    data_filtro = file.read()
    data_filtro = data_filtro.replace(filtro_name, filtro_text)

    #cantidad de imagenes
    data_cantidad = file.read()
    data_cantidad = data_cantidad.replace(Cantidad_imagenes, Cantidad_imagenes_text)

    #tiempo de exposición
    data_tiempo = file.read()
    data_tiempo = data_tiempo.replace(Exp_name, Exp_text)
  

with open(r'Flat_dummy.esq', 'r') as file:
    
    #filtro
    data_filtro = file.read()
    data_filtro = data_filtro.replace(filtro_name, filtro_text)

    #tiempo de exposición
    data_tiempo = file.read()
    data_tiempo = data_tiempo.replace(Exp_name, Exp_text)


with open(r'Dark_dummy.esq', 'r') as file:
    
    #tiempo de exposición
    data_tiempo = file.read()
    data_tiempo = data_tiempo.replace(Exp_name, Exp_text)


#Reemplazos de las palabras clave en los esq
with open(r'Target_dummy.esq', 'w') as file: 
  
    file.write(data_target)
    file.write(data_filtro)
    file.write(data_cantidad)
    file.write(data_tiempo)

with open(r'Flat_dummy.esq', 'w') as file:

    file.write(data_filtro)
    file.write(data_tiempo)

with open(r'Dark_dummy.esq', 'w') as file:
    file.write(data_tiempo)



#nombre del target
os.rename('Target_dummy.esq',f'{Target_text}_{filtro_text}_{Exp_text}_sec.esq')

#Nombre para el FLAT
os.rename('Flat_dummy.esq',f'Flat_{filtro_text}_{Exp_text}_sec.esq')

#nombre para Darks
os.rename('Dark_dummy.esq',f'Dark_{Exp_text}_sec.esq')


print("Tabla de observación creada") 