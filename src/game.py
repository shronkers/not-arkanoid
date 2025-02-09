import pygame
from player import Player
from block import Block
from ball import Ball
from consts import BLOCKS_GROUP, BALL_GROUP, WIDTH, HEIGHT, FONT


class Game:
	def __init__(self, rows: int):
		self.player = Player(movespeed=300)
		BLOCKS_GROUP.add(self.player.sprite)
		self.blocks = [[Block(y, x) for x in range(12)] for y in range(rows)]
		self.ball = Ball(WIDTH // 2, HEIGHT - 150, 240)
		self.win_condition = False
		self.score = 0
		self.prevlen = len(BLOCKS_GROUP)
		self.paused = False

	def draw(self, sc: pygame.Surface):
		BLOCKS_GROUP.draw(sc)
		BALL_GROUP.draw(sc)
		if len(BLOCKS_GROUP) < self.prevlen:
			self.score += 10
		self.prevlen = len(BLOCKS_GROUP)
		if not self.paused:
			text_surface = FONT.render(f"{self.score}", True, "white")
			sc.blit(text_surface, (10, 250))
		# only the player left
		if len(BLOCKS_GROUP.sprites()) == 1:
			self.win_condition = True