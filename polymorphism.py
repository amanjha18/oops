# A concept of using common operation in different ways for different data input.

class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot can't swim")

class Penguin:
    def fly(self):
        print("penguin cannot fly")
    def swim(self):
        print("penguin can swim")

#common interface
def flying_test(bird):
    bird.fly()

# instantiate objects
pa = Parrot()
pe = Penguin() 

    
#passing the objects
flying_test(pa)
flying_test(pe)


