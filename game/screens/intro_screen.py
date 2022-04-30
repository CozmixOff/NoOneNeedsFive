import pygame
from pygame import mixer


class IntroScreen:
    @staticmethod
    def init():
        mixer.music.load("../assets/musics/Pleasant_Adventure_Pre.wav")
        mixer.music.play()

    @staticmethod
    def run(window_x, window_y, cloud1_coords, cloud2_coords, cloud3_coords, screen):
        intro_background = pygame.image.load(
            '../assets/graphics/Multi_Platformer_Tileset_v2/modified/intro_animation/intro_background.png')
        intro_background = pygame.transform.scale(intro_background, (window_x, window_y))

        screen.blit(intro_background, (0, 0))

        cloud1 = pygame.image.load(
            '../assets/graphics/Multi_Platformer_Tileset_v2/GrassLand/Background/GrassLand_Cloud_1.png')
        cloud1 = pygame.transform.scale(cloud1, (0.13 * window_x, 0.07 * window_y))
        cloud2 = pygame.image.load(
            '../assets/graphics/Multi_Platformer_Tileset_v2/GrassLand/Background/GrassLand_Cloud_2.png')
        cloud2 = pygame.transform.scale(cloud2, (0.17 * window_x, 0.15 * window_y))
        cloud3 = pygame.image.load(
            '../assets/graphics/Multi_Platformer_Tileset_v2/GrassLand/Background/GrassLand_Cloud_3.png')
        cloud3 = pygame.transform.scale(cloud3, (0.26 * window_x, 0.15 * window_y))

        screen.blit(cloud1, (cloud1_coords, 0.04*window_y))
        screen.blit(cloud2, (cloud2_coords, 0.19*window_y))
        screen.blit(cloud3, (cloud3_coords, 0.30*window_y))

        game_logo = pygame.image.load('../assets/graphics/custom/game_logo.png')
        game_logo = pygame.transform.scale(game_logo, (0.45 * window_x, 0.23 * window_y))
        screen.blit(game_logo, ((window_x - 0.45 * window_x) / 2, 0.15 * window_y))

        if not mixer.music.get_busy():
            mixer.music.load("../assets/musics/Pleasant_Adventure_Loop.wav")
            mixer.music.play()

        pygame.display.flip()