# -*- coding: utf-8 -*-
'''
Created on Mon Nov 20 00:09:42 2017

@author: Administrator
'''

import pygame
from settings import Settings
from plane import Plane
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():
    #初始化游戏
    pygame.init()
    ai_settings=Settings()
    
    #初始化背景
    #screen=pygame.display.set_mode((1200,800))
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("model-yx")
    #初始化游戏窗口
#  创建按钮
    play_button=Button(ai_settings,screen,"play")
  
  
  
    #创建飞机
    plane=Plane(screen,ai_settings)
#    创建储存子弹的编组
    bullets = Group()
#    创建敌人编组
    enemys=Group()
    
    
    
    #设置背景色
#    bg_color=(230,230,231)
    
    
#    创建一个敌人
 #   enemy=Enemy(ai_settings,screen)
#    创建一群敌人
    gf.create_fleet(ai_settings,screen,plane,enemys)
    
    
    
    
#    创建一个用于储存游戏统计信息的实例
    stats=GameStats(ai_settings)
    
    
    
    #开始游戏循环
    while True:
      gf.check_events(ai_settings,screen,stats,play_button,plane,enemys,bullets)
      
#         #监视键盘和鼠标事件
#         '''for event in pygame.event.get():
#             if event.type==pygame.QUIT:  #退出事件
#                 sys.exit()'''
   
      if stats.game_active:
        plane.update()    
#        bullets.update()
#         删除已经消失的子弹 防止内存膨胀
#         for bullet in bullets.copy():
#           if bullet.rect.bottom<=0:
#             bullets.remove(bullet)
#移动到 update_bullets(bullets)
  
        gf.update_bullets(ai_settings,screen,plane,enemys,bullets)
        gf.update_enemys(ai_settings,stats,screen,plane,enemys,bullets)
#         print(len(bullets))
#             检查子弹是否真的删除
         
                 
#         #重绘屏幕
#         screen.fill(bg_color)
#         screen.fill(ai_settings.bg_color)
#         plane.blitme()
#         #绘制飞机
#         
#         
#         # 更新屏幕
#         pygame.display.flip()
      gf.update_screen(ai_settings,screen,stats,plane,enemys,bullets,play_button)
run_game()
