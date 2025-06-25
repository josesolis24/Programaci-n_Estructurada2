#Crear un proyecto  que permita  gestionar (administrar películas); colocar  un menu  de opciones para agregar, borrar,  modificar, consultar, buscar y vaciar películas 
#Notas: 
#1.-utiliza  funciones y mandar a llamar desde otro archivo 
#2.- Utilizar una lista para almacenar  los nombre de películas

import peliculas

opcion=True
while opcion:
    peliculas.borra_pantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n\n 1.- Agregar  \n 2.- Borrar \n 3.- Modificar \n 4.- Mostrar \n 5.- Buscar \n 6.- Limpiar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregar_pelicula()
            peliculas.esperarTecla()
        case "2":
            peliculas.eliminar_pelicula()
            peliculas.esperarTecla() 
        case "3":
            print(".:: Modificar Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscar_Peliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
            peliculas.esperarTecla()
            print("/n\tTerminaste la ejecucion del SW")
        case _:
            opsion=True 
            input("Opción invalida vuelva a intentarlo ... por favor")



