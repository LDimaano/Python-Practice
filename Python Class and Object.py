class Volleyball:
    def __init__(self, name, position, height, club):
        self.name = name
        self.position = position
        self.height = height
        self.club = club


Player_1 = Volleyball("Alyssa Valdez","Open Hitter", "1.75m", "Creamline")
Player_2 = Volleyball("Jia Morado", "Setter", "1.70m", "Creamline")
Player_3 = Volleyball("Yuki Ishikawa", "Open Hitter", "1.90m", "Milano")

print("Player 1: ")
print("Name: ", Player_1.name)
print("Position: ", Player_1.position)
print("Height: ", Player_1.height)
print("Club Team: ", Player_1.club)
print("\n")
print("Player 2: ")
print("Name: ", Player_2.name)
print("Position: ", Player_2.position)
print("Height: ", Player_2.height)
print("Club Team: ", Player_2.club)
print("\n")
print("Player 3: ")
print("Name: ", Player_3.name)
print("Position: ", Player_3.position)
print("Height: ", Player_3.height)
print("Club Team: ", Player_3.club)