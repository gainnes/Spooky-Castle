class RPGInfo():
    
    author = "Anonymous"
    
    def __init__(self, game_title):
        self.title = game_title
   
    def welcome(self):
        """ instance method """
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        """ class method - static """
        print("Made using the OOP RPG game creator (c) Graeme")
        
    @classmethod
    def credits(cls):
        """ class method - Class[cls] """
        print("Thank you for playing")
        print("Created by " + cls.author)