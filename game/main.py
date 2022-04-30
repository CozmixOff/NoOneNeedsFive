import pygame
from screens import intro_screen
from pygame import mixer

mixer.init()
pygame.init()

window_x = 1080
window_y = 720

pygame_icon = pygame.image.load("../assets/graphics/MinifolksHumans/modified/icon.png")
pygame.display.set_caption("No One Needs Five")
screen = pygame.display.set_mode((window_x, window_y))
pygame.display.set_icon(pygame_icon)

cloud1_coords = 0.30 * window_x
cloud2_coords = 0.07 * window_x
cloud3_coords = 0.70 * window_x

intro_screen.IntroScreen.init()

running = True
while running:
    intro_screen.IntroScreen.run(window_x, window_y,cloud1_coords, cloud2_coords, cloud3_coords, screen)

    # clouds animation

    cloud1_coords -= 0.5
    cloud2_coords -= 0.5
    cloud3_coords -= 0.5
    if cloud1_coords <= -0.13*window_x:
        cloud1_coords = window_x
    elif cloud2_coords <= -0.17*window_x:
        cloud2_coords = window_x
    elif cloud3_coords <= -0.26*window_x:
        cloud3_coords = window_x

    # checking closed window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
