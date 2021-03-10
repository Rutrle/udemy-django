my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print(type(my_list))


class Sample():
    pass


x = Sample()
print(type(x))


class Dog():
    # class object attribute
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog("Lab", "Sammy")
print(type(mydog))
print(mydog.breed)
otherdog = Dog(breed="Huskie", name="Black")
print(otherdog.breed)


class Circle():
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius*self.radius*Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
print(myc.radius)
print(myc.area())
myc.radius = 100
print(myc.radius)
myc.set_radius(10)
print(myc.radius)

# Inheritance


class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


mya = Animal()
mya.whoAmI()
mya.eat()


class Cat(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("CAT CREATED")

    def meow(self):
        print("MEOW")

    def eat(self):
        print("CAT EATING")


mycat = Cat()
mycat.whoAmI()
mycat.eat()
mycat.meow()
