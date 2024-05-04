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
        font_size = 50
        self.font = pygame.font.Font("./Roboto-Medium.ttf", font_size)

class ball:
    def __init__(self):
        self.x=game.window_width/2
        self.y=game.window_height/2
        self.color=(248, 182, 43)
        self.radius=10
        self.speed=6
        self.degree=random.choice([random.uniform(math.pi*(-(1/2.5)), math.pi*(1/2.5)) , random.uniform(math.pi*(1-(1/2.5)), math.pi*(1+(1/2.5)))])

    def move(self, dt):
        self.x+=self.speed*math.cos(self.degree)*dt
        self.y+=self.speed*math.sin(self.degree)*dt

    def draw(self, window):
        pygame.draw.circle(window, game.ball_color, (self.x, self.y), self.radius)

class player:
    def __init__(self, x_pos, up_key, down_key):
        self.x=x_pos
        self.y=game.window_height/2
        self.color=(198, 224, 120)
        self.width=10
        self.height=80
        self.speed=7
        self.up=up_key
        self.down=down_key


    def move(self, dt):
        keys=pygame.key.get_pressed()
        if keys[self.up]:
            if self.y>=0:
                self.y-=self.speed*dt
        if keys[self.down]:
            if self.y+self.height<=game.window_height:
                self.y+=self.speed*dt


    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

class key:
    def __init__(self):
        self.get=pygame.KEYDOWN
    def key_set(self):
        self.up=pygame.K_UP
        self.down=pygame.K_DOWN
        self.up2=pygame.K_w
        self.down2=pygame.K_s
        self.escape=pygame.K_ESCAPE
        self.x=pygame.K_x

class collision:
    def check(self):
        if ball.x+ball.radius>=game.window_width:
            if player2.y<=ball.y<=player2.y+player2.height:
                ball.degree=math.pi-ball.degree
            else:
                score.player1+=1
                ball.__init__()
        if ball.x-ball.radius<=0:
            if player1.y<=ball.y<=player1.y+player1.height:
                ball.degree=math.pi-ball.degree
            else:
                score.player2+=1
                ball.__init__()
        if ball.y+ball.radius>=game.window_height:
            ball.degree=math.pi*2-ball.degree
        if ball.y-ball.radius<=0:
            ball.degree=math.pi*2-ball.degree

class score:
    def __init__(self):
        self.player1=0
        self.player2=0
    def draw(self, window):
        score1=game.font.render(str(self.player1), True, (255, 255, 255))
        score2=game.font.render(str(self.player2), True, (255, 255, 255))
        colron=game.font.render(":", True, (255, 255, 255))
        window.blit(score1, (game.window_width/4, game.window_height/2-13))
        window.blit(colron, (game.window_width/2, game.window_height/2-13))
        window.blit(score2, (game.window_width*3/4, game.window_height/2-13))


game = game()
ball = ball()
key = key()
collision = collision()
player1 = player(0, pygame.K_w, pygame.K_s)
player2 = player(game.window_width-10, pygame.K_i, pygame.K_k)
score = score()

game.__init__()
ball.__init__()
player1.__init__(0, pygame.K_w, pygame.K_s)
player2.__init__(game.window_width-10, pygame.K_i, pygame.K_k)
key.__init__()
key.key_set()
score.__init__()

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == key.escape or event.key == key.x:
                game.running = False

    player1.move(game.dt)
    player2.move(game.dt)
    ball.move(game.dt)
    collision.check()
    game.window.fill(game.space_color)
    ball.draw(game.window)
    player1.draw(game.window)
    player2.draw(game.window)
    score.draw(game.window)
    pygame.display.flip()
pygame.quit()

