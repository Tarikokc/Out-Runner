import pygame
from pygame.locals import *
from random import *
pygame.init()

largeur = 700
hauteur = 600

perso_x = -20
perso_y = 370

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

# def detecte_collision ():
#     """ Detecte si il y'a une collision """
# 
#     
#     for i in range (len(obstacle1)):
#         for j in range(len(obstacle1[i])-1):
#             if obstacle1[i][j] == 1 :
#                 xo1 = i*h
#                 yo1 = j*h
#                  
#                 xobasgauche = xo2 - j
#                 yobasgauche= yo1 - j 
#                 
#                 xo2 = yo1 + i
#                 yo2 = xo2 + i
#                 
#                 xo3= xobasgauche + i 
#                 yo3= yobasgauche + i 
#                 
#                 xop = xo1 - xobasgauche
#                 yop = yo2 - yo1
                
                
                

    
# x2 = y1 + i
# y2 = x2 + i
#                 
# x3= xbasgauche - j
# y3= ybasgauche + i 
#                 
# xp = x1 - xbasgauche
# yp = y2 - y1

def collision_rectangle (obstacle) :
    """ Detecte si y'a collision entre deux rectangle"""
    
    

    
    for i in range(len(obstacle)) :
        for j in range (len(obstacle[i])):
            if obstacle[i][j] == 1:
                xog = j*l
                yoh = i*h
                xod = j*l+l
                yob = i*h+h
                
                xpg = perso_x
                yph = perso_y
                xpd = perso_x+150
                ypb = perso_y +150
                
#                 print("perso gauche :", xpg, "perso droite", xpd, "perso haut:" ,yph, "perso bas :", ypb)
#                 print("obs gauche :", xog, "obs droite", xod, "obs haut:" ,yoh, "obs bas :", yob)
#                 print("\nl")
#                 pygame.draw.rect(fenetre, "red", (xog, yoh, l, h))
#                 pygame.draw.rect(fenetre, "blue", (xpg, yph, 150, 150))
                if xog>xpg and xog< xpd and ((yob > yph and yob < ypb) or (yoh > yph and yoh < ypb) ):
                    return True
    return False 
            
           

# obstacle_coli = 0    
# def collision(perso_x , perso_y , obstacle1, projectile_x):
#     """ Permet la collision entre le projectile et l'obstacle,
#     et si il y'a collision avec le personnage """
#     
#     for i in range(len(obstacle1)):
#         for j in range(len(obstacle1[i])-1) :
#             if rectperso.colliderect(rectColli)== True:
# #                     collision(perso_x , perso_y , obstacle1, projectile_x)
#                 print(" je suis mort " )
#             
#     pygame.display.flip()                  


def trace(perso_y,bg_x,obstacle,projectile_x,projectile_y,texte,score):
    fenetre.blit(bg,(bg_x,0))
    fenetre.blit(personnage,(-20,perso_y))
    fenetre.blit(projectile,(projectile_x,projectile_y))
    fenetre.blit(texte ,(0,0))
    dist = font.render(str(score)+"m", 1 , blanc)
    fenetre.blit(dist,(140,0))
    
    l= largeur // len(obstacle[0])
    h= hauteur // len(obstacle)
    
    for i in range(len(obstacle)):
        for j in range(len(obstacle[i])):
            if obstacle[i][j] == 1:
#                 feur= pygame.draw.rect(fenetre,blanc,(j*l,i*h,l,h))
                fenetre.blit (collision_obstacle ,(j*l, i*h ,l,h))
                
#                  print(Rect.x)
    pygame.display.flip()

    
def defiler(obstacle1):
    for i in range (len(obstacle1)) :
        for j in range (len(obstacle1[i])-1) :
            obstacle1[i][j] = obstacle1[i][j+1]
        obstacle1[i][-1]= 0                                       
    return obstacle1

nb_ligne= 15
nb_colonne = 15
obstacle1 = []
for i in range(nb_ligne) :
    ligne = [0]*nb_colonne
    obstacle1.append(ligne)
    
l= largeur // len(obstacle1[0])
h= hauteur // len(obstacle1)
    
def genere_obstacle(obstacle1) :
    i = randint(3,nb_ligne-3)
    
    obstacle1[i][-1] = 1
    
    



