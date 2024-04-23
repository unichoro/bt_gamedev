import pygame
import math
import random

#ping pong game
pygame.init()
pygame.display.set_caption("BT_ Ping Pong Game")

# 16:9 ratio nHD
window_width = 640
window_height = 360

# RGB Tuple
space_color=(16,16,16)
ball_color=(255,215,0)
paddle_color=(65,105,225)

# Paddle_variables
paddle_width = 10
paddle_length = 60
paddle_possition_x=0
paddle_possition_y=window_height /2

paddle_speed=5

# Ball_variables
ball_radius=10
ball_possition_x=window_width/2
ball_possition_y=window_height/2

ball_speed=6
ball_direction_theta= math.pi*random.random()
ball_direction_x=math.cos(ball_direction_theta)
ball_direction_y=math.sin(ball_direction_theta)

#
window=pygame.display.set_mode((window_width,window_height))
window.fill(space_color)
clock=pygame.time.Clock()
dt=clock.tick(60)/1000

running=True

#
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE] or keys[pygame.K_x]:
        running=False
    if keys[pygame.K_UP]:
        if paddle_possition_y > 0:
            paddle_possition_y -= paddle_speed*dt
    if keys[pygame.K_DOWN]:
        if paddle_possition_y < window_height - paddle_length:
            paddle_possition_y += paddle_speed*dt

    # when ball hit the wall
    if ball_possition_y - ball_radius < 0 or ball_possition_y + ball_radius > window_height:
        ball_direction_y *= -1
    if ball_possition_x + ball_radius > window_width:
        ball_direction_x *= -1
    if ball_possition_x - ball_radius < 0:
        ball_direction_x *= -1

    # when ball hit the paddle
    if ball_possition_x - ball_radius < paddle_possition_x + paddle_width and ball_possition_y > paddle_possition_y and ball_possition_y < paddle_possition_y + paddle_length:
        ball_direction_x *= -1

    # reset ball
    if (abs(ball_possition_x-ball_radius)==0 or abs(ball_possition_x+ball_radius)==window_width) and (ball_possition_y==ball_radius or ball_possition_y==window_height-ball_radius):
        ball_possition_x=window_width/2
        ball_possition_y=window_height/2
        ball_direction_theta= math.pi*random.random()
        ball_direction_x=math.cos(ball_direction_theta)
        ball_direction_y=math.sin(ball_direction_theta)

    ball_possition_x += ball_speed * ball_direction_x*dt
    ball_possition_y += ball_speed * ball_direction_y*dt

    window.fill(space_color)
    pygame.draw.rect(window, paddle_color, (paddle_possition_x, paddle_possition_y, paddle_width, paddle_length))
    pygame.draw.circle(window, ball_color, (ball_possition_x, ball_possition_y), ball_radius)
    
    pygame.display.update()

pygame.quit()