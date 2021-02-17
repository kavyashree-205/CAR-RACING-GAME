
import pygame
import random
import os
import math

pygame.init()
screen=pygame.display.set_mode((540,700))
pygame.display.set_caption("Car Racing")
road=pygame.image.load("car racing/road.jpg")
car=pygame.image.load("car racing/car.png")
carx=200
cary=450
speed=0
ob1=pygame.image.load("car racing/barrier.png")
ob1x=random.randint(20,120)
ob1y=0
ob2=pygame.image.load("car racing/construction.png")
ob2x=random.randint(170,270)
ob2y=0
ob3=pygame.image.load("car racing/another.png")
ob3x=random.randint(320,400)
ob3y=0
heart=pygame.image.load("car racing/heart.png")
pos=[420,460,500]
posy=10
life=3

font=pygame.font.Font("freesansbold.ttf",50)

def show_car(x,y):
    screen.blit(car,(carx,cary))
def show_ob1(x,y):
    screen.blit(ob1,(ob1x,ob1y))
def show_ob2(x,y):
    screen.blit(ob2,(ob2x,ob2y))
def show_ob3(x,y):
    screen.blit(ob3,(ob3x,ob3y))
def show_life(x,y):
    for i in range(0,life):
        screen.blit(heart,(pos[i],posy))
def show_out():
    text=font.render("Game Over!!!",True,(255,255,255))
    screen.blit(text,(100,300))

def is_collision():
    global dis1,dis2,dis3
    dis1=math.sqrt(pow((ob1x-carx),2)+pow((ob1y-cary),2))
    dis2=math.sqrt(pow((ob2x-carx),2)+pow((ob2y-cary),2))
    dis3=math.sqrt(pow((ob3x-carx),2)+pow((ob3y-cary),2))
   
    if cary-ob1y<=abs(120) and carx-ob1x<=abs(100) and dis1<=70:
        return True
    elif cary-ob2y<=abs(80) and carx-ob2x<=abs(100) and dis2<=70:
        return True
    elif cary-ob3y<=abs(80) and carx-ob3x<=abs(100) and dis3<=70:
        return True 
              
while True:
    screen.fill((0,0,0))
    screen.blit(road,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.display.quit()
            os._exit(1)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                speed=-0.2
            if event.key==pygame.K_RIGHT:
                speed=0.2
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                speed=-0.2
            if event.key==pygame.K_RIGHT:
                speed=0.2
    ob1y=ob1y+0.1
    ob2y=ob2y+0.2
    ob3y=ob3y+0.15
    carx=carx+speed
    if ob1y>=700:
        ob1x=random.randint(20,140)
        ob1y=0
    elif ob2y>=700:
        ob2x=random.randint(160,280)
        ob2y=0
    elif ob3y>=700:
        ob3x=random.randint(300,400)
        ob3y=0
    elif carx<20:
        carx=20
    elif carx>400:
        carx=400
           
    show_car(carx,cary)
    show_ob1(ob1x,ob1y)
    show_ob2(ob2x,ob2y)
    show_ob3(ob3x,ob3y)
    show_life(pos,posy)
    collision=is_collision()
    if collision==True:
        life=life-1
        if cary-ob1y<=abs(700) and carx-ob1x<=abs(40) and dis1<=70:
         
            ob1x=random.randint(20,120)
            ob1y=-50
        elif cary-ob2y<=abs(100) and carx-ob2x<=abs(100) and dis2<=70:
          
            ob2x=random.randint(170,270)
            ob2y=-50
        elif cary-ob3y<=abs(110) and carx-ob3x<=abs(100) and dis3<=70:
  
            ob3x=random.randint(320,400)
            ob3y=-50
          
    if life==0:
        show_out()
        ob1x=600
        ob2x=670
        ob3x=710   
    pygame.display.update()
    
    
        