import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.utils.constants import SMALL_CACTUS_Y_POS, LARGE_CACTUS_Y_POS, BIRD_Y_POS

list_obstacles = [
                        Cactus(SMALL_CACTUS ),
                        Cactus(LARGE_CACTUS),
                        Bird(BIRD) 
                ]

class ObstacleManager:
        def __init__(self):
                self.obstacles = []

        def update(self, game):
                if len(self.obstacles) == 0:
                        random_obstacles = random.randint(0,2)
                        self.obstacles.append(list_obstacles[random_obstacles])
                
                for obstacle in self.obstacles:
                        obstacle.update(game.game_speed, self.obstacles)

                        if game.player.dino_rect.colliderect(obstacle.rect):
                                pygame.time.delay(500)
                                game.playing = False
                                break
        
        def draw(self, screen):
                for obstacle in self.obstacles:
                        obstacle.draw(screen)