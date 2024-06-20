
class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(self.name,"is old enough to drive")

class Child(Adult):

    def can_drive(self):
        print(self.name,"is too young to drive")


name = input("What is your name? ")

while True:            
    try:
        age=int(input("How old are you? "))
        break
    except ValueError:
        print("The input was not a valid age.")

eye_colour=input("What is your eye colour? ")
hair_colour = input("What is your hair colour? ")

if age >= 18:
    person_1 = Adult(name, age, eye_colour, hair_colour)
    person_1.can_drive()
else:
    person_1 = Child(name, age, eye_colour, hair_colour)
    person_1.can_drive()