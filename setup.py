from setuptools import setup


setup(
    name="repl_demo",
    version="1.0.0",
    packages=["deep_thought"],

    install_requires=["click"],

    entry_points={
        "console_scripts": [
            "deep-thought = deep_thought.repl_cli:main",
        ],
    }
)
