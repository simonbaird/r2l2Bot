import RPi.GPIO as GPIO
from AlphaBot2 import AlphaBot2
import time

Ab = AlphaBot2()

try:
    while True:
        Ab.stop()
        user_input = raw_input("What should I do now?")
        if user_input == "forward":
                Ab.forward()
        elif user_input == "backward":
                Ab.backward()
        elif user_input == "left":
                Ab.left()
        elif user_input == "right":
                Ab.right()
        else:
                print("That command isnt valid.")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
