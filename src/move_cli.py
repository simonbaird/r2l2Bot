# -*- coding: utf-8 -*-

from r2l2_commands import R2L2Commands
#from dummy_commands import R2L2Commands

commands = R2L2Commands()

#prompt = ">> "
prompt = "🤖> "

try:
    while True:
        user_input = raw_input(prompt).strip().lower()
        # help and exit are special commands that we handle here directly
        if user_input in ['help', 'h', '?']:
            print(commands.help())
            print("  help h ? - Help")
            print("  exit x q Ctrl-C - Exit")
        elif user_input in ['exit', 'x', 'q']:
            print("Bye")
            break
        # Other commands are passed through to the command handler
        else:
            print(commands.do_command(user_input))

except KeyboardInterrupt:
    print("\nBye")
finally:
    commands.cleanup()
