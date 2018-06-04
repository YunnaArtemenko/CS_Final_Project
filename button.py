from gpiozero import Button

button = Button(16)

def button_pressed():
    button.wait_for_press
    return True
button_pressed()

