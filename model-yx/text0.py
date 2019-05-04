# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:50:59 2017

@author: Administrator
"""
from settings import Settings
from plane import Plane
#import game_functions as gf
from pygame.sprite import Group
#from game_stats import GameStats
from button import Button
import pygame
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((1200,800))
    bg_colorygame=(230,230,230)
    pygame.display.set_caption("model-yx")
    play_button=Button(ai_settings,screen,"play")
    plane=Plane(screen,ai_settings)
    bullets = Group()
    enemys=Group()
    
    while True:
            screen.fill(bg_colorygame)
            pygame.display.flip()
run_game()