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
    def __init__(self, screen, previousData, newData, chosenOnes, enemiesSpritesList, fovSprite):
        self.animationSpeed = 20
        self.animationPart = 1
        self.timeCount = 0
        self.previousData = previousData
        self.newData = newData
        self.chosenOnes = chosenOnes
        self.chosenOnesSprites = [0,0]
        self.chosenOnesFov = [0,0]
        self.fovSprite = fovSprite
        self.enemiesSpritesList = enemiesSpritesList
        self.enemiesSpritesList2 = enemiesSpritesList
        self.enemiesSpritesList3 = enemiesSpritesList
        self.enemiesSpritesList4 = enemiesSpritesList
        self.screenCenterX = screen.get_rect().centerx
        self.screenCenterY = screen.get_rect().centery
        self.listPositions = [[((LARGURA/6)*1, (ALTURA/9)*2),
                               ((LARGURA/6)*1, (ALTURA/10)*9),
                               ((LARGURA/8)*3, (ALTURA/10)*4),
                               ((LARGURA/8)*5, (ALTURA/10)*4),
                               ((LARGURA/8)*3, (ALTURA/11)*7),
                               ((LARGURA/8)*5, (ALTURA/11)*7)],
                              [((LARGURA/6)*2, (ALTURA/9)*2),
                               ((LARGURA/6)*2, (ALTURA/10)*9),
                               ((LARGURA/8)*3, (ALTURA/10)*4),
                               ((LARGURA/8)*5, (ALTURA/10)*4),
                               ((LARGURA/8)*3, (ALTURA/11)*7),
                               ((LARGURA/8)*5, (ALTURA/11)*7)],
                              [((LARGURA/6)*3, (ALTURA/9)*2),
                               ((LARGURA/6)*3, (ALTURA/10)*9),
                               ((LARGURA/8)*3, (ALTURA/10)*4),
                               ((LARGURA/8)*5, (ALTURA/10)*4),
                               ((LARGURA/8)*3, (ALTURA/11)*7),
                               ((LARGURA/8)*5, (ALTURA/11)*7)],
                              [((LARGURA/6)*4, (ALTURA/9)*2),
                               ((LARGURA/6)*4, (ALTURA/10)*9),
                               ((LARGURA/8)*3, (ALTURA/10)*4),
                               ((LARGURA/8)*5, (ALTURA/10)*4),
                               ((LARGURA/8)*3, (ALTURA/11)*7),
                               ((LARGURA/8)*5, (ALTURA/11)*7)],
                              [((LARGURA/6)*5, (ALTURA/9)*2),
                               ((LARGURA/6)*5, (ALTURA/10)*9),
                               ((LARGURA/8)*3, (ALTURA/10)*4),
                               ((LARGURA/8)*5, (ALTURA/10)*4),
                               ((LARGURA/8)*3, (ALTURA/11)*7),
                               ((LARGURA/8)*5, (ALTURA/11)*7)]]

        self.getChosenOnesSprites()

    def getChosenOnesSprites(self):
        i = 0
        j = 0
        while j < 2:
            while i < len(self.previousData):
                if self.previousData[i][0] == self.chosenOnes[j][0]:
                    self.chosenOnesSprites[j] = i

                i+=1

            i=0
            j+=1

        self.chosenOnesFov[0] = self.chosenOnesSprites[0]
        self.chosenOnesFov[1] = self.chosenOnesSprites[1]

    def update(self, pygame, screen, pause_ticks):
        if self.timeCount < 7600:
            self.timeCount += pause_ticks

        if self.timeCount >= 1500:
            self.animationPart = 1
        if self.timeCount >= 3500:
            self.animationPart = 2
        if self.timeCount >= 5500:
            self.animationPart = 3
        if self.timeCount >= 7000:
            self.animationPart = 4

        
        screen.fill(PRETO)

        font = pygame.font.Font(None, 48)
        text = font.render("CROSSOVER ANIMATION", 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.screenCenterY - 200
        screen.blit(text, textpos)

        if self.animationPart >= 1:
            self.drawBefore(pygame, screen)
        if self.animationPart >= 2:
            self.drawSelected(pygame, screen)
        if self.animationPart >= 3:
            self.drawChildren(pygame, screen)
        if self.animationPart >= 4:
            self.drawAfter(pygame, screen)

        pygame.display.flip()

    def drawBefore(self, pygame, screen):
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[0],(30,30)), self.listPositions[0][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[1],(30,30)), self.listPositions[1][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[2],(30,30)), self.listPositions[2][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[3],(30,30)), self.listPositions[3][0])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList[4],(30,30)), self.listPositions[4][0])

        font = pygame.font.Font(None, 17)
        text = font.render("Before: "+str(self.previousData), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.listPositions[0][0][1] + 40
        screen.blit(text, textpos)


    def drawSelected(self, pygame, screen):
        screen.blit(pygame.transform.scale(self.enemiesSpritesList3[self.chosenOnesSprites[0]],(30,30)), self.listPositions[self.chosenOnesSprites[0]][2])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList3[self.chosenOnesSprites[1]],(30,30)), self.listPositions[self.chosenOnesSprites[1]][3])

        screen.blit(pygame.transform.scale(self.fovSprite,(30,30)), self.listPositions[self.chosenOnesFov[0]][0])
        screen.blit(pygame.transform.scale(self.fovSprite,(30,30)), self.listPositions[self.chosenOnesFov[1]][0])

        font = pygame.font.Font(None, 17)
        text = font.render("Selected for crossover!", 1, VERMELHO)
        textpos = text.get_rect()
        textpos.centerx = self.listPositions[self.chosenOnesFov[0]][0][0] + 15
        textpos.centery = self.listPositions[self.chosenOnesFov[0]][0][1] + 55
        screen.blit(text, textpos)
        text = font.render("Selected for crossover!", 1, VERMELHO)
        textpos = text.get_rect()
        textpos.centerx = self.listPositions[self.chosenOnesFov[1]][0][0] + 15
        textpos.centery = self.listPositions[self.chosenOnesFov[1]][0][1] + 55
        screen.blit(text, textpos)

        text = font.render(str(self.chosenOnes[0]), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.listPositions[0][2][0] + 15
        textpos.centery = self.listPositions[0][2][1] + 40
        screen.blit(text, textpos)
        text = font.render(str(self.chosenOnes[1]), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.listPositions[0][3][0] + 15
        textpos.centery = self.listPositions[0][3][1] + 40
        screen.blit(text, textpos)
        text = font.render("Parents", 1, VERMELHO)
        textpos = text.get_rect()
        textpos.centerx = (LARGURA/2)
        textpos.centery = self.listPositions[0][3][1] + 40
        screen.blit(text, textpos)

    def drawChildren(self, pygame, screen):
        screen.blit(pygame.transform.scale(self.enemiesSpritesList4[0],(30,30)), self.listPositions[0][4])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList4[1],(30,30)), self.listPositions[1][5])

        font = pygame.font.Font(None, 17)
        text = font.render(str(self.newData[0][0]), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.listPositions[0][4][0] + 15
        textpos.centery = self.listPositions[0][4][1] + 40
        screen.blit(text, textpos)
        text = font.render(str(self.newData[1][0]), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.listPositions[0][5][0] + 15
        textpos.centery = self.listPositions[0][5][1] + 40
        screen.blit(text, textpos)
        text = font.render("Children", 1, VERMELHO)
        textpos = text.get_rect()
        textpos.centerx = (LARGURA/2)
        textpos.centery = self.listPositions[0][4][1] + 40
        screen.blit(text, textpos)

    def drawAfter(self, pygame, screen):
        self.chosenOnesSprites[0] = 3
        self.chosenOnesSprites[1] = 4
        
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[0],(30,30)), self.listPositions[0][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[1],(30,30)), self.listPositions[1][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[2],(30,30)), self.listPositions[2][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[3],(30,30)), self.listPositions[3][1])
        screen.blit(pygame.transform.scale(self.enemiesSpritesList2[4],(30,30)), self.listPositions[4][1])
        
        font = pygame.font.Font(None, 17)
        text = font.render("After: "+str(self.newData), 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.listPositions[0][1][1] + 40
        screen.blit(text, textpos)

        font = pygame.font.Font(None, 25)   
        text = font.render("Press space to continue", 1, BRANCO)
        textpos = text.get_rect()
        textpos.centerx = self.screenCenterX
        textpos.centery = self.screenCenterY + 250
        screen.blit(text, textpos)
