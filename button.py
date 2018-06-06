from gpiozero import Button

button = Button(16)

def button_pressed():
    button.wait_for_press
    print ("True")
    return True
button_pressed()

def button_released():
    button.wait_for_release
    print ("True")
    return True
button_released()     
    

