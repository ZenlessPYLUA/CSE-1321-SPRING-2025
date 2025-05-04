import pygame
import random
import Config as CFG


class Meteor:
    def __init__(self):
        self.type = random.choice(["big", "medium", "small", "tiny"])
        self.speed = CFG.METEOR_SPEEDS[self.type]

        image_path = random.choice(CFG.METEOR_IMAGES[self.type])
        self.sprite = pygame.image.load(image_path).convert_alpha()
        self.rect = self.sprite.get_rect()

        self.spawn_sound = pygame.mixer.Sound(random.choice(CFG.SPAWN_SOUNDS))

        self.rect.top = 0
        self.rect.left = random.randint(0, CFG.WIDTH - self.rect.width)

    def fall(self):
        self.rect = self.rect.move(0, self.speed)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect.topleft)
