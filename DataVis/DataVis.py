import pygame, time
import data.txt


pygame.display.init()

canvas = pygame.display.set_mode((320,240))

redish = (255, 50, 50)
bounds = pygame.Rect(100, 100, 50, 30)

pygame.draw.rect(canvas, redish, bounds, 2)

pygame.display.update()

