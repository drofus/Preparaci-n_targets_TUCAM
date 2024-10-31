# Preparación_targets_TUCAM
En este codigo se hizo con el fin de crear tablas de formatos .esq para que el software de KStars pueda leer nuestras noches de observación

## ¿como se usa?
Es un codigo simple de python en donde solamente corres el Main.py y se te presentará el siguiente menú:
> 
		******** 
          Bienvenido al menu de Generación de secuencia de la cámara Tucan.
            ********
            Menu:
        
        1) Generar un Target
        
        2) Generar un Calib
        
        3) Generar un DomeFlat
        
        4) Salir
1. La opción número 1 te permitira crear la secuencia de targets y tambien sus respectivos darks.
2. La opción número 2 simplemente genera la secuencia de calibración de bias y skyflats.
3. La opción número 3 genera la secuencia para los domflats (Los domeflats se deben tomar de manera mensual).
4. La cuarta opción es para salir del programa

Todas las secuencias que se cree en el run se guardan en una carpeta llamada **Secuencia de obsrvación**
