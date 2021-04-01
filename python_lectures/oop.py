class Dog():

    # Class object attribute
    species = "mammal"

    # ie. constructor
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


mydog = Dog(breed = "lab", name = "sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_radius):
        self.radius = new_radius

myc = Circle(3)
print(myc.radius)
myc.set_radius(999)
print(myc.area())


# INHERITANCE
class Animal():
    def __init__(self):
        print('animal created')

    def whoAmI(self):
        print("animal")
        return 'aninal'

    def eat(self):
        print('eating')

    # similar to toString()
    def __str__(self):
        return 'I am an {}'.format(self.whoAmI())
    # defines what to do when len(animal) is called
    def __len__(self):
        return len(self.whoAmI())


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('dog created')

    def whoAmI(self):
        print('dog')
        return 'dog'

    def eat(self):
        print('eating')


animal = Animal()
print(animal.whoAmI())
print(animal.eat())
print(animal)
print(len(animal))

dog = Dog()
print(dog.whoAmI())
print(dog.eat())
print(dog)
print(len(dog))




