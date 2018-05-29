import pygame

def Game_Background():
	screen = pygame.display.set_mode((500, 500))
	ULcorner = (0, 0)
	LLcorner = (0, 500)
	URcorner = (500, 0)
	LRcorner = (500, 500)
	Center = (250, 250)
	LC = (0, 250)
	RC = (500, 250)
	UC = (250, 0)
	DC = (250, 500)

	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break
		screen.fill((77, 148, 255))
		pygame.display.flip()
	return

def Fishing_Line(BUTTON):
	if button_pressed == True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break
		elif event.type == pygame.MOUSEMOTION:
			x, y = event.pos
		
		pygame.draw.line(screen, (0, 0, 0), UC, (x, y))
		pygame.display.flip()