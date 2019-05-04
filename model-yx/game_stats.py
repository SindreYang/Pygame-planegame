# -*- coding: utf-8 -*-
'''
Created on Fri Nov 24 15:16:06 2017

@author: Administrator
'''

class GameStats():
#  统计信息
  def __init__(self,ai_settings):
#    初始化统计信息
    self.ai_settings = ai_settings
    self.reset_stats()
    
    
    
#    游戏启动是处于false状态
    self.game_active=False
    
    
  def reset_stats(self):
    
#     初始化在游戏中变化的统计信息
    self.planes_left=self.ai_settings.plane_limit
    
    
    
    
  
    