# 
def accueil ():
    """ Affiche le menu du jeu, permet le lancement du jeu """
    
    fenetre.blit(menu,(0,0))
    fenetre.blit(setting,(0,0))
    fenetre.blit(espace,(0,35))
    fenetre.blit(fleche_haut,(0,60)) 
    fenetre.blit(fleche_double_haut,(0,90))
    
    

    pygame.display.flip()


    
try:
    
    
    continuer = True
    stop = True
    menu = 0
    
    
    
    
    
    fenetre = pygame.display.set_mode((largeur,hauteur))
    personnage = pygame.image.load("player1.png").convert_alpha()
    rectperso = personnage.get_rect()
    bg = pygame.image.load("ui.png").convert_alpha()
    personnage= pygame.transform.scale(personnage,(150,150))
    
    bg = pygame.transform.scale(bg,(1500,600))
    fenetre.blit(personnage,(-20,300))
    pygame.display.flip()
    pygame.display.set_caption("Out-Runner")
    
    repet= USEREVENT
    mouvement = USEREVENT+1
    rept_dist = USEREVENT+2
    defil_obstacle = USEREVENT+3
    
    pygame.time.set_timer(repet,4)
    pygame.time.set_timer(mouvement,4)
    pygame.time.set_timer(rept_dist, 150)
    pygame.time.set_timer(defil_obstacle,80)
    
    saut = 0
    tir = False
    termine = True
    executer = False
    
    projectile = pygame.image.load("stone.png").convert_alpha()
#     rectprojectile = projectile.get_Rect()
    projectile = pygame.transform.scale(projectile,(120,120))
    
    
    font = pygame.font.SysFont(" Arial Black : ", 24, bold=False, italic=False)
    texte= font.render("Distance : ", 1, blanc)
    dist = font.render(str(score), 1 , blanc)
    
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
                
            
            
        elif ecran == 1:
            
            
            
            
            
                
                    
                
            for event in pygame.event.get():
                if event.type==QUIT:
                    continuer = False
#                 if score == 100:
#                     pygame.time.set_timer(defil_obstacle,70)
                
                
               
                    
                if event.type == defil_obstacle :
                    defiler(obstacle1)
                    
                    proba_obs -=1
                    if proba_obs == 0:
                        genere_obstacle(obstacle1)
                        

                        proba_obs= 10
                    
             
                    
                if event.type == repet :
                    if bg_x == -735 :
                        bg_x = 0
                    trace(perso_y,bg_x, obstacle1, projectile_x,projectile_y,texte,score)
                    collision_rectangle (obstacle1)
                    bg_x -= 1
                    pygame.display.flip()
                    if collision_rectangle(obstacle1):
                        ecran = 0
                        obstacle1 = []
                        for i in range(nb_ligne) :
                            ligne = [0]*nb_colonne
                            obstacle1.append(ligne)
#                     if rectperso.colliderect(rectColli) == True :
#                         print (" Je suis dead " )
             
                    pygame.display.flip()
                if event.type == rept_dist :
                    score += 1
                    
                if event.type == mouvement and saut == 1 and executer :
                    perso_y -= mouv
    #                 print(saut)
                    temp += 1
                    mouv -= 0.1
                    pygame.display.flip()
                    if temp == 101 :
                        executer = False
                        saut = 0
                if event.type == mouvement and saut == 2 and executer :
    #                 print(saut)
                    perso_y -= mouv
                    temp += 1
                    mouv -= 0.1
    #                 print(perso_y)
#                     print(temp)
                    pygame.display.flip()
                    if perso_y >= 371 :
                        executer = False
                        saut = 0
                        perso_y = 370
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
    #                 print(projectile_x , projectile_y)
                    trace(perso_y,bg_x, obstacle1, projectile_x,projectile_y,texte,score)
                    pygame.display.flip()
                    if projectile_x >= 800 :
                        tir = False
                        termine = True
                if event.type == KEYDOWN :
                    if event.key == K_SPACE and termine == True :
                        projectile_x = perso_x+75
                        projectile_y = perso_y+50
                        tir = True
                        termine = False

    
              
        



finally:
    pygame.quit()
