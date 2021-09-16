import numpy as np
import tensorflow as tf
import pygame
import random

model = tf.keras.models.load_model('snake.h5')

class Apple:
    def __init__(self):
        self.r=8
        self.x=random.randint(40,width-40)
        self.y=random.randint(40,height-40)
        self.color=(255,0,0)
    def show(self):
        apl=pygame.image.load('apple.png')
        disp.blit(apl,(self.x,self.y))

        
class Snake:
    def __init__(self):
        self.w=10
        self.h=10
        self.x=width/2
        self.y=height/2
        self.color=(255,0,0)
        self.color3=(255,204,0)
        self.color2=(255,102,0)
        self.score=0
        self.x_change=0
        self.y_change=0
        self.speed=10
        self.body=[]

    def show(self):
        pygame.draw.rect(disp,self.color,[self.x,self.y,self.w,self.h])
        i=0
        for x in self.body:
            i+=1
            if i%2==0:
                pygame.draw.rect(disp,self.color3,[x['x'],x['y'],self.w,self.h])
            else:
                pygame.draw.rect(disp,self.color2,[x['x'],x['y'],self.w,self.h])
            
    def move(self):
        self.body.append({'x':self.x,'y':self.y})
        if len(self.body)>self.score:
            self.body.remove(self.body[0])
        if self.x_change==-1:
            self.x-=self.speed
        elif self.x_change==1:
            self.x+=self.speed
        elif self.y_change==-1:
            self.y-=self.speed
        elif self.y_change==1:
            self.y+=self.speed
        


    def eat_apple(self):
        if apple.x-apple.r <= self.x <= apple.x+apple.r and apple.y-apple.r <= self.y <= apple.y+apple.r:
            return True
        else:
            return False

    def lose(self):
        if self.x>=width-10 and self.y<height-10:
            snake.x_change=0
            snake.y_change=1
        if self.x<=10 and self.y<height-10:
            snake.x_change=0
            snake.y_change=1
        if self.y>=height-10 and self.x<width-10:
            snake.y_change=0
            snake.x_change=1
        if self.y<=10 and self.x<width-10:
            snake.y_change=0
            snake.x_change=1
            



if __name__=='__main__':
    bg=pygame.image.load('green_background.jpg')
    pygame.font.init()
    font=pygame.font.SysFont('comicsansms',35)
    width=400
    height=400
    disp=pygame.display.set_mode((width,height))
    clock=pygame.time.Clock()
    apple=Apple()
    snake=Snake()
    direction=0
    while True:
        w0=snake.y
        w1=width-snake.x
        w2=height-snake.y
        w3=snake.x
        if snake.y>=apple.y:
            a2=0
            a0=snake.y-apple.y
            if snake.x>=apple.x:
                a1=snake.x-apple.x
                a3=0
            else:
                a3=apple.x-snake.x
                a1=0
        else:
            a0=0
            a2=apple.y-snake.y
            if snake.x>=apple.x:
                a1=snake.x-apple.x
                a3=0
            else:
                a3=apple.x-snake.x
                a1=0

       
        t=np.array([w0,w1,w2,w3,a0,a1,a2,a3])
        t=t.reshape(1,8)
        dir=model.predict(t)
        dir = np.argmax(dir)
        print(dir)
        if dir==0 :
            snake.y_change=-1
            snake.x_change=0
            # snake.lose()
        if dir==2 :
            snake.y_change=1
            snake.x_change=0
            # snake.lose()
        if dir==3:
            snake.x_change=-1
            snake.y_change=0
            # snake.lose()
        if dir==4 :
            snake.y_change=0
            snake.x_change=1
            # snake.lose()
        snake.move()
        disp.blit(bg,(0,0))
        txt_score=font.render('Score: '+str(snake.score),True,(255,215,0))
        disp.blit(txt_score,(150,0))
        snake.lose()
        
        snake.show()
        apple.show()
        res_apple=snake.eat_apple()
        if res_apple==True:
            apple=Apple()
            snake.score+=1

                
        clock.tick((snake.score/2)+5)
        pygame.display.update()

    
