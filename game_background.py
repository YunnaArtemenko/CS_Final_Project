import pygame
from time import sleep
import random

def Fishing_Line(button_pressed):
	screen = pygame.display.set_mode((500, 500))
	x = y = 250
	UC = (250, 0)
	WHITE = (255, 255, 255)
	BACKGROUND = (77, 148, 255)
	
	if button_pressed != True:
		print("LEMON")
		
	while button_pressed == True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break
		elif event.type == pygame.MOUSEMOTION:
			x, y = event.pos
			
		screen.fill(BACKGROUND)
		pygame.draw.line(screen, WHITE, UC, (x, y))
		pygame.display.flip()
		

	if random.randint(0,1) == 0:
		#led_on()
		print("You got a fish!")
	else:
		print("Better luck next time!")
	
button_pressed = True

Fishing_Line(button_pressed)