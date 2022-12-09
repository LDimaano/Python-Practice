import UserFave

class Fave_Actor(UserFave.UserFave):
    def __init__(self, user_name, name, birthday, country, agency, fave_drama):
        super().__init__(user_name, name, birthday, country)
        self.agency = agency
        self.fave_drama = fave_drama
    
    def getuser_name(self):
        return self.user_name
    
    def getname(self):
        return self.name
    
    def getbirthday(self):
        return self.birthday

    def getcountry(self):
        return self.country
    
    def getagency(self):
        return self.agency
    
    def getfave_drama(self):
        return self.fave_drama

    def actor_display(self):
        print(f"+---------------------------------------------+")
        print(f"\n{self.getuser_name()}'s Favorite Actor\n")
        print(f"Name: {self.getname()}") 
        print(f"Birthday: {self.getbirthday()}") 
        print(f"Country: {self.getcountry()}") 
        print(f"Agency: {self.getagency()}") 
        print(f"Favorite Drama: {self.getfave_drama()}\n")
        print(f"+---------------------------------------------+")

    def runFA():
        print("\n-----Favorite Actor------")
        print("_____________________________\n")
        user_name = input("Enter Your Name: ")
        name = input("Enter Actor's Name: ")
        birthday = input("Enter Actor's Birthday: ")
        country = input("Enter Actor's Country: ")
        agency = input("Enter Actor's Agency: ")
        fave_drama = input("Enter Favorite Drama: ")
        global fave_actor
        fave_actor = Fave_Actor(user_name, name, birthday, country, agency, fave_drama)
    
        while True:
            trans = input("\nDo you want To Display your Favorite Actor? (y/n): ")
            if trans == "y":
                fave_actor.actor_display()
                exit()
            elif trans == "n":
                print("Exiting...")
                exit()
            else:
                print("Wrong Command!  Enter 'y' for yes and 'n' for no.\n")
