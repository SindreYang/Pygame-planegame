# -*- coding: utf-8 -*-
'''
Created on Mon Nov 20 01:10:32 2017

@author: Administrator
'''

import pygame
class Plane():
  def __init__(self,screen,ai_settings):
    #初始化飞机位置
    self.screen=screen
    self.ai_settings=ai_settings

    #加载非常图像
    self.image=pygame.image.load('images/plane.png')
    self.rect=self.image.get_rect()
    self.screen_rect=screen.get_rect()

    #将飞机放在中间位置
    self.rect.centerx=self.screen_rect.centerx
    self.rect.bottom=self.screen_rect.bottom

    #在属性center中储存小数值
    self.center =float(self.rect.centerx)

    #移动标志
    self.moving_right=False
    self.moving_left=False
    
    
    
    
  def update(self):
    #根据移动标志调整位置
    if self.moving_right and self.rect.right<self.screen_rect.right:
      #self.rect.centerx +=1
      self.center += self.ai_settings.plane_speed_factor
    if self.moving_left and self.rect.left>0:
      #self.rect.centerx -=1  
      self.center -= self.ai_settings.plane_speed_factor
      
#    根据center更新centerx
    self.rect.centerx =self.center
    
    
    
    
    
    
    
  def center_plane(self):
#    让飞船居中
    self.center=self.screen_rect.centerx
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
  def blitme(self):
    #绘制飞船
    self.screen.blit(self.image,self.rect)