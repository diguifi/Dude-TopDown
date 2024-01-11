# -*- coding: cp1252 -*-
"""
    Copyright (C) 2017 - Instituto Federal de Educacao, Ciencia e Tecnologia do Sul de Minas Gerais, Muzambinho
    Author: Diego Penha - diego.penha95@gmail.com


    This file is part of As Aventuras de Dude no Mundo Top-Down.

    As Aventuras de Dude no Mundo Top-Down is free software:
    you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    As Aventuras de Dude no Mundo Top-Down
    is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with As Aventuras de Dude no Mundo Top-Down.
    If not, see <http://www.gnu.org/licenses/>.
"""
import pygame, os
from pygame.locals import *
from random import randint
from Configs import *
from Enemy import enemy as e
from Player import dude
from Shot import shot
from GeneticPool import geneticPool
from Powerups import *
from Animation import animation
from sys import exit

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()
relat=False

#Function to load images
def load_image(image_loaded,tipo):
        try:
            image = pygame.image.load(image_loaded)
        except pygame.error as message:
            print("Impossivel carregar imagem: " + image_loaded)
            raise SystemExit(message)
        if tipo == "sprite":
                x,y = pygame.Surface.get_width(image), pygame.Surface.get_height(image)
                x=int(x*MULT_TAM)
                y=int(y*MULT_TAM)
                image = pygame.transform.scale(image,(x,y))
                return image.convert_alpha()
        elif tipo == "background":
                return image.convert()
        elif tipo == "collider":
                x,y = pygame.Surface.get_width(image), pygame.Surface.get_height(image)
                x=int(x*1)
                y=int(y*1)
                image = pygame.transform.scale(image,(x,y))
                return image.convert_alpha()

#Pause main function
def pause():
    global paused
    global clock
    global paused_ticks
    drawpause()
    while paused:
        paused_ticks += clock.tick()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                paused = False
                return

#Pause draw function
def drawpause():
    font = pygame.font.Font(None, 48)
    text1 = font.render("PAUSE", 1, BRANCO)
    text1pos = text1.get_rect()
    text1pos.centerx = screen.get_rect().centerx
    text1pos.centery = screen.get_rect().centery
    screen.blit(text1, text1pos)
    font = pygame.font.Font(None, 36)
    text2 = font.render("Pressione qualquer tecla para continuar", 1, BRANCO)
    text2pos = text2.get_rect()
    text2pos.centerx = screen.get_rect().centerx
    text2pos.centery = screen.get_rect().centery + 50
    screen.blit(text2, text2pos)
    pygame.display.flip()

#Function executed when player has life<0
def morto():
    drawmorto()
    waiting = True
    while waiting:
        clock2.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sair()
                sair()

#Function for next level
def vitorioso():
    drawvitorioso()
    waiting = True
    while waiting:
        clock2.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sair()
                elif event.key == K_y:
                    waiting=False
                elif event.key == K_n:
                    sair()

#Function for drawing the dead status
def drawmorto():
    font = pygame.font.Font(None, 48)
    text1 = font.render("GAME OVER", 1, BRANCO)
    text1pos = text1.get_rect()
    text1pos.centerx = screen.get_rect().centerx
    text1pos.centery = screen.get_rect().centery
    screen.blit(text1, text1pos)

    font = pygame.font.Font(None, 30)
    txtAgain = font.render("Any key to exit", 1, BRANCO)
    txtAgain_rect = txtAgain.get_rect()
    txtAgain_rect.midtop = (LARGURA/2, ALTURA/2+0.1*ALTURA)
    screen.blit(txtAgain, txtAgain_rect)
    pygame.display.flip()

#Function for drawing the victorious status
def drawvitorioso():
    font = pygame.font.Font(None, 48)
    text1 = font.render("VITORIA!", 1, BRANCO)
    text1pos = text1.get_rect()
    text1pos.centerx = screen.get_rect().centerx
    text1pos.centery = screen.get_rect().centery
    screen.blit(text1, text1pos)

    font = pygame.font.Font(None, 30)
    txtAgain = font.render("Play again? (y/n)", 1, BRANCO)
    txtAgain_rect = txtAgain.get_rect()
    txtAgain_rect.midtop = (LARGURA/2, ALTURA/2+0.1*ALTURA)
    screen.blit(txtAgain, txtAgain_rect)
    pygame.display.flip()

