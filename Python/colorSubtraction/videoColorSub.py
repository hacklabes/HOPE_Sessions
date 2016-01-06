import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys

camera = cv2.VideoCapture(0)
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([1280,720])

try:
	font = pygame.font.SysFont("tahoma", 50)
	text = font.render("Please step out of the Frame", 1, (0, 0, 0))
	textpos = text.get_rect()
	textpos.centerx = screen.get_rect().centerx
	screen.fill([255,255,255])
	screen.blit(text, textpos)

	text = font.render("Press any key to continue", 1, (0, 0, 0))
	textpos.centery = 200
	screen.blit(text, textpos)

	pygame.display.update()
	event = pygame.event.clear()
	while True:
		event = pygame.event.wait()
		if event.type == QUIT:
			sys.exit(0)
		elif event.type == KEYDOWN:
			break
	while True:
		ret, frame = camera.read()
		screen.fill([0,0,0])
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		frame = np.rot90(frame)
		frame = pygame.surfarray.make_surface(frame)
		screen.blit(frame, (0,0))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				sys.exit(0)
except KeyboardInterrupt,SystemExit:
    pygame.quit()
    cv2.destroyAllWindows()
