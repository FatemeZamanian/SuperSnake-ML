import pygame
import random
import time
from pygame.constants import KEYDOWN
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
        if self.y>=height-10 and self.x>width-10:
            snake.y_change=0
            snake.x_change=1
        if self.y-10<0 and self.x<width-10:
            snake.y_change=0
            snake.x_change=1

    def accident(self):
        global flag
        flag=False
        for i in self.body:
            if pygame.Rect(i['x'],i['y'],10,10).colliderect(pygame.Rect(self.x,self.y,10,10)):
                if  self.x_change==-1 and flag==False:
                    self.x_change=0
                    snake.y_change=1
                    flag=True
                elif  self.x_change==1 and flag==False:
                    self.x_change=0
                    snake.y_change=-1
                    flag=True
                elif self.y_change==-1 and flag==False:
                    self.y_change=0
                    snake.x_change=1
                    flag=True
                elif self.y_change==1 and flag==False:
                    self.y_change=0
                    snake.x_change=-1
                    flag=True
                            
            



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
    fl=open('train_snake.csv','a')
    fl.writable=True
    while True:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                fl.close()
                exit()
        # snake.accident()
        if apple.x+5>=snake.x and  snake.x_change==0 or snake.y+5>=apple.y and apple.y>=snake.y-5:
            snake.y_change=0
            snake.x_change=1
            snake.lose()
        if apple.x-5<=snake.x and snake.x_change==0 or snake.y+5>=apple.y and apple.y>=snake.y-5:
            snake.x_change=-1
            snake.y_change=0
            snake.lose()
        if apple.x+5>=snake.x and apple.x-5<=snake.x or apple.y+5>=snake.y and apple.y-5<=snake.y :
            if apple.y+5>snake.y and snake.y_change==0:
                snake.y_change=1
                snake.x_change=0
                snake.lose()
            elif apple.y-5<=snake.y and snake.y_change==0:
                snake.y_change=-1
                snake.x_change=0
                snake.lose()
        




        
        disp.blit(bg,(0,0))
        txt_score=font.render('Score: '+str(snake.score),True,(255,215,0))
        disp.blit(txt_score,(150,0))
        snake.lose()
        snake.move()
        snake.show()
        apple.show()
        
        res_apple=snake.eat_apple()
        if res_apple==True:
            apple=Apple()
            snake.score+=1
        
        

        
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
            
        # for b in snake.body:
        #     if b['y']<=snake.y:
        #         b2=0
        #         b0=snake.y-b['y']
        #         if snake.x>=b['x']:
        #             b1=snake.x-b['x']
        #             b3=0
        #         else:
        #             b3=b['x']-snake.x
        #             b1=0
        #     else:
        #         a0=0
        #         a2=b['y']-snake.y
        #         if snake.x>=b['x']:
        #             a1=snake.x-b['x']
        #             a3=0
        #         else:
        #             a3=b['x']-snake.x
        #             a1=0
            
            
        if snake.y_change == 1:
            direction=2
        if snake.y_change == -1:
            direction=0

        if snake.x_change == -1:
            direction=3
        if snake.x_change == 1:
            direction=1

            
        fl.write(str(w0)+','+str(w1)+','+str(w2)+','+str(w3)+','+str(a0)+','+str(a1)+','+str(a2)+','+str(a3)+','+str(direction)+'\n')

        clock.tick(10)
        pygame.display.update()
    