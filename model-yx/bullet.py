# -*- coding: utf-8 -*-
'''
Created on Wed Nov 22 14:37:19 2017

@author: Administrator
'''

import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
#  子弹管理
  def __init__(self,ai_settings,screen,plane):
    
#    在飞船所处位置创建子弹
    super(Bullet,self).__init__()
    self.screen=screen
    
#    在（0，0）创建一个表示子弹的矩形，设置位置
    self.rect =pygame.Rect(0,0,ai_settings.bullet_width,
                           ai_settings.bullet_height)
    self.rect.centerx =plane.rect.centerx
    self.rect.top=plane.rect.top
 
#用小数表示子弹位置
    self.y=float(self.rect.y)
    self.color=ai_settings.bullet_color
    self.speed_factor=ai_settings.bullet_speed_factor
    
    
  def update(self):
#    向上更新子弹
    self.y -=self.speed_factor
    self.rect.y= self.y
    
  def draw_bullet(self):
#    绘制子弹
    pygame.draw.rect(self.screen,self.color,self.rect)
    
    
