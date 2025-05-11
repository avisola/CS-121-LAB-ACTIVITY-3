

from abc import ABC, abstractmethod

# Abstract base class for GameCharacter, all specific characters will inherit from it
class GameCharacter(ABC):
    def __init__(self, health, mana, action_points):
        # Unique properties related to the character's health, mana, and action points
        self.health = health  # The character's health points
        self.mana = mana  # The character's mana points
        self.action_points = action_points  # The character's available action points
        self.defending = False  # Indicates if the character is defending
        self.evading = False  # Indicates if the character is evading
        self.special_defense = False  # Special defense flag for specific actions
        self.reflect_attack = False  # Reflect attack flag for counterattacks
        self.frozen = False  # Indicates if the character is frozen
        self.confused = False  # Indicates if the character is confused and may hurt themselves
        self.heal = False  # If the character has a healing state active

    @abstractmethod
    def attack(self):
        pass  # Attack method to be implemented in each subclass

    @abstractmethod
    def defend(self):
        pass  # Defend method to be implemented in each subclass

    @abstractmethod
    def evade(self):
        pass  # Evade method to be implemented in each subclass

    @abstractmethod
    def cast_spell(self):
        pass  # Cast spell method to be implemented in each subclass

    def take_damage(self, damage, is_spell=False):
        # Method that applies damage to the character based on defense, evasion, or reflection state
        if self.evading and not is_spell:
            print(f"{self.__class__.__name__} evaded the attack! No damage taken.")
            self.evading = False
            return None

        if self.reflect_attack and not is_spell:
            print(f"{self.__class__.__name__} reflected the attack back!")
            self.reflect_attack = False
            return "reflect", damage

        if self.heal:
            self.health += 500  # Healing mechanism
            self.heal = False
            print(f"{self.__class__.__name__} recovered 500 health! Current health: {self.health}")

        if self.defending:
            damage //= 2  # Defend reduces damage by half
            self.defending = False
            print(f"{self.__class__.__name__} is defending! Damage reduced to {damage}")

        if self.special_defense:
            damage //= 4  # Special defense reduces damage by a quarter
            self.special_defense = False
            print(f"{self.__class__.__name__} used Special Defense! Damage reduced to {damage}")

        self.health -= damage  # Apply the final damage after all conditions
        print(f"{self.__class__.__name__} took {damage} damage! Remaining health: {self.health}")
        return damage

    def is_defeated(self):
        return self.health <= 0  # Check if the character's health is below or equal to zero

# Specific character classes that inherit from GameCharacter

