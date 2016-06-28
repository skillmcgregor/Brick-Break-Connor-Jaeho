import pygame
import sys
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.music.load("dundertale.mp3")
pygame.mixer.music.play()

size = width,height = 1200,1000
bspeed = [5,5]
pspeed = [0,0]
white = (25,247,244)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball,(30,30))
ballrect = ball.get_rect()



paddle = pygame.image.load("rectang.png")



paddlerect = paddle.get_rect()
lasttime = 0
lasttime2 = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				pspeed = [pspeed[0] + 5, pspeed[1]]
		if event.type == pygame. KEYUP:
			if event.key == pygame.K_RIGHT:
				pspeed = [0,0]
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pspeed = [pspeed[0] - 5, pspeed[1]]
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				pspeed = [0,0]
	if (pygame.time.get_ticks() - lasttime > 10):
		ballrect = ballrect.move(bspeed)
		lasttime = pygame.time.get_ticks()
	
	if (pygame.time.get_ticks() - lasttime2 > 10):
		paddlerect = paddlerect.move(pspeed)
		lasttime2 = pygame.time.get_ticks()
		

	if ballrect.left < 0 or ballrect.right > width:
		bspeed[0] = -bspeed[0]
	if ballrect.bottom > height:
		bspeed[1] = -bspeed[1]
	if ballrect.colliderect(paddlerect):
		bspeed[1] = -bspeed[1]
	

	screen.fill(white)
	screen.blit(paddle,paddlerect)
	screen.blit(ball, ballrect)
	pygame.display.flip()
