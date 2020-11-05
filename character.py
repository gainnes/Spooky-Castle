# FutureLearn Week 4 OOP
# Text based adventure game
# character.py

class Character():
    
    class_name = "Character"
        
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def __str__(self):
        return ("Class Name : %s" % (self.class_name))

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
    
    enemies_to_defeat = 0
    
    def __init__(self,char_name,char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1
    
    ## setter  - what is the enemy's weakness
    def set_weakness(self,item_weakness):
        ''' kryptonite is supermans's weakness'''
        self.weakness = item_weakness
        
    ### getter - get the enemy's weakness
    def get_weakness(self):
        return self.weakness
        
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item )
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False


class Friend(Character):

    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(self.name + " hugs you back!")
