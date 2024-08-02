import os

def Archivos_Target(Target_name, Target_text, filtro_name, filtro_text, Cantidad_imagenes, Cantidad_imagenes_text, Exp_name, Exp_text):
    #lectura de los archivos
    with open(r'Target_dummy.esq', 'r') as file: 
    
        #Target
        data_target = file.read() 
        data_target = data_target.replace(Target_name, Target_text)

    with open(r'Target_dummy.esq', 'w') as file:
    
        file.write(data_target)

    os.rename('Target_dummy.esq','Target_dummy_2.esq')

    with open(r'Target_dummy_2.esq', 'r') as file:
        #filtro
        data_filtro = file.read()
        data_filtro = data_filtro.replace(filtro_name, filtro_text)

    with open(r'Target_dummy_2.esq', 'w') as file:
        file.write(data_filtro)

    os.rename('Target_dummy_2.esq', 'Target_dummy_3.esq')

    with open(r'Target_dummy_3.esq', 'r') as file:

        #cantidad de imagenes
        data_cantidad = file.read()
        data_cantidad = data_cantidad.replace(Cantidad_imagenes, Cantidad_imagenes_text)

    with open(r'Target_dummy_3.esq', 'w') as file:
        file.write(data_cantidad)

    os.rename('Target_dummy_3.esq', 'Target_dummy_4.esq')


    with open(r'Target_dummy_4.esq', 'r') as file:
        #tiempo de exposición
        data_tiempo = file.read()
        data_tiempo = data_tiempo.replace(Exp_name, Exp_text)

    with open(r'Target_dummy_4.esq', 'w') as file:
        file.write(data_tiempo)