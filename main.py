import pygame
from random import randint
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
 
        self.image = pygame.transform.scale(pygame.image.load(player_image).convert_alpha(), (w, h))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):

    reload = 20

    def update(self):
        self.reload += 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("pp.png")
background = pygame.transform.scale(pygame.image.load("pp.png"), (win_width, win_height))
player1 = Player('ping_rocket1 (1).png', 5, win_height - 200, 100, 50,150)
game = True
finish = False
win = False
ticks = 0

clock = pygame.time.Clock()
FPS = 60
window.blit(background,(0, 0))    
while game:
    pygame.display.set_caption("pp.png (fps-" + \
                    str(int(clock.get_fps())) + ")")
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False

    player1.update()
    window.blit(background,(0, 0)) 
    player1.draw()
    pygame.display.update()
    clock.tick(FPS)
    ticks += 1