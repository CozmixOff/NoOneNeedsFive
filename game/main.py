import pygame
from screens import intro_screen
from pygame import mixer

mixer.init()
pygame.init()

window_x = 1080
window_y = 720

intro_screen.IntroScreen.init()

running = True
while running:
    intro_screen.IntroScreen.run(window_x, window_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
