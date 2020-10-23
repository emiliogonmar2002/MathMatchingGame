import random
import os
import time

def limpia():
    os.system("cls")

def limpiaTiempo(): #Función para limpiar despúes de 3 segundos
    time.sleep(3)       #Espera 3 segundos antes de borrar
    os.system('cls')    #Borra la consola

def tableroBooleano(eleccion):      #Tablero booleando de la elección del usuario para una fácil manipulación de datos
    tablero_booleano = []

    if eleccion == "1":             #Tablero de 2x4
        tablero_booleano = [[0,0,0,0],
                            [0,0,0,0]]
        
    elif eleccion == "2":           #Tablero de 3x6
        tablero_booleano = [[0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0]]
        
    elif eleccion == "3":           #Tablero de 4x6
        tablero_booleano = [[0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0],
                            [0,0,0,0,0,0]]

    return tablero_booleano

def tableroFichas(eleccion):        #Tablero del juego de memorama que se randomiza cada que se ejecuta
    if eleccion == "1":
        tab_fichas = [["3+5","7+3","1*2","12+7"],["4+4","2*5","1+1","26-7"]]

        random.shuffle(tab_fichas[0])   #Revolver los elementos de cada fila
        random.shuffle(tab_fichas[1]) 

        
    elif eleccion == "2":
        tab_fichas = [["3+5","7+3","1*2","12+7", "25*2","23+26"],["11*11","10+10","8*3","4+4","2*5","1+1"],["12+7", "80-30","49+0","110+11","25-5","4*6"]]

        random.shuffle(tab_fichas[0])   #Revolver los elementos de cada fila
        random.shuffle(tab_fichas[1]) 
        random.shuffle(tab_fichas[2])

    elif eleccion == "3":
        tab_fichas = [["3+5","5+5","1+1","10+2", "16+4","4+6"],["40-10","17+5","16/2","20+20","5*2","1+1"],["25+5", "10*2","5+5","36+4","22+0","1+4"],["15*2","6*2","4+4", "4+1","20*2","10-2"]]

        random.shuffle(tab_fichas[0])   #Revolver los elementos de cada fila
        random.shuffle(tab_fichas[1]) 
        random.shuffle(tab_fichas[2])
        
    random.shuffle(tab_fichas)      #Revolver las filas de la matriz

    return tab_fichas

def muestraTablero(tablero_booleano,tablero_fichas):    #Función para mostrar el tablero tapado, e irse destapando

    if eleccion == "1":
        print()
        print("\n\t\t   ▲▲-T A B L E R O-▲▲\n\n")
        print("\t    1 \t     2 \t      3        4")
        for i in range(len(tablero_booleano)):                              #Renglones
            print("\n\t-------------------------------------")
            print(i+1,end="\t")
            print("|",end=" ")    
            for ii in range(len(tablero_booleano[i])):                      #Columnas

                if tablero_booleano[i][ii] == 1:
                    print(f"{tablero_fichas[i][ii]}".center(6),end=" ")     #Si en el tablero booleano hay un 1, se despliega la ficha destapada
                        
                else:                    
                    print(f"■".center(6),end=" ")                           #Si en el tablero booleano hay un 0, se despliega la ficha tapada
                    
                print("|",end=" ")
            print("\n\t-------------------------------------")
                        
            print()
        
    elif eleccion == "2":                                                   #Mismo que elección anterior pero con más renglones y columnas
        print()
        print("\n\t\t\t   ▲▲-T A B L E R O-▲▲\n\n")
        print("\t    1 \t     2 \t      3        4 \t5 \t 6")
        for i in range(len(tablero_booleano)):
            print("\n\t-------------------------------------------------------")
            print(i+1,end="\t")
            print("|",end=" ")    
            for ii in range(len(tablero_booleano[i])):

                if tablero_booleano[i][ii] == 1:
                    print(f"{tablero_fichas[i][ii]}".center(6),end=" ")
                        
                else:                    
                    print(f"■".center(6),end=" ")
                    
                print("|",end=" ")
            print("\n\t-------------------------------------------------------")
                        
            print()
        
    elif eleccion == "3":                                                   #Mismo que elección anterior pero con más columnas
        print()
        print("\n\t\t\t   ▲▲-T A B L E R O-▲▲\n\n")
        print("\t    1 \t     2 \t      3        4 \t5 \t 6 \t")
        for i in range(len(tablero_booleano)):
            print("\n\t-------------------------------------------------------")
            print(i+1,end="\t")
            print("|",end=" ")    
            for ii in range(len(tablero_booleano[i])):
                    
                if tablero_booleano[i][ii] == 1:
                    print(f"{tablero_fichas[i][ii]}".center(6),end=" ")
                        
                else:                    
                    print(f"■".center(6),end=" ")
                    
                print("|",end=" ")
            print("\n\t-------------------------------------------------------")
                        
            print()

