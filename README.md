# CS 121
# Overview
The assigned activity for our group is to make a mini game with function to attack, defend, evade, and cast spells.
The game we made is inspired by a visual novel/anime Fate Series. It is a mini turn based game that allows two player to fight each other using different servants.


# Members
| Name | Username |
|-----|-----------|
|Anyayahan, Jerlyn P.|[username](https://github.com)|
|Orcio, Benidick A.|[username](https://github.com)|
| Velasco, Iah Shanelle E.|[username](https://github.com)|
|Vitug, Gian Christian V.|[avisola](https://github.com/avisola)|

# Game Intrucstions
1. Make sure that python is installed in you computer or laptop.
2. Open the FSN.py using python runner in your device.
3. Once the code is running, a starting menu will pop up there that let you choose which Servant you want to use.
4. Follow the Instructions given in the menu after picking a servant
5. Enjoy the game :>


# CODES


## Background Music
```python
   import pygame

# Initialize the mixer
pygame.mixer.init()

pygame.mixer.music.load("[SPOTDOWNLOADER.COM] Revelation.mp3")

pygame.mixer.music.set_volume(100.0)


pygame.mixer.music.play(-1)
```
## Background Music for each other made by the Servants
```python
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
```

## To cast Noble Phantasm
```python
    def cast_spell(self):
        if self.mana >= 1000:
            print("Gilgamesh unleashed his Noble Phantasm: Enuma Elish")
            self.mana -= 999
            return 10000  # Spell damage
        print("Not enough mana")
        return 0
```

To cast a spell,the ```cast_spell``` method is called.

# To Attack
```python
   class Archer(GameCharacter):
    def attack(self):
        if self.action_points >= 10:
            print("Gilgamesh opens his Gate of Babylon to attack")
            self.action_points -= 10
            play_action_sound("a", "1")  
            return 1500  # Attack damage
        print("Can't attack right now - not enough action points")
        return 0
```
To cast a spell,the ```attack``` method is called.
# To Defend
```python
def defend(self):
        if self.action_points >= 30:
            print("Gilgamesh used his Golden Rule of a King")
            self.special_defense = True # Reduce damage to 1/4
            self.action_points -= 30
            play_action_sound("a", "2")  
        else:
            print("Can't defend - not enough action points")
```
To cast a spell,the ```defend``` method is called.
# To Evade
```python
def evade(self):
        if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False # Can't use evade
            self.action_points -= 10
            play_action_sound("a", "3")  
        else:
            print("Not enough action points to evade")
```
To cast a spell,the ```evade``` method is called.


# Acknowledgements
