import pygame
from consts import PRELOADED_SPRITES, WIDTH, HEIGHT


# player class
class Player:
	def __init__(self, movespeed):
		self.x = WIDTH // 2
		self.y = HEIGHT - 30
		self.movespeed = movespeed
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = PRELOADED_SPRITES["player"]
		self.rect = pygame.Rect(self.x - 25, self.y - 5, 50, 10)
		self.sprite.rect = self.rect

	# move player position based on dt
	def move(self, dx):
		nx = self.x + dx * self.movespeed
		if 35 < nx < WIDTH - 35:
			self.x = nx
		self.update_rect()

	# update player's hitbox
	def update_rect(self):
		self.rect = pygame.Rect(self.x - 25, self.y - 5, 50, 10)
		self.sprite.rect = pygame.Rect(self.x - 25, self.y - 5, 50, 10)