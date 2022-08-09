# -*- coding: utf-8 -*-
'''
Created on Mon Nov 20 18:14:32 2017

@author: Administrator
'''

import sys
import pygame
from bullet import Bullet
from enemy import Enemy
from time import sleep #暂停游戏

def check_keydown_events(event,ai_settings,screen,plane,bullets):
  if event.key==pygame.K_RIGHT:
        plane.moving_right=True
  elif event.key==pygame.K_LEFT:
        plane.moving_left=True 
        
  elif event.key==pygame.K_SPACE:
    
    fire_bullet(ai_settings,screen,plane,bullets)
#    if len(bullets)<ai_settings.bullet_allowed:
#      new_bullet =Bullet(ai_settings,screen,plane)
#      bullets.add(new_bullet)
#   移动到 fire_bullet(ai_settings,screen,plane,bullets)
  elif event.key==pygame.K_q:
    pygame.quit()
    sys.exit()
	
  
    
        
        
def check_keyup_events(event,plane):
  if event.key==pygame.K_RIGHT:
        plane.moving_right=False
  elif event.key==pygame.K_LEFT:
        plane.moving_left=False
        
def check_events(ai_settings,screen,stats,play_button,plane,enemys,bullets):
  #响应按键和鼠标事件
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      pygame.quit()
      sys.exit()
	  
    elif event.type==pygame.MOUSEBUTTONDOWN:
		mouse_x,mouse_y=pygame.mouse.get_pos()
		check_play_button(ai_settings,screen,stats,play_button,plane,enemys,bullets,mouse_x,mouse_y)
		
    elif event.type==pygame.KEYDOWN:
      check_keydown_events(event,ai_settings,screen,plane,bullets)
 
#      if event.key==pygame.K_RIGHT:
#        plane.moving_right=True
#      elif event.key==pygame.K_LEFT:
#        plane.moving_left=True 
        
        
    elif event.type==pygame.KEYUP:
		check_keyup_events(event,plane)
#      if event.key==pygame.K_RIGHT:
#        plane.moving_right=False
#      elif event.key==pygame.K_LEFT:
#        plane.moving_left=False
      
      
def check_play_button(ai_settings,screen,stats,play_button,plane,enemys,bullets,mouse_x,mouse_y):
	# 玩家单机在play按钮 ，执行
	button_clicked= play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		pygame.mouse.set_visible(False)#隐藏光标
		stats.reset_stats()#重置游戏
		stats.game_active=True  
		
		
    # 清空敌人和子弹列表
		enemys.empty()
		bullets.empty()
		
		# 创建一群新敌人，并将飞船重置到屏幕中央
		create_fleet(ai_settings,screen,plane,enemys)
		plane.center_plane()
		
      
      
      
def update_screen(ai_settings,screen,stats,plane,enemys,bullets,play_button):
  #更新屏幕图像
  #screen.fill(ai_settings.bg_color)
  screen.blit(ai_settings.background_image, (0, 0))
#  重绘所有子弹
  for bullet in bullets.sprites():
    bullet.draw_bullet()
    
    
  plane.blitme()
         #绘制飞机
  enemys.draw(screen)
#          绘制敌人
         
#  如果游戏处于非活动状态，绘制play按钮
  if not stats.game_active:
    play_button.draw_button()
         
         
         # 更新屏幕
  pygame.display.flip()
  








  
def update_bullets(ai_settings,screen,plane,enemys,bullets):
  
#更新子弹位置，删除子弹

  #更新子弹位置
  
  bullets.update()
#删除消失子弹
  for bullet in bullets.copy():
           if bullet.rect.bottom<=0:
             bullets.remove(bullet)
             
  check_bullet_enemy_collisions(ai_settings,screen,plane,enemys,bullets)
#检查是否有子弹击中敌人
#             如果是，删除相应子弹和敌人
#  collsions=pygame.sprite.groupcollide(bullets,enemys,True,True)
#  
#  
#  检验敌人是否为空 
#  if len(enemys)==0:
#    删除编组剩余精灵
#    bullets.empty()
#    create_fleet(ai_settings,screen,plane,enemys)
    

def check_bullet_enemy_collisions(ai_settings,screen,plane,enemys,bullets):
#  响应子弹与敌人碰撞
 
#检查是否有子弹击中敌人
#             如果是，删除相应子弹和敌人
  collisions=pygame.sprite.groupcollide(bullets,enemys,True,True)
  
  #  检验敌人是否为空 
  if len(enemys)==0:
