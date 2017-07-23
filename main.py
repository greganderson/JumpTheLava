import os
import pygame

fps = 60
image_size = 31
num_x_tiles = 30
num_y_tiles = 20

screen_size = (image_size * num_x_tiles, image_size * num_y_tiles)
done = False

pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

image_library = {}

def get_image(path):
	global image_library
	image = image_library.get(path)
	if image == None:
		canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
		image = pygame.image.load(canonicalized_path)
		image_library[path] = image
	return image

def draw_border(screen):
	row = 5
	col = 1

	(x, y) = get_grid_position(0, 0)

	bottom = 0
	while bottom < num_x_tiles:
		screen.blit(get_image('images/tileset.png'), get_grid_position(bottom, y), get_tileset_image(row, col))
		bottom += 1

	(x, y) = get_grid_position(0, num_y_tiles - 1)

	top = 0
	while top < num_x_tiles:
		screen.blit(get_image('images/tileset.png'), get_grid_position(top, y), get_tileset_image(row, col))
		top += 1

	(x, y) = get_grid_position(0, 0)

	left = 0
	while left < num_y_tiles:
		screen.blit(get_image('images/tileset.png'), get_grid_position(x, left), get_tileset_image(row, col))
		left += 1

	(x, y) = get_grid_position(num_x_tiles, 0)

	right = 0
	while right < num_y_tiles:
		screen.blit(get_image('images/tileset.png'), get_grid_position(x, right), get_tileset_image(row, col))
		right += 1

def draw_level(screen):
	draw_border(screen)

	#screen.blit(get_image('images/tileset.png'), (x, y + image_size * right), get_tileset_image(0, 0))

def get_grid_position(row, col):
	return (image_size * col, (screen_size[1] - (image_size * (row + 1))))

def get_tileset_image(row, col):
	return (image_size * col + 1, image_size * row, image_size, image_size)


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill((255, 255, 255))

	draw_level(screen)

	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]: y -= 3
	if pressed[pygame.K_DOWN]: y += 3
	if pressed[pygame.K_LEFT]: x -= 3
	if pressed[pygame.K_RIGHT]: x += 3


	pygame.display.flip()
	clock.tick(fps)
