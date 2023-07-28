import keyboard
import random
import time

buffer = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
posProd = -1
posCons = -1

while True:
    num = random.randint(0, 10000) #NUMERO ALEATORIO PARA EL TURNO DE A QUIEN LE TOCA TRABAJAR
    noElementos = False
    par = False
    faltoElem = 0
    falto = False

    if(keyboard.is_pressed('ESC')):
        print("\n<<<FIN DE PROGRAMA>>>")
        exit()

    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||", end="\n")

    if num % 2 == 0: #TURNO DE PRODUCTOR
        print("CONSUMIDOR DORMIDO")
        print("PRODUCTOR")
        time.sleep(1)
        producir = random.randint(1, 4) #NUMERO ALEATORIO DE ELEMENTOS A PRODUCIR
        print("Elementos a producir: ", producir)

        for i in range(producir):
            if posProd + 1 >= 20:
                posProd = -1

            if buffer[posProd + 1] == '*':
                if i >= 1: #FALTARON ELEMENTOS POR PRODUCIR
                    faltoElem = producir - i #NUMERO ALEATORIO A PRODUCIR - NUMERO DE ELEMENTOS QUE SE PRODUJERON
                    falto = True 
                    break
                
                else: #BUFFER LLENO DESDE UN INICIO, NO SE PUDO PRODUCIR NADA
                    print("Buffer esta lleno")
                    noElementos = True
                    break
                
                
            buffer[posProd + 1] = '*'
            posProd += 1
        
        par = True

    else: #TURNO DE CONSUMIDOR
        print("PRODUCTOR DORMIDO")
        print("CONSUMIDOR")
        time.sleep(1)
        consumir = random.randint(1, 4) #NUMERO ALEATORIO DE ELEMENTOS A CONSUMIR
        print("Elementos a consumir: ", consumir) 

        for i in range(consumir): #CONSUMIR ELEMENTOS DE BUFFER
            if posCons + 1 >= 20: #LLEGO AL FINAL DEL BUFFER
                posCons = -1 #INICIAR NUEVAMENTE AL INICIO DEL BUFFER

            if buffer[posCons + 1] == '-': #BUFFER VACIO
                if i >= 1: #FALTARON ELEMENTOS POR CONSUMIR
                    faltoElem = consumir - i #NUMERO ALEATORIO A CONSUMIR - NUMERO DE ELEMENTOS QUE SE PRODUJERON
                    falto = True
                    break

                else: #BUFFER VACIO DESDE UN INICIO, NO SE PUDO CONSUMIR NADA
                    print("No hay elementos para consumir")
                    time.sleep(1.5)
                    noElementos = True
                    break
                    

            buffer[posCons + 1] = '-'
            posCons += 1
    
    if noElementos == False: #SI HABIA ELEMENTOS EN EL BUFFER
        for elemento in buffer: #MOSTRAR ELEMENTOS DE BUFFER
            if keyboard.is_pressed('ESC'):
                print("\n<<<FIN DE PROGRAMA>>>")
                exit()

            time.sleep(0.5)
            print(elemento, end = " ", flush = True)
    
    print("\n")

    if par == True: #PRODUCTOR
        print("Posicion en que se quedo PRODUCTOR: ", posProd + 1)
        if falto == True: #FALTARON ELEMENTOS A PRODUCIR, BUFFER SE LLENO ANTES DE TERMINAR
            print("Elementos faltantes a producir: ", faltoElem)

    else: #CONSUMIDOR
        print("Posicion en que se quedo CONSUMIDOR: ", posCons + 1)
        if falto == True: #FALTARON ELEMENTOS A CONSUMIR, BUFFER QUEDO VACIO
            print("Elementos faltantes a consumir: ", faltoElem)
    
    print("\n")