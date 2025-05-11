import pygame

# Initialize the mixer
pygame.mixer.init()

pygame.mixer.music.load("[SPOTDOWNLOADER.COM] Revelation.mp3")

pygame.mixer.music.set_volume(100.0)


pygame.mixer.music.play(-1)

def play_intro(servant):
    intro_sounds = {
        "a": "AI.wav",
        "s": "SI.wav",
        "l": "LI.wav",
        "c": "CI.wav",
        "b": "BI.wav",
        "as": "ASI.wav",
        "r": "RI.wav"
    }
    file = intro_sounds.get(servant)
    if file:
        sound = pygame.mixer.Sound(file)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))  # Wait until the sound finishes
        
def play_action_sound(servant, action):
    action_sounds = {
             "s": {
        "1": "SA.wav",
        "2": "SD.wav",
        "4": "SC.wav",
        "3": "NULL.wav",
    },
    "a": {
        "1": "AA.wav",
        "2": "AD.wav",
        "4": "AC.wav",
        "3": "NULL.wav",
    },
    "l": {
        "1": "LA.wav",
        "2": "LD.wav",
        "4": "LC.wav",
        "3": "NULL.wav",
    },
    "c": {
        "1": "CA.wav",
        "2": "CD.wav",
        "4": "CC.wav",
        "3": "NULL.wav",
    },
    "b": {
        "1": "BA.wav",
        "2": "BD.wav",
        "4": "BC.wav",
        "3": "NULL.wav",
    },
    "as": {
        "1": "ASA.wav",
        "2": "ASD.wav",
        "4": "ASC.wav",
        "3": "ASE.wav",
    },
    "r": {
        "1": "RA.wav",
        "2": "RD.wav",
        "4": "RC.wav",
        "3": "NULL.wav",
    },        
    }
             
    file = action_sounds.get(servant, {}).get(action)
    if file:
        sound = pygame.mixer.Sound(file)
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))  # Wait until the sound finishes

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
        self.consume = False #Indicates that the character is consuming hp
        self.regen_mana = False

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
        
        if self.consume: #Consumes hp to cast noble phantasm
            self.health -=5000
            self.comsume = False
        
        if self.regen_mana: #regenerates mana when attacking to fill the noble phantasm mana required
            self.mana += 300
            self.regen_mana = False

        if self.reflect_attack and not is_spell: #reflect incoming attacks except noble phantasm
            print(f"{self.__class__.__name__} reflected the attack back!")
            self.reflect_attack = False
            return "reflect", damage

        if self.heal: #allows servant to heal
            self.health += 500  # Healing mechanism
            self.heal = False

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
            self.regen_mana = True
            print(f"{self.__class__.__name__} Attack has been made, mana regen +300, current mana: {self.mana}")
            play_action_sound("s", "1")
            return 500  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Artoria uses Blessing of the Avalon")
            print(f"{self.__class__.__name__} recovered 500 health! Current health: {self.health}")
            self.heal = True # Means healing is working
            self.defending = True
            self.action_points -= 30
            play_action_sound("s", "2")         
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False # Can't use evade
            self.action_points -= 10
            play_action_sound("s", "3")   
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 200:
            print("Artoria unleashed her Noble Phantasm: Excalibur")
            self.mana -= 200
            play_action_sound("s", "4")   
            return 5000  # Spell damage
        print("Not enough mana")
        return 0

