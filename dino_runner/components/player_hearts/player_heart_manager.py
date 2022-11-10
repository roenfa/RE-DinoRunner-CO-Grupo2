import pygame
from dino_runner.utils.constants import HEART_COUNT
from dino_runner.components.player_hearts.heart import Heart

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT
        self.restHearth = pygame.mixer.Sound("dino_runner/components/-vida.mp3")
    def draw(self, screen):
        x_position = 10
        y_position = 20
        for counter in range(self.heart_count): # 0,1,2,3,4 -> 5 - 1
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30
    
    def reduce_heart(self):
        self.heart_count -= 1
        self.restHearth.play()