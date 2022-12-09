import UserFave

class Fave_Chef(UserFave.UserFave):
    def __init__(self, user_name, name, birthday, country, restaurant, fave_dish):
        super().__init__(user_name, name, birthday, country)
        self.restaurant = restaurant
        self.fave_dish = fave_dish
    
    def getuser_name(self):
        return self.user_name
    
    def getname(self):
        return self.name
    
    def getbirthday(self):
        return self.birthday

    def getcountry(self):
        return self.country
    
    def getrestaurant(self):
        return self.restaurant
    
    def getfave_dish(self):
        return self.fave_dish

    def chef_display(self):
        print(f"+---------------------------------------------+")
        print(f"\n{self.getuser_name()}'s Favorite Chef\n")
        print(f"Name: {self.getname()}") 
        print(f"Birthday: {self.getbirthday()}") 
        print(f"Country: {self.getcountry()}")
        print(f"Restaurant Name: {self.getrestaurant()}")
        print(f"Favorite Dish: {self.getfave_dish()}\n")
        print(f"+---------------------------------------------+")
        
    def runCS():
        print("\n-----Favorite Chef------")
        print("_____________________________\n")
        user_name = input("Enter Your Name: ")
        name = input("Enter Chef's Name: ")
        birthday = input("Enter Chef's Birthday: ")
        country = input("Enter Chef's Country: ")
        restaurant = input("Enter Chef's Restaurant: ")
        fave_dish = input("Enter Favorite Dish: ")
        global fave_chef
        fave_chef = Fave_Chef(user_name, name, birthday, country, restaurant, fave_dish)

        while True:
            trans = input("\nDo you want To Display your Favorite Chef? (y/n): ")
            if trans == "y":
                fave_chef.chef_display()
                exit()
            elif trans == "n":
                print("Exiting...")
                exit()
            else:
                print("Wrong Command!  Enter 'y' for yes and 'n' for no.\n")