#Function for Main Menu
def menuprincipal(gamemode):
    screen.fill(PRETO)
    textoMenuPrincipal()
    screen.blit(sprite_arrow, (LARGURA/2-0.33*LARGURA, ALTURA/2-0.03*ALTURA))

    pygame.display.flip()
    gamemode=selecaoModo()
    return gamemode

#Draw Main Menu
def textoMenuPrincipal():
    font = pygame.font.Font("fonts/font.ttf", 25)
    txtTitle = font.render("As aventuras de Dude", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/5)
    screen.blit(txtTitle, txt_rect)
    txtTitle = font.render("no mundo Top Down", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/4)
    screen.blit(txtTitle, txt_rect)

    font = pygame.font.Font("fonts/font.ttf", 18)
    txtTitle = font.render("Modo: Estados Finitos", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/2-0.03*ALTURA)
    screen.blit(txtTitle, txt_rect)

    txtTitle = font.render("Modo: Algoritmo Genetico", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/2+0.03*ALTURA)
    screen.blit(txtTitle, txt_rect)

    font = pygame.font.Font("fonts/font.ttf", 15)
    txtTitle = font.render("Select mode and press Enter", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/1.2)
    screen.blit(txtTitle, txt_rect)

#Draw post menu screen
def posmenu():
    screen.fill(PRETO)
    font = pygame.font.Font("fonts/font.ttf", 18)
    txtTitle = font.render("Setas - movimenta��o", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/4)
    screen.blit(txtTitle, txt_rect)

    screen.blit(pygame.transform.scale(sprite_a,(30,30)), (120,172))
    screen.blit(pygame.transform.scale(sprite_sh,(30,30)), (120,212))
    screen.blit(pygame.transform.scale(sprite_hp,(30,30)), (120,252))
    screen.blit(pygame.transform.scale(sprite_pts,(30,30)), (120,291))

    font = pygame.font.Font("fonts/font.ttf", 18)
    txtTitle = font.render("+"+str(BONUS_AMMO)+" muni��es", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, 176)
    screen.blit(txtTitle, txt_rect)

    txtTitle = font.render("+"+str(SHIELD_TIME)+"s de imunidade", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, 216)
    screen.blit(txtTitle, txt_rect)

    txtTitle = font.render("+"+str(BONUS_HEALTH)+" de vida", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, 256)
    screen.blit(txtTitle, txt_rect)

    txtTitle = font.render("+"+str(BONUS_POINTS)+" pontos extra", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, 295)
    screen.blit(txtTitle, txt_rect)

    font = pygame.font.Font("fonts/font.ttf", 15)
    txtTitle = font.render("Press any key to start!", 1, BRANCO)
    txt_rect = txtTitle.get_rect()
    txt_rect.midtop = (LARGURA/2, ALTURA/1.2)
    screen.blit(txtTitle, txt_rect)

    pygame.display.flip()
    aguardarBotao()

#Wait for button press
def aguardarBotao():
    waiting = True
    while waiting:
        clock2.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()
            if event.type == pygame.KEYDOWN:
                waiting = False

#Mode select function (Main menu)
def selecaoModo():
    waiting = True
    arrow_position=1
    while waiting:
        clock2.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sair()
                elif event.key == K_UP:
                    screen.fill(PRETO)
                    textoMenuPrincipal()
                    arrow_position*=-1
                    if arrow_position==1:
                        screen.blit(sprite_arrow, (LARGURA/2-0.33*LARGURA, ALTURA/2-0.03*ALTURA))
                    elif arrow_position==-1:
                        screen.blit(sprite_arrow, (LARGURA/2-0.33*LARGURA, ALTURA/2+0.03*ALTURA))
                    pygame.display.flip()
                elif event.key == K_DOWN:
                    screen.fill(PRETO)
                    textoMenuPrincipal()
                    arrow_position*=-1
                    if arrow_position==1:
                        screen.blit(sprite_arrow, (LARGURA/2-0.33*LARGURA, ALTURA/2-0.03*ALTURA))
                    elif arrow_position==-1:
                        screen.blit(sprite_arrow, (LARGURA/2-0.33*LARGURA, ALTURA/2+0.03*ALTURA))
                    pygame.display.flip()
                elif event.key == K_RETURN:
                    if arrow_position==1:
                        return 1
                    elif arrow_position==-1:
                        return 2
                elif event.key == K_SPACE:
                    if arrow_position==1:
                        return 1
                    elif arrow_position==-1:
                        return 2

