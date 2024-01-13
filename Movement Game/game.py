import pygame, sys
from pygame.locals import *
from bullet import Bullet
from wall import Wall
from map import GameMap

WIDTH, HEIGHT = 800, 800
TITLE = "Block shooting"


# pygame initialization
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# main player class
class Player:

  # initializes the player attributes and position
  def __init__(self, x, y):
    self.x = int(x)
    self.y = int(y)
    self.rect = pygame.Rect(self.x, self.y, 32, 32)
    self.color = (255, 255, 255)
    self.velX = 0
    self.velY = 0
    self.left_pressed = False
    self.right_pressed = False
    self.up_pressed = False
    self.down_pressed = False
    self.speed = 4
    self.is_shooting = False
    self.bullets = []
    self.game_map = game_map

  # draws the player
  def draw(self, win):
    pygame.draw.rect(win, self.color, self.rect)
    for bullet in self.bullets:
      bullet.draw(win)

  # defines the updates for player position based on key press as well as shooting logic
  # LONG FUNCTION MIGHT UPDATE
  def update(self):
    self.velX = 0
    self.velY = 0
    if self.left_pressed and not self.right_pressed:
      self.velX = -self.speed
    if self.right_pressed and not self.left_pressed:
      self.velX = self.speed
    if self.up_pressed and not self.down_pressed:
      self.velY = -self.speed
    if self.down_pressed and not self.up_pressed:
      self.velY = self.speed
    
    # wall collision
    self.x += self.velX
    self.y += self.velY
    # boundary of screen
    self.x = max(0, min(self.x, WIDTH - 32))
    self.y = max(0, min(self.y, HEIGHT - 32))
    self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    # shooting logic
    if self.is_shooting:
      self.shoot()
    bullets_to_remove = []
    for bullet in self.bullets:
      bullet.update()
      if bullet.lifespan <= 0:
        bullets_to_remove.append(bullet)
    for bullet in bullets_to_remove:
      self.bullets.remove(bullet)

    self.game_map.update(self)

  def shoot(self):
    mx, my = pygame.mouse.get_pos()
    bullet = Bullet(self.x + 16, self.y + 16, mx, my)
    self.bullets.append(bullet)

# player creation, map creation, clock
game_map = GameMap()
player = Player(WIDTH/2, HEIGHT/2)
clock = pygame.time.Clock()

# game loop to handle in game events
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # for movement and shooting key downs
    if event.type == KEYDOWN:
      if event.key == pygame.K_a:
        player.left_pressed = True
      if event.key == pygame.K_d:
        player.right_pressed = True
      if event.key == pygame.K_s:
        player.down_pressed = True
      if event.key == pygame.K_w:
        player.up_pressed = True
      if event.key == pygame.K_SPACE:
        player.is_shooting = True
    # for movement and shooting key release
    if event.type == KEYUP:
      if event.key == pygame.K_a:
        player.left_pressed = False
      if event.key == pygame.K_d:
        player.right_pressed = False
      if event.key == pygame.K_s:
        player.down_pressed = False
      if event.key == pygame.K_w:
        player.up_pressed = False
      if event.key == pygame.K_SPACE:
        player.is_shooting = False

  # draws player on window, updates player position and walls
  win.fill((12, 24, 36))
  game_map.draw(win)
  player.draw(win)
  player.update()

  pygame.display.flip()

  clock.tick(120)