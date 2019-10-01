"""Superheroes."""
import random
import pickle


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
            damg = abl.attack()
            print(f'Attacking with {abl.name} for {damg} damage.')
            # print('{} | {}'.format(abl.name, dmg))
            dmg += damg
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
            blo = arm.block()
            print(f'Up to {blo} damage blocked with {arm.name}.')
            bl += blo
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
                # print(damage)
                opponent.take_damage(damage)
                fighter = 1
            else:
                damage = opponent.attack()
                # print(damage)
                self.take_damage(damage)
                fighter = 0
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

    def get_stats(self):
        """Return hero's stats in a formatted string."""
        return '{} | Kills: {} | Deaths: {}'.format(
            self.name, self.kills, self.deaths)


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

    def list_living_names(self):
        """Return a string with the names of all living hereos."""
        live_list = self.list_living()
        rtn = ''
        for hero in live_list:
            rtn += hero.name + ' '
        return rtn.strip()

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


class Arena:
    """Arena to hold teams of heroes."""

    def __init__(self, username):
        """
        Instantiate properties.

        team_one: None
        team_two: None
        """
        self.username = username
        self.team_one = None
        self.team_one = None

    def create_ability(self):
        """
        Prompt for Ability information.

        Return Ability with values from user Input
        """
        ability_name = input('Name of Ability: ').title()
        ability_power = ''
        while not ability_power.isnumeric():
            ability_power = input('Max. Power of Ability: ')
        ability_power = int(ability_power)
        return Ability(ability_name, ability_power)

    def create_weapon(self):
        """
        Prompt for Weapon information.

        Return Weapon with values from user Input
        """
        weapon_name = input('Name of Weapon: ').title()
        weapon_power = ''
        while not weapon_power.isnumeric():
            weapon_power = input('Max. Power of Weapon: ')
        weapon_power = int(weapon_power)
        return Weapon(weapon_name, weapon_power)

    def create_armor(self):
        """
        Prompt for Armor information.

        Return Armor with values from user Input
        """
        armor_name = input('Name of Armor: ').title()
        armor_power = ''
        while not armor_power.isnumeric():
            armor_power = input('Max. Power of Armor: ')
        armor_power = int(armor_power)
        return Armor(armor_name, armor_power)

    def create_hero(self):
        """
        Prompt for Hero information.

        Return Hero with values from user Input
        """
        hero_name = input('Name of Hero: ').title()
        hero_health = ''
        while not hero_health.isnumeric():
            hero_health = input('Max. Health of Hero: ')
        hero_health = int(hero_health)
        hero = Hero(hero_name, hero_health)

        abilities_count = ''
        while not abilities_count.isnumeric():
            abilities_count = input('Number of abilities: ')
        abilities_count = int(abilities_count)
        for x in range(0, abilities_count):
            hero.add_ability(self.create_ability())

        weapons_count = ''
        while not weapons_count.isnumeric():
            weapons_count = input('Number of weapons: ')
        weapons_count = int(weapons_count)
        for x in range(0, weapons_count):
            hero.add_weapon(self.create_weapon())

        armors_count = ''
        while not armors_count.isnumeric():
            armors_count = input('Number of armors: ')
        armors_count = int(armors_count)
        for x in range(0, armors_count):
            hero.add_armor(self.create_armor())

        return hero

    def create_team(self):
        """
        Prompt for Team information.

        Return Team with values from user Input
        """
        team_name = input('Name of Team: ').title()
        team = Team(team_name)

        heroes_count = input('Number of heroes on {}: '.format(team_name))
        while not heroes_count.isnumeric() or int(heroes_count) < 1:
            heroes_count = input('There must be at least one hero! ')
        heroes_count = int(heroes_count)
        for x in range(0, heroes_count):
            team.add_hero(self.create_hero())
        return team

    def build_team_one(self):
        """Set arena team one."""
        self.team_one = self.create_team()

    def build_team_two(self):
        """Meet specs w/ this function."""
        self.team_two = self.create_team()

    def team_battle(self):
        """Battle team_one and team_two together."""
        self.team_one.attack(self.team_two)
        self.show_stats()

    def show_stats(self):
        """Display team statistics."""
        print('------BATTLE RESULTS------')
        if not self.team_one.any_alive():
            print(f'Winner: {self.team_two.name}')
            print('Surviving heroes: ' + self.team_two.list_living_names())
        elif not self.team_two.any_alive():
            print(f'Winner: {self.team_one.name}')
            print('Surviving heroes: ' + self.team_one.list_living_names())
        else:
            print('No clear winner...')
        print(f'{self.team_one.name} | ' + self.avg_kd(self.team_one))
        print(f'{self.team_two.name} | ' + self.avg_kd(self.team_two))

    def avg_kd(self, team):
        """Return average K/D ratio for heroes on the team."""
        kills = 0
        for hero in team.heroes:
            kills += hero.kills
        kills = kills//len(team.heroes)
        deaths = 0
        for hero in team.heroes:
            deaths += hero.deaths
        deaths = deaths//len(team.heroes)
        return f'Average Kills: {kills} / Average Deaths: {deaths}'

    def save_arena(self):
        """Add the arena data to savefile."""
        filename = 'save_data/'+self.username
        savefile = open(filename, 'wb')
        pickle.dump(self, savefile)
        savefile.close()


def load_arena(username):
    """Load an already existing user."""
    filename = 'save_data/'+username
    loadfile = open(filename, 'rb')
    user = pickle.load(loadfile)
    loadfile.close()
    return user


if __name__ == "__main__":
    game_is_running = True

    load_new = input('Load existing arena or create new arena? [LOAD/NEW]: ')
    while 'load' not in load_new.lower() and 'new' not in load_new.lower():
        load_new = input('[LOAD/NEW]: ')
    if 'new' in load_new:
        new_name = input('Name new arena: ').strip()
        while not new_name.isalnum() or ' ' in new_name:
            if not new_name.isalnum():
                new_name = input('Only alphanumerical characters please!: ')
            else:
                new_name = input('No spaces please!: ')
        # Instantiate Game Arena
        arena = Arena(new_name)

        # Build Teams
        arena.build_team_one()
        arena.build_team_two()
    elif 'load' in load_new:
        print('CAUTION: This process is held together with duct tape and hope'
              ' and if you enter a name that doesn\'t exist you will have to'
              ' restart the program.')
        load_name = input('Name of existing arena: ')
        arena = load_arena(load_name)
        arena.team_one.revive_heroes()
        arena.team_two.revive_heroes()
    else:
        print('This wasn\'t supposed to happen. Please restart.')

    while game_is_running:

        arena.team_battle()
        arena.save_arena()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            print('-------------------------')
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
