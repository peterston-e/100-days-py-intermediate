# ******* class inheritance *********


class Dog:
    def __init__(self):
        self.temperament = "loyal"


class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.color = "black"


doggo = Dog()

my_doggo = Labrador()

print(doggo.temperament)
print(my_doggo.temperament)
print(my_doggo.color)
