from consts import FONT, SCORE_DB


# score menu class
class ScoreMenu:
	def __init__(self):
		self.scores = []
		self.query()
		pass

	# draws the top 3 scores
	def draw(self, sc):
		text_surface = FONT.render("TOP SCORES:", True, "green")
		sc.blit(text_surface, (10, 10))

		y_val = 210
		res = self.scores
		for i in range(len(res)):
			text_surface = FONT.render(f"{res[i][0]} - {res[i][1]}", True, "red")
			sc.blit(text_surface, (10, y_val))
			y_val += 100
		if len(res) == 0:
			text_surface = FONT.render("no scores yet :(", True, "yellow")
			sc.blit(text_surface, (10, y_val))

	# queries the SCORE_DB for top scores, saving the top 3
	def query(self):
		query = """SELECT date(dt, 'unixepoch'), score
					FROM scores
					ORDER BY score DESC"""
		self.scores = SCORE_DB.execute(query).fetchall()[:3]