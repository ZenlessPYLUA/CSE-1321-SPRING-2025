import pygame


WIDTH = 480
HEIGHT = 800
FPS = 60

BLACK = (0,0,0)
WHITE = (255,255,255)

SPAWN_METEOR_EVENT = pygame.USEREVENT + 1

PLAYER_SPEED = 12
PLAYER_SPRITE = "img/player_sprite.png"
PLAYER_DEATH_SOUND = "audio/player_dead.ogg"

METEOR_SPEEDS = {
    "big": 10,
    "medium": 11,
    "small": 12,
    "tiny": 12
}

METEOR_IMAGES = {
    "big": [
        "img/meteor_big_1.png",
        "img/meteor_big_2.png",
        "img/meteor_big_3.png",
        "img/meteor_big_4.png"
    ],
    "medium": [
        "img/meteor_med_1.png",
        "img/meteor_med_2.png"
    ],
    "small": [
        "img/meteor_small_1.png",
        "img/meteor_small_2.png"
    ],
    "tiny": [
        "img/meteor_tiny_1.png",
        "img/meteor_tiny_2.png"
    ]
}

SPAWN_SOUNDS = [
    "audio/spawn_sound_1.ogg",
    "audio/spawn_sound_2.ogg",
    "audio/spawn_sound_3.ogg"
]
