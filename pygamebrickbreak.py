import pygame
import sys
import time
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(22000, 16, 2, 2049)
pygame.mixer.music.load("dundertale.mp3")
pygame.mixer.music.play(-1,0)

size = width,height = 600,1000
speed = [0,0]
pspeed = [0,0]
black = (70, 70, 70)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (153, 102, 255)
ggreen = (102, 255, 204)
gyul = (255, 153, 51)
pink = (255, 204, 255)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball,(30,30))
paddle = pygame.image.load("rectang.png")
ballrect = ball.get_rect()
paddlerect = paddle.get_rect()
lasttime = 0
lasttime2 = 0

colorlist = [[0 for x in range(20)] for y in range(6)]
for i in range(6):
	for j in range(20):
		wc = random.randint(1, 7)
		if wc == 1:
			colorlist[i][j] = 'red'
		elif wc == 2:
		 	colorlist[i][j] = 'green'
		elif wc == 3:
		 	colorlist[i][j] = 'blue'
		elif wc == 4:
		 	colorlist[i][j] = 'purple'
		elif wc == 5:
		 	colorlist[i][j] = 'ggreen'
		elif wc == 6:
		 	colorlist[i][j] = 'gyul'
		elif wc == 7:
		 	colorlist[i][j] = 'pink'

breaklist = [[1 for x in range(20)] for y in range(6)]
for i in range(6):
	for j in range(20):
		breaklist[i][j] = random.randint(1, 5)
		if j < 9:
			breaklist[i][j] = 1
 
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				if speed[:] == pspeed[:]:
					pspeed = [5, pspeed[1]]
					speed[:] = pspeed[:]
				else:
					pspeed = [5, pspeed[1]]
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				if pspeed[0] == -5:
					continue
				if speed[:] == pspeed[:]:
					pspeed = [0,0]
					speed[:] = pspeed[:]
				else:
					pspeed = [0,0]
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if speed[:] == pspeed[:]:
					pspeed = [-5, pspeed[1]]
					speed[:] = pspeed[:]
				else:
					pspeed = [-5, pspeed[1]]
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				if pspeed[0] == 5:
					continue
				if speed[:] == pspeed[:]:
					pspeed = [0,0]
					speed[:] = pspeed[:]
				else:
					pspeed = [0,0]
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if speed[:] == pspeed[:]:
					speed = [5,5]

	if (pygame.time.get_ticks() - lasttime > 10):
		ballrect = ballrect.move(speed)
		lasttime = pygame.time.get_ticks() #Update the timer so that it happens again in another 100 ticks

	if (pygame.time.get_ticks() - lasttime2 > 10):
		paddlerect = paddlerect.move(pspeed)
		lasttime2 = pygame.time.get_ticks()

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.bottom > height:
		speed[1] = -speed[1]
	if ballrect.colliderect(paddlerect):
		speed[1] = -speed[1]

	screen.fill(black)
	for i in range(6):
		for j in range(20):
			if j < 9:
				continue
			if colorlist[i][j] == 'red':
				pygame.draw.rect(screen, red, (i*100,j*50, 100,50))
			elif colorlist[i][j] == 'green':
				pygame.draw.rect(screen, green, (i*100,j*50, 100,50))
			elif colorlist[i][j] == 'blue':
				pygame.draw.rect(screen, blue, (i*100,j*50, 100,50))
			elif colorlist[i][j] == 'purple':
				pygame.draw.rect(screen, purple, (i*100,j*50, 100,50))
			elif colorlist[i][j] == 'ggreen':
				pygame.draw.rect(screen, ggreen, (i*100,j*50, 100,50))
			elif colorlist[i][j] == 'gyul':
				pygame.draw.rect(screen, gyul, (i*100,j*50, 100,50))
			elif colorlist[i][j] == 'pink':
				pygame.draw.rect(screen, pink, (i*100,j*50, 100,50))
			if breaklist[i][j] == 1:
				pygame.draw.rect(screen, black, (i*100,j*50, 100,50))
			else:
				if (ballrect.left == i*100+100 and j*50 <= ballrect.centery <= j*50+50) or (ballrect.right == i*100 and j*50 <= ballrect.centery <= j*50+50):
					speed[0] = -speed[0]
					pygame.draw.rect(screen, pink, (i*100,j*50, 100,50))
					breaklist[i][j] = 1
				if (ballrect.top == j*50+50 and i*100 <= ballrect.centerx <= i*100+100) or (ballrect.bottom == j*50 and i*100 <= ballrect.centerx <= i*100+100):
					speed[1] = -speed[1]
					pygame.draw.rect(screen, black, (i*100,j*50, 100,50))
					breaklist[i][j] = 1

	screen.blit(ball,ballrect)
	screen.blit(paddle,paddlerect)
	pygame.display.flip()