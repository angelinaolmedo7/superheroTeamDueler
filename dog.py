"""Dog class in python."""


class Dog:
    """Dog class."""

    def __init__(self, name, breed):
        """Dog initializes with a name and breed."""
        self.name = name
        self.breed = breed

    def bark(self):
        """Print 'woof' to the terminal."""
        print(self.name + ": Woof!")
