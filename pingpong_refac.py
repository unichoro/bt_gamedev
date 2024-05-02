import pygame
import math
import random

class game:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.window_width = 640
        self.window_height = 360

        self.space_color = (16, 72, 98)
        self.ball_color = (248, 182, 43)
        self.ball_colorplayer_color = (198, 224, 120)

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60) / 1000
        font_size = 36
        font = pygame.font.Font("./Roboto-Medium.ttf", font_size)

class ball:
    def __init__(self):
        self.x=game.window_width/2
        self.y=game.window_height/2
        self.color=(248, 182, 43)
        self.radius=10
        self.speed=10
        self.degree=random.uniform(0, math.pi*2)

    def move(self, dt):
        self.x+=self.speed*math.cos(self.degree)*dt
        self.y+=self.speed*math.sin(self.degree)*dt

    def draw(self, window):
        pygame.draw.circle(window, game.ball_color, (self.x, self.y), self.radius)

class player:
    def __init__(self):
        self.x=0
        self.y=game.window_height/2
        self.color=(198, 224, 120)
        self.width=10
        self.height=60
        self.speed=6

    def move(self, dt, key.up, key.down):
        if key.up:
            self.y+=self.speed*dt
        if key.down:
            self.y-=self.speed*dt

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

class key:
    def 

game = game()
ball = ball()
player = player()

game.__init__(game)
ball.__init__(ball)
player.__init__(player)

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.move(ball, game.dt)
    game.window.fill(game.space_color)
    ball.draw(ball, game.window)
    pygame.display.flip()

