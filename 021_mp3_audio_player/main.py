import pygame

pygame.mixer.init()

pygame.mixer.music.load('audio.mp3')

pygame.mixer.music.play()

input("Press enter to stop...")