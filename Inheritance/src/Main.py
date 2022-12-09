import Fave_Actor
import Fave_Singer
import Fave_Writer
import Fave_Chef

while True:
    print(f"1. Favorite Actor")
    print(f"2. Favorite Singer")
    print(f"3. Favorite Writer")
    print(f"4. Favorite Chef")
    print(f"5. Exit")
    choice = int(input("Enter Choice -> "))

    if choice == 1:
        Fave_Actor.Fave_Actor.runFA()
    elif choice == 2:
        Fave_Singer.Fave_Singer.runFS()
    elif choice == 3:
        Fave_Writer.Fave_Writer.runWS()
    elif choice == 4:
        Fave_Chef.Fave_Chef.runCS()
    elif choice == 5:
        exit()
    else:
        print("Invalid!")



