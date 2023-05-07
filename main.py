import csv
from Viajero import ViajeroFrecuente
from manejador import Manejador

if __name__== '__main__':
    print("EJERCICIO 1")
    archivo = open('info.csv')
    reader = csv.reader(archivo,delimiter=',')
    newViajero= Manejador()
    bandera = True

    for fila in reader:
        if bandera:
            bandera = False
        else:
             print("\n")
             print("Datos del archivo cargado")
             numero=int(fila[0])
             documento=fila[1]
             nombre=fila[2]
             apellido=fila[3]
             millas=fila[4]
             print("\n")
             newViajero.cargarViajero(numero, documento, nombre, apellido, millas)
    archivo.close()
    print("--------------------------------------------------------------------------------------------")
    newViajero.ordenarViajeros()
    newViajero.showViajeros()
    print("\n")
    print("--------------------------------------------------------------------------------------------")
    print("EJERCICIO 2")
    
    newViajero.sumar_millas()

    print("--------------------------------------------------------------------------------------------")
    print("EJERCICIO 3")
    xnumero = int(input ("Ingresar un numero de viajero: "))
    resp=newViajero.compara(numero,documento,nombre,apellido,millas,xnumero)
    if resp != None:
        millas_a_canjear = int(input("Ingrese la cantidad de millas a canjear: "))
        viajero1 = ViajeroFrecuente(xnumero,documento,nombre,apellido, millas)
        viajero1 = viajero1 - millas_a_canjear
        newViajero.canjear_millas(viajero1)
    else:
        print("El número de viajero ingresado no existe.")





        

