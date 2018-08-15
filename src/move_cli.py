from AlphaBot2 import AlphaBot2
import time

Ab = AlphaBot2()

try:
    while True:
        Ab.stop()
        user_input = raw_input("What should I do now?")
        if user_input == "forward" or user_input.lower() == "f":
            Ab.forward()
        elif user_input == "backward" or user_input.lower() == "b" :
            Ab.backward()
        elif user_input == "left" or user_input.lower() == "l":
            Ab.left()
        elif user_input == "right" or user_input.lower() == "r":
            Ab.right()
        elif user_input == "x":
            raise KeyboardInterrupt
        else:
            print("That command isnt valid. Please try f=forward, b=backwards, l=left, r=right or x to exit.")
        time.sleep(1)
except KeyboardInterrupt:
    AlphaBot2.gpio_cleanup()
