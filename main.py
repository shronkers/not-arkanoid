import pygame
import os
import sys
from random import randint


FPS = 144
WIDTH = 800
HEIGHT = 600
BLOCKS_GROUP = pygame.sprite.Group()
BALL_GROUP = pygame.sprite.Group()
pygame.init()
FONT = pygame.font.Font("./assets/font.ttf", size=72)
pygame.display.set_caption("arkanoid")
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def load_image(name, colorkey=None):
	fullname = os.path.join('assets', name)
	# если файл не существует, то выходим
	if not os.path.isfile(fullname):
		print(f"Файл с изображением '{fullname}' не найден")
		sys.exit()
	image = pygame.image.load(fullname)
	if colorkey is not None:
		image = image.convert()
		if colorkey == -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey)
	else:
		image = image.convert_alpha()
	return image


PRELOADED_SPRITES = {
	"red": load_image("red.png"),
	"player": load_image("red.png"),
	"ball": load_image("ball.png")
}


class Block:
	def __init__(self, br, bc):
		self.is_super = randint(0, 149) in range(0, 10)
		self.is_alive = True
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = PRELOADED_SPRITES["red"]
		self.rect = pygame.Rect(35 + bc * (50 + 10), 35 + br * (10 + 10), 50, 10)
		self.sprite.rect = self.rect
		BLOCKS_GROUP.add(self.sprite)

	def get_rect(self):
		return self.rect


class Ball:
	def __init__(self, x, y, movespeed):
		self.x = x
		self.y = y
		self.vx = 240
		self.vy = movespeed
		self.not_colliding = True
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = PRELOADED_SPRITES["ball"]
		self.rect = pygame.Rect(x, y, 30, 30)
		self.sprite.rect = self.rect
		BALL_GROUP.add(self.sprite)

	def update_rect(self):
		self.rect.left = self.x
		self.rect.top = self.y

	def move(self, dt):
		self.x += self.vx * dt
		self.y += self.vy * dt
		if self.y < 15 or self.y + 15 >= HEIGHT:
			self.vy = -self.vy
		if self.x >= WIDTH - 15 or self.x < 15:
			self.vx = -self.vx
		if self.sprite is None:
			return
		coll = pygame.sprite.spritecollideany(self.sprite, BLOCKS_GROUP)
		if coll and self.not_colliding:
			self.not_colliding = False
			self.vy = -self.vy
			if coll.image != PRELOADED_SPRITES["player"]:
				BLOCKS_GROUP.remove(coll)
		if coll is None:
			self.not_colliding = True
		self.update_rect()


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


class Player:
	def __init__(self, movespeed):
		self.x = WIDTH // 2
		self.y = HEIGHT - 30
		self.movespeed = movespeed
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = PRELOADED_SPRITES["player"]
		self.rect = pygame.Rect(self.x - 25, self.y - 5, 50, 10)
		self.sprite.rect = self.rect

	def move(self, dx):
		nx = self.x + dx * self.movespeed
		if 35 < nx < WIDTH - 35:
			self.x = nx
		self.update_rect()

	def update_rect(self):
		self.rect = pygame.Rect(self.x - 25, self.y - 5, 50, 10)
		self.sprite.rect = pygame.Rect(self.x - 25, self.y - 5, 50, 10)


if __name__ == "__main__":
	running = True
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
						print("down", menu.selected_button)
					if event.key == pygame.K_UP:
						menu.selected_button = (menu.selected_button - 1) % 3
						print("up", menu.selected_button)
					if event.type == pygame.K_RETURN:
						in_menu = False
						print("here")
		keystate = pygame.key.get_pressed()
		if in_menu:
			menu.draw(screen)
			pygame.display.flip()
			continue
		if game.win_condition:
			running = False
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
