import UserFave

class Fave_Writer(UserFave.UserFave):
    def __init__(self, user_name, name, birthday, country, agency, fave_book):
        super().__init__(user_name, name, birthday, country)
        self.agency = agency
        self.fave_book = fave_book
    
    def getuser_name(self):
        return self.user_name
    
    def getname(self):
        return self.name
    
    def getbirthday(self):
        return self.birthday

    def getcountry(self):
        return self.country
    
    def getpublisher(self):
        return self.agency
    
    def getfave_book(self):
        return self.fave_book

    def writer_display(self):
        print(f"+---------------------------------------------+")
        print(f"\n{self.getuser_name()}'s Favorite Writer\n")
        print(f"Name: {self.getname()}") 
        print(f"Birthday: {self.getbirthday()}") 
        print(f"Country: {self.getcountry()}")
        print(f"Publisher: {self.getpublisher()}")
        print(f"Favorite Book: {self.getfave_book()}\n")
        print(f"+---------------------------------------------+")
        
    def runWS():
        print("\n-----Favorite Writer------")
        print("_____________________________\n")
        user_name = input("Enter Your Name: ")
        name = input("Enter Writer's Name: ")
        birthday = input("Enter Writer's Birthday: ")
        country = input("Enter Writer's Country: ")
        publisher = input("Enter Writer's Publisher: ")
        fave_book = input("Enter Favorite Book: ")
        global fave_writer
        fave_writer = Fave_Writer(user_name, name, birthday, country, publisher, fave_book)

        while True:
            trans = input("\nDo you want To Display your Favorite Writer? (y/n): ")
            if trans == "y":
                fave_writer.writer_display()
                exit()
            elif trans == "n":
                print("Exiting...")
                exit()
            else:
                print("Wrong Command!  Enter 'y' for yes and 'n' for no.\n")