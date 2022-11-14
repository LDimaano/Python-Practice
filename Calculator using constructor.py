class Operation:
    F_num = 0
    S_num = 0
    Answer_num = 0

    def __init__(self, fnum, snum):
        self.F_num = fnum
        self.S_num = snum

    def sum(self):
        self.Answer_num = self.F_num + self.S_num
        print(str(self.F_num) + " + " + str(self.S_num) + " = " + str(self.Answer_num))

    def difference(self):
        self.Answer_num = self.F_num - self.S_num
        print(str(self.F_num) + " - " + str(self.S_num) + " = " + str(self.Answer_num))

    def product(self):
        self.Answer_num = self.F_num * self.S_num
        print(str(self.F_num) + " * " + str(self.S_num) + " = " + str(self.Answer_num))

    def quotient(self):
        self.Answer_num = self.F_num / self.S_num
        print(str(self.F_num) + " / " + str(self.S_num) + " = " + str(self.Answer_num))

U_repeat = "Y"
while (U_repeat == "Y"):
    U_1num = int(input("\nEnter first number: "))
    U_2num = int(input("Enter second number: "))
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division\n")
    User_Choice = input("Enter choice: ")
    UI = Operation(U_1num, U_2num)

    if User_Choice == "1":
        UI.sum()
    elif User_Choice == "2":
        UI.difference()
    elif User_Choice == "3":
        UI.product()
    elif User_Choice == "4":
        UI.quotient()
    else:
        print("Invalid Input!")
    U_repeat = str(input("\nCalculate again? [Y/N]: "))







