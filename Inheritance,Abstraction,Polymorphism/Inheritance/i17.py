class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow")

class Cow(Animal):
    def sound(self):
        print("Cow: Moo")


dog = Dog()
cat = Cat()
cow = Cow()
dog.sound()
cat.sound()
cow.sound()