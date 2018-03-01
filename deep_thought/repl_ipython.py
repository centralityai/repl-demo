import IPython

header = "Welcome to REPL! We hope you enjoy your stay!"
footer = "Thanks for visiting the REPL today!"

scope_vars = {"answer": 42}

print(header)
IPython.start_ipython(argv=[], user_ns=scope_vars)
print(footer)
