from gpiozero import LED
from time import sleep

led = LED(26)

def led_on():
    led.on()
    sleep(4)
    led.off()

led_on()
  