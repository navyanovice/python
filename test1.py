# Sample code to test OOP (Objected Oriented Programming)

class Animal:                                                                                   # Creating a class named 'Animal' with attributes 'name' & 'age'
    """ Create's a animal class  """    # doc-string
    def __init__(self,name,age):                                                                # Initializing the attributes by referring to the instance as 'self'
        self.name = name
        self.age = age
        print(f"Hey! I'm {self.name} & I'm {self.age} months old")
    
    def sound(self):                                                                            # Defining a 'sound' method on the 'Animal' class
        return "I'd love to talk to you, can you please learn meow meow and bow bow"
class Dog(Animal):                                                                              # Inherted into the child 'Dog' class from the Parent 'Animal' class
    def __init__(self,name,age,breed):                                                          # Adding a additonal attribute to the 'Dog' class naamed 'breed'
        Animal.__init__(self,name,age)                                                          # Calling the Parent class Contructor for the Dog Class 
        self.breed = breed
        print(f"I'm a {self.breed}")
    def sound(self):                                                                            # Modifying the 'sound' method on the 'Dog' class
        return "I only BOW BOW"
class Cat(Animal):                                                                              # Inherted into the child 'Dog' class from the Parent 'Animal' class
    def __init__(self,name,age,color):                                                          # Adding a additonal attribute to the 'Cat' class naamed 'color'
        Animal.__init__(self,name,age)                                                          # Calling the Parent class Contructor for the Dog Class 
        self.color = color
        print("My mumma calls me {self.name} * I'm a {color} cat & {self.age} old")
    def sound(self):                                                                            # Modifying the 'sound' method on the 'Dog' class
        return "My MEOW MEOW is music !"


a = Animal("meows",3)
print(a)
print(a.age)
print(a.sound())
d = Dog("Tony",5,"german shepherd")
print(d.name)
print(d.breed)
print(d.sound())                     # demonstrates polymorphirsm
g = Cat("Bublue",7,"White")
print(g.name)
print(g.color)
print(g.sound())
print(Animal.__doc__)
print(Animal.__dict__)
