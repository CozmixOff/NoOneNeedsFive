import pygame

pygame.init()

pygame.display.set_caption("No One Needs Five")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/graphics/Multi_Platformer_Tileset_v2/GrassLand/Background/GrassLand_Background_Guide.png')
background = pygame.transform.scale(background, (1080, 720))
pygame.display.set_caption('Button Demo')
start_img = pygame.image.load('assets/graphics/custom')

running = True
while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
