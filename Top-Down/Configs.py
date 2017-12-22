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

p = os.getcwd()

#CONFIGS DO PLAYER
SPEED_PLAYER = 150
LIFE_PLAYER = 1000
AMMO_PLAYER = 25
MULTI_SHOTS = True
SPEED_SHOT = 400
SHIELD_TIME = 10
SPRITE_PLAYER = p+'/images/sprites/dude/dudeE0.png'
SPRITE_PLAYER_SH = p+'/images/sprites/dude/dude_shE0.png'
SPRITE_SHOT = p+'/images/sprites/shot.png'
SPRITE_AMMO = p+'/images/sprites/ammo.png'

#CONFIGS DOS INIMIGOS
SPEED_ENEMY = 100
LIFE_ENEMY = 600
MUTATION_RATE = 0.01
SHOW_FOV = False
SPRITE_ENEMY = p+'/images/sprites/enemy.png'
SPRITE_ENEMY2 = p+'/images/sprites/enemy2.png'
SPRITE_ENEMY3 = p+'/images/sprites/enemy3.png'
SPRITE_ENEMY4 = p+'/images/sprites/enemy4.png'
SPRITE_ENEMY5 = p+'/images/sprites/enemy5.png'
SPRITE_ENEMYC = p+'/images/sprites/enemyc.png'
SPRITE_ENEMY_SH = p+'/images/sprites/enemy_sh.png'

#CONFIGS DO MAPA
ICONE = p+'/images/sprites/icon.png'
BACKGROUND = p+'/images/bg/dungeon2.png'
SPRITE_SHIELD = p+'/images/sprites/shield.png'
SPRITE_HEALTH = p+'/images/sprites/health.png'
SPRITE_POINTS = p+'/images/sprites/points.png'
SPRITE_ARROW = p+'/images/sprites/arrow.png'
BACK_MUSIC = p+'/audio/stayingAlive.mp3'
SHOOT_SOUND = p+'/audio/shoot.wav'
POWERUP_SOUND = p+'/audio/powerup.wav'
DEAD_SOUND = p+'/audio/dead.wav'
RELOAD_SOUND = p+'/audio/reload.wav'
SHIELD_SOUND = p+'/audio/shield.wav'
FPS = 60
MULT_TAM = 1.5
BONUS_AMMO = 25
BONUS_HEALTH = 500
BONUS_POINTS = 500
ALTURA = 480          #Colisao
LARGURA = 940         #Colisao
ALTURA2 = 540         #Tela
LARGURA2 = 940        #Tela

#CONFIGS CORES
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
