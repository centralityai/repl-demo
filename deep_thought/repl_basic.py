from code import InteractiveConsole

header = "Welcome to REPL! We hope you enjoy your stay!"
footer = "Thanks for visiting the REPL today!"

scope_vars = {"answer": 42}

InteractiveConsole(locals=scope_vars).interact(header, footer)
