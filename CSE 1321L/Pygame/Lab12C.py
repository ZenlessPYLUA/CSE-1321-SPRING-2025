# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 12

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Blue square setup
player = pygame.Rect(225, 225, 50, 50)
player_surface = pygame.Surface((player.width, player.height))
player_surface.fill((0, 0, 255))

speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                sys.exit(0)
            if event.key == K_r:
                player.topleft = (225, 225)
                print("[EVENT] KEYDOWN: USER PRESSED BUTTON R -> RESETTING PLAYER POSITION")

    keys = pygame.key.get_pressed()

    # up
    if keys[K_w]:
        if player.top - speed >= 0:
            player.y -= speed
            print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> MOVING PLAYER UP")
        else:
            print("[EVENT] KEY STATE: W KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    # down
    if keys[K_s]:
        if player.bottom + speed <= 500:
            player.y += speed
            print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> MOVING PLAYER DOWN")
        else:
            print("[EVENT] KEY STATE: S KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    # left
    if keys[K_a]:
        if player.left - speed >= 0:
            player.x -= speed
            print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> MOVING PLAYER TO THE LEFT")
        else:
            print("[EVENT] KEY STATE: A KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")

    # right
    if keys[K_d]:
        if player.right + speed <= 500:
            player.x += speed
            print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> MOVING PLAYER TO THE RIGHT")
        else:
            print("[EVENT] KEY STATE: D KEY IS BEING PRESSED -> CANNOT MOVE PLAYER OUT OF BOUNDS")


    screen.fill((0, 0, 0))  # black
    screen.blit(player_surface, player.topleft)
    pygame.display.flip()
    clock.tick(60)
