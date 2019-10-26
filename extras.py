import pygame
from pygame.locals import *
from configuracion import *
from principal import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

""" la funcion cambioMayusPorMinus realiza el cambio de las mayusculas en los
nombres antes de que ingresen a la pantalla"""
def cambioMayusPorMinus(nombre):

    nombreDeSalida=""

    for char in nombre:
        if char == "A":
            nombreDeSalida= nombreDeSalida+"a"
        elif char=="a":
            nombreDeSalida=nombreDeSalida+char
        elif char=="B":
            nombreDeSalida=nombreDeSalida+"b"
        elif char=="b":
            nombreDeSalida=nombreDeSalida+char
        elif char=="C":
            nombreDeSalida=nombreDeSalida+"c"
        elif char=="c":
            nombreDeSalida=nombreDeSalida+char
        elif char=="D":
            nombreDeSalida=nombreDeSalida+"d"
        elif char=="d":
            nombreDeSalida=nombreDeSalida+char
        elif char=="E":
            nombreDeSalida=nombreDeSalida+"e"
        elif char=="e":
            nombreDeSalida=nombreDeSalida+char
        elif char=="F":
            nombreDeSalida=nombreDeSalida+"f"
        elif char=="f":
            nombreDeSalida=nombreDeSalida+char
        elif char=="G":
            nombreDeSalida=nombreDeSalida+"g"
        elif char=="g":
            nombreDeSalida=nombreDeSalida+char
        elif char=="H":
            nombreDeSalida=nombreDeSalida+"h"
        elif char=="h":
            nombreDeSalida=nombreDeSalida+char
        elif char=="I":
            nombreDeSalida=nombreDeSalida+"i"
        elif char=="i":
            nombreDeSalida=nombreDeSalida+char
        elif char=="J":
            nombreDeSalida=nombreDeSalida+"j"
        elif char=="j":
            nombreDeSalida=nombreDeSalida+char
        elif char=="K":
            nombreDeSalida=nombreDeSalida+"k"
        elif char=="k":
            nombreDeSalida=nombreDeSalida+char
        elif char=="L":
            nombreDeSalida=nombreDeSalida+"l"
        elif char=="l":
            nombreDeSalida=nombreDeSalida+char
        elif char=="M":
            nombreDeSalida=nombreDeSalida+"m"
        elif char=="m":
            nombreDeSalida=nombreDeSalida+char
        elif char=="N":
            nombreDeSalida=nombreDeSalida+"n"
        elif char=="n":
            nombreDeSalida=nombreDeSalida+char
        elif char=="O":
            nombreDeSalida=nombreDeSalida+"o"
        elif char=="o":
            nombreDeSalida=nombreDeSalida+char
        elif char=="P":
            nombreDeSalida=nombreDeSalida+"p"
        elif char=="p":
            nombreDeSalida=nombreDeSalida+char
        elif char=="Q":
            nombreDeSalida=nombreDeSalida+"q"
        elif char=="q":
            nombreDeSalida=nombreDeSalida+char
        elif char=="R":
            nombreDeSalida=nombreDeSalida+"r"
        elif char=="r":
            nombreDeSalida=nombreDeSalida+char
        elif char=="S":
            nombreDeSalida=nombreDeSalida+"s"
        elif char=="s":
            nombreDeSalida=nombreDeSalida+char
        elif char=="T":
            nombreDeSalida=nombreDeSalida+"t"
        elif char=="t":
            nombreDeSalida=nombreDeSalida+char
        elif char=="U":
            nombreDeualida=nombreDeSalida+"u"
        elif char=="u":
            nombreDeSalida=nombreDeSalida+char
        elif char=="V":
            nombreDeSalida=nombreDeSalida+"v"
        elif char=="v":
            nombreDeSalida=nombreDeSalida+char
        elif char=="W":
            nombreDeSalida=nombreDeSalida+"w"
        elif char=="w":
            nombreDeSalida=nombreDeSalida+char
        elif char=="X":
            nombreDeSalida=nombreDeSalida+"x"
        elif char=="x":
            nombreDeSalida=nombreDeSalida+char
        elif char=="Y":
            nombreDeSalida=nombreDeSalida+"y"
        elif char=="y":
            nombreDeSalida=nombreDeSalida+char
        elif char=="Z":
            nombreDeSalida=nombreDeSalida+"z"
        elif char=="z":
            nombreDeSalida=nombreDeSalida+char

    return nombreDeSalida


def escribirEnPantalla(screen, palabra, posicion, tamano, color):
    defaultFont= pygame.font.Font( pygame.font.get_default_font(), tamano)
    ren = defaultFont.render(palabra, 1, color)
    screen.blit(ren, posicion)

def dibujar(screen, candidata, listaPalabras, posiciones, puntos, segundos, vidas):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)


    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render(candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO)
    ren4 = defaultFont.render("Vidas: " + str(int(vidas)), 1, COLOR_TEXTO) # Si no logramos hacer que baje cuando hay un error lo tendremos que sacar
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)

    for i in range(len(listaPalabras)):
        screen.blit(defaultFont.render(listaPalabras[i], 1, COLOR_LETRAS), posiciones[i])

    screen.blit(ren1, (190, 570))
    screen.blit(ren2, (850, 10))
    screen.blit(ren3, (10, 10))
    screen.blit(ren4, (450, 10))



# Esta funcion dibuja en pantalla el fin del juego con los puntos totales

def dibujarFIN(screen, puntos):

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 70) # Cambiamos el tamaño de la letra

    renFin = defaultFont.render("FIN DEL JUEGO!!!", 1, COLOR_TEXTO)
    renFinPuntos = defaultFont.render("Puntos Totales: " + str(int(puntos)), 1, COLOR_TEXTO)

    screen.blit(renFin, (200, 200))
    screen.blit(renFinPuntos, (210, 300))