import pygame
from consts import FONT


class Menu:
	def __init__(self):
		self.selected_button = 0
		pass

	def draw(self, sc: pygame.Surface):
		text_surface = FONT.render("NOT ARKANOID", True, "green")
		sc.blit(text_surface, (10, 10))
		text_surface = FONT.render("PLAY", True, "green" if self.selected_button == 0 else "red")
		sc.blit(text_surface, (10, 210))
		text_surface = FONT.render("EXIT", True, "green" if self.selected_button == 1 else "red")
		sc.blit(text_surface, (10, 310))
		text_surface = FONT.render("SCORE", True, "green" if self.selected_button == 2 else "red")
		sc.blit(text_surface, (10, 410))
		pass