def jugada(tablero_booleano,tablero_fichas):            #Función para recibir las elecciones del jugador

    muestraTablero(tablero_booleano,tablero_fichas)     #Muestra el tablero

    r1 = input("Ingrese el número de fila de la ficha: ")      #Renglon
    c1 = input("Ingrese el número de columna de la ficha: ")   #Columnas

    validar = validacion(tablero_booleano,r1,c1)                    #Función que valida la elección del usuario

    while validar == False:                                         #Mientras la elección sea inválida, se vuelve a pedir la elección
        print("\nDATOS INGRESADOS INVÁLIDOS\n")
        r1 = input("Ingrese el número de fila de la ficha: ")
        c1 = input("Ingrese el número de columna de la ficha: ")
        validar = validacion(tablero_booleano,r1,c1)

    tablero_booleano[int(r1)-1][int(c1)-1] = 1                                #Cambiamos el lugar indicado por el usuario en el tablero booleano un 0 por un 1
    ficha1 = tablero_fichas[int(r1)-1][int(c1)-1]                             #Se guarda la elección del usuario

    limpia()    

    muestraTablero(tablero_booleano,tablero_fichas)                 #Mismo proceso que jugada anterior

    r2 = input("Ingrese el número de fila de la ficha: ")
    c2 = input("Ingrese el número de columna de la ficha: ")

    validar = validacion(tablero_booleano,r2,c2)

    while validar == False:
        print("\nDATOS INGRESADOS INVÁLIDOS\n")
        r2 = input("Ingrese el número de fila de la ficha: ")
        c2 = input("Ingrese el número de columna de la ficha: ")
        validar = validacion(tablero_booleano,r2,c2)

    tablero_booleano[int(r2)-1][int(c2)-1] = 1
    ficha2 = tablero_fichas[int(r2)-1][int(c2)-1]

    limpia()

    muestraTablero(tablero_booleano,tablero_fichas)

    if eval(ficha1) != eval(ficha2):                #Si las dos fichas son diferentes se vuelve el valor en el booleano a 0, para que se "tapen"
        tablero_booleano[int(r1)-1][int(c1)-1] = 0
        tablero_booleano[int(r2)-1][int(c2)-1] = 0
        cont = 0
        
    else:                                           #Si las fichas son iguales, se deja el booleano como 1 para mantener las fichas destapadas y se regresa un punto al jugador
        tablero_booleano[int(r1)-1][int(c1)-1] = 1
        tablero_booleano[int(r2)-1][int(c2)-1] = 1
        cont = 1
        
    return cont

def terminar_continuar(tablero_booleano,player):
    tablero_lista = []
    contador = 0
    for i in tablero_booleano:
        for ii in i:
            tablero_lista.append(ii)
        
    for i in tablero_lista:
        if i == 1:
            contador += 1
        
    if contador == len(tablero_lista):
        player = 1
    else:
        player = 0
        
    return player
        
def validacion(tablero_booleano,r1,c1):
    renglones = len(tablero_booleano)
    columnas = len(tablero_booleano[0])

    try:
        if int(r1) and int(c1):
            if int(r1) > 0 and int(r1) <= renglones:
                if int(c1) > 0 and int(c1) <= columnas:
                    if tablero_booleano[int(r1)-1][int(c1)-1] != 1:
                        return True
                    else:
                        return False
                else:
                    return False
                    
            else:
                return False
    except:
        return False

def validacionMenu(eleccion):
    if eleccion in "1234":
        return False
    else:
        print("\nNÚMERO INVÁLIDO\n")
        return True
                

#Main

validacion_menu = True

while validacion_menu:
    print("\nElige que nivel deseas jugar:\n\n\
            \t1. Fácil\n\
            \t2. Medio\n\
            \t3. Dificil\n\
            \t4. Salir del juego\n")

    eleccion = input("\nIngrese el número correspondiente: ")

    validacion_menu = validacionMenu(eleccion)

if eleccion in "123":
    tablero_booleano = tableroBooleano(eleccion)
    tablero_fichas = tableroFichas(eleccion)
    jugadorUno_cont = 0
    jugadorDos_cont = 0
    ronda = 0

    player = 0

    limpia()

    while player == 0:

        ronda += 1

        print(f"\nRonda {ronda}\n")

        print("\nTurno de jugador 1\n")

        jugadorUno_cont += jugada(tablero_booleano,tablero_fichas)

        limpiaTiempo()

        player = terminar_continuar(tablero_booleano,player)

        if player == 1:
            break

        print("\nTurno de jugador 2\n")

        jugadorDos_cont += jugada(tablero_booleano,tablero_fichas)

        limpiaTiempo()

        player = terminar_continuar(tablero_booleano,player)

        if player == 1:
            break


    print(f"\n\
    █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   ▄█   ▀      {jugadorUno_cont}\n\
    █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   ░█   ▀\n")

    print(f"\n\
    █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   ▀█    ▀       {jugadorDos_cont}\n\
    █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   █▄    ▀\n")

    if jugadorUno_cont > jugadorDos_cont:
        print("\nJUGADOR UNO GANA!!\n")
    elif jugadorDos_cont > jugadorUno_cont:
        print("\nJUGADOR DOS GANA!!\n")
    else:
        print("\nEMPATE\n")

else:
    print("\n GRACIAS POR JUGAR :) \n")