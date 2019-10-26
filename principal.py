#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Atrapame si Puedes.")
        screen = pygame.display.set_mode((ANCHO, ALTO))


    # se muestran lo cambios en pantalla
        pygame.display.flip()

        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial


        puntos = 0
        palabra = ""
        listaPalabras = []
        posiciones = []
        nombres=[]
        vidas = 5

        nombres = InitNombres()


        dibujar(screen, palabra, listaPalabras, posiciones, puntos, segundos, vidas)

        while segundos > 0 and vidas > 0:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabra += letra
                    if e.key == K_BACKSPACE:
                        palabra = palabra[0:len(palabra)-1]
                    if e.key == K_RETURN:
                        vidas += VIDAS(palabra,listaPalabras)
                        puntos += procesar(palabra, listaPalabras, posiciones)
                        palabra = ""

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000



            #Limpiar pantalla anterior
            # Carga una imagen como fondo de pantalla
            fondo = pygame.image.load("imagen1.png").convert()


            screen.blit(fondo, (0, 0))

            # se muestran lo cambios en pantalla
            pygame.display.flip()


            #Dibujar de nuevo todo
            dibujar(screen, palabra, listaPalabras, posiciones, puntos, segundos, vidas )

            pygame.display.flip()

            actualizar(listaPalabras, posiciones, nombres)


        # Carga una nueva imagen para el final del juego y muestra los puntos obtenidos
        fondo = pygame.image.load("MATRIX.png").convert()
        screen.blit(fondo, (0, 0))

        dibujarFIN(screen,puntos)
        pygame.display.flip()


        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

#Programa Pirncipal ejecuta Main
if __name__ == "__main__":
    main()