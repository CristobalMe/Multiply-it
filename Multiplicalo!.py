#Notas del juego:
#Para que el juego pueda funcionar tiene que cambiar la ubicación del archivo a la que haya guardado su carpeta, gracias!
#For the game to work properly, you first have to change the path to the correct one, thank you!

#Instructions: Just press space and have fun


# Made by Cristobal Medina Meza


#Librerias
# Import libraries
import pygame
from sys import exit
import random



#Ejecutar Pygame
pygame.init()
#Tamaño de la pantalla
#Screen size
screen = pygame.display.set_mode((800,400))
#Nombre del juego en la ventana
#Name that appears in the tab
pygame.display.set_caption('Multiplicalo!!')
clock = pygame.time.Clock()
game_active = True


#Musica
#Music
pygame.mixer.music.load('Juego\\Musica.mp3')
pygame.mixer.music.play(3000)

#Fuente
#Font
test_font = pygame.font.Font('Juego\\Fuentes\\Cooper.otf', 30)
test_font2 = pygame.font.Font('Juego\\Fuentes\\Cooper.otf', 60)

#Texto introduccion y final
#Text
texto_intro = pygame.font.SysFont('console', 30, True)
texto_resultado = pygame.font.SysFont('console', 80, True)
esta_en_intro = True



#Here, we define 2 random numbers to generate the correct response
current_time = pygame.time.get_ticks()
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)

#Respuesta
#Response
respuesta = n1*n2
y_respuesta = 100
respuesta_surf = test_font.render(f"{respuesta}", False, 'White')
respuesta_rec = respuesta_surf.get_rect(topleft = (600,y_respuesta))

#Problema
#Generating the problem
problem_surf = test_font2.render(f'{n1} x {n2}',False,'White')
problem_rec = problem_surf.get_rect(center = (400,150))
screen.blit(problem_surf, problem_rec)

#Respuesta falsa
#Incorrect response
respuestaf = random.randint(respuesta-5,respuesta+5)
y_respuestaf = 270
respuestaf_surf = test_font.render(f"{respuestaf}", False, 'White')
respuestaf_rec = respuestaf_surf.get_rect(topleft = (600,y_respuestaf))


#Redimencionar imagen
#Image
Fondo_O = pygame.image.load('Juego\\Graficos\\Suelo.jpg').convert()
Fondo_R = pygame.transform.scale(Fondo_O, (800,400))

test_surface = Fondo_R
x = 0
text_surface = test_font.render(f'Puntuacion: {x}', False, 'White')

#Enemigo
#Enemy
Enemigo1 = pygame.image.load('Juego\\Graficos\\Enemigo.jpg').convert_alpha()
Enemigo1R = pygame.transform.scale(Enemigo1, (40,40))
snail_surface = Enemigo1R
snail_rec = snail_surface.get_rect(topleft = (600, 270))

#Jugador
#Player
Jugador = pygame.image.load('Juego\\Graficos\\Jugador.png')
JugadorR = pygame.transform.scale(Jugador, (80,90))
player_surf = JugadorR
player_rec = player_surf.get_rect(topleft = (90,200))
player_gravity = 0

#Luna
#Moon
luna = pygame.image.load('Juego\\Graficos\\Luna.png')
lunaR = pygame.transform.scale(luna, (300,300))
lunaR2 = pygame.transform.scale(luna, (100,100))
pygame.display.set_icon(lunaR2)

#Rectangulo 1
#Rectangle 1
rectangulo1 = pygame.image.load('Juego\\Graficos\\Rectangulo 1.jpg').convert_alpha()
rectangulo1R = pygame.transform.scale(rectangulo1, (70,155))
rectangulo1_surf = rectangulo1R
rectangulo1_rec = rectangulo1_surf.get_rect(topleft = (650,0))

#Rectangulo 2
#Rectangle 2
rectangulo2 = pygame.image.load('Juego\\Graficos\\Rectangulo 2.jpg').convert_alpha()
rectangulo2R = pygame.transform.scale(rectangulo2, (70,155))
rectangulo2_surf = rectangulo2R
rectangulo2_rec = rectangulo2_surf.get_rect(topleft = (600,155))

x = 0

#While para mantener la ventana abierta
#While loop to keep the game running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            #if event.type == pygame.MOUSEMOTION (Testing)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rec.bottom >= 200:
                    player_gravity = -20
            
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rec.left = 800
                x = 0
                game_active = True
  
    if game_active:
        #Coordenadas del fondo
        #Back image
        screen.blit(test_surface, (0,0))        
        screen.blit(text_surface, (0,0))

        #Enemigo
        #Enemy and stage movement
        if x <= 1000:
            snail_rec.x -= 6
        elif x < 2000 and x > 1000:
            snail_rec.x -= 8
        elif x >= 2000:
            snail_rec.x -= 10
        respuesta_rec.x = snail_rec.x
        respuestaf_rec.x = snail_rec.x

        rectangulo1_rec.x = respuesta_rec.x - 20
        rectangulo2_rec.x = respuestaf_rec.x - 20

        if snail_rec.right <= -50:
            
            posicion_r = random.randint(1, 2)
            if posicion_r == 1:
                snail_rec.y = 270
                y_respuesta = 100
                y_respuestaf = 270

            else:
                snail_rec.y = 100
                y_respuesta = 270
                y_respuestaf = 100

            snail_rec.left = 800
            respuesta_rec.left = 800
            respuestaf_rec.left = 800

            
            n1 = random.randint(1, 10)
            n2 = random.randint(1, 10)
            respuesta = n1*n2
            respuestaf = random.randint(respuesta-5,respuesta+5)
            if respuestaf == respuesta:
                respuestaf = respuestaf + 2
             
            
            
            respuesta_surf = test_font.render(f"{respuesta}", False, 'White')
            respuesta_rec = respuesta_surf.get_rect(topleft = (600,y_respuesta))

            respuestaf_surf = test_font.render(f"{respuestaf}", False, 'White')
            respuestaf_rec = respuestaf_surf.get_rect(topleft = (600,y_respuestaf))

            problem_surf = test_font2.render(f'{n1} x {n2}',False,'White')
            problem_rec = problem_surf.get_rect(center = (400,150))


        #we blit the objects in screen
        screen.blit(problem_surf, problem_rec)
        screen.blit(snail_surface, snail_rec)
        screen.blit(rectangulo1_surf, rectangulo1_rec)
        screen.blit(rectangulo2_surf, rectangulo2_rec)
        screen.blit(respuesta_surf, respuesta_rec)
        screen.blit(respuestaf_surf, respuestaf_rec)
        
        



        #Jugador
        #Player
        player_gravity += 0.85
        player_rec.y += player_gravity
        if player_rec.bottom >= 325:
            player_rec.bottom = 325
        screen.blit(player_surf, player_rec)

        

        #Sistema de coliciones
        #Colision sistem
        if snail_rec.colliderect(player_rec):
            game_active = False

    #Puntuación
    #score
        x += 1
        text_surface = test_font.render(f'Puntuación: {x}', False, 'White')
        
    
    else:
        text_surface = test_font.render(f'Puntuación: {x}', True, 'White')
        death_surface = test_font.render(f'Presione "Espacio" para volver a comenzar', True, 'White')
        screen.fill('Black')
        screen.blit(text_surface, (110,80))
        screen.blit(death_surface, (110,120))
        screen.blit(lunaR, (110,100))
    pygame.display.update()
    pygame.display.update()    
    pygame.display.update()
    pygame.display.update()
    #Limitar los fps
    #fps limit
    clock.tick(60)