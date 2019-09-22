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
        print('Attacking with {}.'.format(self.name))
        return random.randint(0, self.max_damage)


class Weapon(Ability):
    """The Weapon class is a type of Ability."""

    def attack(self):
        """Return a damage value between 50% and 100% of self.max_damage."""
        return random.randint(self.max_damage//2, self.max_damage)


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
        deaths: Integer
        kills: Integer
        """
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        """Add ability to abilities list."""
        self.abilities.append(ability)
        print('{} now has {}.'.format(self.name, ability.name))

    def add_weapon(self, weapon):
        """Add a weapon to abilities list."""
        self.abilities.append(weapon)
        print('{} now has {}.'.format(self.name, weapon.name))

    def attack(self):
        """
        Calculate the total damage from all ability attacks.

        return: total:Int
        """
        dmg = 0
        for abl in self.abilities:
            dmg += abl.attack()
            print('{} | {}'.format(abl.name, dmg))
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
        for arm in self.armors:
            bl += arm.block()
        return bl

    def take_damage(self, damage):
        """Update self.current_health with damage-defense."""
        dmg = self.defend()-damage
        if dmg < 0:
            self.current_health += dmg

    def is_alive(self):
        """Check whether the hero is alive and return true or false."""
        return self.current_health > 0

    def revive(self):
        """Reset health."""
        self.current_health = self.starting_health

    def fight(self, opponent):
        """Fight between hero and opponent."""
        print('A fight is beginning between ' + self.name + ' and ' +
              opponent.name + '!')
        # choose first attacker
        fighter = random.randint(0, 1)
        rounds = 0
        while self.is_alive() and opponent.is_alive() and rounds < 200:
            if fighter == 0:
                damage = self.attack()
                print(damage)
                opponent.take_damage(damage)
                fighter = 0
            else:
                damage = opponent.attack()
                print(damage)
                self.take_damage(damage)
                fighter = 1
            print('{}: {} HP | {}: {} HP'.
                  format(self.name, self.current_health,
                         opponent.name, opponent.current_health))
            rounds += 1
        if (self.is_alive()):
            self.add_kills()
            opponent.add_deaths()
            print(self.name + ' won!')
        elif (opponent.is_alive()):
            self.add_deaths()
            opponent.add_kills()
            print(opponent.name + ' won!')
        else:
            print('Draw!')

    def add_kills(self, num_kills=1):
        """Update kills with num_kills."""
        self.kills += num_kills

    def add_deaths(self, num_deaths=1):
        """Update deaths with num_deaths."""
        self.deaths += num_deaths


class Team:
    """A list of heroes."""

    def __init__(self, name):
        """Instantiate instance properties.

        name: String
        heroes: List of Hero objects
        """
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        """Add a hero to the team."""
        self.heroes.append(hero)

    def remove_hero(self, hero):
        """Remove Hero object from heores list by object passed in."""
        if hero in self.heroes:
            self.heroes.remove(hero)
        else:
            return 0

    def remove_hero_by_name(self, hero_name):
        """Remove Hero object from heores list by name passed in."""
        for hero in self.heroes:
            if hero.name == hero_name:
                self.remove_hero(hero)
        return 0

    def view_all_heroes(self):
        """Print all hero names in list."""
        rtn = ""
        if len(self.heroes) > 0:
            for hero in self.heroes:
                rtn += hero.name + ', '
            print(rtn[:-2])
        else:
            print('No heroes on the team {}!'.format(self.name))

    def revive_heroes(self):
        """Reset health of all heroes in the team."""
        for hero in self.heroes:
            hero.revive()

    def any_alive(self):
        """Return true if any heroes on the team are alive."""
        for hero in self.heroes:
            if hero.is_alive():
                return True
        return False

    def list_living(self):
        """Return a list of living heroes."""
        living = []
        for hero in self.heroes:
            if hero.is_alive():
                living.append(hero)
        return living

    def attack(self, other_team):
        """Battle each team against eachother."""
        print('A fight is beginning between {} and {}!'
              .format(self.name, other_team.name))
        while self.any_alive() and other_team.any_alive():
            random.choice(self.list_living()).fight(
                random.choice(other_team.list_living()))
        if self.any_alive():
            print('{} won!'.format(self.name))
        else:
            print('{} won!'.format(other_team.name))

    def stats(self):
        """Print K/D stats for each hero in the team."""
        for hero in self.heroes:
            print('{} | Kills: {} | Deaths: {}'.
                  format(hero.name, hero.kills, hero.deaths))


if __name__ == '__main__':
    hero = Hero('Superdog Tahoe', 200)
    hero2 = Hero('Supercat Lilac', 200)
    hero.add_ability(Ability('Sonic Bark', 50))
    hero.add_armor(Armor('Tough Fur', 30))
    hero2.add_ability(Ability('Sharp Claws', 50))
    hero2.add_armor(Armor('Whisker Shield', 30))

    team = Team('Cool Team')
    team.add_hero(hero)
    team.add_hero(hero2)
    team.view_all_heroes()

    hero3 = Hero('Superdog Dora', 200)
    hero4 = Hero('Supercat Boogie', 200)
    hero3.add_ability(Ability('Sonic Bark', 50))
    hero3.add_armor(Armor('Tough Fur', 30))
    hero4.add_ability(Ability('Sharp Claws', 50))
    hero4.add_armor(Armor('Whisker Shield', 30))

    team2 = Team('Less Cool Team')
    team2.add_hero(hero3)
    team2.add_hero(hero4)
    team2.view_all_heroes()

    team.attack(team2)
    team.stats()
    team2.stats()
