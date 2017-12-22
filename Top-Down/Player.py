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
from Shot import shot
from random import randint
p = os.getcwd()

class dude(pygame.sprite.Sprite):
    def __init__(self,spriteP,spriteShot):
        pygame.sprite.Sprite.__init__(self)
        self.spriteInicial = spriteP
        self.image = spriteP
        self.spriteShot = spriteShot
        self.sizeX=pygame.Surface.get_width(self.image)
        self.sizeY=pygame.Surface.get_height(self.image)
        self.X = randint(self.sizeX,LARGURA/2)
        self.Y = randint(self.sizeY,ALTURA/2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.speed = SPEED_PLAYER
        self.life = LIFE_PLAYER
        self.barGreen = 0
        self.barRed = 0
        self.pontos = 0
        self.ammo = AMMO_PLAYER
        self.shield_on = False
        self.secondsLeft = 0
        #animaçao
        self.contCont = 0
        self.animCont = 0
        self.QUANT_IMAGES = 4
        self.listDudeRight = []
        self.listDudeLeft = []
        self.listDudeShRight = []
        self.listDudeShLeft = []
        self.animation()
        self.auxDir=0

    def getLife(self):
        return self.life
    
    def animation(self):
        global p
        #lendo as imagens dos personagens para direita...
        for i in range(self.QUANT_IMAGES):
         image = pygame.image.load(p+'/images/sprites/dude/dudeD'+str(i)+'.png').convert_alpha()
         x,y = pygame.Surface.get_width(image), pygame.Surface.get_height(image)
         x=int(x*MULT_TAM)
         y=int(y*MULT_TAM)
         image = pygame.transform.scale(image,(x,y))        
         self.listDudeRight.append(image)
          
        #lendo as imagens dos personagens andando para esquerda...
        for i in range(self.QUANT_IMAGES):
         image = pygame.image.load(p+'/images/sprites/dude/dudeE'+str(i)+'.png').convert_alpha()
         x,y = pygame.Surface.get_width(image), pygame.Surface.get_height(image)
         x=int(x*MULT_TAM)
         y=int(y*MULT_TAM)
         image = pygame.transform.scale(image,(x,y))
         self.listDudeLeft.append(image)
         
         
        #lendo as imagens dos personagens andando para cima...
        for i in range(self.QUANT_IMAGES):
         image = pygame.image.load(p+'/images/sprites/dude/dude_shD'+str(i)+'.png').convert_alpha()
         x,y = pygame.Surface.get_width(image), pygame.Surface.get_height(image)
         x=int(x*MULT_TAM)
         y=int(y*MULT_TAM)
         image = pygame.transform.scale(image,(x,y))
         self.listDudeShRight.append(image)
         
          
        #lendo as imagens dos personagens andando para baixo...
        for i in range(self.QUANT_IMAGES):
         image = pygame.image.load(p+'/images/sprites/dude/dude_shE'+str(i)+'.png').convert_alpha()
         x,y = pygame.Surface.get_width(image), pygame.Surface.get_height(image)
         x=int(x*MULT_TAM)
         y=int(y*MULT_TAM)
         image = pygame.transform.scale(image,(x,y))
         self.listDudeShLeft.append(image)

    def reset(self):
        self.image = self.spriteInicial
        self.X = randint(self.sizeX,LARGURA/2)
        self.Y = randint(self.sizeY,ALTURA/2)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.speed = SPEED_PLAYER
        self.life = LIFE_PLAYER
        self.barGreen = 0
        self.barRed = 0
        self.ammo = AMMO_PLAYER
        self.shield_on = False
        self.secondsLeft = 0

    def testCollisionShot(self,shot,enemy,time_passed):
        pts = time_passed/2
        tam=len(enemy)
        x=0
        while x<tam:
            if pygame.sprite.collide_rect(shot, enemy[x]):
                self.pontos += pts
            x+=1

    def testCollision(self,enemy,time_passed,dead_sound):
        dano = time_passed/3
        if not self.shield_on:
            if pygame.sprite.collide_rect(self, enemy):
                self.life -= dano
                if self.life<2:
                    dead_sound.play()

    def lifeBar(self,screen):
        self.barGreen = float(self.life)/float(LIFE_PLAYER)
        self.barRed = ((float(LIFE_PLAYER)-float(self.life))/float(LIFE_PLAYER))*(-1)
        if self.life == LIFE_PLAYER:
            pygame.draw.rect(screen, VERDE, (self.X-5,self.Y-12,40,10), 0)
        else:
            if self.life>5:
                pygame.draw.rect(screen, VERDE, (self.X-5,self.Y-12,self.barGreen*40,10), 0)
                pygame.draw.rect(screen, VERMELHO, (self.X+35,self.Y-12,self.barRed*40,10), 0)
            else:
                pygame.draw.rect(screen, VERMELHO, (self.X-5,self.Y-12,40,10), 0)

    def activatePower(self,sprite,tipo):
        if tipo == "shield":
            self.changeSprite(sprite)
            self.secondsLeft = SHIELD_TIME
            self.shield_on = True

    def onShield(self,sprite):
        self.secondsLeft -= 1
        if self.secondsLeft <= 0:
            self.shield_on = False
            self.changeSprite(sprite)
            

    def changeSprite(self,sprite):
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        
    
    def update(self,xis,yps,screen,time_passed,spr,cont,lista_inimigos,shot_x,shot_y,dead_sound):
        time_passed_seconds = time_passed/1000.0
        distance_moved = time_passed_seconds * self.speed #Distancia = tempo * velocidade
        
        self.X +=xis*distance_moved
        self.Y +=yps*distance_moved
        
        self.rect.topleft = (self.X, self.Y)

        self.lifeBar(screen)

        self.testCollision(lista_inimigos[0],time_passed,dead_sound)
        self.testCollision(lista_inimigos[1],time_passed,dead_sound)
        self.testCollision(lista_inimigos[2],time_passed,dead_sound)
        self.testCollision(lista_inimigos[3],time_passed,dead_sound)
        self.testCollision(lista_inimigos[4],time_passed,dead_sound)
        
        
        if self.X>LARGURA-self.sizeX-33:
            self.X-=2*distance_moved

        elif self.X<self.sizeX:
            self.X+=2*distance_moved

        if self.Y>ALTURA-self.sizeY-33:
            self.Y-=2*distance_moved

        elif self.Y<self.sizeY:
            self.Y+=2*distance_moved

        if shot_x==1:
            screen.blit(self.spriteShot, (self.X+self.sizeX,self.Y+self.sizeY/2))
        elif shot_x==-1:
            screen.blit(self.spriteShot, (self.X-8,self.Y+self.sizeY/2))
        elif shot_y==1:
            screen.blit(self.spriteShot, (self.X+self.sizeX/2,self.Y+self.sizeY))
        elif shot_y==-1:
            screen.blit(self.spriteShot, (self.X+self.sizeX/2,self.Y-10))

        if not self.shield_on:    
            if xis==1:
                screen.blit(self.listDudeRight[self.animCont], (self.X,self.Y))
                self.auxDir=1
            elif xis==-1 or (yps==1 or yps==-1):
                screen.blit(self.listDudeLeft[self.animCont], (self.X,self.Y))
                self.auxDir=0
            else:
                if self.auxDir==0:
                    screen.blit(self.listDudeLeft[0], (self.X,self.Y))
                else:
                    screen.blit(self.listDudeRight[0], (self.X,self.Y))
        else:
            if xis==1:
                screen.blit(self.listDudeShRight[self.animCont], (self.X,self.Y))
                self.auxDir=1
            elif xis==-1:
                screen.blit(self.listDudeShLeft[self.animCont], (self.X,self.Y))
                self.auxDir=0
            else:
                if self.auxDir==0:
                    screen.blit(self.listDudeShLeft[0], (self.X,self.Y))
                else:
                    screen.blit(self.listDudeShRight[0], (self.X,self.Y))

        self.contCont+=distance_moved

        if self.contCont>20:
            self.animCont+=1
            self.contCont=0
 
        if self.animCont > self.QUANT_IMAGES-1:
           self.animCont = 0

        if cont==1:
            if self.shield_on:
                self.onShield(spr)

    
