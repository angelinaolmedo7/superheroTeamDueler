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

    def add_ability(self, ability):
        """Add ability to abilities list."""
        self.abilities.append(ability)

    def attack(self):
        """
        Calculate the total damage from all ability attacks.

        return: total:Int
        """
        dmg = 0
        for abl in self.abilities:
            dmg += abl.attack()
        return dmg

    def add_armor(self, armor):
        """Add armor to armors list."""
        self.armors.append(armor)

    def defend(self):
        """
        Calculate the total damage blocked from all armors.

        return: total:Int
        """
        bl = 0
        for bl in self.armors:
            bl += bl.block()
        return bl

    def take_damage(self, damage):
        """Update self.current_health with damage-defense."""
        dmg = self.defend()-damage
        if dmg < 0:
            self.current_health += dmg

    def is_alive(self):
        """Check whether the hero is alive and return true or false."""
        return self.current_health > 0


if __name__ == "__main__":
    hero = Hero("Super Tahoe", 200)
    print(hero.name + ", HP: " + str(hero.current_health))
    ability = Ability("Sonic Bark", 50)
    hero.add_ability(ability)
    armor = Armor("Tough Fur", 30)
    hero.take_damage(ability.attack())
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
