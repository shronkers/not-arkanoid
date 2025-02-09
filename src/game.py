import pygame
from player import Player
from block import Block
from ball import Ball
from consts import *


class Game:
	def __init__(self, rows: int):
		self.player = player = Player(movespeed=300)
		BLOCKS_GROUP.add(self.player.sprite)
		self.blocks = [[Block(y, x) for x in range(12)] for y in range(rows)]
		self.ball = Ball(WIDTH // 2, HEIGHT - 150, 240)
		self.win_condition = False

	def draw(self, sc: pygame.Surface):
		BLOCKS_GROUP.draw(sc)
		BALL_GROUP.draw(sc)
		# only the player left
		if len(BLOCKS_GROUP.sprites()) == 1:
			self.win_condition = True