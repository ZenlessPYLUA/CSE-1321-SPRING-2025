# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 11

import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

color = 0
while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            sys.exit(0)


    screen.fill((color,color,color))

    pygame.display.flip()

    clock.tick(60)

    color+=1

    if color >= 255:
        color = 0