header = "Welcome to REPL! We hope you enjoy your stay!"
footer = "Thanks for visiting the REPL today!"

scope_vars = {"answer": 42}

try:
    import IPython
except ImportError:
    from code import InteractiveConsole
    InteractiveConsole(locals=scope_vars).interact(header, footer)
else:
    print(header)
    IPython.start_ipython(argv=[], user_ns=scope_vars)
    print(footer)
