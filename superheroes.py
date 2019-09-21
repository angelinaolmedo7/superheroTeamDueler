"""Superheroes."""
import random


class Ability:
    """Create ability class."""

    def __init__(self, name, attack_strength):
        """
        Create instance variables.

        name: string
        max_damage; integer
        """
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        """
        Return a damage value.

        Damage between 0 and the value set by self.max_damage.
        """
        return random.randint(0, self.max_damage)


if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
