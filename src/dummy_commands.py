
from command_handler import CommandHandler

# Use the same name as the real hander and the same
# command list so we can drop it in without other changes.
class R2L2Commands(CommandHandler):
    VALID_COMMANDS = [
        ["forward", "f", "go", "Move forward"],
        ["backward", "b", "Move backward"],
        ["left", "l", "Move left"],
        ["right", "r", "Move right"],
    ]

    # Override the base class method so we do nothing
    def call_method(self, *args):
        pass
