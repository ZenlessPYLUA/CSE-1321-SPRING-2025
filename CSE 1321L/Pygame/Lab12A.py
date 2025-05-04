# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 12

import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

rect1 = pygame.Rect(175, 0, 50, 400)
red_surface = pygame.Surface((rect1.width, rect1.height))
red_surface.fill((255, 0, 0))

rect2 = pygame.Rect(0, 175, 50, 50)
blue_surface = pygame.Surface((rect2.width, rect2.height))
blue_surface.fill((0, 0, 255))

speed = 5
direction = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit(0)

    rect2.x += speed * direction
    if rect2.right >= 400 or rect2.left <= 0:
        direction *= -1

    if rect1.colliderect(rect2):
        red_surface.fill((0, 255, 0))
    else:
        red_surface.fill((255, 0, 0))

    screen.fill((0, 0, 0))
    screen.blit(red_surface, rect1.topleft)
    screen.blit(blue_surface, rect2.topleft)

    pygame.display.flip()
    clock.tick(60)

