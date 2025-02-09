from consts import FONT


class LevelSelect:
	def __init__(self):
		self.selected_button = 0

	def draw(self, sc):
		draw_colors = [
			"green" if self.selected_button == x else "red"
			for x in range(3)
		]

		text_surface = FONT.render("SELECT LEVEL", True, "green")
		sc.blit(text_surface, (10, 10))
		text_surface = FONT.render("1", True, draw_colors[0])
		sc.blit(text_surface, (10, 210))
		text_surface = FONT.render("2", True, draw_colors[1])
		sc.blit(text_surface, (10, 310))
		text_surface = FONT.render("3", True, draw_colors[2])
		sc.blit(text_surface, (10, 410))