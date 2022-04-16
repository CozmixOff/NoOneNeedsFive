import pygame
from pygame import mixer

mixer.init()
pygame.init()

window_x = 1080
window_y = 720

pygame_icon = pygame.image.load("assets/graphics/MinifolksHumans/icon.png")
pygame.display.set_caption("No One Needs Five")
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_icon(pygame_icon)

mixer.music.load("assets/musics/Pleasant_Adventure_Pre.wav")
mixer.music.play()

background = pygame.image.load(
    'assets/graphics/Multi_Platformer_Tileset_v2/GrassLand/Background/GrassLand_Background_Guide.png')
background = pygame.transform.scale(background, (window_x, window_y))

game_logo = pygame.image.load('assets/graphics/custom/game_logo.png')
game_logo = pygame.transform.scale(game_logo, (0.45 * window_x, 0.23 * window_y))

start_button_image = pygame.image.load('assets/graphics/custom/start_button.png')

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(game_logo, ((window_x - 0.45 * window_x) / 2, 0.15 * window_y))
    pygame.display.flip()
    if not mixer.music.get_busy():
        mixer.music.load("assets/musics/Pleasant_Adventure_Loop.wav")
        mixer.music.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
