import pygame
import math
import random

pygame.init()
pygame.font.init()

# 16:9 window ratio nHD
window_width = 640
window_height = 360

# RGB Tuple
space_color = (16, 72, 98)
ball_color = (248,182,43)
player_color = (198,224,120)

window = pygame.display.set_mode((window_width, window_height))

# Declare state/flag : running
running = True

# player
player_width = 20
player_height = 100

player_left_position_x = 0
player_left_position_y = window_height/3

player_right_position_x = window_width - player_width
player_right_position_y = window_height/3

player_left_score = 0
player_right_score = 0

player_speed = 200

# ball
ball_radius = 10

ball_position_x = window_width/2
ball_position_y = window_height/2

direction_theta = math.pi / 4
ball_direction_x = math.cos(direction_theta)
ball_direction_y = -math.sin(direction_theta)

ball_speed = 300

# Declare Clock
clock = pygame.time.Clock()

# Declare font
font_size = 36
font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", font_size)

while(running):
    
    # deltaTime
    dt = clock.tick(60) / 1000
    # print(dt)
    
    # retrieves a list of events that have occurred since the last frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
    # retrieves a list of pressed_key from events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    # if keys[pygame.K_a]:
    #     player_position_x -= speed
    # if keys[pygame.K_d]:
    #     player_position_x += speed
    
    # player_left
    if keys[pygame.K_w]:
        player_left_position_y -= player_speed * dt
        if (player_left_position_y < 0):
            player_left_position_y = 0
    if keys[pygame.K_s]:
        player_left_position_y += player_speed * dt
        if (player_left_position_y > window_height - player_height):
            player_left_position_y = window_height - player_height
    # player_right
    if keys[pygame.K_i]:
        player_right_position_y -= player_speed * dt
        if (player_right_position_y < 0):
            player_right_position_y = 0
    if keys[pygame.K_k]:
        player_right_position_y += player_speed * dt
        if (player_right_position_y > window_height - player_height):
            player_right_position_y = window_height - player_height
            
    ball_position_x += ball_direction_x * ball_speed * dt
    ball_position_y += ball_direction_y * ball_speed * dt
    
    if (ball_position_y < 0 + ball_radius / 2):
        ball_position_y = 0 + ball_radius / 2
        ball_direction_y *= -1
    if (ball_position_y > window_height - ball_radius / 2):
        ball_position_y = window_height - ball_radius / 2
        ball_direction_y *= -1
    
    if (ball_position_x < 0 + player_width): # left_player
        if (ball_position_y > player_left_position_y and ball_position_y < player_left_position_y + player_height):
            ball_position_x = 0 + player_width
            ball_direction_x *= -1
    
    if (ball_position_x > window_width - player_width): # right_player
        if (ball_position_y > player_right_position_y and ball_position_y < player_right_position_y + player_height):
            ball_position_x = window_width - player_width
            ball_direction_x *= -1
    
    if (ball_position_x < 0 + ball_radius / 2): # left_player win
        player_right_score += 1
        
        random_angle = random.randrange(1, 8)
        # random_ball_direction = 1 if random_angle % 2 == 0 else -1
        
        ball_position_x = window_width/2
        ball_position_y = window_height/2

        direction_theta = (math.pi/8 + (math.pi / 32) * random_angle) * 1
        ball_direction_x = math.cos(direction_theta)
        ball_direction_y = -math.sin(direction_theta)
        
    if (ball_position_x > window_width - ball_radius / 2): # right_player win
        # ball_position_x = window_width - ball_radius / 2
        # ball_direction_x *= -1
        player_left_score += 1
        
        random_angle = random.randrange(1, 8)
        # random_ball_direction = 1 if random_angle % 2 == 0 else -1
        
        ball_position_x = window_width/2
        ball_position_y = window_height/2

        direction_theta = (math.pi/8 + (math.pi / 32) * random_angle) * -1
        ball_direction_x = math.cos(direction_theta)
        ball_direction_y = -math.sin(direction_theta)
        
    window.fill(space_color)
    
    score_textSurface = font.render(f'{player_left_score}       |       {player_right_score}', True, (255, 255, 255))
    score_textRect = score_textSurface.get_rect()
    score_textRect.center = (window_width/2, window_height/2)
    
    pygame.draw.rect(window, player_color, (player_left_position_x, player_left_position_y, player_width, player_height))
    pygame.draw.rect(window, player_color, (player_right_position_x, player_right_position_y, player_width, player_height))
    pygame.draw.circle(window, ball_color, (ball_position_x, ball_position_y), ball_radius)
    
    window.blit(score_textSurface, score_textRect)
    
    pygame.display.update()

pygame.quit()