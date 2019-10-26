from principal import *
from configuracion import *

import random
import math



#inicializa la lista de nombres con los que estan en el archivo nombres.txt
def InitNombres():
    archivo = open("nombres.txt")
    lista=archivo.readlines()
    nombres=[]
    for nombre in lista:
        nombreNuevo = ""
        for pos in range(len(nombre)-1):
            nombreNuevo += nombre[pos]
        nombres.append(nombreNuevo)
    archivo.close()
    return nombres


#toma de nombres una nueva palabra

def nuevaPalabra(nombres):
    NombresAleatorios=random.choice(nombres)
    return cambioMayusPorMinus(NombresAleatorios)

#Debe eliminar las palabras y sus posiciones cuando empiezan a escaparse de la pantalla
#Debe ir actualizando las posiciones de las palabras para que vayan descendiendo
#Debe agregar nuevas en posiciones al azar, siempre con el cuidado
#de que las palabras no se superpongan, no aparezcan incompletas ni llenen por
#completo la pantalla.

def actualizar(listaPalabras, posiciones, nombres):
    x=random.randint(20,900)            # Genera al azar la coordenada "x"
    y=random.randint(000,000)           # Inicializa la coordenada "y" en cero
    nombre=nuevaPalabra(nombres)        # Genera un nombre al azar

    listaPalabras.append(nombre)        # Carga el nombre a la lista "ListaNombres"
    posiciones.append([x,y])            # Carga en la matriz "posiciones" las cooredenadas [x,y]
    pos=0
    for i in listaPalabras:
        posiciones[pos][1] += 30        # Incrementa el valor de "y" de a 30 pixeles
        if posiciones[pos][1] > 515:    # Cuando la coordenada "y" es mayor que 515 (linea blanca del piso) se borra la palabra y la posicion
            listaPalabras.pop(pos)
            posiciones.pop(pos)
        pos+=1


#quita del listado de palabras y su respectiva posicion a la palabra
def quitar(palabra, listaPalabras, posiciones):
    pos=0
    for i in listaPalabras:
        if i == palabra:
            listaPalabras.pop(pos)
            posiciones.pop(pos)
        pos+=1
    return True

#determina si la palabra pertenece a listaPalabras
def esValida(palabra, listaPalabras):
    if palabra in listaPalabras:
        return True
    else:
        return False

# cantidad de puntos que da una palabra segun la letra
def Puntos(palabra,listaPalabras):
    vocal="aeiou"
    cons_facil="bdfghlmnprstv"
    cons_dif="jkqwxyz"
    puntaje=0
    if esValida(palabra,listaPalabras):
        for i in palabra:
            if i in vocal:
                puntaje+=1
            if i in cons_facil:
                puntaje+=2
            if i in cons_dif:
                puntaje+=5
    return puntaje


# Debe controlar si la palabra ingresada esta en la pantalla y en caso
# afirmativo quitarla de la pantalla y sumar los puntos correspondientes.
# Cuando el usuario ingresa correctamente la palabra en pantalla se emite un sonido y
# otro distinto cuando la palabra es incorrecta

def procesar(palabra, listaPalabras, posiciones):

    if esValida(palabra,listaPalabras):
        pygame.mixer.music.load("SONIDO3.mp3")
        pygame.mixer.music.play()

        puntaje= Puntos(palabra,listaPalabras)
        quitar(palabra,listaPalabras,posiciones)
        return puntaje

    else:
        pygame.mixer.music.load("ERROR.mp3")
        pygame.mixer.music.play()
        return 0

# Si el usuario ingresa una palabra incorrecta se le resta una vida

def VIDAS (palabra,listaPalabras):
    if esValida(palabra,listaPalabras):
        return 0
    else:
        return -1