import pygame, sys
import time
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
screen= pygame.display.set_mode((640,480))
pygame.display.set_caption('pong')
fontobj= pygame.font.Font('LCD_Solid.ttf',50)
mousex,mousey=0,0
x_1=15
x_2=600 #these varaibles (x_1, x_2) are different, but they are constants-- they will never change; think jon, the paddle will not move from left to right
y=0 #the y variable changes, but for this test it will be the same for both paddles bc they are moving in unisen.
x_ball=320
y_ball=240
direction=""
bar=""
speed=2
speed_for_streight= int(round((speed*speed + speed*speed)**0.5,0))
score_left=0
score_right=0
top_bar=False
bottom_bar=False

def create_rect(x_1,x_2,y):
    rect_right=pygame.Rect((x_1,y), (30,190))
    rect_left=pygame.Rect((x_2,y), (30,190))
    return rect_right,rect_left
def draw_stuff (y):
        rect_right,rect_left=create_rect(x_1,x_2,y)
        ball_obj=ball(x_ball,y_ball)
        top_bar,bottom_bar=test_horizontal(x_ball,y_ball,ball_obj,rect_left,rect_right)
        msgl=str(score_left)
        msgr=str(score_right)
        global x_ball,y_ball,direction,bar,speed,score_left,score_right
        textobjl=fontobj.render(msgl, False , pygame.Color('green'))
        textobjr=fontobj.render(msgr, False , pygame.Color('green'))
        screen.blit(textobjl,(160,5))
        screen.blit(textobjr,(480,5))
        pygame.draw.line(screen,pygame.Color('grey'),(320,0), (320,480), 4)
        pygame.draw.line(screen,pygame.Color('grey'),(0,3), (640,3), 10)
        pygame.draw.line(screen,pygame.Color('grey'),(0,475), (640,475), 10)
        pygame.draw.rect(screen, pygame.Color('grey'),rect_left,0)
        pygame.draw.rect(screen, pygame.Color('grey'),rect_right,0)
        x_ball,y_ball,score_left,score_right,direction,speed=score(x_ball,y_ball,score_left,score_right,direction,speed)
        bar=""
        if ball_obj.colliderect(rect_left) or ball_obj.colliderect(rect_right):
            topl,middlel,bottoml=loc_of_ball_hitl(y,x_ball,y_ball)
            topr,middler,bottomr=loc_of_ball_hitr(y,x_ball,y_ball)
            if topl:
                direction="upleft"
            elif middlel:
                direction='midleft'
            elif bottoml:
                direction='downleft'
            elif topr:
                direction="upright"
            elif middler:
                direction="midright"
            elif bottomr:
                direction="downright"
            else:
                direction=""
   #figure out why this is opisite

        if  top_bar:
            bar="bottom_bar"
        elif bottom_bar:
            bar="top_bar"
        elif not top_bar and not bottom_bar:
            bar=""
        print bar, direction
        if not direction:
            x_ball-=speed_for_streight
        elif direction=="upleft":
            if bar=="top_bar":
                x_ball+=speed*time_sec
                y_ball+=speed*time_sec
            else:
                x_ball+=speed*time_sec
                y_ball-=speed*time_sec
        elif direction=="midleft":
            x_ball+=speed
        elif direction=="downleft":
            if bar=="bottom_bar":
                x_ball+=speed*time_sec
                y_ball-=speed*time_sec
            else:
                x_ball+=speed*time_sec
                y_ball+=speed*time_sec
        elif direction=="upright":
            if bar=="top_bar":
                x_ball-=speed*time_sec
                y_ball+=speed*time_sec
            else:
                x_ball-=speed*time_sec
                y_ball-=speed*time_sec
        elif direction=="midright":
            x_ball-=speed_for_streight
        elif direction=="downright":
            if bar=="bottom_bar":
                x_ball-=speed*time_sec
                y_ball-=speed*time_sec
            else:
                x_ball-=speed*time_sec
                y_ball+=speed*time_sec
        #ball(x_ball,y_ball)

def test_horizontal(x_ball,y_ball,ball_obj,rect_left,rect_right):
    global top_bar, bottom_bar
    if y_ball<=6:
     top_bar=True
    elif y_ball>=475:
        bottom_bar=True
    elif ball_obj.colliderect(rect_left) or ball_obj.colliderect(rect_right):
        bottom_bar=False
        top_bar=False
    print bottom_bar, top_bar
    return bottom_bar,top_bar


def score(ball_x,ball_y,score_left,score_right,direction,speed):
    if ball_x<0:
        score_right+=1
        textobjtxt=fontobj.render("Point for Computer!", False , pygame.Color('green'))
        screen.blit(textobjtxt,(480,240))
        ball_x=320
        ball_y=240
        direction="midright"
        speed=2
    elif ball_x>=632:
        score_left+=1
        textobjtxt1=fontobj.render("Point for Player!", False , pygame.Color('green'))
        screen.blit(textobjtxt1,(160,240))
        ball_x=320
        ball_y=240
        direction="midleft"
        speed=2
    return ball_x,ball_y,score_left,score_right, direction,speed


def ball(x,y):
    ball_rect = pygame.draw.circle(screen, pygame.Color('green'), (x,y), 10, 0)
    return ball_rect
def ball_hit(y,ball_x,ball_y):
    if ball_x==60 and ball_y>=y and ball_y<y+190 or ball_x==570 and ball_y>=y and ball_y<y+190:
        return True
    return False
def loc_of_ball_hitl(y,ball_x,ball_y):
   middle=False
   top=False
   bottom=False
   if ball_x<=60 and ball_y>=y+66 and ball_y<y+128:
        middle=True
   elif ball_x<=60 and ball_y>=y+10 and ball_y<y+64:
        top=True
   elif ball_x<=60 and ball_y>=y+128 and ball_y<y+198:
        bottom=True
   return top, middle, bottom
def loc_of_ball_hitr(y,ball_x,ball_y):
   middle=False
   top=False
   bottom=False
   if ball_x>=570 and ball_y>=y+64 and ball_y<y+128:
        middle=True
   elif ball_x>=570 and ball_y>=y+15 and ball_y<y+64:
        top=True
   elif ball_x>=570 and ball_y>=y+133 and ball_y<y+192:
        bottom=True
   return top, middle, bottom
while True:
    screen.fill(pygame.Color('black'))
    if mousey>y:
        draw_stuff(y)
        y+=2
    if mousey<y:
        draw_stuff(y)
        y-=2
    if mousey==y:
        draw_stuff(y)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        elif event.type== MOUSEMOTION:
            mousex,mousey=event.pos
    time_passed = clock.tick(60)
    time_sec = int( time_passed / 1000.0)
    pygame.display.update()