# -*- coding: utf-8 -*-
'''
Created on Mon Nov 20 00:09:42 2017

@author: Administrator
'''
import pygame
class Settings():
  #存储游戏设置
  def __init__(self):
    #初始化游戏设置
    #屏幕设置
    self.screen_width=1200
    self.screen_height=768
    #self.bg_color=(84,119,161)
    self.background_image=pygame.image.load('images/sky.jpg')
    
    #设置飞船速度
    self.plane_speed_factor = 1.6
    self.plane_limit =3
    
#    子弹设置
    self.bullet_speed_factor =1
    self.bullet_width=300
    self.bullet_height=150
    self.bullet_color=0,60,60
    self.bullet_allowed=4
#    敌人速度设置
    self.enemy_speed_factor =1
    self.fleet_drop_speed =1
    #下移速度
    #左右移动方向，-1表示左移动 1代表右移动
    self.fleet_direction=1
    
    
    
    