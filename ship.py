import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        
        #加载飞船图像并获取其外接矩形
        self.image=pygame.image.load('images/奶娃.bmp')
        self.rect=self.image.get_rect()
        
        #新飞船位置
        self.rect.midbottom=self.screen_rect.midbottom
        
        #在飞船的属性x中存储一个浮点数
        self.x=float(self.rect.x)
        
        #移动标志（飞船一开始不移动）
        self.moving_right=False
        self.moving_left=False
        
        
        
        
    #检查移动标志的值并做出回应   
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        #根据self.x更新rect对象
        self.rect.x=self.x
            
            
        
        
        
    
    def blitme(self):
        #指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
        