
from AlphaBot2 import AlphaBot2
from command_handler import CommandHandler

class R2L2Commands(CommandHandler):
    VALID_COMMANDS = [
        ["forward", "f", "Move forward"],
        ["backward", "b", "Move backward"],
        ["left", "l", "Move left"],
        ["right", "r", "Move right"],
    ]

    def setup(self):
        self.bot = AlphaBot2()
        self.bot.stop()

    def cleanup(self):
        self.bot.stop()
        AlphaBot2.gpio_cleanup()

    def forward(self):
        self.bot.forward()

    def backward(self):
        self.bot.backward()

    def left(self):
        self.bot.left()

    def right(self):
        self.bot.right()
