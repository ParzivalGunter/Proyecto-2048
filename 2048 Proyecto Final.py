import time
import numpy as np

#Entrada: Llamada en el shell del juego con pantallaInicio()
#Salida: Versión jugable del juego 2048
#Restricciones: Utilzar exclusivamente recursividad para las partes de lógica en el código

#Mostrar un título al juego
def pantallaInicio():
    print("")
    print("")
    print("xxxxxxxxxxx  xxxxxxxxxx  xxxx    xxxx  xxxxxxxxxxxx")
    print("       xxxx  xxxx  xxxx  xxxx    xxxx  xxxx    xxxx")
    print("       xxxx  xxxx  xxxx  xxxx    xxxx  xxxx    xxxx")
    print("xxxxxxxxxxx  xxxx  xxxx  xxxxxxxxxxxx  xxxx    xxxx")
    print("xxxxxxxxxxx  xxxx  xxxx  xxxxxxxxxxxx  xxxxxxxxxxxx")
    print("xxxx         xxxx  xxxx          xxxx  xxxx    xxxx")
    print("xxxx         xxxx  xxxx          xxxx  xxxx    xxxx")
    print("xxxxxxxxxxx  xxxxxxxxxx          xxxx  xxxx    xxxx")
    print("xxxxxxxxxxx  xxxxxxxxxx          xxxx  xxxxxxxxxxxx")
    print("")
    ingresarDatos()

#Solicita los datos necesarios al usuario (nombre y modo de juego al usuario)
def ingresarDatos():
    print("Escriba su nombre: ")
    nombre = input()
    print("Bienvenido " + nombre)
    print("")
    print("Elija un modo de juego (decimal, binario, octal o hexadecimal): ")
    modo = input()
    if(modo == "decimal"):
        print("Usted escogió el modo decimal")
        mat()
        timer()
    elif(modo == "binario"):
        print("Usted escogió el modo binario")
        mat()
        timer()
    elif(modo == "octal"):
        print("Usted escogió el modo octal")
        mat()
        timer()
    elif(modo == "hexadecimal"):
        print("usted escogió el modo hexadecimal")
        mat()
        timer()
    else:
        print("Ingrese un modo válido")
        ingresarDatos()

#Cronometro para el juego con un límite de 300 segundos(5 minutos)
def timer():
    for s in range(0,300):
        time.sleep(1)
    print("se acabó el tiempo")

def mat():
    m = np.zeros([4,4])
    print("\n2048 : \n", m)
    
  
