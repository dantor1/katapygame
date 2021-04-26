import pygame as pg

pg.init() # Inicializamos todos los sistemas de pygame
pantalla = pg.display.set_mode((600, 400))
pg.display.set_caption("Hola")

game_over = False

while not game_over:
    #Gestión de eventos
    for evento in pg.event.get():
        pass
    #Gestión del estado (que si la bola, que si el personaje pierde la vida, etc)
    print('Hola mundo')
    # Refrescar pantalla
    pantalla.fill((0, 255, 0))
    pg.display.flip() # Esta instrucción es la última de refrescar pantalla

