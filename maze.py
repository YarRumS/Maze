#создай игру "Лабиринт"!
from pygame import *
game = True
finish = False
win_width = 700
win_height = 500
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 65:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, lg, rg):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.direction = 'right'
        self.lg = lg
        self.rg = rg
    def update(self):
        self.rect.x +=1
        x1 = 500
        x2 = 635
        if self.rect.x <= self.lg:
            self.direction = "right"
        if self.rect.x >= self.rg:  
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= 4
        if self.direction == 'right':
            self.rect.x += 2    
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width= wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


clock = time.Clock()
FPS = 60
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
treasure = GameSprite("treasure.png", 635, 435, 0)
player = Player("hero.png", 0, 0, 5)
kakashka_zlaya = Enemy("cyborg.png", 500, 320, 3, 460, 635)
kaka_zlaya_iz_raya = Enemy("cyborg.png", 240, 10, 0, 240, 635)
kaka = Enemy('cyborg.png', 625, 120, 0, 460, 625)
wall_1 = Wall(115, 252, 3, 100, 0, 10, 400)
wall_2 = Wall(115, 252, 3, 230, 0, 10, 80)
wall_3 = Wall(115, 252, 3, 200, 80, 100, 10)
wall_4 = Wall(115, 252, 3, 230, 200, 10, 520)
wall_5 = Wall(115, 252, 3, 200, 200, 250, 10)
wall_6 = Wall(115, 252, 3, 440, 90, 10, 110)
wall_7 = Wall(115, 252, 3, 440, 90, 150, 10)
wall_8 = Wall(115, 252, 3, 590, 90, 10, 500)
wall_9 = Wall(115, 252, 3, 100, 400, 50, 10)
mixer.init()
font.init()
font = font.SysFont("Arial", 36)
winfont = font.render('YOU WIN!', True, (255, 215, 0)) # выигрыш 
lose = font.render("YOU LOSE", True, (255, 0, 0))
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
win = mixer.Sound('money.ogg')
background = transform.scale(image.load("background.jpg"), (700, 500))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        treasure.reset()
        player.reset()
        player.update()
        kakashka_zlaya.reset()
        kakashka_zlaya.update()
        kaka_zlaya_iz_raya.reset()
        kaka_zlaya_iz_raya.update()
        kaka.reset()
        kaka.update()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
        wall_7.draw_wall()
        wall_8.draw_wall()
        wall_9.draw_wall()
        if sprite.collide_rect(player, kaka_zlaya_iz_raya) or sprite.collide_rect(player, kakashka_zlaya) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3) or sprite.collide_rect(player, wall_4) or sprite.collide_rect(player, wall_5) or sprite.collide_rect(player, wall_6) or sprite.collide_rect(player, wall_7) or sprite.collide_rect(player, wall_8) or sprite.collide_rect(player, wall_9) or sprite.collide_rect(player, kaka):
            #game = False
            kick.play()
            window.blit(lose, (250, 250))
            finish = True
        if sprite.collide_rect(player, treasure):
            win.play
            window.blit(winfont, (250, 250))
            finish  = True




    clock.tick(FPS)
    display.update()