def startAnimation(previousData, newData, chosenOnes):
    global paused
    global clock
    global paused_ticks

    anim = animation(screen, previousData, newData, chosenOnes, enemiesSpritesList, sprite_ec, pygame)
    animationRunning = True
    while animationRunning:
        paused_ticks += clock.tick()

        for event in pygame.event.get():
          if event.type == KEYDOWN:
              if event.key == K_SPACE:
                  animationRunning = False
              elif event.key == K_ESCAPE:
                  listaRound.append([life,pontos,minutos,segundos])
                  enemiesData=getEnemiesData()
                  listaCrom.append(enemiesData)
                  sair()
                
        anim.update(pygame, screen, paused_ticks)
        

#Function for displaying game status
def status(gamemode,gene1,gene2,gene3,gene4,gene5):
    font = pygame.font.Font("fonts/font.ttf", 18)
    txtStatus = font.render("Vida: "+str(life), 1, PRETO, BRANCO)
    txtStatusPos = 2,2
    screen.blit(txtStatus, txtStatusPos)
    font = pygame.font.Font("fonts/font.ttf", 18)
    txtPontos = font.render("Pontos: "+str(pontos), 1, PRETO, BRANCO)
    txtPontosPos = LARGURA2/2-txtPontos.get_width()/2,2
    screen.blit(txtPontos, txtPontosPos)
    font = pygame.font.Font("fonts/font.ttf", 18)
    txtAmmo = font.render("Muni��o: "+str(ammo), 1, PRETO, BRANCO)
    txtAmmoPos = LARGURA2-txtAmmo.get_width(),2
    screen.blit(txtAmmo, txtAmmoPos)
    font = pygame.font.Font("fonts/font.ttf", 18)
    txtRound = font.render("Round: "+str(Round), 1, PRETO, BRANCO)
    txtRoundPos = 2,445
    screen.blit(txtRound, txtRoundPos)
    font = pygame.font.Font(None, 48)
    txtTime = font.render(str(minutos).zfill(2)+":"+str(segundos).zfill(2), 1, BRANCO,PRETO)
    txtTimePos = LARGURA2-txtTime.get_width(),445
    screen.blit(txtTime, txtTimePos)

    font = pygame.font.Font(None, 18)
    txtGene1 = font.render(str(gene1), 1, PRETO, BRANCO)
    txtGene1Pos = 6,520
    screen.blit(txtGene1, txtGene1Pos)
    txtGene2 = font.render(str(gene2), 1, PRETO, BRANCO)
    txtGene2Pos = 194,520
    screen.blit(txtGene2, txtGene2Pos)
    txtGene3 = font.render(str(gene3), 1, PRETO, BRANCO)
    txtGene3Pos = 382,520
    screen.blit(txtGene3, txtGene3Pos)
    txtGene4 = font.render(str(gene4), 1, PRETO, BRANCO)
    txtGene4Pos = 570,520
    screen.blit(txtGene4, txtGene4Pos)
    txtGene5 = font.render(str(gene5), 1, PRETO, BRANCO)
    txtGene5Pos = 758,520
    screen.blit(txtGene5, txtGene5Pos)

#Exit game function
def sair():
    if relat:
        gerarRelatorio(listaRound,gamemode,Round,listaCrom)
    pygame.quit()
    exit()

