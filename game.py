import pygame
pygame.init()
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("FLAME-GAME")

player = pygame.image.load("idle.png")
player = pygame.transform.scale(player,(100,100))
bg = pygame.image.load("bg.png")

x = 0
y = 0
speed = 5
jump_count = 1
jump = False
temp = False

clock = pygame.time.Clock()
run = True
win.blit(bg, (0, 0))
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    win.blit(player, (500, 400))

    rel_x = x % bg.get_rect().width
    if keys[pygame.K_LEFT]:
        x += 5
        win.blit(bg, (rel_x-bg.get_rect().width, 0))
        win.blit(player, (500, 400))

        if rel_x < 1920:
            win.blit(bg,(rel_x, 0))
            win.blit(player, (500, 400))
    elif keys[pygame.K_RIGHT]:
        win.blit(player, (500, 400))
        x -= 5
        win.blit(bg, (rel_x-bg.get_rect().width, 0))
        win.blit(player, (500, 400))
        if rel_x < 1920:
            win.blit(bg, (rel_x, 0))
            win.blit(player, (500, 400))
    if keys[pygame.K_UP]:
        jump = True
        ''' короче я тут пытался прыжки сделать но голова ваще не соображает'''
        if jump_count < 40 and jump_count != 0:
            y -= 5
            jump_count += 1
            print(jump_count)
        elif jump_count >= 40:
            temp = True
            print(temp)
        elif temp == True:
            y += 5
            jump_count -= 1
            print(jump_count)
        elif jump_count == 0:
            jump_count = 1
            jump = False
            y = 0
        win.blit(player, (500, y+400))

    pygame.display.update()

pygame.quit()