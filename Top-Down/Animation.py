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
import os
from Configs import *

class animation():
    def __init__(self, screen, previousData, newData, enemiesSpritesList):
        self.previousData = previousData
        self.newData = newData
        self.enemiesSpritesList = enemiesSpritesList
        self.enemiesSpritesList2 = enemiesSpritesList
        self.screenCenterX = screen.get_rect().centerx
        self.screenCenterY = screen.get_rect().centery
        self.listPositions = [[((LARGURA/6)*1, (ALTURA/8)*3),
                               ((LARGURA/6)*1, (ALTURA/8)*6)],
                              [((LARGURA/6)*2, (ALTURA/8)*3),
                               ((LARGURA/6)*2, (ALTURA/8)*6)],
                              [((LARGURA/6)*3, (ALTURA/8)*3),
                               ((LARGURA/6)*3, (ALTURA/8)*6)],
                              [((LARGURA/6)*4, (ALTURA/8)*3),
                               ((LARGURA/6)*4, (ALTURA/8)*6)],
                              [((LARGURA/6)*5, (ALTURA/8)*3),
                               ((LARGURA/6)*5, (ALTURA/8)*6)]]

    def update(self, pygame, screen):
        screen.fill(PRETO)

        screen.blit(pygame.transform.scale(self.enemiesSpritesList[0],(30,30)), self.listPositions[0][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[1],(30,30)), self.listPositions[1][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[2],(30,30)), self.listPositions[2][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[3],(30,30)), self.listPositions[3][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[4],(30,30)), self.listPositions[4][0])

        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[0],(30,30)), self.listPositions[0][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[1],(30,30)), self.listPositions[1][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[2],(30,30)), self.listPositions[2][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[3],(30,30)), self.listPositions[3][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[4],(30,30)), self.listPositions[4][1])
        
        font = pygame.font.Font(None, 48)
        text = font.render("CROSSOVER ANIMATION", 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.screenCenterY - 200
        screen.blit(text, textpos)
        font = pygame.font.Font(None, 36)
        text = font.render("soon there will be an animation here", 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.screenCenterY - 150
        screen.blit(text, textpos)
        font = pygame.font.Font(None, 17)
        text = font.render("Before:"+str(self.previousData), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = (ALTURA/8)*3 + 40
        screen.blit(text, textpos)
        text = font.render("After:"+str(self.newData), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = (ALTURA/8)*6 + 40
        screen.blit(text, textpos)
        font = pygame.font.Font(None, 25)
        text = font.render("Press space to continue", 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.screenCenterY + 200
        screen.blit(text, textpos)
        pygame.display.flip()
