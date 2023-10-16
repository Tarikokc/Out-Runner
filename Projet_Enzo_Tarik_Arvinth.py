import pygame
from pygame.locals import *
from random import *
from pygame import mixer
pygame.init()






largeur = 700
hauteur = 600
perso_x = -20
perso_y = 450
noir = (0,0,0)
blanc = (255,255,255)
y_mouv = 0
bg_x = 0
bg_y = 0
projectile_x = 1000
projectile_y = perso_y+55
mouv = 5
temp = 0
score= 0
vie = 3

obstacle_evite = 0 
def collision_rectangle (obstacle1) :
    """ Detecte si y'a collision entre deux rectangle""" 
    for i in range(len(obstacle1)) :
        for j in range (len(obstacle1[i])-1):
            if obstacle1[i][j] == 1: 
                x_obs_g = j*l
                y_obs_h = i*h
                x_obs_d = j*l+l
                y_obs_b = i*h+h
                x_perso_g = perso_x
                y_perso_h = perso_y
                x_perso_d = perso_x + 140
                y_perso_b = perso_y + 140
                y_perso_d = (perso_x + 140) + (perso_y + 140)
                if x_perso_d > x_obs_g  and x_obs_g > x_perso_g and y_perso_h < y_obs_b and y_obs_b < y_perso_b  :
                    return True
                if y_perso_d > y_obs_b and y_obs_b > y_perso_h and x_perso_g > x_obs_d and x_obs_d > x_perso_d :
                    return True
    return False 
    pygame.display.flip()       


def trace(perso_y,bg_x,obstacle,projectile_x,projectile_y,texte,score):
    fenetre.blit(bg,(bg_x,0))
    fenetre.blit(personnage,(17,perso_y))
    fenetre.blit(projectile,(projectile_x,projectile_y))
    fenetre.blit(texte ,(0,0))
    dist = font.render(str(score)+"m", 1 , blanc)
    nb_vie = font.render("Vie : "+str(vie), 1 , blanc)
#     obs_evite= font.render (" Obstacle évité " + str(obstacle_evite) , 1 , blanc )
    fenetre.blit(dist,(140,0))
    fenetre.blit(nb_vie,(600,0))
#     fenetre.blit(obs_evite,(350, 0))
    
    for i in range(len(obstacle)):
        for j in range(len(obstacle[i])):
            if obstacle[i][j] == 1:
                fenetre.blit (collision_obstacle ,(j*l, i*h ,l,h))
    pygame.display.flip()

def trace1(perso_y,bg_x,obstacle,projectile_x,projectile_y,texte,score):
    fenetre.blit(bg,(bg_x,0))
    fenetre.blit(personnage,(17,perso_y))
    fenetre.blit(projectile,(projectile_x,projectile_y))
    fenetre.blit(texte ,(0,0))
    fenetre.blit(fond,(bg_x,0))
    dist = font.render(str(score)+"m", 1 , blanc)
    nb_vie = font.render("Vie : "+str(vie), 1 , blanc)
#     obs_evite= font.render (" Obstacle évité " + str(obstacle_evite) , 1 , blanc )
    fenetre.blit(dist,(140,0))
    fenetre.blit(nb_vie,(600,0))
#     fenetre.blit(obs_evite,(350, 0))
    
    for i in range(len(obstacle)):
        for j in range(len(obstacle[i])):
            if obstacle[i][j] == 1:
                fenetre.blit (collision_obstacle ,(j*l, i*h ,l,h))
    pygame.display.flip()

    
def defiler(obstacle1):
    for i in range (len(obstacle1)) :
        for j in range (len(obstacle1[i])-1) :
            obstacle1[i][j] = obstacle1[i][j+1]
        obstacle1[i][-1]= 0
#         obstacle1[i][1]= 0
    return obstacle1

nb_ligne= 15
nb_colonne = 15 
obstacle1 = []

def genere_obstacle(obstacle1) :
    i = randint(2,nb_ligne-3)
    obstacle1[i][-1] = 1
    
def supprime_obstacle(obstacle1) :
    for i in range (0,15) :
        obstacle1[i][0] = 0
        obstacle1[i][1] = 0
        obstacle1[i][2] = 0
        
    
    
for i in range(nb_ligne) :
    ligne = [0]*nb_colonne
    obstacle1.append(ligne)

def accueil ():
    """ Affiche le menu du jeu, permet le lancement du jeu """  
    fenetre.blit(menu,(0,0))
    fenetre.blit(setting,(0,0))
    fenetre.blit(espace,(0,35))
    fenetre.blit(fleche_haut,(0,60)) 
    fenetre.blit(fleche_double_haut,(0,90))
    pygame.display.flip()

