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
    def __init__(self, previousData, newData):
        self.previousData = previousData
        self.newData = newData

    def update(self, pygame, screen):
        screen.fill(BRANCO)
        font = pygame.font.Font(None, 48)
        text = font.render("CROSSOVER ANIMATION", 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery - 50
        screen.blit(text, textpos)
        font = pygame.font.Font(None, 36)
        text = font.render("soon there will be an animation here", 1, (10,10,10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery
        screen.blit(text, textpos)
        font = pygame.font.Font(None, 17)
        text = font.render("Before:"+str(self.previousData), 1, (10,10,10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery + 50
        screen.blit(text, textpos)
        text = font.render("After:"+str(self.newData), 1, (10,10,10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery + 100
        screen.blit(text, textpos)
        font = pygame.font.Font(None, 25)
        text = font.render("Press space to continue", 1, (10,10,10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        textpos.centery = screen.get_rect().centery + 150
        screen.blit(text, textpos)
        pygame.display.flip()
