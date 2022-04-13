class Animal:
    def __init__(self):
        self.number_of_eyes = "two eyes"

    def breath(self):
        print("Inhale and Exhale")

# to inherit from a class add that class inside (). here Fish class is inheriting from Animal class


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):       # adding own methods to methods from Fish class while retaining everything from Animal class
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("moving in water")

fish = Fish()
fish.breath()
print(fish.number_of_eyes)
fish.swim()



