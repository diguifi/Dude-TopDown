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
from Configs import *
from random import randint,randrange,uniform

#Object for field of view
class collider(pygame.sprite.Sprite):
    def __init__(self,spriteEC,x,y,sizeX,sizeY):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteEC
        x,y = pygame.Surface.get_width(self.image), pygame.Surface.get_height(self.image)
        x = x/2 - sizeX/2
        y = y/2 - sizeY/2
        self.X = x
        self.Y = y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x-self.X, y-self.Y)

#Object for the enemy
class enemy(pygame.sprite.Sprite):
    def __init__(self,spriteE,spriteEC,gamemode):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteE
        self.sizeX=pygame.Surface.get_width(self.image)
        self.sizeY=pygame.Surface.get_height(self.image)
        self.X = randint(LARGURA/2,LARGURA-self.sizeX-33)
        self.Y = randint(ALTURA/2,ALTURA-self.sizeY-33)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.speed = SPEED_ENEMY
        self.totalLife = LIFE_ENEMY
        self.life = LIFE_ENEMY
        self.barGreen = 0
        self.barRed = 0
        self.shield_on = False
        self.secondsLeft = 0
        self.dead = False
        self.dead2 = 0
        self.xis=1
        self.yps=1
        self.segundos = 0
        self.pontos=0
        self.coll = 0
        self.round = 1
        self.gamemode=gamemode

        #Chromossome (If gamemode == genetic algorithm)
        if gamemode==2:
            #[movement, speed, relation with hp, relation with shield, relation with points, relation with player, field of view, life]
            self.dna=[randint(1,10),randint(70,130),randint(0,2),randint(0,2),randint(0,2),randint(0,1),round(uniform(0.5, 2),2),round(uniform(0.5, 2),2)]

            self.setLife()
            self.setVision(spriteEC)

        else:
            self.dna=["","","","","","","",""]
            self.coll = collider(spriteEC,self.X,self.Y,self.sizeX,self.sizeY)

        self.fitness=0

        #Movement attributes
        self.crazyness=1
        self.lado=1
        self.direx=1
        self.direy=1
        self.stop=50

        self.proxHP = 0
        self.proxSh = 0
        self.proxPts = 0
        self.proxPlayer = 0
        
    #Gets chromossome
    def getDNA(self):
        return self.dna
    
    #Gets fitness score
    def getFitness(self):
        return self.fitness

    #Gets seconds alive
    def getSegundos(self):
        return self.segundos

    #Sets fitness score
    def setFitness(self,lifeP,pontosP):
        self.fitness = (self.pontos/25)+(self.segundos/2)+(self.life/15)
        print(self.fitness)

    #Sets attribute fitness
    def setFitnessValue(self,fit):
        self.fitness = fit

    #Sets life
    def setLife(self):
        self.totalLife = self.dna[7]*LIFE_ENEMY

    #Sets how large is the field of view, based on the cromossome
    def setVision(self,spriteEC):
        a,b = pygame.Surface.get_width(spriteEC), pygame.Surface.get_height(spriteEC)
        a=int(a*self.dna[6])
        b=int(b*self.dna[6])
        spriteEC = pygame.transform.scale(spriteEC,(a,b))
        spriteEC = spriteEC.convert_alpha()
        self.coll = collider(spriteEC,self.X,self.Y,self.sizeX,self.sizeY)

    #Resets for next level
    def reset(self,dna,gamemode,spriteEC,Round):
        self.X = randint(LARGURA/2,LARGURA-self.sizeX-33)
        self.Y = randint(ALTURA/2,ALTURA-self.sizeY-33)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.speed = SPEED_ENEMY
        self.life = LIFE_ENEMY
        self.barGreen = 0
        self.barRed = 0
        self.shield_on = False
        self.secondsLeft = 0
        self.dead = False
        self.dead2 = 0
        self.xis=1
        self.yps=1
        self.segundos = 0
        self.pontos=0
        self.coll = 0
        self.round=Round

        #Chromossome
        if gamemode==2:
            self.dna=dna

            self.setLife()
            self.setVision(spriteEC)

        else:
            self.dna=["","","","","","","",""]
            self.coll = collider(spriteEC,self.X,self.Y,self.sizeX,self.sizeY)

        self.fitness=0

        #Movement attributes
        self.crazyness=1
        self.lado=1
        self.direx=1
        self.direy=1
        self.stop=50

        self.proxHP = 0
        self.proxSh = 0
        self.proxPts = 0

    #Tests if got hit by shot
    def testCollisionShot(self,time_passed,shot,player,dead_sound):
        dano = time_passed/2
        if not self.shield_on:
            if pygame.sprite.collide_rect(self, shot):
                if self.life>=0:
                    self.life -= dano
                else:
                    dead_sound.play()
                    player.pontos += 1000
                    self.Dead(player.life,player.pontos)

    #Tests if collided with player
    def testCollisionPlayer(self,player,time_passed):
        pts = time_passed/25
        if pygame.sprite.collide_rect(self, player):
            self.pontos += pts

    #Manages the life bar
    def lifeBar(self,screen):
        self.barGreen = float(self.life)/float(LIFE_ENEMY)
        self.barRed = ((float(LIFE_ENEMY)-float(self.life))/float(LIFE_ENEMY))*(-1)
        if self.life == LIFE_ENEMY:
            pygame.draw.rect(screen, VERDE, (self.X+3,self.Y-12,40,10), 0)
        else:
            if not self.dead:
                pygame.draw.rect(screen, VERDE, (self.X+3,self.Y-12,self.barGreen*40,10), 0)
                pygame.draw.rect(screen, VERMELHO, (self.X+43,self.Y-12,self.barRed*40,10), 0)
            else:
                pygame.draw.rect(screen, VERMELHO, (self.X+3,self.Y-12,40,10), 0)

    #Activates a power
    def activatePower(self,sprite,tipo):
        if tipo == "shield":
            self.changeSprite(sprite)
            self.secondsLeft = SHIELD_TIME
            self.shield_on = True

    #Manages changes by getting the shield
    def onShield(self,sprite):
        self.secondsLeft -= 1
        if self.secondsLeft <= 0:
            self.shield_on = False
            self.changeSprite(sprite)
            
    #Changes sprite
    def changeSprite(self,sprite):
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)            

    #Activates "Dead" state
    def Dead(self,plife,ppontos):
        self.dead = True
        self.dead2 = 1
        self.X,self.Y=1000,1000
        self.setFitness(plife,ppontos)
        
    #Main game function for the enemy
    def update(self,screen,time_passed,spr,cont,healthGroup,placeHP,ptsGroup,placePts,shieldGroup,placeSh,plife,ppontos,player):
        time_passed_seconds = time_passed/1000.0
        distance_moved = time_passed_seconds * self.speed

        self.rect.topleft = (self.X, self.Y)
        self.coll.rect.topleft = (self.X-self.coll.X, self.Y-self.coll.Y)
        screen.blit(self.image, (self.X,self.Y))

        if not player.shield_on:
            self.testCollisionPlayer(player, time_passed)
        
        if SHOW_FOV:
            screen.blit(self.coll.image, (self.X-self.coll.X, self.Y-self.coll.Y))

        if (plife<5) and (not self.dead):
            self.setFitness(plife,ppontos)
        if self.gamemode==2:    
            #Testes de aproximaçao de itens
            if self.dna[2]==1:
                if pygame.sprite.spritecollide(self.coll, healthGroup, False):
                    self.proxHP = 1
                else:
                    self.proxHP = 0
            elif self.dna[2]==2:
                if pygame.sprite.spritecollide(self.coll, healthGroup, False):
                    self.proxHP = 2
                else:
                    self.proxHP = 0
                    
            if self.dna[3]==1:
                if pygame.sprite.spritecollide(self.coll, shieldGroup, False):
                    self.proxSh = 1
                else:
                    self.proxSh = 0
            elif self.dna[3]==2:
                if pygame.sprite.spritecollide(self.coll, shieldGroup, False):
                    self.proxSh = 2
                else:
                    self.proxSh = 0
                    
            if self.dna[4]==1:
                if pygame.sprite.spritecollide(self.coll, ptsGroup, False):
                    self.proxPts = 1
                else:
                    self.proxPts = 0
            elif self.dna[4]==2:
                if pygame.sprite.spritecollide(self.coll, ptsGroup, False):
                    self.proxPts = 2
                else:
                    self.proxPts = 0

            if self.dna[5]==1:
                if pygame.sprite.collide_rect(self.coll, player):
                    self.proxPlayer = 1
                else:
                    self.proxPlayer = 0
        
        
        #Tests colision with items
        #Health
        if pygame.sprite.spritecollide(self, healthGroup, True):
            if self.life+BONUS_HEALTH<=LIFE_ENEMY:
                self.life += BONUS_HEALTH
            else:
                self.life = LIFE_ENEMY
        #Pts
        if pygame.sprite.spritecollide(self, ptsGroup, True):
            self.pontos+=1000
        #Shield
        if pygame.sprite.spritecollide(self, shieldGroup, True):
            self.shield_on = True
            shieldImage = pygame.image.load(SPRITE_ENEMY_SH).convert_alpha()
            x,y = pygame.Surface.get_width(shieldImage), pygame.Surface.get_height(shieldImage)
            x=int(x*MULT_TAM)
            y=int(y*MULT_TAM)
            shieldImage = pygame.transform.scale(shieldImage,(x,y))
            self.activatePower(shieldImage,"shield")


        self.lifeBar(screen)
        
        if not self.dead:

            #Finite state machine behaviours
            if self.gamemode==1:
                if self.round==1:
                    self.movimentacao1(distance_moved,cont)
                elif self.round==2:
                    self.movimentacao2(distance_moved,cont)
                elif self.round==3:
                    self.movimentacao3(distance_moved)
                elif self.round==4:
                    self.movimentacao4(distance_moved,cont)
                elif self.round==5:
                    self.movimentacao5(distance_moved,cont)
                elif self.round==6:
                    self.movimentacao6(distance_moved,cont)
                elif self.round==7:
                    self.movimentacao7(distance_moved)
                elif self.round==8:
                    self.movimentacao8(distance_moved)
                elif self.round==9:
                    self.movimentacao9(distance_moved)
                else:
                    self.movimentacao10(distance_moved,cont)
                    
            #Genetic algorithm behaviours
            elif self.gamemode==2:
                #Movimentation
                if self.proxHP>0 or self.proxSh>0 or self.proxPts>0 or self.proxPlayer>0:
                    if self.proxPlayer==1:
                        self.pegarPlayer(distance_moved,(player.X,player.Y))

                    elif self.proxHP==1:
                        self.pegarHP(distance_moved,placeHP)
                    elif self.proxHP==2:
                        self.evitarHP(distance_moved,placeHP)

                    elif self.proxPts==1:
                        self.pegarPts(distance_moved,placePts)
                    elif self.proxPts==2:
                        self.evitarPts(distance_moved,placePts)

                    elif self.proxSh==1:
                        self.pegarSh(distance_moved,placeSh)
                    elif self.proxSh==2:
                        self.evitarSh(distance_moved,placeSh)

                else:
                    if self.dna[0]==1:
                        self.movimentacao1(distance_moved,cont)
                    elif self.dna[0]==2:
                        self.movimentacao2(distance_moved,cont)
                    elif self.dna[0]==3:
                        self.movimentacao3(distance_moved)
                    elif self.dna[0]==4:
                        self.movimentacao4(distance_moved,cont)
                    elif self.dna[0]==5:
                        self.movimentacao5(distance_moved,cont)
                    elif self.dna[0]==6:
                        self.movimentacao6(distance_moved,cont)
                    elif self.dna[0]==7:
                        self.movimentacao7(distance_moved)
                    elif self.dna[0]==8:
                        self.movimentacao8(distance_moved)
                    elif self.dna[0]==9:
                        self.movimentacao9(distance_moved)
                    elif self.dna[0]==10:
                        self.movimentacao10(distance_moved,cont)
                #Speed
                self.speed = self.dna[1]

        if (cont==1) and (not self.dead):
            self.segundos+=1
            if self.shield_on:
                self.onShield(spr)


    #IA Methods:
    #Movement methods

    #Border collision test
    def hitWallTest(self):
        if self.X>LARGURA-self.sizeX-33:
            self.X-=2
            self.xis=-1
        elif self.X<self.sizeX:
            self.X+=2
            self.xis=1
            
        if self.Y>ALTURA-self.sizeY-33:
            self.Y-=2
            self.yps=1
        elif self.Y<self.sizeY:
            self.Y+=2
            self.yps=-1
            
    #Mov type 1: 'X Axis'
    def movimentacao1(self,distance_moved,cont):
        self.X += self.xis*distance_moved       
        self.hitWallTest()

    #Mov type 2: 'Y Axis'
    def movimentacao2(self,distance_moved,cont):
        self.Y -= self.yps*distance_moved
        self.hitWallTest()
            
    #Mov type 3: 'DVD Screensaver'
    def movimentacao3(self,distance_moved):
        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved
        self.hitWallTest()

    #Mov type 4: 'Crazy DVD screensaver'
    def movimentacao4(self,distance_moved,cont):
        if cont==1:
            self.lado=randint(1,3)
            if self.segundos%2==0:
                self.crazyness=randrange(-1, 2, 2)
            else:
                self.crazyness=1
                
       
        if(self.lado==1):
            self.X += self.xis*distance_moved
            self.Y -= self.yps*distance_moved*self.crazyness
        elif(self.lado==2):
            self.X += self.xis*distance_moved*self.crazyness
            self.Y -= self.yps*distance_moved
        else:
            self.X += self.xis*distance_moved*self.crazyness
            self.Y -= self.yps*distance_moved*self.crazyness
            
        self.hitWallTest()
        
    #Mov type 5:  '50% still 50% DVD'
    def movimentacao5(self,distance_moved,cont):
        if cont==1:
            if self.segundos%2==0:
                self.crazyness=randint(1,100)

        if self.crazyness<=50:
            self.X += self.xis*distance_moved
            self.Y -= self.yps*distance_moved
                
        self.hitWallTest()
        
    #Mov type 6: '50% X 50% Y'
    def movimentacao6(self,distance_moved,cont):
        if cont==1:
            if self.segundos%2==0:
                self.crazyness=randint(1,100)

        if self.crazyness<=50:
            self.X += self.xis*distance_moved
        else:
            self.Y -= self.yps*distance_moved
                
        self.hitWallTest()

    #Mov type 7: 'improved DVD 1'
    def movimentacao7(self,distance_moved):
        if self.xis>=1:
            self.direx=1
        elif self.xis<=-1:
            self.direx=-1
        if self.direx==1:
            self.xis-=0.002*distance_moved
            if (self.xis>-0.05) and (self.xis<0.05):
                self.xis-=0.9*distance_moved
        elif self.direx==-1:
            self.xis+=0.002*distance_moved
            if (self.xis>-0.05) and (self.xis<0.05):
                self.xis+=0.9*distance_moved
                

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved
            
        self.hitWallTest()

    #Mov type 8: 'improved DVD 2'
    def movimentacao8(self,distance_moved):
        if self.yps>=1:
            self.direy=1
        elif self.yps<=-1:
            self.direy=-1
        if self.direy==1:
            self.yps-=0.002*distance_moved
            if (self.yps>-0.05) and (self.yps<0.05):
                self.yps-=0.9*distance_moved
        elif self.direy==-1:
            self.yps+=0.002*distance_moved
            if (self.yps>-0.05) and (self.yps<0.05):
                self.yps+=0.9*distance_moved


        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved
        self.hitWallTest()

    #Mov type 9: 'improved DVD 3'
    def movimentacao9(self,distance_moved):
        if self.xis>=1:
            self.direx=1
        elif self.xis<=-1:
            self.direx=-1
        if self.direx==1:
            self.xis-=0.002*distance_moved
            if (self.xis>-0.05) and (self.xis<0.05):
                self.xis-=0.9*distance_moved
        elif self.direx==-1:
            self.xis+=0.002*distance_moved
            if (self.xis>-0.05) and (self.xis<0.05):
                self.xis+=0.9*distance_moved
            
        if self.yps>=1:
            self.direy=1
        elif self.yps<=-1:
            self.direy=-1
        if self.direy==1:
            self.yps-=0.002*distance_moved
            if (self.yps>-0.05) and (self.yps<0.05):
                self.yps-=0.9*distance_moved
        elif self.direy==-1:
            self.yps+=0.002*distance_moved
            if (self.yps>-0.05) and (self.yps<0.05):
                self.yps+=0.9*distance_moved
        

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved
        self.hitWallTest()

    #Mov type 10: 'Walking'
    def movimentacao10(self,distance_moved,cont):
        if cont==1:
            if self.segundos%2==0:
                self.crazyness=randint(1,100)
                self.stop=randint(1,100)


        if self.stop>30:
            if self.crazyness<=50:
                self.X += self.xis*distance_moved
            else:
                self.Y -= self.yps*distance_moved
                
        self.hitWallTest()

    #Item interaction methods
    #Takes HP
    def pegarHP(self,distance_moved,placeHP):
        itemX=placeHP[0]
        itemY=placeHP[1]
        if self.X<itemX:
            self.xis=1
        elif self.X>itemX:
            self.xis=-1
        if self.Y<itemY:
            self.yps=-1
        elif self.Y>itemY:
            self.yps=1

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved

    #Avoid HP
    def evitarHP(self,distance_moved,placeHP):
        itemX=placeHP[0]
        itemY=placeHP[1]
        if self.X<itemX:
            self.xis=-1
        elif self.X>itemX:
            self.xis=1
        if self.Y<itemY:
            self.yps=1
        elif self.Y>itemY:
            self.yps=-1

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved

    #Takes shield
    def pegarSh(self,distance_moved,placeSh):
        itemX=placeSh[0]
        itemY=placeSh[1]
        if self.X<itemX:
            self.xis=1
        elif self.X>itemX:
            self.xis=-1
        if self.Y<itemY:
            self.yps=-1
        elif self.Y>itemY:
            self.yps=1

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved

    #Avoids shield
    def evitarSh(self,distance_moved,placeSh):
        itemX=placeSh[0]
        itemY=placeSh[1]
        if self.X<itemX:
            self.xis=-1
        elif self.X>itemX:
            self.xis=1
        if self.Y<itemY:
            self.yps=1
        elif self.Y>itemY:
            self.yps=-1

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved

    #Takes points
    def pegarPts(self,distance_moved,placePts):
        itemX=placePts[0]
        itemY=placePts[1]
        if self.X<itemX:
            self.xis=1
        elif self.X>itemX:
            self.xis=-1
        if self.Y<itemY:
            self.yps=-1
        elif self.Y>itemY:
            self.yps=1

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved

    #Avoids points
    def evitarPts(self,distance_moved,placePts):
        itemX=placePts[0]
        itemY=placePts[1]
        if self.X<itemX:
            self.xis=-1
        elif self.X>itemX:
            self.xis=1
        if self.Y<itemY:
            self.yps=1
        elif self.Y>itemY:
            self.yps=-1

        self.X += self.xis*distance_moved
        self.Y -= self.yps*distance_moved

    #Run towards player
    def pegarPlayer(self,distance_moved,placePlayer):
        playerX=placePlayer[0]
        playerY=placePlayer[1]
        if self.X<playerX:
            self.xis=1
        elif self.X>playerX:
            self.xis=-1
        if self.Y<playerY:
            self.yps=-1
        elif self.Y>playerY:
            self.yps=1

        self.X += self.xis*distance_moved/1.4
        self.Y -= self.yps*distance_moved/1.4
