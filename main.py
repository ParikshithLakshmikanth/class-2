class student:
    grade = 10
    name = "penguin"
    def introself(self):
        print("Hi! I am a student")
    def details(self):
        print("my name is:",self.name)
        print("I study in class",self.grade)

ob = student()
ob.introself()
ob.details()