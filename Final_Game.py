import pygame 
from gpiozero import Button, LED
import random
import game_background.py
import button.py
import LED.py

if __name__ == '__main__':
	while True:
		button_pressed()
		button_released()
		Fishing_Line()
		led_on()
		