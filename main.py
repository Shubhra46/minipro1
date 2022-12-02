import pygame,time
from random import randint
#setting screensize of pygame window to 800x600 px
screen=pygame.display.set_mode((800,600))
background=pygame.image.load('background.jpg')   #this img is already available in folder

#title
pygame.display.set_caption("Shubhra Gupta")

class Ball:
    ball_img=pygame.image.load('basketball.png')
    g=1
    def __init__(self):
        self.velocityX=4
        self.velocityY=4
        self.X=randint(0,768)
        self.Y=randint(0,350)
        
    def render_ball(self):
        screen.blit(ball.ball_img,(self.X,self.Y))
        
    def mov_ball(self):
        #changing vel y due to gravity
        self.velocityY+=ball.g
        
        #changing position of ball
        self.X+=self.velocityX
        self.Y+=self.velocityY
        
        #collision in balls due to change in velocity
        if self.X<0 or self.X>768:
            self.velocityX*-1
        if self.Y<0 and self.velocityY<0:
            self.velocityY*-1
        if self.Y>568 and self.velocityY>0:
            self.velocityY*-1
            self.Y=568
            
Ball_list=[Ball(),Ball(),Ball(),Ball(),Ball()]
    
    #main prog loop
running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            # running=False
                
    time.sleep(0.02)
    screen.blit(background,(0,0))
    for ball in Ball_list:
        ball.render_ball()
        ball.mov_ball()
        
    pygame.display.update()