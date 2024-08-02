import os


def Archivos_Flat(filtro_name, filtro_text,Exp_name, Exp_text):

    with open(r'Flat_dummy.esq', 'r') as file:
        
        #filtro
        data_filtro = file.read()
        data_filtro = data_filtro.replace(filtro_name, filtro_text)

    with open(r'Flat_dummy.esq', 'w') as file:
        file.write(data_filtro)

    os.rename('Flat_dummy.esq', 'Flat_dummy_2.esq')

    with open(r'Flat_dummy_2.esq', 'r') as file:
        #tiempo de exposición
        data_tiempo = file.read()
        data_tiempo = data_tiempo.replace(Exp_name, Exp_text)

    with open(r'Flat_dummy_2.esq', 'w') as file:
        file.write(data_tiempo)
