import pygame

class Wall:
    def __init__(self, x, y, breakable=True):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (0, 0, 255) if breakable else (0, 255, 0)
        self.breakable = breakable

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def is_collision(self, player_rect):
        return self.rect.colliderect(player_rect)
