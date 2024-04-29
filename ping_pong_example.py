import pygame

pygame.init()

# 16:9 ratio nHD
window_width = 640
window_height = 360

# RGB Tuple
space_color = (16,72,98)
ball_color = (248,182,43)

# Player variables
player_radius = 10
player_position_x = window_width / 2
player_position_y = window_height / 2

player_speed = 0.01

window = pygame.display.set_mode((window_width, window_height))
window.fill(space_color)

running = True

while(running):
    # retrieves a list of events that have occurred since the last frame
    pygame.event.get()
    # retrieves a list of pressed_key from events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_a]:
        player_position_x -= player_speed
    if keys[pygame.K_d]:
        player_position_x += player_speed
    if keys[pygame.K_w]:
        player_position_y -= player_speed
    if keys[pygame.K_s]:
        player_position_y += player_speed
        
    pygame.draw.circle(window, ball_color, (player_position_x, player_position_y), player_radius)
    
    pygame.display.update()

    
pygame.quit()