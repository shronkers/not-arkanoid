import pygame
from consts import FONT, PRELOADED_SPRITES


# main menu class
class Menu:
	def __init__(self):
		self.selected_button = 0
		self.clock = 0
		# cat animation frames
		self.frames = [
			PRELOADED_SPRITES["frame1"],
			PRELOADED_SPRITES["frame2"],
			PRELOADED_SPRITES["frame3"]
		]
		self.current_frame = 0

	# draws the main menu
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

		# cat animation controlled by a clock
		self.clock += 1
		if self.clock == 72:
			self.clock = 0
			self.current_frame = (self.current_frame + 1) % 3
		sc.blit(self.frames[self.current_frame], (400, 300))
