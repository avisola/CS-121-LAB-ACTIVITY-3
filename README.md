# CS 121
# Overview
The assigned activity for our group is to make a mini game with function to attack, defend, evade, and cast spells.
The game we made is inspired by a visual novel/anime Fate Series. It is a mini turn based game that allows two player to fight each other using different servants.


# Members
| Name | Username |
|-----|-----------|
|Anyayahan, Jerlyn P.|[jerlynanyhn](https://github.com/jerlynanyhn)|
|Orcio, Benidick A.|[benidickorcio](https://github.com/benidickorcio)|
| Velasco, Iah Shanelle E.|[Shanelle](https://github.com/macherieshanelle)|
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
        if self.mana >= 200:
            print("Artoria unleashed her Noble Phantasm: Excalibur")
            self.mana -= 200
            play_action_sound("s", "4")   
            return 5000  # Spell damage
        print("Not enough mana")
        return 0
```

To cast a spell,the ```cast_spell``` method is called.

# To Attack
```python
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
```
To cast a spell,the ```attack``` method is called.
# To Defend
```python
if self.action_points >= 30:
            print("Artoria uses Blessing of the Avalon")
            print(f"{self.__class__.__name__} recovered 500 health! Current health: {self.health}")
            self.heal = True # Means healing is working
            self.defending = True
            self.action_points -= 30
            play_action_sound("s", "2")         
        else:
```
To cast a spell,the ```defend``` method is called.
# To Evade
```python
if self.action_points >= 10:
            print("Impossible: Exclusive only to Assassin")
            self.evading = False # Can't use evade
            self.action_points -= 10
            play_action_sound("s", "3")   
        else:
            print("Not enough action points to evade")

```
To cast a spell,the ```evade``` method is called.

# Fan-Made Project Disclaimer
We are sincerly 
This game is a non-commercial fan project inspired by Fate/Grand Order. All character names, abilities, sound effects, and other assets referencing the original game are the property of TYPE-MOON, Aniplex, Lasengle, and their respective rights holders.

We do not claim ownership of any official Fate/Grand Order content. This project is unaffiliated with and not endorsed by the official creators. All content is used under fair use for fan enjoyment and tribute.

Please contact us if there are any concerns regarding the use of copyrighted material.


# Acknowledgements
t is with sincere appreciation that we extend our gratitude to our teacher, Ma'am Fatima Marie Agdon, for giving us invaluable support and guidance throughout the semester. Your love for teaching has become a big part of our learning and growth which helped us gain knowledge and achieve success. Again, thank you for your unwavering support and commitment in teaching, you are truly one of the source of inspiration of the many.
