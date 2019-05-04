# -*- coding: utf-8 -*-
'''
Created on Thu Nov 23 18:45:20 2017

@author: Administrator
'''

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
#  表示单个敌人的类
  def __init__(self,ai_settings,screen):
#    初始化并设置初始位置
    super(Enemy,self).__init__()
    
      #初始化位置
    self.screen=screen
    self.ai_settings=ai_settings
    
    #加载非常图像
    self.image=pygame.image.load('images/enemy.tga')
    self.rect=self.image.get_rect()
    
    
    #放在左上位置
    self.rect.x=self.rect.width
    self.rect.y=self.rect.height
    
    #在属性center中储存小数值
    self.x =float(self.rect.x)
    
  def blitme(self):
#    绘制敌人
    self.screen.blit(self.image,self.rect)
    
    
  def update(self):
#    向左右移动敌人
    self.x+=(self.ai_settings.enemy_speed_factor*
             self.ai_settings.fleet_direction)
    self.rect.x =self.x
    
  def check_edges(self):
#    敌人位于屏幕边缘，就返回true
    screen_rect=self.screen.get_rect()
    if self.rect.right>=screen_rect.right:
      return True
    elif self.rect.left<=0:
      return True
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    