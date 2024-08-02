import os


def Archivos_Dark(Exp_name, Exp_text):
    with open(r'Dark_dummy.esq', 'r') as file:
        
        #tiempo de exposición
        data_tiempo = file.read()
        data_tiempo = data_tiempo.replace(Exp_name, Exp_text)


    #Reemplazos de las palabras clave en los esq

    with open(r'Dark_dummy.esq', 'w') as file:
        file.write(data_tiempo)
