import pygame
import random
from Meteor import Meteor
from Player import Player
import Config as CFG


pygame.init()
pygame.mixer.init()


pygame.time.set_timer(CFG.SPAWN_METEOR_EVENT, 1000)

screen = pygame.display.set_mode((CFG.WIDTH, CFG.HEIGHT))
pygame.display.set_caption("Meteor Dodge")
clock = pygame.time.Clock()


font = pygame.font.Font(None, 48)
text_surf = font.render("You Lost!", True, CFG.WHITE)
text_rect = text_surf.get_rect(center=(CFG.WIDTH // 2, CFG.HEIGHT // 2))


shade = pygame.Surface((CFG.WIDTH, CFG.HEIGHT))
shade.set_alpha(100)
shade.fill(CFG.BLACK)


background = pygame.image.load("img/bg.png").convert()


meteors = []
player = Player()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == CFG.SPAWN_METEOR_EVENT:
            meteor = Meteor()
            meteors.append(meteor)
            meteor.spawn_sound.play()
            pygame.time.set_timer(CFG.SPAWN_METEOR_EVENT, random.randint(800, 1500))

    screen.blit(background, (0, 0))

    for meteor in meteors[:]:
        meteor.draw(screen)
        meteor.fall()

        if meteor.rect.top >= CFG.HEIGHT:
            meteors.remove(meteor)
        elif player.alive and meteor.rect.colliderect(player.rect):
            player.deadSound.play()
            player.alive = False
            meteors.remove(meteor)

    keys = pygame.key.get_pressed()

    if player.alive:
        player.move(keys)
        player.draw(screen)
    else:
        screen.blit(shade, (0, 0))
        screen.blit(text_surf, text_rect)

    pygame.display.flip()
    clock.tick(CFG.FPS)
