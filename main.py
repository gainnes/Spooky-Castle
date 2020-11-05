# FutureLearn Week 4 OOP
# Text based adventure game
# main.py

from room import Room
from item import Item
from character import Enemy, Friend
from rpginfo import RPGInfo


import sys

spooky_castle = RPGInfo("The Spooky Castle RPG")
spooky_castle.welcome()
RPGInfo.info()

# define the rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

dining_room = Room("Dining Room")
dining_room.set_description("A large room with ornate golden decorations on each wall")

cellar = Room("Gimp Cave")
cellar.set_description("Graeme's secret Gimp cave")

sun_room = Room("Sun Room")
sun_room.set_description("A spherical room made of glass and steel")

stairs = Room("Stairs")
stairs.set_description("Dark oaked panelled room with a set of stairs up to the landing")

landing = Room("Landing")
landing.set_description("Long, narrow landing with a creaking floor")

games_room = Room("Games Room")
games_room.set_description("Full sized snooker table sits in the center of the room")

bedroom = Room("Master Bedroom")
bedroom.set_description("Massive bedroom with a four poster bed taking center stage")

# link the rooms together
kitchen.link_room(dining_room, "south")
dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")
dining_room.link_room(stairs,"south")
ballroom.link_room(dining_room, "east")
ballroom.link_room(cellar, "south")
ballroom.link_room(sun_room,"north")
cellar.link_room(ballroom, "north")
cellar.link_room(stairs,"east")
sun_room.link_room(ballroom,"south")
stairs.link_room(cellar,"west")
stairs.link_room(dining_room,"north")
stairs.link_room(landing,"up")
landing.link_room(stairs,"down")
landing.link_room(bedroom,"east")
landing.link_room(games_room,"south")
games_room.link_room(landing,"north")
bedroom.link_room(landing,"west")


# start off in a room
current_room = sun_room

## create a Zombie and locate it in a room ##
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("book")
ballroom.set_character(dave)

## create a Zombie and locate it in a room ##
brian = Enemy("Brian", "A tall zombie")
brian.set_conversation("Hmmm... rgrhl... oophf...")
brian.set_weakness("crackers")
cellar.set_character(brian)

## create a Zombie and locate it in a room ##
keith = Enemy("Keith", "A short, fat zombie")
keith.set_conversation("yum yum I like to eat you.")
keith.set_weakness("sword")
bedroom.set_character(keith)

# create a Friend and locate them in a room ##
catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there.")
kitchen.set_character(catrina)

# stick Items aboout the place
book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_room.set_item(book)

crackers = Item("crackers")
crackers.set_description("The nice crisp ones from Waitrose")
sun_room.set_item(crackers)

sword = Item("sword")
sword.set_description("Beautiful Japanese Katana")
games_room.set_item(sword)

print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
print("There are " + str(Enemy.enemies_to_defeat) + " Zombies to fight")

dead = False
backpack=[]


while dead == False:
    try:
        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()
        
        item = current_room.get_item()
        if item is not None:
            item.describe()

        command = input(">> ")
        # check whether a direction was typed
        if command in ["north","south","east","west","up","down"]:
            current_room = current_room.move(command)

        elif command == "talk":
            # talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()
                
        elif command =="take":
            # check that an item is available, and if it is, stick in in your backpack
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                print("Items are: %s" % (','.join(list(backpack))))
                current_room.set_item(None)

        elif command =="fight":
            # You can check whether an object is an instance of a particular
            # class with isinstance() - useful! This code means
            # "If the character is an Enemy"
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                print("Items are: %s" % (','.join(list(backpack))))
                print("What will you fight with?")
                fight_with = input(">")
                if fight_with in backpack:
                    if inhabitant.fight(fight_with) == True:
                        # what happens if you win
                        print("Hooray, you won the fight!")
                        current_room.set_character(None)
                        if Enemy.enemies_to_defeat == 0:
                            print("Well done - you've killed them all")
                            dead = True
                    else:
                        # what happens if you lose
                        print("Oh dear, you lost the fight")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with)       
            else:
                print("There is no one here to fight with")

        elif command == "hug":
            # hug the inhabitant - if friend
            if inhabitant is not None:
                if isinstance(inhabitant,Enemy):
                    print("I wouldn't do that if I were you")
                else:
                    inhabitant.hug()
            else:
                 print("There is no one to hug")
        elif command == "help":
             print(""" commands are :
                       'north','south','east','west' [move]
                       'fight','hug','talk',
                       'take',
                       'up','down' [stairs]..""")

    except KeyboardInterrupt:
        sys.exit()


RPGInfo.author = "Buchan Boy Productions"
RPGInfo.credits()







