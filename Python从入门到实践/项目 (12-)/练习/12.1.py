import sys
import pygame

pygame.init()
screen=pygame.display.set_mode((1920,1080))
pygame.display.set_caption("Azure Sky")

bg_color=(50,50,255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(bg_color)
    pygame.display.flip()