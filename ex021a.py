import pygame
pygame.init()

pygame.mixer.music.load('archive.mp3')
pygame.mixer.music.play()
pygame.event.wait()
