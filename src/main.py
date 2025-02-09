import pygame
import sys
from game import Game
from menu import Menu
from scoremenu import ScoreMenu


pygame.init()
pygame.display.set_caption("not-arkanoid")
from consts import FPS, WIDTH, HEIGHT, FONT, SCORE_DB
screen = pygame.display.set_mode((WIDTH, HEIGHT))


if __name__ == "__main__":
	running = True
	clock = pygame.time.Clock()
	in_menu = True
	score_menu = None
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
							in_menu = False
							score_menu = ScoreMenu()
							pass
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					if score_menu is not None:
						score_menu = None
						in_menu = True
					game.paused = not game.paused
		keystate = pygame.key.get_pressed()
		if in_menu:
			menu.draw(screen)
			pygame.display.flip()
			continue
		if score_menu is not None:
			score_menu.draw(screen)
			pygame.display.flip()
			continue
		if game.win_condition:
			SCORE_DB.execute(f"INSERT INTO scores VALUES (unixepoch(), {game.score})")
			SCORE_DB.commit()
			running = False
		if game.paused:
			game.draw(screen)
			text_surface = FONT.render("PAUSED", True, "white")
			screen.blit(text_surface, (10, 250))
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
	SCORE_DB.close()
	pygame.quit()
	sys.exit()
