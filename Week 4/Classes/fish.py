class Fish (object):  #can remove (object) also, only for superclass
      
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")
        
fish_1 = Fish('A')
        
print(fish_1)