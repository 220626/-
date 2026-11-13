import sys

import pygame

from 游戏数值设置 import Settings
from ship import Ship


#管理游戏资源和行为的类
class zhanji_invasion:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        
        """游戏数值设置"""
        self.settings=Settings()
        
        self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width=self.screen.get_rect().width
        self.settings.screen_height=self.screen.get_rect().height
        pygame.display.set_caption("战机入侵")
        
        self.ship=Ship(self)
        
    
    
    
    
    
    #游戏运行管理
    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self._update_screen()        
            
            """帧率设置"""
            self.clock.tick(60)
            
    
    
    
    
    
     
     #检查用户键盘反应并做出回应       
    def _check_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)    
                
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
                    
                
    
    #用户按下键盘后的回应
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            #向右移动
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            #向左移动
            self.ship.moving_left=True 
        #快速退出游戏
        elif event.key==pygame.K_q:
            sys.exit()            
    
    
    
    #用户松开键盘的回应
    def _check_keyup_events(self,event):
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                #停止持续右移
                self.ship.moving_right=False
            elif event.key==pygame.K_LEFT:
                #停止持续左移
                self.ship.moving_left=False  
    
    
    
    
     #更新屏幕程序           
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()    
        pygame.display.flip()
    
    
    
    
    
            

#创建游戏实例并运行游戏
if __name__=='__main__':
    ai=zhanji_invasion()
    ai.run_game()