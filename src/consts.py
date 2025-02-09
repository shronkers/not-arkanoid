import pygame
import os


def load_image(name, colorkey=None):
	fullname = os.path.join('../assets', name)
	# если файл не существует, то выходим
	if not os.path.isfile(fullname):
		print(f"Файл с изображением '{fullname}' не найден")
		sys.exit()
	image = pygame.image.load(fullname)
	"""
	if colorkey is not None:
		image = image.convert()
		if colorkey == -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey)
	else:
		image = image.convert_alpha()
	"""
	return image


FPS = 144
WIDTH = 800
HEIGHT = 600
BLOCKS_GROUP = pygame.sprite.Group()
BALL_GROUP = pygame.sprite.Group()
FONT = pygame.font.Font("../assets/font.ttf", size=72)

PRELOADED_SPRITES = {
	"red": load_image("red.png"),
	"player": load_image("red.png"),
	"ball": load_image("ball.png")
}
