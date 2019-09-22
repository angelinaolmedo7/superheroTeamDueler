"""Class 'Animal'."""


class Animal:
    """Class 'Animal' can eat() and drink() and has a name."""

    def __init__(self, name):
        """Init with name."""
        self.name = name

    def eat(self):
        """Print {{name}} is eating."""
        print(self.name + ' is eating.')

    def drink(self):
        """Print {{name}} is drinking."""
        print(self.name + ' is drinking.')
