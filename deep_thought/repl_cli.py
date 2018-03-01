import click


class DeepThought:
    def __init__(self, host):
        super().__init__()
        self.host = host

    @property
    def answer(self):
        print(f"Connecting to {self.host}...")
        return 42


@click.command()
@click.option("--host", default="localhost", help="Host to connect to.")
def main(host):
    header = "Deep Thought initialised as `cpu`.  Type `help(cpu)` for assistance."
    footer = ""

    scope_vars = {"cpu": DeepThought(host)}

    try:
        import IPython
    except ImportError:
        from code import InteractiveConsole
        InteractiveConsole(locals=scope_vars).interact(header, footer)
    else:
        print(header)
        IPython.start_ipython(argv=[], user_ns=scope_vars)
        print(footer)


if __name__ == "__main__":
    main()
