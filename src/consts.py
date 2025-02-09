import pygame
import os
import sqlite3
import sys


# this module has various constants needed for the game


PROGRAM_FOLDER_PATH = "/".join(sys.path[0].split("/"))


# function to load image from file
def load_image(name, colorkey=None):
	fullname = os.path.join(f'{PROGRAM_FOLDER_PATH}/../assets', name)
	# если файл не существует, то выходим
	if not os.path.isfile(fullname):
		print(f"Файл с изображением '{fullname}' не найден")
		sys.exit()
	image = pygame.image.load(fullname)
	""" this is commented out because it broke for no reason
	and it is not needed
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
FONT = pygame.font.Font(f"{PROGRAM_FOLDER_PATH}/../assets/font.ttf", size=72)

PRELOADED_SPRITES = {
	"red": load_image("red.png"),
	"player": load_image("green.png"),
	"ball": load_image("ball.png"),
	"frame1": load_image("frame1.jpg"),
	"frame2": load_image("frame2.jpg"),
	"frame3": load_image("frame3.jpg")
}

# score db setup
SCORE_DB = sqlite3.connect("score.sqlite")
SCORE_DB.execute("""
CREATE TABLE IF NOT EXISTS scores (
	dt INTEGER,
	score INTEGER
);
""")