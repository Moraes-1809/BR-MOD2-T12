import random

from dino_runner.utils.constants import BIRD, BIRD_Y_POS
from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,1)
        self.image = BIRD[0]
        self.step_index = 0
        super().__init__(images,self.type)

        self.rect.y = BIRD_Y_POS

    def fly(self):
         self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
         self.rect.y = BIRD_Y_POS
         self.step_index += 1
         if self.step_index >= 10:
            self.step_index = 0

    def update(self, game_speed, obstacles):
        self.fly()
        super().update(game_speed, obstacles)