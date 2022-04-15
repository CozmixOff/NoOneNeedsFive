import pygame
from pygame import mixer

mixer.init()
pygame.init()

pygame.display.set_caption("No One Needs Five")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/graphics/Multi_Platformer_Tileset_v2/GrassLand/Background/GrassLand_Background_Guide.png')
background = pygame.transform.scale(background, (1080, 720))
mixer.music.load("assets/musics/Pleasant_Adventure_Pre.wav")
mixer.music.play()

running = True
while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    if not mixer.music.get_busy():
        mixer.music.load("assets/musics/Pleasant_Adventure_Loop.wav")
        mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
