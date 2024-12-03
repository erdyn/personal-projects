"""
Game: Mage vs Monster

Description: Simple game involving class Hero and Monster with customizable strength attributes.
Hero fights two monsters then the amalgamation of both monsters
Made this to revise classes creatively

Date: 02/12/24

Author: Susanna Perkins
"""

class Hero(object):

   def __init__(self, name="", power_level=1, health_points=100):
       self.__name = name
       self.health_points = health_points
       self.power_level = power_level

   # Punch method
   def punch(self) -> float:
       return self.power_level * 2

   # Hero stats
   def __str__(self):
       hero_info = f"Name: {self.__name}\n"
       hero_info += f"Power level: {self.power_level}\n"
       hero_info += f"Health points: {self.health_points}\n"
       return hero_info
#end Hero class


# Mage Class, inheritance of Hero class
class Mage(Hero):
   def __init__(self, name="", power_level=100, health_points=100, elemental=""):
       Hero.__init__(self, name, power_level, health_points)
       self.elemental = elemental.lower()

   # Attack spell value (fire= more attack power)
   def attackSpell(self) -> float:
       if self.elemental == 'fire':
            return self.power_level * 5
       else:
           return self.power_level * 3

   # Healing spell value, (fire = Less healing power, water = more healing power)
   def healingSpell(self):
       if self.elemental == 'fire':
            self.health_points += 10
       elif self.elemental == "water":
           self.health_points += 200
       else:
           self.health_points += 100

   # Combat method
   def combat(self, monster) -> bool:
       # Opponent is a monster
        if isinstance(monster, Monster):
            # Fighto!!
            while self.health_points > 0 and monster.health_points > 0:
                monster.health_points -= self.attackSpell()
                # Hero wins
                if monster.health_points <= 0:
                    print("Hero wins!")
                    return True
                self.health_points -= monster.attack()
                # Monster wins
                if self.health_points <= 0:
                    print("Monster wins D:")
                    return False
        # Opponent is not a monster
        else:
            print("Hero only fights monster")
            # Must exit, return false
            return False

   # Mage stats
   def __str__(self):
       hero_info = "Mage's Stats:\n"
       hero_info += Hero.__str__(self)
       hero_info += f"Elemental: {self.elemental}\n"
       return hero_info
# end Mage class


# Monster class
class Monster(object):
    def __init__(self, name="", strength=1, health_points=100, roar="Rah!"):
        self.name = name
        self.strength = strength
        self.health_points = health_points
        self.roar = roar

    def attack(self) -> float:
        return self.strength * 2

    def Roar(self):
        print(self.roar)

    # Amalgamating monsters to create hybrid monster
    def __add__(self, other):
        new_name = self.name + other.name
        new_strength = self.strength * other.strength
        new_health_points = self.health_points + other.health_points
        new_roar = self.roar + " " + other.roar + "!!!"
        return Monster(new_name, new_strength, new_health_points, new_roar)

   # Monster stats
    def __str__(self):
        monster_info = f"Monster {self.name}'s Stats:\n"
        monster_info += f"Power level: {self.strength}\n"
        monster_info += f"Health points: {self.health_points}\n"
        monster_info += f"Roar: {self.roar}\n"
        return monster_info
# end Monster class


# Main

# Your Hero
name = str(input("Enter Hero's name: "))
powerLevel = int(input("Enter Hero's power points: "))
health = int(input("Enter Hero's health points: "))
elemental = str(input("Enter Hero's element (such as fire, water, etc): "))
hero = Mage(name, powerLevel, health, elemental)
print("\n\n")

# Monster 1
name = str(input("Enter monster1's name: "))
strengthLevel = float(input("Enter monster1's power points: "))
health = float(input("Enter monster1's health points: "))
roar = str(input("Enter monster1's roar: "))
m1 = Monster(name, strengthLevel, health, roar)
print("\n\n")

# Monster 2
name = str(input("Enter monster2's name: "))
strengthLevel = float(input("Enter monster2's power points: "))
health = float(input("Enter monster2's health points: "))
roar = str(input("Enter monster2's roar: "))
m2 = Monster(name, strengthLevel, health, roar)
print("\n\n")

# Monster Hybrid
hybrid = m1 + m2

# Hybrid stats
print("Hybrid", hybrid, "\n")

# Let the battles begin!
# Battle 1
print("Hero's Health: ", hero.health_points)
print()
hero.combat(m1)
print("Health after", m1.name, "battle: ", hero.health_points)
# Battle 2
print()
if hero.health_points > 0:
    hero.combat(m2)
    print("Health after", m2.name, "battle: ", hero.health_points)
    print()
    if hero.health_points > 0:
        # Battle 3 (if it made it thus far)
        hero.combat(hybrid)
        print("Health after hybrid battle", hero.health_points)
