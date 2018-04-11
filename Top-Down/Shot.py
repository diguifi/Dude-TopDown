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
from random import randint

#Shot object
class shot(pygame.sprite.Sprite):
    def __init__(self,spriteS,posx,posy,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteS
        self.X = posx+12
        self.Y = posy+12
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.X, self.Y)
        self.speed = SPEED_SHOT
        self.xis = x
        self.yps = y
        self.cantShoot = True

    #Main update function
    def update(self,screen,time_passed):
        time_passed_seconds = time_passed/1000.0
        distance_moved = time_passed_seconds * self.speed

        if self.cantShoot:
            self.X +=self.xis*distance_moved
            self.Y +=self.yps*distance_moved
            self.rect.topleft = (self.X, self.Y)
            screen.blit(self.image, (self.X,self.Y))

        if self.X>LARGURA-32:
            self.cantShoot = False
            self.X = 1000
            self.Y = 1000
        elif self.X<30:
            self.cantShoot = False
            self.X = 1000
            self.Y = 1000
        if self.Y>ALTURA-32:
            self.cantShoot = False
            self.X = 1000
            self.Y = 1000
        elif self.Y<30:
            self.cantShoot = False
            self.X = 1000
            self.Y = 1000
