# Futurelearn Week 4 OOP
# Text based adventure game
# item.py

class Item():
    
    class_name = "Item"
    
    ### constructor method ###
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        
    def __str__(self):
        return ("Class Name : %s" % (self.class_name))

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def describe(self):
        print("The [" + self.name + "] is here - " + self.description)
        
