import pygame
from consts import FONT


class Menu:
	def __init__(self):
		self.selected_button = 0
		pass

	def draw(self, sc: pygame.Surface):
		draw_colors = [
			"green" if self.selected_button == x else "red"
			for x in range(3)
		]

		text_surface = FONT.render("NOT ARKANOID", True, "green")
		sc.blit(text_surface, (10, 10))
		text_surface = FONT.render("PLAY", True, draw_colors[0])
		sc.blit(text_surface, (10, 210))
		text_surface = FONT.render("EXIT", True, draw_colors[1])
		sc.blit(text_surface, (10, 310))
		text_surface = FONT.render("SCORE", True, draw_colors[2])
		sc.blit(text_surface, (10, 410))
		pass