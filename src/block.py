import pygame
from random import randint
from consts import PRELOADED_SPRITES, BLOCKS_GROUP


class Block:
	def __init__(self, br, bc):
		self.is_super = randint(0, 149) in range(0, 10)
		self.is_alive = True
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = PRELOADED_SPRITES["red"]
		self.rect = pygame.Rect(35 + bc * (50 + 10), 35 + br * (10 + 10), 50, 10)
		self.sprite.rect = self.rect
		BLOCKS_GROUP.add(self.sprite)

	def get_rect(self):
		return self.rect