#Final report function
def gerarRelatorio(listaRound,g,Round,listaCrom):
        fname = "Relatorio.txt"
        if os.path.isfile(fname):
                file = open("Relatorio.txt","a")
        else:
                file = open("Relatorio.txt","w")
                
        file.write("___________________________________________________\n")
        file.write("\tRelatorio final:\n\n")
        file.write("Modo de jogo: ")
        file.write("Maquina de estados finitos\n" if g == 1 else "Algoritmo Genetico\n\n")
        x=0
        while x<Round:
          file.write("ROUND "+str(x+1)+":\n")
          file.write("Vida restante: "+str(listaRound[x][0])+"/1000\n")
          file.write("Pontos: "+str(listaRound[x][1])+"\n")
          file.write("Tempo de jogo: "+str(listaRound[x][2]).zfill(2)+":"+str(listaRound[x][3]).zfill(2)+"\n")
          file.write("\n")
          if gamemode!=1:
                  file.write("Cromossomos: "+str(listaCrom[x])+"\n")
                  file.write("\n")
          x+=1

        file.close()

#Gets enemies chromossomes and fitness
def getEnemiesData():
        enemiesData = [[DNA1,enemy.getFitness()],[DNA2,enemy2.getFitness()],[DNA3,enemy3.getFitness()],[DNA4,enemy4.getFitness()],[DNA5,enemy5.getFitness()]]
        return enemiesData


#Initializes main screen
os.environ["SDL_VIDEO_CENTERED"] = "1"
screen = pygame.display.set_mode((LARGURA2, ALTURA2),0,32)
bg = load_image(BACKGROUND,"background")
pygame.display.set_caption("TCC - Diego Penha")
pygame.display.set_icon(load_image(ICONE,"sprite"))
pygame.mouse.set_visible(0)
gamemode = 0
playagain = True
Round=1
listaRound = []
listaCrom = []
vitoria=0
control1 = 1
control2 = 1
full_screen = False
pygame.mixer.music.load(BACK_MUSIC)
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1)
shoot_sound = pygame.mixer.Sound(SHOOT_SOUND)
powerup_sound = pygame.mixer.Sound(POWERUP_SOUND)
dead_sound = pygame.mixer.Sound(DEAD_SOUND)
reload_sound = pygame.mixer.Sound(RELOAD_SOUND)
shield_sound = pygame.mixer.Sound(SHIELD_SOUND)

#Initializes sprites
sprite_p = load_image(SPRITE_PLAYER,"sprite")
sprite_p_sh = load_image(SPRITE_PLAYER_SH,"sprite")
sprite_e = load_image(SPRITE_ENEMY,"sprite")
sprite_e2 = load_image(SPRITE_ENEMY2,"sprite")
sprite_e3 = load_image(SPRITE_ENEMY3,"sprite")
sprite_e4 = load_image(SPRITE_ENEMY4,"sprite")
sprite_e5 = load_image(SPRITE_ENEMY5,"sprite")
sprite_ec = load_image(SPRITE_ENEMYC,"collider")
sprite_e_sh = load_image(SPRITE_ENEMY_SH,"sprite")
sprite_a = load_image(SPRITE_AMMO,"sprite")
sprite_s = load_image(SPRITE_SHOT,"background")
sprite_sh = load_image(SPRITE_SHIELD,"sprite")
sprite_hp = load_image(SPRITE_HEALTH,"sprite")
sprite_pts = load_image(SPRITE_POINTS,"sprite")
sprite_arrow = pygame.image.load(SPRITE_ARROW).convert_alpha()
enemiesSpritesList = [sprite_e, sprite_e2, sprite_e3, sprite_e4, sprite_e5]

#Powerups initialization
ammoBox = ammobox(sprite_a)
shield = Shield(sprite_sh)
health = Health(sprite_hp)
itemPts = Points(sprite_pts)

#Player initialization
move_x, move_y = 0, 0
shot_x, shot_y = 1, 0
player = dude(sprite_p,sprite_s)
life = player.life
pontos = player.pontos
ammo = player.ammo
sh_time = shield.shieldTime
shooting = False
cantShoot = False
s=[]
tiros=-1

#Main menu call
clock2 = pygame.time.Clock()
gamemode=menuprincipal(gamemode)
if gamemode==1:
    screen = pygame.display.set_mode((LARGURA, ALTURA),0,32)