#    删除编组剩余精灵
    bullets.empty()
    create_fleet(ai_settings,screen,plane,enemys)



            
def fire_bullet(ai_settings,screen,plane,bullets):
  
  if len(bullets)<ai_settings.bullet_allowed:
      new_bullet =Bullet(ai_settings,screen,plane)
      bullets.add(new_bullet)










def get_number_rows(ai_settings,plane_height,enemy_height):
#  计算屏幕可容纳多少行敌人
  available_space_y=(ai_settings.screen_height - (3*enemy_height)
  -plane_height)
  return int(available_space_y/(2*enemy_height))


def cerate_enemy(ai_settings,screen,enemys,enemy_number,row_number):
  enemy =Enemy(ai_settings,screen)
  enemy_width=enemy.rect.width
  enemy.x=enemy_width + 2 * enemy_width * enemy_number
  enemy.rect.x=enemy.x
  
  enemy.rect.y=enemy.rect.height+2*enemy.rect.height*row_number
  
  enemys.add(enemy)     



def get_number_enemys_x(ai_settings,enemy_width): 
#     计算一行可容纳多少个敌人
 #enemy =Enemy(ai_settings,screen)
  available_space_x=ai_settings.screen_width-2*enemy_width
  return int(available_space_x/(2*enemy_width))
          
             

def create_fleet(ai_settings,screen,plane,enemys):
#  创建一群敌人
#  计算一行可容纳多少个敌人
#  敌人间距为敌人的宽度
  
   enemy =Enemy(ai_settings,screen)
#   为了知道敌人宽度和高度进行初始化
#   enemy_width=enemy.rect.width
#   available_space_x=ai_settings.screen_width-2*enemy_width
#   number_enemys_x=int(available_space_x/(2*enemy_width))
   number_enemys_x = get_number_enemys_x(ai_settings,enemy.rect.width)
   number_rows=get_number_rows(ai_settings,plane.rect.height,enemy.rect.height)
#   创建一行敌人
   for row_number in range(number_rows):
     
     for enemy_number in range(number_enemys_x):
       
#     创建一个敌人并加入到这行
#     enemy =Enemy(ai_settings,screen)
#     enemy.x=enemy_width+2*enemy_width*enemy_number
#     enemy.rect.x=enemy.x
#     enemys.add(enemy)
       cerate_enemy(ai_settings,screen,enemys,enemy_number,
                    row_number)
       
     






def check_fleet_edges(ai_settings,enemys):
#  敌人到达边缘采用措施
  for enemy in enemys.sprites():
    if enemy.check_edges():
      change_fleet_direction(ai_settings,enemys)
      break
    
    
def change_fleet_direction(ai_settings, enemys):
#  敌人下移动，并改变方向
  for enemy in enemys.sprites():
		enemy.rect.y+=ai_settings.fleet_drop_speed
		ai_settings.fleet_direction *= -1
		
    
    
    
def plane_hit(ai_settings,stats,screen,plane,enemys,bullets):
#  响应被敌人撞到的飞船
  
  if stats.planes_left>0:
    
#  将planes_left-1
    stats.planes_left-=1
  
#  清空敌人和子弹列表
    enemys.empty()
    bullets.empty()
  
#  创建一群新敌人，并将飞船重置到屏幕中央
    create_fleet(ai_settings,screen,plane,enemys)
    plane.center_plane()
  
#  暂停
    sleep(0.5)
    
    
    
  else:
		stats.game_active =False
		pygame.mouse.set_visible(True)
  
  
  
  
    
    
    
    
def update_enemys(ai_settings,stats,screen,plane,enemys,bullets):
#  检查是否 有敌人位于屏幕边缘， 更新所有敌人位置
  check_fleet_edges(ai_settings,enemys)
  enemys.update()
  
#  检查敌人与飞船碰撞
  if pygame.sprite.spritecollideany(plane,enemys):
    
#    print("碰撞")
    plane_hit(ai_settings,stats,screen,plane,enemys,bullets)
    
    check_enemys_bottom(ai_settings,stats,screen,plane,enemys,bullets)
    
    
    
    
      
    
  
def check_enemys_bottom(ai_settings,stats,screen,plane,enemys,bullets):
#  检查是否有敌人到达屏幕底端  
  screen_rect=screen.get_rect()
  for enemy in enemys.sprites():
    if enemy.rect.bottom>=screen_rect.bottom:
      #按飞机被撞到进行处理
      plane_hit(ai_settings,stats,screen,plane,enemys,bullets)
      break
    





  
  

  
  
             
             
             
  

