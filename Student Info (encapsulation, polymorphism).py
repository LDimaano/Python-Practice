class Payment:
    def __init__(self, tuition, miscellaneous):
        self.tuition = tuition
        self.miscellaneous = miscellaneous
    
    def total_payment(self):
        return self.tuition + self.miscellaneous
    

class Student:
    def __init__(self, name, student_number,age, year_level, tuition, miscellaneous):
        self.name = name
        self.student_number = student_number
        self.age = age
        self.year_level = year_level
        self.fee = Payment(tuition, miscellaneous)
    
    def display(self):
        print("Name: " + self.name)
        print("Student Number: " + self.student_number)
        print("Age: " + str(self.age))
        print("Year Level: " + self.year_level)
        print("Tuition Fee: " + str(self.fee.total_payment()))
        print()

student1 = Student(name="Jisoo", student_number="09-51232", age=18, year_level="1st year",tuition=50000, miscellaneous=5000)
student2 = Student(name="Jennie", student_number="10-09169", age=16, year_level="Grade 11",tuition=30000, miscellaneous=7000)
student3 = Student(name="Lisa", student_number="12-05636", age=14, year_level="Grade 9",tuition=25000, miscellaneous=10000)
student4 = Student(name="Rose", student_number="07-01125", age=21, year_level="3rd year",tuition=65000, miscellaneous=8000)

student1.display()
student2.display()
student3.display()
student4.display()