# Archer class has a high damage and high defense
class Archer(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Gilgamesh opens his Gate of Babylon to attack")
            self.regen_mana = True
            print(f"{self.__class__.__name__} Attack has been made, mana regen +300, current mana: {self.mana}")
            self.action_points -= 10
            play_action_sound("a", "1")  
            return 1500  # Attack damage
        print("Can't attack right now - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Gilgamesh used his Golden Rule of a King")
            self.special_defense = True # Reduce damage to 1/4
            self.action_points -= 30
            play_action_sound("a", "2")  
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False # Can't use evade
            self.action_points -= 10
            play_action_sound("a", "3")  
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 1000:
            print("Gilgamesh unleashed his Noble Phantasm: Enuma Elish")
            self.mana -= 999
            play_action_sound("a", "4")  
            return 10000  # Spell damage
        print("Not enough mana")
        return 0

# Berserker class has a high damage, high hp, bloodlusted, and high hp consumption
class Berserker(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Heracles attacks with a powerful stomp")
            self.regen_mana = False
            print(f"{self.__class__.__name__} Berserker can't regen mana, current mana: {self.mana}")
            self.action_points -= 10
            play_action_sound("b", "1")  
            return 2000  # Attack damage
        else:
            print("Can't attack - not enough action points")
            return 0

    def defend(self):
        print("Heracles cannot defend due to rage")
        self.defending = False
        self.evading = False
        self.action_points -= 10
        play_action_sound("b", "2")  

    def evade(self):
        print("Heracles cannot evade due to rage")
        play_action_sound("b", "3")  

    def cast_spell(self):
        self.consume = True
        if self.health >= 5000: # It consumes hp everytime he cast noble phantasm
            print("Heracles consume 5000 hp to unleash his Noble Phantasm: The Nine labors from God")
            play_action_sound("b", "4")  
            return 15000  # Spell damage
        else:
            print("Can't cast, not enough health")
            return 0

# Caster class can confuse the enemy
class Caster(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Medea launched Scarlet Barrage")
            self.regen_mana = True
            print(f"{self.__class__.__name__} Attack has been made, mana regen +300, current mana: {self.mana}")
            self.action_points -= 10
            play_action_sound("c", "1") 
            return 600  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Medea used Trickster Coffin")
            self.defending = True
            self.action_points -= 30
            play_action_sound("c", "2") 
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False
            self.action_points -= 10
            play_action_sound("c", "3") 
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 300:
            print("Medea released Rule Breaker (Confuse)!")  # Cast confuse spell
            self.mana -= 300
            play_action_sound("c", "4") 
            return "confuse"
        print("Can't cast, not enough mana")
        return 0

# Assassin class has a high versatility, low action points consumption, and can evade
class Assassin(GameCharacter):
    def attack(self):
        if self.action_points >= 5:
            print("Kojiro used Focus Slash")
            self.regen_mana = True
            print(f"{self.__class__.__name__} Attack has been made, mana regen +300, current mana: {self.mana}")
            self.action_points -= 5
            play_action_sound("as", "1") 
            return 500  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 25:
            print("Kojiro use his sheathe to defend")
            self.defending = True
            self.action_points -= 25
            play_action_sound("as", "2") 
        else:
            print("Can't defend- not enough action points")

    def evade(self):
        if self.action_points >= 1:
            print("Kojiro use Phantom Shadow to Evade attack")
            self.defending = True
            self.evading = True # Can use evade
            self.action_points -= 1
            play_action_sound("as", "3") 
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 800:
            print("Kojiro unleashed his Noble Phantasm: Tsubame Gaeshi")
            self.mana -= 800
            play_action_sound("as", "4") 
            return 12000  # Spell damage
        print("Not enough mana")
        return 0

# Lancer class has a reflect mechanics that can reflect any attacks except noble phantasm
class Lancer(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Cu used Impale Thrust")
            self.regen_mana = True
            print(f"{self.__class__.__name__} Attack has been made, mana regen +300, current mana: {self.mana}")
            self.action_points -= 10
            play_action_sound("l", "1") 
            return 1000  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Cu uses Protection from the Wind to reflect any form of attack")
            self.reflect_attack = True
            self.defending = True
            self.action_points -= 30
            play_action_sound("l", "2") 
        else:
            print("Can't defend- not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False
            self.action_points -= 10
            play_action_sound("l", "3") 
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 700:
            print("Cu unleashed Gae Bolg")
            self.mana -= 700
            play_action_sound("l", "4") 
            return 7500  # Spell damage
        print("Not enough mana")
        return 0

# Rider class has freeze mechanics that can petrify enemies, preventing them from attacking
class Rider(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Medusa lashes out with Endless Chains")
            self.regen_mana = True
            print(f"{self.__class__.__name__} Attack has been made, mana regen +300, current mana: {self.mana}")
            self.action_points -= 10
            play_action_sound("r", "1") 
            return 600  # Attack damage
        print("Can't attack - not enough action points")
        return 0

    def defend(self):
        if self.action_points >= 30:
            print("Medusa uses Protection from the Snakes")
            self.defending = True
            self.action_points -= 30
            play_action_sound("r", "1") 
        else:
            print("Can't defend - not enough action points")

    def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False
            self.action_points -= 10
            play_action_sound("r", "3") 
        else:
            print("Not enough action points to evade")

    def cast_spell(self):
        if self.mana >= 300:
            print("Medusa cast Breaker Gorgon (Petrifies)!")  # Cast freeze spell
            self.mana -= 300
            play_action_sound("r", "4") 
            return "freeze"
        print("Not enough mana")
        return 0

# Game setup - Initialize characters with their attributes
while True:
    # Reset characters to full stats
    Gilgamesh = Archer(health=10000, mana=0, action_points=500)
    Artoria = Saber(health=20000, mana=0, action_points=500)
    Heracles = Berserker(health=30000, mana=0, action_points=500)
    Medussa = Rider(health=12000, mana=0, action_points=500)
    Kojiro = Assassin(health=9000, mana=0, action_points=500)
    Cu = Lancer(health=13000, mana=0, action_points=500)
    Medea = Caster(health=8000, mana=300, action_points=500)
    # Action Commands
    actions = {
        "1": "attack",
        "4": "cast_spell",
        "2": "defend",
        "3": "evade"
    }
    # Character selection for the main game
    characters = {
        "a": Gilgamesh,
        "s": Artoria,
        "b": Heracles,
        "r": Medussa,
        "as": Kojiro,
        "l": Cu,
        "c": Medea
    }


    
   # Main Game
    print("-----------------------------------------------------------------------------")
    print("WELCOME TO FATE STAY NIGHT SERVANTS BATTLE")
    print("-----------------------------------------------------------------------------")
    print("CHOOSE YOUR SERVANT:\n-----------------------------------------------------------------------------\n Archer(A): Specialized Defense, High damage\n Saber(S): High Hp, Can use heal\n Lancer(L):Versitile attacks, can reflect attacks\n Caster(C): High mana, can confuse enemies\n Berserker(B): High HP, High damage, Consume  health\n Assassin(AS): Flexible, can evade attacks, High damage\n Rider(R): Versitile, can petrify the enemies\n-----------------------------------------------------------------------------")
    print("Servant Stats:\n Archer: Health=10000, Attack=1500, NP gauge=1000\nSaber: Health=20000, NP gauge=500 \nLancer: Health=13000, NP gauge=700\nCaster: Health=8000, NP gauge=300, Action points=200\nBerserker: Health=30000, HP consumption=5000\nAssassin: Health=9000, Np gauge=800\nRider: Health=12000, NP gauge=300\n")
    print("-----------------------------------------------------------------------------")
    p1 = input("Which servant do you want to use Master 1: ").strip().lower()
    play_intro(p1)

    p2 = input("Which servant do you want to use Master 2: ").strip().lower()
    play_intro(p2)

    if p1 not in characters or p2 not in characters or p1 == p2:
        print("Invalid character choices. Restarting the round.")
        continue

    char1 = characters[p1]
    char2 = characters[p2]
    print("-----------------------------------------------------------------------------")
    print(f"Our Fighters:\n {p1.upper()} VS {p2.upper()}")
    print("-----------------------------------------------------------------------------")
    print("Game Mechanics:\n-----------------------------------------------------------------------------\nType your  servants initial as well as your moves(1=attack), (2=defend),\n"
    " (3=evade), (4=cast) (e.g., A 1, A 2, A 3), and type 0 if you run out of moves" \
    "\n-----------------------------------------------------------------------------\nPlayers need to fill the NP gauge to cast Noble Phantasm""\n Every action made except Noble phantasm cost a Action points\n All servants has a Fixed Action points of 500\n Each Action has specific cost: Attack=10, defend =30, evade=25")
    print("-----------------------------------------------------------------------------")
    print("The game ends when a Servant is defeated.")
    print("-----------------------------------------------------------------------------")

    turn = 1  # Player 1 starts

    while True:
        print("-----------------------------------------------------------------------------")
        current_player = p1 if turn == 1 else p2
        actor = char1 if turn == 1 else char2
        target = char2 if turn == 1 else char1
        print(f"Player {turn}'s turn: {current_player.upper()}")

        user_input = input(f"{current_player} action: ").strip().lower()
        print("-----------------------------------------------------------------------------")

        if user_input == "0":
            print("Battle sequence is over.")
            break

        try:
            char_name, action_name = user_input.split()
            if char_name != current_player:
                print("It's not your turn!")
                continue

            if actor.frozen:
                print(f"{actor.__class__.__name__} is frozen and can't move this turn!")
                actor.frozen = False
                turn = 2 if turn == 1 else 1
                continue

            if actor.confused and action_name == "1":
                print(f"{actor.__class__.__name__} is confused and attacks themselves!")
                damage = actor.attack()
                actor.take_damage(damage)
                actor.confused = False
                turn = 2 if turn == 1 else 1
                continue

            action_method = getattr(actor, actions[action_name])

            if action_name in ["2", "3"]:
                action_method()
            else:
                is_spell = action_name == "4"
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

            turn = 2 if turn == 1 else 1

        except (ValueError, KeyError, AttributeError):
            print("Invalid input. Use format: 'A 1', 'A 2', etc.")

    play_again = input("Do you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thanks for playing!")
        break

import pygame

# Initialize the mixer
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load("[SPOTDOWNLOADER.COM] Revelation.mp3")
pygame.mixer.music.set_volume(100.0)
pygame.mixer.music.play(-1)

