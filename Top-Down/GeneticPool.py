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
from random import randint,uniform
from Configs import *

class geneticPool():
    def __init__(self,enemiesData):
        self.enemiesData = enemiesData
        self.tam = len(self.enemiesData)
        self.enemiesDataSelecteds = []
        self.somaFit = 0
        self.somaProbs = 0
        self.mutationChance = MUTATION_RATE
        
        self.selecao()
        self.crossover()
        self.mutacao()
            
    def sortFitness(self):
        self.enemiesData=sorted(self.enemiesData, key=lambda fit: fit[1])

    def selecao(self):
        self.sortFitness()
        self.somaFitness()
        y=0
        while y<2:
            pick    = uniform(0, 1)
            current = 0
            x=0
            while x < self.tam and y<2:
                current += float(self.enemiesData[x][1])/self.somaFit
                if current > pick and y<2:
                    self.enemiesDataSelecteds.append(self.enemiesData[x])
                    self.enemiesData.pop(x)
                    self.tam = len(self.enemiesData)
                    y+=1
                x+=1
            

    def crossover(self):
        #Adicionar os melhores
        novoRandom = [[randint(1,10),randint(70,130),randint(0,2),randint(0,2),randint(0,2),randint(0,1),round(uniform(0.5, 2),2),round(uniform(0.5, 2),2)],0,0]
        self.enemiesData[2] = novoRandom
        self.enemiesData.append(self.enemiesDataSelecteds[1])
        self.enemiesData.append(self.enemiesDataSelecteds[0])
        
        #Aplicar cruzamento em um ponto
        self.enemiesData[0][0]=[self.enemiesData[3][0][0],self.enemiesData[3][0][1],self.enemiesData[3][0][2],self.enemiesData[3][0][3],self.enemiesData[4][0][4],self.enemiesData[4][0][5],self.enemiesData[4][0][6],self.enemiesData[4][0][7]]
        self.enemiesData[1][0]=[self.enemiesData[4][0][0],self.enemiesData[4][0][1],self.enemiesData[4][0][2],self.enemiesData[4][0][3],self.enemiesData[3][0][4],self.enemiesData[3][0][5],self.enemiesData[3][0][6],self.enemiesData[3][0][7]]

    def mutacao(self):
        x=0
        while x<2:
            y=0
            while y<8:
                valorRandom = uniform(0, 1)
                if valorRandom<=self.mutationChance:
                    if y==0:
                        self.enemiesData[x][0][y]=randint(1,10)
                    elif y==1:
                        self.enemiesData[x][0][y]=randint(70,130)
                    elif y==2:
                        self.enemiesData[x][0][y]=randint(0,2)
                    elif y==3:
                        self.enemiesData[x][0][y]=randint(0,2)
                    elif y==4:
                        self.enemiesData[x][0][y]=randint(0,2)
                    elif y==5:
                        self.enemiesData[x][0][y]=randint(0,1)
                    elif y==6:
                        self.enemiesData[x][0][y]=round(uniform(0.5, 2),2)
                    elif y==7:
                        self.enemiesData[x][0][y]=round(uniform(0.5, 2),2)
                y+=1
            x+=1
            

    def somaFitness(self):
        x=0
        while x<self.tam:
            self.somaFit += self.enemiesData[x][1]
            x+=1
        self.somaFit=float(self.somaFit)

    def reset(self):
        self.enemiesData = []
        self.tam = len(self.enemiesData)
        self.enemiesDataSelecteds = []
        self.somaFit = 0
        self.somaProbs = 0
