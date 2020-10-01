import pygame
pygame.init()
win = pygame.display.set_mode((1000,500))
pygame.display.set_caption("FLAME-GAME")

player = pygame.image.load("idle.png")
bg = pygame.image.load("bg.png")

x = 50
y = 50
speed = 5

clock = pygame.time.Clock()

run = True
while(run):
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        bg.scroll(5, 0)
    elif keys [pygame.K_RIGHT]:
        bg.scroll(-5, 0)
    '''elif keys [pygame.K_UP]:
        y -= speed
    elif keys [pygame.K_DOWN]:
        y += speed'''


    win.blit(bg, (0, 0))
    win.blit(player, (50,50))
    pygame.display.update()

pygame.quit()