elif gamemode==2:
    screen = pygame.display.set_mode((LARGURA2, ALTURA2),0,32)

#Post menu call
posmenu()

#Enemies initialization
enemy = e(sprite_e,sprite_ec,gamemode)
enemy2 = e(sprite_e2,sprite_ec,gamemode)
enemy3 = e(sprite_e3,sprite_ec,gamemode)
enemy4 = e(sprite_e4,sprite_ec,gamemode)
enemy5 = e(sprite_e5,sprite_ec,gamemode)
lista_inimigos = [enemy,enemy2,enemy3,enemy4,enemy5]

#Genetic reading
DNA1 = enemy.getDNA()
DNA2 = enemy2.getDNA()
DNA3 = enemy3.getDNA()
DNA4 = enemy4.getDNA()
DNA5 = enemy5.getDNA()

#Creating group entities for collision tests
inimigos = pygame.sprite.Group()
inimigos.add(enemy)
inimigos.add(enemy2)
inimigos.add(enemy3)
inimigos.add(enemy4)
inimigos.add(enemy5)

ammoGroup = pygame.sprite.Group()
shieldGroup = pygame.sprite.Group()
shieldGroup.add(shield)
healthGroup = pygame.sprite.Group()
healthGroup.add(health)
ptsGroup = pygame.sprite.Group()

personagem = pygame.sprite.Group()
personagem.add(player)

#Clock object setup
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
minutos = 00
segundos = 00
i=0
cont = 0
pygame.time.set_timer(USEREVENT+1,1000)
paused = False
paused_ticks = 0

#Change this to true if want to generate reports at the end of the game
relat=False


