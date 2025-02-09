import pygame
import sys


pygame.init()
from consts import PROGRAM_FOLDER_PATH as PFP
from consts import FPS, WIDTH, HEIGHT, FONT, SCORE_DB


from game import Game
from menu import Menu
from scoremenu import ScoreMenu
from levelselect import LevelSelect


pygame.display.set_caption("not-arkanoid")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


if __name__ == "__main__":
	running = True
	clock = pygame.time.Clock()
	in_menu = True
	score_menu = None
	level_menu = None
	game = None
	menu = Menu()

	pygame.mixer.music.load(f"{PFP}/../assets/bloop.wav")
	pygame.mixer.music.set_volume(0.1)

	while running:
		dt = clock.tick(FPS) / 1000
		screen.fill("#0e1621")
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if in_menu:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						menu.selected_button = (menu.selected_button + 1) % 3
						pygame.mixer.music.play()
					if event.key == pygame.K_UP:
						menu.selected_button = (menu.selected_button - 1) % 3
						pygame.mixer.music.play()
					if event.key == pygame.K_RETURN:
						if menu.selected_button == 0:
							in_menu = False
							level_menu = LevelSelect()
							enter_pressed = True
						elif menu.selected_button == 1:
							running = False
						else:
							# score menu
							in_menu = False
							score_menu = ScoreMenu()
							pass
						pygame.mixer.music.play()
			if level_menu is not None:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						level_menu.selected_button = (level_menu.selected_button + 1) % 3
						pygame.mixer.music.play()
					if event.key == pygame.K_UP:
						level_menu.selected_button = (level_menu.selected_button - 1) % 3
						pygame.mixer.music.play()
					if event.key == pygame.K_RETURN and not enter_pressed:
						if level_menu.selected_button == 0:
							game = Game(1)
							level_menu = None
						elif level_menu.selected_button == 1:
							game = Game(5)
							level_menu = None
						else:
							game = Game(10)
							level_menu = None
						pygame.mixer.music.play()
				if event.type == pygame.KEYUP:
					enter_pressed = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					if score_menu is not None or level_menu is not None:
						score_menu = None
						level_menu = None
						in_menu = True
					elif game is not None:
						game.paused = not game.paused
					pygame.mixer.music.play()
				if event.key == pygame.K_RETURN:
					if game is not None and game.paused:
						running = False
		keystate = pygame.key.get_pressed()
		if in_menu:
			menu.draw(screen)
			pygame.display.flip()
			continue
		if score_menu is not None:
			score_menu.draw(screen)
			pygame.display.flip()
			continue
		if level_menu is not None:
			level_menu.draw(screen)
			pygame.display.flip()
			continue
		if game.win_condition:
			SCORE_DB.execute(f"INSERT INTO scores VALUES (unixepoch(), {game.score})")
			SCORE_DB.commit()
			in_menu = True
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
