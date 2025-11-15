"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Amya Ratcliff Prince]
Date: [11/6/2025]

AI Usage: [Document any AI assistance used]
Example: AI helped with inheritance structure and method overriding concepts
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================
#(parent class)
class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """

        damage = self.strength   #set damage to characters strength
        target.take_damage(damage) #applying the damage to the target
        print(f"{self.name} attacks {target.name} for {damage} damage!")

        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """

        #subtracts the incoming damage from character's current health
        current_health = self.health - damage 
        #if the calculated health is below 0, set to zero
        if current_health < 0:
            current_health = 0 #prevents health from going below 0
            #updates current health of player
        self.health = current_health  


        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print("=== Character Stats ===")
        print(f"Name: {self.name}\n")
        print(f"Health: {self.health}\n")
        print(f"Strength: {self.strength} \n")
        print(f"Magic: {self.magic}\n")

#child class
class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        
        super().__init__(name, health, strength, magic)#calls methods from parent class
        #adds player attributes
        self.character_class = character_class
        self.level = 1
        self.experience = 0 
        self.gold = 0

        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """

        super().display_stats() #calling parent displsy method
        #adds to the display method
        print(f"Character Class: {self.character_class}\n")
        print(f"Level: {self.level}\n")
        print(f"Experience: {self.experience}\n")
        print(f"Gold: {self.gold}\n")

    

class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a warrior with appropriate stats.
        Warriors should have: high health, high strength, low magic
        """

        #calls the parent constructor but with warrior-specific stats
        super().__init__(name, character_class= "Warrior",health=120, strength=15, magic=5)
        
    def attack(self, target):
        """
        Override the basic attack to make it warrior-specific.
        Warriors should do extra physical damage.
        """

        #calls the parent class attack method so the basic strength damage is applied
        super().attack(target)
        #increase the warriors strength by 5
        self.strength = self.strength + 5
        print(f"{self.name} attacks with a mighty blow for {self.strength} damage.")


        
    def power_strike(self, target):
        """
        Special warrior ability - a powerful attack that does extra damage.
        """

        #create a new warrior object using the same name
        warrior = Warrior(self.name)
        #call warrior's attack twice to stimulate a power strike
        warrior.attack(target)
        warrior.attack(target)

class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a mage with appropriate stats.
        Mages should have: low health, low strength, high magic
        """ 
        super().__init__(name, character_class= "Mage",health=80, strength=8, magic=20)

        
    def attack(self, target):
        """
        Override the basic attack to make it magic-based.
        Mages should use magic for damage instead of strength.
        """

        #calculate damage using the mage's magic stat instead of strength
        damage = self.magic
        #apply damage to target
        target.take_damage(damage)
        print(f"{self.name} cast a magic attack on {target.name} for {damage} damage!")
        
        
    def fireball(self, target):
        """
        Special mage ability - a powerful magical attack.
        """
        # Calculate fireball damage as double the mage's magic stat
        damage = self.magic * 2
        #apply the damage to the target
        target.take_damage(damage)
        print(f"{self.name} hurls a fireball at {target.name} for {damage} damage!")
        
import random 
class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        """
        Create a rogue with appropriate stats.
        Rogues should have: medium health, medium strength, medium magic
        """

        #Call the parent constructor with Rogue specific stats
        super().__init__(name, character_class= "Rogue",health=90, strength=12, magic=10)

    def attack(self, target):
        """
        Override the basic attack to make it rogue-specific.
        Rogues should have a chance for extra damage (critical hits).
        """
        
        #Roll a random number between 1 and 10 to determine if the attack crits
        roll = random.randint(1,10)
        # Base damage is equal to the Rogue's strength
        damage = self.strength
        # If the roll is 3 or below, the attack becomes a critical hit (double damage)
        if roll <= 3:
            damage *= 2 # Double the damage for a crit
            print(f"Critical hit! {self.name} strikes {target.name} for {damage} damage!")
        else:
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        # Apply the damage to the target character    
        target.take_damage(damage) # Failed one of my test cases becasue I had this line of code inside my if statement block(Used AI to help me understand what i got wrong)

    def sneak_attack(self, target):
        """
        Special rogue ability - guaranteed critical hit.
        """

        # Calculate guaranteed critical damage (always double the Rogue's strength)
        damage = self.strength * 2
        # Apply the damage to the target character
        target.take_damage(damage)
        print(f"Sneak Attack! {self.name} strikes {target.name} for {damage}!")



class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        self.name = name
        # Store how much additional damage the weapon provides
        self.damage_bonus = damage_bonus
        """
        Create a weapon with a name and damage bonus.
        """

        
    def display_info(self):
        """
        Display information about this weapon.
        """
        
        print(f"Weapon: {self.name} | Damage Bonus: {self.damage_bonus}")

class Sword(Weapon):
    def __init__(self):
    # Call the Weapon constructor with fixed values for a Sword   
        super().__init__("Sword", 5)#bonus 5
class Wand(Weapon):
    def __init__(self):
         # Call the Weapon constructor with fixed values for a Wand
        super().__init__("Wand",4) #bonus 4

class Dagger(Weapon):
    def __init__(self):
    # Call the Weapon constructor with fixed values for a Dagger 
        super().__init__("Dagger", 3) #bonus 3


# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)

    # Create one of each character type
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Display their stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Test polymorphism - same method call, different behavior
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy health
    
    # Test special abilities
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Test composition with weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Sword()
    staff = Wand()
    dagger = Dagger()
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Test the battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")
