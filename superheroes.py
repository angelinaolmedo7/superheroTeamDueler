"""Superheroes."""
import random


class Ability:
    """Create ability class."""

    def __init__(self, name, max_damage):
        """
        Create instance variables.

        name: string
        max_damage; integer
        """
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        """
        Return a damage value.

        Damage between 0 and the value set by self.max_damage.
        """
        return random.randint(0, self.max_damage)


class Armor:
    """Create armor class."""

    def __init__(self, name, max_block):
        """
        Instantiate instance properties.

        name: String
        max_block: Integer
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        """Return a block value.

        Block between 0 and max_block damage.
        """
        return random.randint(0, self.max_block)


class Hero:
    """Create Hero class."""

    def __init__(self, name, starting_health=100):
        """Instantiate instance properties.

        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer
        """
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
    armor = Armor("Shield", 12)
    print(armor.name)
    print(armor.block())

    my_hero = Hero("Super Tahoe", 200)
    print(my_hero.name)
    print(my_hero.current_health)
