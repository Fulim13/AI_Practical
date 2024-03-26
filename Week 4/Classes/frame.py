class Animal:
    def __init__(self):
        print("A {} object is created".format(Animal.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Animal.__mro__[0].__name__.lower(), Animal.__mro__[1].__name__.lower()))

class Fish(Animal):
    def __init__(self):
        print("A {} object is created".format(Fish.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Fish.__mro__[0].__name__.lower(), Fish.__mro__[1].__name__.lower()))
        
class Mammal(Animal):
    def __init__(self):
        print("A {} object is created".format(Mammal.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Mammal.__mro__[0].__name__.lower(), Mammal.__mro__[1].__name__.lower()))
        self.obj_verterbra = Vertebra()
        print("The {} has {}".format(Mammal.__mro__[0].__name__.lower(), Vertebra.__mro__[0].__name__.lower()))

class Bear(Mammal):
    def __init__(self):
        print("A {} object is created".format(Bear.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Bear.__mro__[0].__name__.lower(), Bear.__mro__[1].__name__.lower()))
        self.obj_fur = Fur()
        print("The {} has {}".format(Bear.__mro__[0].__name__.lower(), Fur.__mro__[0].__name__.lower()))

class Whale(Mammal):
    def __init__(self):
        print("A {} object is created".format(Whale.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Whale.__mro__[0].__name__.lower(), Whale.__mro__[1].__name__.lower()))

class Cat(Mammal):
    def __init__(self):
        print("A {} object is created".format(Cat.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Cat.__mro__[0].__name__.lower(), Cat.__mro__[1].__name__.lower()))
        self.obj_fur = Fur()
        print("The {} has {}".format(Cat.__mro__[0].__name__.lower(), Fur.__mro__[0].__name__.lower()))
        
class Vertebra:
    def __init__(self):
        print("A {} object is created".format(Vertebra.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Vertebra.__mro__[0].__name__.lower(), Vertebra.__mro__[1].__name__.lower()))

class Water:
    def __init__(self):
        print("A {} object is created".format(Water.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Water.__mro__[0].__name__.lower(), Water.__mro__[1].__name__.lower()))
        self.obj_fish = Fish()
        self.obj_whale = Whale()
        print("The {} lives in the {}".format(Fish.__mro__[0].__name__.lower(), Water.__mro__[0].__name__.lower()))
        print("The {} lives in the {}".format(Whale.__mro__[0].__name__.lower(), Water.__mro__[0].__name__.lower()))

class Fur:
    def __init__(self):
        print("A {} object is created".format(Fur.__mro__[0].__name__.lower()))
        print("A {} is an instance of {}\n".format(Fur.__mro__[0].__name__.lower(), Fur.__mro__[1].__name__.lower()))