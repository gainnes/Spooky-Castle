# FutureLearn Week 4 OOP
# Text based adventure game
# room.py

class Room():

    class_name = "Room"
    
    number_of_rooms = 0 # class variable

    ## constructor method ###
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        
        Room.number_of_rooms = Room.number_of_rooms + 1


    def __str__(self):
        return ("Class Name : %s" % (self.class_name))

    ### 'setter' - used to set the room name ###
    def set_name(self,room_name):
        self.name = room_name

    ### ' getter' - used to get the room name ###
    def get_name(self):
        return self.name

    ### 'setter' - used to set the room description ###
    def set_description(self,room_description):
        self.description = room_description

    ### 'getter' - used to get the room description ###
    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    ### link_room method ###
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print('----------')
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


    ### getter - get the character in the room
    def get_character(self):
        return self.character

    ## setter - set the character in the room
    def set_character(self,new_character):
        self.character = new_character
        
        
    ### getter - return what item is in the room    
    def get_item(self):
        return self.item
    
    ### setter - set the item to be found in the room
    def set_item(self, item_name):
        self.item = item_name       