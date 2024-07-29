from abc import ABC


class Dog:
    species = "mammal"

    def __init__(self, breed, name) -> None:
        self.breed = breed
        self.name = name

    def bark(self, number):
        print(f"WOOF My name is {self.name} and the number is {number}")


dog = Dog("Lab", "Sammy")


print(dog.breed)
print(dog.name)
print(dog.species)
dog.bark(10)


class Circle:
    pi = 3.14

    def __init__(self, radius=1) -> None:
        self.radius = radius
        self.area = radius * radius * self.pi

    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle(10)
print(my_circle.area)
print(my_circle.get_circumference())


class Animal:

    def __init__(self) -> None:
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


myanimal = Animal()
myanimal.eat()


class Dog2(Animal):

    def __init__(self) -> None:
        super().__init__()
        print("Dog created")

    def who_am_i(self):
        print("I am a dog!")

    def bark(self):
        print("WOOF")


mydog = Dog2()
mydog.eat()
mydog.who_am_i()
mydog.bark()


# Polymorphism:
class Animal3:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")


class Dog3(Animal3):
    def speak(self):
        return self.name + "says woof"


class Cat(Animal3):
    def speak(self):
        return self.name + "says meow"


niko = Dog3("Niko")
felix = Cat("felix")


def pet_speak(pet):
    print(pet.speak())


pet_speak(niko)
pet_speak(felix)