# def touche_collision(obstacle,projectile_x,projectile_y) :
#     """ Verifie si il y'a une collision entre un projectile et l'obstacle """
#     
#     for i in range(len(obstacle) :
#         for j in range(len(obstacle[i]-1) :
#                        if x_perso_d > x_obs_g  and x_obs_g > x_perso_g and y_perso_h < y_obs_b and y_obs_b < y_perso_b
# 
try:
    continuer = True
    fenetre = pygame.display.set_mode((largeur,hauteur))
    l= largeur // len(obstacle1[0])
    h= hauteur // len(obstacle1)
    personnage = pygame.image.load("player1.png").convert_alpha()
    rectperso = personnage.get_rect()
    bg = pygame.image.load("ui.png").convert_alpha()
    personnage= pygame.transform.scale(personnage,(160,60))
    bg = pygame.transform.scale(bg,(3312,600))
    fenetre.blit(personnage,(-20,300))
    pygame.display.flip()
    pygame.display.set_caption("Out-Runner")
    tir_projectile_son = pygame.mixer.Sound ("shot.mp3")
    collision_obstacle_son= pygame.mixer.Sound ("ooh.mp3")
    repet= USEREVENT
    mouvement = USEREVENT+1
    rept_dist = USEREVENT+2
    defil_obstacle = USEREVENT+3
    degat = USEREVENT+4
    pygame.time.set_timer(repet,4)
    pygame.time.set_timer(mouvement,4)
    pygame.time.set_timer(rept_dist, 150)
    pygame.time.set_timer(defil_obstacle,80)
    pygame.time.set_timer(degat,300)
    saut = 0
    tir = False
    termine = True
    executer = False
    projectile = pygame.image.load("stone.png").convert_alpha()
    projectile = pygame.transform.scale(projectile,(120,120))
    fond2= pygame.image.load("fond2.jpg").convert_alpha()
    font = pygame.font.SysFont(" Arial Black : ", 24, bold=False, italic=False)
    texte= font.render("Distance : ", 1, blanc)
    dist = font.render(str(score), 1 , blanc)
    nb_vie = font.render(str(vie), 1 , blanc)
    obs_evite= font.render ( str(obstacle_evite) , 1 , blanc )
    fenetre.blit(dist,(10,10))
    fenetre.blit(texte ,(0,0))
    obstacle = 0
    menu = pygame.image.load("menu.png").convert_alpha()
    menu = pygame.transform.scale(menu,(700,600))
    proba_obs = 10 
    ecran = 0
    style = pygame.font.SysFont(" Arial Black : ", 17, bold=False, italic=False)
    setting = font.render(" Commandes : ", 1, blanc)
    espace = style.render (" ESPACE pour tirer ",1, blanc)
    fleche_haut = style.render ( " ↑ pour sauter " ,1 , blanc)
    fleche_double_haut = style.render(" ↑↑ pour un double saut ",1, blanc)
    mort = style.render (" Vous etes mort ",1, blanc)
    collision_obstacle = pygame.image.load("collis_obs.png").convert_alpha()
    rectColli = collision_obstacle.get_rect()
    collision_obstacle = pygame.transform.scale(collision_obstacle,(l,h))
    
    
    while continuer:
        if ecran == 0:
            accueil()
            for event in pygame.event.get():
                if event.type==QUIT:
                    continuer = False
                elif event.type == KEYDOWN :
                    if event.key == K_RETURN:
                        ecran = 1

            
            
        elif ecran == 1 :
           for event in pygame.event.get():
                if event.type==QUIT:
                    continuer = False
                    
                if event.type == defil_obstacle :
                    defiler(obstacle1)
                    collision_rectangle(obstacle1)
                    if collision_rectangle(obstacle1) == True :
                        vie -= 1
                        supprime_obstacle(obstacle1)
                        pygame.mixer.Sound.play(collision_obstacle_son)
                    else :
                        obstacle_evite += 1
                        
                    proba_obs -=1
                    if proba_obs == 0:
                        genere_obstacle(obstacle1)
                        proba_obs= 10
                    
                    
                if event.type == repet :
                    if bg_x == -2612 :
                         bg_x = 0
                    trace(perso_y,bg_x, obstacle1, projectile_x,projectile_y,texte,score)
                    bg_x -= 1
#                     if texte >= 500 :
#                         trace(perso_y,bg_x, obstacle1, projectile_x,projectile_y,texte,score)
#                         
                        
#                     print(bg_x)
                    pygame.display.flip()
                    
                    if vie == 0 :
                        continuer = False
                    
                    
                if event.type == rept_dist :
                    score += 1
                    
                if event.type == mouvement and saut == 1 and executer :
                    perso_y -= mouv
                    temp += 1
                    mouv -= 0.1
                    pygame.display.flip()
                    if temp == 101 :
                        executer = False
                        saut = 0
                if event.type == mouvement and saut == 2 and executer :
                    perso_y -= mouv
                    temp += 1
                    mouv -= 0.1
                    pygame.display.flip()
                    if perso_y >= 451 :
                        executer = False
                        saut = 0
                        perso_y = 450
                if event.type == KEYDOWN :
                    if event.key == K_UP and saut <= 1 :
                        temp = 0
                        if saut <= 1 :
                            if saut == 1 :
                                temp = 0
                            saut += 1
                        mouv = 5
                        executer = True       
                        
                if event.type == mouvement and tir:
                    projectile_x += 5
                    trace(perso_y,bg_x, obstacle1, projectile_x,projectile_y,texte,score)
                    
                    pygame.display.flip()
                    if projectile_x >= 800 :
                        tir = False
                        termine = True
                if event.type == KEYDOWN :
                    if event.key == K_SPACE and termine == True :
                        projectile_x = perso_x+130
                        projectile_y = perso_y-20
                        pygame.mixer.Sound.play(tir_projectile_son)
                        tir = True
                        termine = False
                    
    
              
        



finally:
    pygame.quit()