pygame.mixer.music.set_volume(0.15)
#Main loop
while playagain:
  #ROUND LOOP
  while (life>0) and (vitoria<5):
      #Calculates in ms how long it took since last call of clock.tick()
      time_passed = clock.tick()

      milissegundos = pygame.time.get_ticks()-start_ticks-paused_ticks
      segundos = int(((pygame.time.get_ticks()-start_ticks-paused_ticks)/1000)-60*i)
      segundoss = segundos+60*i
      minutos = int((pygame.time.get_ticks()-start_ticks-paused_ticks)/60000)
      cont=0
      if segundos>59:
          i+=1
          
      #Game events
      for event in pygame.event.get():
          #Quit game
          if event.type == QUIT:
              listaRound.append([life,pontos,minutos,segundos])
              enemiesData=getEnemiesData()
              listaCrom.append(enemiesData)
              sair()
          if event.type == USEREVENT + 1:
              cont = 1
          if event.type == KEYDOWN:
              if event.key == K_ESCAPE:
                  listaRound.append([life,pontos,minutos,segundos])
                  enemiesData=getEnemiesData()
                  listaCrom.append(enemiesData)
                  sair()
              elif event.key == K_p:
                  paused = True
                  pause()
              elif event.key == K_f:
                  if not full_screen:
                      screen = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN, 32)
                      full_screen = True
                  else:
                      if gamemode==1:
                          screen = pygame.display.set_mode((LARGURA, ALTURA),0,32)
                      elif gamemode==2:
                          screen = pygame.display.set_mode((LARGURA2, ALTURA2),0,32)
                      full_screen = False
          #Player movimentation inputs
          if event.type == KEYDOWN:
              if event.key == K_LEFT:
                  move_x = -1
                  shot_y = 0
                  shot_x = -1
              elif event.key == K_RIGHT:
                  move_x = +1
                  shot_y = 0
                  shot_x = +1
              elif event.key == K_UP:
                  move_y = -1
                  shot_x = 0
                  shot_y = -1
              elif event.key == K_DOWN:
                  move_y = +1
                  shot_x = 0
                  shot_y = +1

              #Shot key
              elif event.key == K_SPACE:
                  if ammo>0:
                      if not cantShoot:
                          shoot_sound.play()
                          tiros+=1
                          player.ammo-=1
                          ammo = player.ammo
                          shooting = True
                          sho=shot(sprite_s,player.X,player.Y,shot_x,shot_y)
                          s.append(sho)

          elif event.type == KEYUP:
              if event.key == K_LEFT:
                  move_x = 0
              elif event.key == K_RIGHT:
                  move_x = 0
              elif event.key == K_UP:
                  move_y = 0
              elif event.key == K_DOWN:
                  move_y = 0

      #Background positioning and game status
      screen.blit(bg, (0,0))
      status(gamemode,DNA1,DNA2,DNA3,DNA4,DNA5)

      #Player movimentation
      player.update(move_x,move_y,screen,time_passed,sprite_p,cont,lista_inimigos,shot_x,shot_y,dead_sound)

      #Item placement reading
      placeHP = (health.X,health.Y)
      placeSh = (shield.X,shield.Y)
      placePts = (itemPts.X,itemPts.Y)
      
      #Enemies movimentation
      enemy.update(screen,time_passed,sprite_e,cont,healthGroup,placeHP,ptsGroup,placePts,shieldGroup,placeSh,player.life,player.pontos,player)
      enemy2.update(screen,time_passed,sprite_e2,cont,healthGroup,placeHP,ptsGroup,placePts,shieldGroup,placeSh,player.life,player.pontos,player)
      enemy3.update(screen,time_passed,sprite_e3,cont,healthGroup,placeHP,ptsGroup,placePts,shieldGroup,placeSh,player.life,player.pontos,player)
      enemy4.update(screen,time_passed,sprite_e4,cont,healthGroup,placeHP,ptsGroup,placePts,shieldGroup,placeSh,player.life,player.pontos,player)
      enemy5.update(screen,time_passed,sprite_e5,cont,healthGroup,placeHP,ptsGroup,placePts,shieldGroup,placeSh,player.life,player.pontos,player)

      #Test if shooting (enables multi shots and single shots on Configs.py)
      if shooting:
          j=-1
          while j<tiros:
            if not MULTI_SHOTS:
              cantShoot = True
            player.testCollisionShot(s[j],lista_inimigos,time_passed)
            enemy.testCollisionShot(time_passed,s[j],player,dead_sound)
            enemy2.testCollisionShot(time_passed,s[j],player,dead_sound)
            enemy3.testCollisionShot(time_passed,s[j],player,dead_sound)
            enemy4.testCollisionShot(time_passed,s[j],player,dead_sound)
            enemy5.testCollisionShot(time_passed,s[j],player,dead_sound)
            s[j].update(screen,time_passed)
            j+=1
            #shooting = s[tiros].cantShoot
            if s[j].cantShoot==False:
                s.pop(j)
                tiros=tiros-1
                j=j-1
      else:
        cantShoot = False

      #Status variables update
      pontos = player.pontos
      life = player.life
      vitoria = enemy.dead2+enemy2.dead2+enemy3.dead2+enemy4.dead2+enemy5.dead2

      #Collision with powerups
      if pygame.sprite.spritecollide(player, ammoGroup, True):
          reload_sound.play()
          player.ammo += ammoBox.bonusAmmo
          ammo = player.ammo
      if pygame.sprite.spritecollide(player, healthGroup, True):
          powerup_sound.play()
          if player.life+health.bonusHP<=LIFE_PLAYER:
              player.life += health.bonusHP
          else:
              player.life = LIFE_PLAYER
          life = player.life
          player.lifeBar(screen)
      if pygame.sprite.spritecollide(player, ptsGroup, True):
          powerup_sound.play()
          player.pontos += itemPts.bonusPts
          pontos = player.pontos
      if pygame.sprite.spritecollide(player, shieldGroup, True):
          shield_sound.play()
          player.shield_on = True
          player.activatePower(sprite_p_sh,"shield")

      #Powerups powerups
      #Ammo
      if (segundos%20==0) and segundos != 0:
          if control1 == 1:
              spawnPower = randint(0,100)
              spawnPower2 = randint(0,100)
              control1 = 0
              if spawnPower > 70:
                  if health not in healthGroup:
                      healthGroup.add(health)
                      health.changePos()
              elif spawnPower > 50:
                  if itemPts not in ptsGroup:
                      ptsGroup.add(itemPts)
                      itemPts.changePos() 
              if spawnPower2 < 95:
                  if ammoBox not in ammoGroup:
                      ammoGroup.add(ammoBox)
                      ammoBox.changePos()

      if (segundos%21==0):
          control1 = 1
      #Shield
      if (segundos%30==0) and segundos != 0:
          if control2 == 1:
              spawnPower2 = randint(0,100)
              control2 = 0
              if spawnPower2 > 40:
                  if ammoBox not in shieldGroup:
                      shieldGroup.add(shield)
                      shield.changePos()

      if (segundos%31==0):
          control2 = 1

      ammoGroup.draw(screen)
      ptsGroup.draw(screen)
      healthGroup.draw(screen)
      shieldGroup.draw(screen)

      #General tests
      #PLACE TESTS LINES HERE

      #Refresh (by FPS)
      pygame.display.update()

      #END OF THE ROUND LOOP
      
  enemiesData=getEnemiesData()
  if life<5:
    listaRound.append([life,pontos,minutos,segundos])
    listaCrom.append(enemiesData)
    morto()
  else:
    listaRound.append([life,pontos,minutos,segundos])
    listaCrom.append(enemiesData)
    vitorioso()
  #ROUND CHANGE
  Round+=1
  vitoria=0  
  #INICIALIZATIONS
  #Clock
  clock = pygame.time.Clock()
  start_ticks = pygame.time.get_ticks()
  minutos = 00
  segundos = 00
  i=0
  cont = 0
  pygame.time.set_timer(USEREVENT + 1,1000)
  paused = False
  paused_ticks = 0
  
  #Powerups
  ammoBox = ammobox(sprite_a)
  shield = Shield(sprite_sh)
  health = Health(sprite_hp)
  itemPts = Points(sprite_pts)

  #Player
  move_x, move_y = 0, 0
  shot_x, shot_y = 1, 0
  player.reset()
  life = player.life
  pontos = player.pontos
  ammo = player.ammo
  sh_time = shield.shieldTime
  shooting = False
  cantShoot = False
  s=[]
  tiros=-1

  '''
    Before reseting the enemies, apply genetic modifications
  '''
  
  #Send of chromosomes and fitness scores to the Genetic Pool
  if gamemode==2:
          enemiesData=getEnemiesData()
          previousData = enemiesData
          
          g = geneticPool(enemiesData)
          enemiesData = g.enemiesData

          chosenOnes = [g.enemiesDataSelecteds[0], g.enemiesDataSelecteds[1]]
          newData = g.enemiesData

          #New chromosomes
          DNA1=enemiesData[4][0]
          DNA2=enemiesData[3][0]
          DNA3=enemiesData[2][0]
          DNA4=enemiesData[1][0]
          DNA5=enemiesData[0][0]

          startAnimation(previousData, newData, chosenOnes)
            
  else:
          DNA1=["","","","","","","",""]
          DNA2=["","","","","","","",""]
          DNA3=["","","","","","","",""]
          DNA4=["","","","","","","",""]
          DNA5=["","","","","","","",""]

  #Reset of enemies with new chromosomes
  enemy.reset(DNA1,gamemode,sprite_ec,Round)
  enemy2.reset(DNA2,gamemode,sprite_ec,Round)
  enemy3.reset(DNA3,gamemode,sprite_ec,Round)
  enemy4.reset(DNA4,gamemode,sprite_ec,Round)
  enemy5.reset(DNA5,gamemode,sprite_ec,Round)

  #Entities groups
  inimigos = pygame.sprite.Group()
  inimigos.add(enemy)
  inimigos.add(enemy2)
  inimigos.add(enemy3)
  inimigos.add(enemy4)
  inimigos.add(enemy5)

  ammoGroup = pygame.sprite.Group()
  shieldGroup = pygame.sprite.Group()
  shieldGroup.add(shield)
  healthGroup = pygame.sprite.Group()
  healthGroup.add(health)
  ptsGroup = pygame.sprite.Group()

  personagem = pygame.sprite.Group()
  personagem.add(player)

#Exit
sair()
