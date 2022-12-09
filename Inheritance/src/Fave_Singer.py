import UserFave

class Fave_Singer(UserFave.UserFave):
    def __init__(self, user_name, name, birthday, country, agency, fave_song):
        super().__init__(user_name, name, birthday, country)
        self.agency = agency
        self.fave_song = fave_song
    
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
    
    def getfave_song(self):
        return self.fave_song

    def singer_display(self):
        print(f"+---------------------------------------------+")
        print(f"\n{self.getuser_name()}'s Favorite Singer\n")
        print(f"Name: {self.getname()}") 
        print(f"Birthday: {self.getbirthday()}") 
        print(f"Country: {self.getcountry()}")
        print(f"Agency: {self.getagency()}")
        print(f"Favorite Song: {self.getfave_song()}\n")
        print(f"+---------------------------------------------+")
        
    def runFS():
        print("\n-----Favorite Singer------")
        print("_____________________________\n")
        user_name = input("Enter Your Name: ")
        name = input("Enter Singer's Name: ")
        birthday = input("Enter Singer's Birthday: ")
        country = input("Enter Singer's Country: ")
        agency = input("Enter Singer's Agency: ")
        fave_song = input("Enter Favorite Song: ")
        global fave_singer
        fave_singer = Fave_Singer(user_name, name, birthday, country, agency, fave_song)

        while True:
            trans = input("\nDo you want To Display your Favorite Singer? (y/n): ")
            if trans == "y":
                fave_singer.singer_display()
                exit()
            elif trans == "n":
                print("Exiting...")
                exit()
            else:
                print("Wrong Command!  Enter 'y' for yes and 'n' for no.\n")