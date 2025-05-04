# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 11

import pygame, sys

from pygame.locals import *

pygame.init()

resolution = (1000, 500)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

surf1 = pygame.Surface((100, 100))
surf1.fill((0, 255, 0))
rect1 = pygame.Rect(0, 0, 50, 50)


surf2 = pygame.Surface((100, 100))
surf2.fill((0, 0, 255))
rect2 = pygame.Rect(0, 400, 50, 50)

square_speed = 5
rect1_direction = 1
rect2_direction = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit(0)

    rect1.x += square_speed * rect1_direction
    rect2.x += square_speed * rect2_direction

    if rect1.right >= resolution[0] or rect1.left <= 0:
        rect1_direction *= -1
    if rect2.right >= resolution[0] or rect2.left <= 0:
        rect2_direction *= -1


    screen.fill((0, 0, 0))
    screen.blit(surf1, rect1.topleft)
    screen.blit(surf2, rect2.topleft)

    pygame.display.flip()
    clock.tick(60)