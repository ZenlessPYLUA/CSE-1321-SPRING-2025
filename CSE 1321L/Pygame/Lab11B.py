# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 11

import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (600, 600)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

surf1 = pygame.Surface((60,60))
surf1.fill((255,0,0))

surf2 = pygame.Surface((60,60))
surf2.fill((255,0,0))

surf3 = pygame.Surface((60,60))
surf3.fill((255,0,0))

surf4 = pygame.Surface((60,60))
surf4.fill((255,0,0))

surf5 = pygame.Surface((60,60))
surf5.fill((255,0,0))

color = 0
direction = 5
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)


    screen.fill((color,color,color))
    screen.blit(surf1, (0,0))
    screen.blit(surf2, (540, 0))
    screen.blit(surf3, (540, 540))
    screen.blit(surf4, (0, 540))
    screen.blit(surf5, (270, 270))

    pygame.display.flip()

    clock.tick(60)
