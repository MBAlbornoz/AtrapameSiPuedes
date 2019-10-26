from collections import namedtuple


NIVEL = int(input("Ingrese el nivel de dificultad deseado - 1 a 5-")) # El usuario debe ingresar el nivel que quiere jugar

while NIVEL > 5 or NIVEL < 1: # Hasta que el usuario no ingrese un nivel dentro del rango estipulado, el programa se lo sigue solicitando
    NIVEL = ((int(input("Debe ingresar un valor entre 1 y 5"))))

TAMANNO_LETRA = 20
FPS_inicial = NIVEL
TIEMPO_MAX = 61

ANCHO = 1000
ALTO = 600
COLOR_LETRAS = (0,255,0)
COLOR_FONDO = (176,156,231)
COLOR_TEXTO = (217,255,255)
COLOR_TIEMPO_FINAL = (200,20,10)
Punto = namedtuple('Punto','x y')