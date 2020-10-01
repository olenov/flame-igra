import pygame
pygame.init()
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("FLAME-GAME")

player = pygame.image.load("idle.png")
bg = pygame.image.load("bg.png")

x = 0
y = 0
speed = 5

clock = pygame.time.Clock()
run = True
win.blit(bg, (0, 0))
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    rel_x = x % bg.get_rect().width

    if keys[pygame.K_LEFT]:
        x += 5
        win.blit(bg, (rel_x-bg.get_rect().width, 0))

        if rel_x < 1000:
            win.blit(bg,(rel_x, 0))
    elif keys [pygame.K_RIGHT]:
        x -= 5
        win.blit(bg, (rel_x-bg.get_rect().width, 0))

        if rel_x < 1000:
            win.blit(bg, (rel_x, 0))

    '''elif keys [pygame.K_UP]:
        y -= speed
    elif keys [pygame.K_DOWN]:
        y += speed'''



    win.blit(player, (50,50))
    pygame.display.update()

pygame.quit()