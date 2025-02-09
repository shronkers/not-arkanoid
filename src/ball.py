import pygame
from consts import *


class Ball:
	def __init__(self, x, y, movespeed):
		self.x = x
		self.y = y
		self.vx = 240
		self.vy = movespeed
		self.not_colliding = True
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = PRELOADED_SPRITES["ball"]
		self.rect = pygame.Rect(x, y, 30, 30)
		self.sprite.rect = self.rect
		BALL_GROUP.add(self.sprite)

	def update_rect(self):
		self.rect.left = self.x
		self.rect.top = self.y

	def move(self, dt):
		self.x += self.vx * dt
		self.y += self.vy * dt
		if self.y < 15 or self.y + 15 >= HEIGHT:
			self.vy = -self.vy
		if self.x >= WIDTH - 15 or self.x < 15:
			self.vx = -self.vx
		if self.sprite is None:
			return
		coll = pygame.sprite.spritecollideany(self.sprite, BLOCKS_GROUP)
		if coll and self.not_colliding:
			self.not_colliding = False
			self.vy = -self.vy
			if coll.image != PRELOADED_SPRITES["player"]:
				BLOCKS_GROUP.remove(coll)
		if coll is None:
			self.not_colliding = True
		self.update_rect()