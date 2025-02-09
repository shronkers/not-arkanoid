import pygame
import os
import sys
from random import randint


pygame.init()
pygame.display.set_caption("not-arkanoid")
from consts import *
screen = pygame.display.set_mode((WIDTH, HEIGHT))


from block import Block
from ball import Ball
from game import Game
from menu import Menu
from player import Player


if __name__ == "__main__":
	running = True
	paused = False
	clock = pygame.time.Clock()
	in_menu = True
	game = Game(1)
	menu = Menu()

	while running:
		# seconds
		dt = clock.tick(FPS) / 1000
		screen.fill("black")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if in_menu:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						menu.selected_button = (menu.selected_button + 1) % 3
					if event.key == pygame.K_UP:
						menu.selected_button = (menu.selected_button - 1) % 3
					if event.key == pygame.K_RETURN:
						if menu.selected_button == 0:
							in_menu = False
						elif menu.selected_button == 1:
							running = False
						else:
							# score menu
							pass
		keystate = pygame.key.get_pressed()
		if in_menu:
			menu.draw(screen)
			pygame.display.flip()
			continue
		if game.win_condition:
			running = False
		if keystate[pygame.K_ESCAPE]:
			paused = not paused
		if paused:
			game.draw(screen)
			pygame.display.flip()
			continue
		if keystate[pygame.K_LEFT]:
			game.player.move(-dt)
		elif keystate[pygame.K_RIGHT]:
			game.player.move(dt)
		game.ball.move(dt)
		game.draw(screen)
		pygame.display.flip()
	pygame.display.quit()
	pygame.quit()
	sys.exit()
