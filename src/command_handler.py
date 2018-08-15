
import time

#
# Base class for taking user input text and calling
# a method based on what the command is.
#
class CommandHandler(object):
    def __init__(self):
        self.setup()

    #
    # Takes a user command, calls the applicable method (maybe) and
    # returns an informational string that we expect the user to see.
    # TODO: Use proper logging instead of returning strings
    #
    def do_command(self, user_input):
        # Support passing extra params even though it's
        # not used for anything yet
        split_input = user_input.strip().lower().split()
        command, args = split_input[0], split_input[1:]

        # valid_commands returns a list of commands, each one like this:
        # ["methodname", "shortcut1", "shortcut2", ..., "Description"]
        for valid_command in self.valid_commands():
            if command in valid_command[0:-1]:
                self.call_method(valid_command[0], *args)
                return "Performed '{}'".format(valid_command[-1])

        return "Unknown command '{}'".format(command)

    def call_method(self, method_name, *args):
        # Assume a method with the right name is defined
        getattr(self, method_name)(*args)
        # In future this could configurable or done in a post-command
        # hook, but for now we sleep for a second after all commands
        time.sleep(1)

    def help(self):
        help_text = "Commands:\n"
        for valid_command in self.valid_commands():
            help_text += "  "
            help_text += " ".join([c for c in valid_command[0:-1]])
            help_text += " - " + valid_command[-1] + "\n"
        return help_text.rstrip()

    def valid_commands(self):
        if hasattr(self.__class__, 'VALID_COMMANDS'):
            return self.__class__.VALID_COMMANDS
        return []

    def setup(self):
        pass

    def cleanup(self):
        pass
