import pygame
import Config as CFG

class Player:
    def __init__(self):
        self.speed = CFG.PLAYER_SPEED
        self.sprite = pygame.image.load(CFG.PLAYER_SPRITE).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.midbottom = (CFG.WIDTH // 2, CFG.HEIGHT - 20)
        self.alive = True
        self.deadSound = pygame.mixer.Sound(CFG.PLAYER_DEATH_SOUND)

    def move(self, keys):
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect = self.rect.move(-self.speed, 0)
        elif keys[pygame.K_d] and self.rect.right < CFG.WIDTH:
            self.rect = self.rect.move(self.speed, 0)

    def draw(self, surface):
        surface.blit(self.sprite, self.rect.topleft)
