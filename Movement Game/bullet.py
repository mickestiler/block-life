# bullet.py

import pygame
import math

class Bullet:
    def __init__(self, x, y, target_x, target_y, speed=8, lifespan=60):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y
        self.speed = speed
        self.lifespan = lifespan
        self.color = (255, 0, 0)

    def update(self):
        angle = math.atan2(self.target_y - self.y, self.target_x - self.x)
        self.x += self.speed * math.cos(angle)
        self.y += self.speed * math.sin(angle)
        self.lifespan -= 1

    def draw(self, win):
        pygame.draw.line(win, self.color, (self.x, self.y), (self.x, self.y), 2)