# Saber class has a healing factor
class Saber(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Artoria launched a barrage of wind blades")
            self.action_points -= 10
            return 500  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Artoria uses Blessing of the Avalon")
            self.heal = True # Means healing is working
            self.defending = True
            self.action_points -= 30
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False # Can't use evade
            self.action_points -= 10
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 1500:
            print("Artoria unleashed her Noble Phantasm: Excalibur")
            self.mana -= 1499
            return 5000  # Spell damage
        print("Not enough mana")
        return 0

# Archer class has a high damage and high defense
class Archer(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Gilgamesh opens his Gate of Babylon to attack")
            self.action_points -= 10
            return 1500  # Attack damage
        print("Can't attack right now - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Gilgamesh used his Golden Rule of a King")
            self.special_defense = True # Reduce damage to 1/4
            self.action_points -= 30
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False # Can't use evade
            self.action_points -= 10
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 1000:
            print("Gilgamesh unleashed his Noble Phantasm: Enuma Elish")
            self.mana -= 999
            return 10000  # Spell damage
        print("Not enough mana")
        return 0

# Berserker class has a high damage, high hp, and high hp consumption
class Berserker(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Heracles attacks with a powerful stomp")
            self.action_points -= 10
            return 2000  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        print("Heracles cannot defend due to rage")
        self.defending = False
        self.evading = False
        self.action_points -= 10

    def evade(self):
        print("Heracles cannot evade due to rage")

    def cast_spell(self):
        if self.health >= 5000: # It consumes hp everytime he cast noble phantasm
            print("Heracles unleash his Noble Phantasm: The Twelve Labors")
            self.health -= 5000
            return 15000  # Spell damage
        print("Can't cast, not enough health")
        return 0

# Caster class can confuse the enemy
class Caster(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Medea launched Scarlet Barrage")
            self.action_points -= 10
            return 600  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Medea used Trickster Coffin")
            self.defending = True
            self.action_points -= 30
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False
            self.action_points -= 10
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 300:
            print("Medea released Rule Breaker (Confuse)!")  # Cast confuse spell
            self.mana -= 149
            return "confuse"
        print("Can't cast, not enough mana")
        return 0

# Assassin class has a high versatility, low action points consumption, and can evade
class Assassin(GameCharacter):
    def attack(self):
        if self.action_points >= 5:
            print("Kojiro used Focus Slash")
            self.action_points -= 5
            return 500  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 25:
            print("Kojiro use his sheathe to defend")
            self.defending = True
            self.action_points -= 25
        else:
            print("Can't defend- not enough action points")

    def evade(self):
        if self.action_points >= 1:
            print("Kojiro use Phantom Shadow to Evade attack")
            self.evading = True # Can use evade
            self.action_points -= 1
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 1000:
            print("Kojiro unleashed his Noble Phantasm: Tsubame Gaeshi")
            self.mana -= 400
            return 12000  # Spell damage
        print("Not enough mana")
        return 0

# Lancer class has a reflect mechanics that can reflect any attacks except noble phantasm
class Lancer(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Cu used Impale Thrust")
            self.action_points -= 10
            return 1000  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Cu uses Protection from the Wind to reflect any form of attack")
            self.reflect_attack = True
            self.defending = True
            self.action_points -= 30
        else:
            print("Can't defend- not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False
            self.action_points -= 10
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 1000:
            print("Cu unleashed Gae Bolg")
            self.mana -= 400
            return 7500  # Spell damage
        print("Not enough mana")
        return 0

# Rider class has freeze mechanics that can petrify enemies, preventing them from attacking
class Rider(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Medusa lashes out with Endless Chains")
            self.action_points -= 10
            return 600  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Medusa uses Protection from the Snakes")
            self.defending = True
            self.action_points -= 30
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False
            self.action_points -= 10
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 500:
            print("Medusa cast Breaker Gorgon (Petrifies)!")  # Cast freeze spell
            self.mana -= 200
            return "freeze"
        print("Not enough mana")
        return 0

# Game setup - Initialize characters with their attributes
Emiya = Archer(health=10000, mana=2000, action_points=200)
Artoria = Saber(health=20000, mana=4000, action_points=200)
Heracles = Berserker(health=30000, mana=0, action_points=200)
Medussa = Rider(health=12000, mana=3000, action_points=200)
Kojiro = Assassin(health=9000, mana=5000, action_points=200)
Cu = Lancer(health=13000, mana=3500, action_points=200)
Medea = Caster(health=8000, mana=8000, action_points=200)

# A dictionary to map characters to their actions
actions = {
    "attack": "attack",  # Action for attacking
    "defend": "defend",  # Action for defending
    "cast": "cast_spell",  # Action for casting spells
    "evade": "evade"  # Action for evading
}

# A dictionary to store the characters
characters = {
    "archer": Emiya,
    "saber": Artoria,
    "berserker": Heracles,
    "rider": Medussa,
    "assassin": Kojiro,
    "lancer": Cu,
    "caster": Medea
}

# Display welcome message and game instructions
print("-----------------------------------------------------------------------------")
print("WELCOME TO FATE STAY NIGHT SERVANTS GAUNTLET BATTLE")
print("-----------------------------------------------------------------------------")
print("Choose two fighters: Archer, Saber, Lancer, Caster, Berserker, Assasin, Rider ")
p1 = input("Which servant do you want to use Player 1: ").strip().lower()
p2 = input("Which servant do you want to use Player 2: ").strip().lower()

# Validation of character choices
if p1 not in characters or p2 not in characters or p1 == p2:
    print("Invalid character choices. Restart the game.")
else:
    char1 = characters[p1]
    char2 = characters[p2]
    print("-----------------------------------------------------------------------------")
    print(f"Our Fighters:\n {p1.upper()} VS {p2.upper()}")
    print("Game Mechanics:\nType your moves as 'character action' (e.g., archer attack, saber cast, saber defend, saber evade)")
    print("The game ends when a Servant is defeated.")
    print("-----------------------------------------------------------------------------")

    # Main game loop - Continues until one player is defeated
    turn = 1  # 1 for Player 1, 2 for Player 2

while True:
    print("-----------------------------------------------------------------------------")
    current_player = p1 if turn == 1 else p2
    actor = char1 if turn == 1 else char2
    target = char2 if turn == 1 else char1
    print(f"Player {turn}'s turn: {current_player.upper()}")

    user_input = input(f"{current_player} action: ").strip().lower()
    print("-----------------------------------------------------------------------------")

    if user_input == "end":
        print("Battle sequence is over.")
        break

    try:
        char_name, action_name = user_input.split()
        if char_name != current_player:
            print("It's not your turn!")
            continue

        # Check frozen
        if actor.frozen:
            print(f"{actor.__class__.__name__} is frozen and can't move this turn!")
            actor.frozen = False
            turn = 2 if turn == 1 else 1  # Switch turn
            continue

        # Check confused
        if actor.confused and action_name == "attack":
            print(f"{actor.__class__.__name__} is confused and attacks themselves!")
            damage = actor.attack()
            actor.take_damage(damage)
            actor.confused = False
            turn = 2 if turn == 1 else 1
            continue

        # Perform action
        action_method = getattr(actor, actions[action_name])

        if action_name in ["defend", "evade"]:
            action_method()
        else:
            is_spell = action_name == "cast"
            result = action_method()

            if result == "freeze":
                target.frozen = True
                print(f"{target.__class__.__name__} is frozen and will miss their next turn!")
            elif result == "confuse":
                target.confused = True
                print(f"{target.__class__.__name__} is confused and may hurt themselves!")
            elif isinstance(result, tuple) and result[0] == "reflect":
                reflected_damage = result[1]
                print(f"{actor.__class__.__name__} took {reflected_damage} reflected damage!")
                actor.take_damage(reflected_damage, is_spell=is_spell)
            elif isinstance(result, int) and result > 0:
                reflect_result = target.take_damage(result, is_spell=is_spell)
                if isinstance(reflect_result, tuple) and reflect_result[0] == "reflect":
                    actor.take_damage(reflect_result[1], is_spell=is_spell)

        if target.is_defeated():
            print(f"{target.__class__.__name__} has been defeated!")
            print(f"{actor.__class__.__name__} wins the battle!")
            break

        turn = 2 if turn == 1 else 1  # Switch turn

    except (ValueError, KeyError, AttributeError):
        print("Invalid input. Use format: 'archer attack', 'saber cast', etc.")
