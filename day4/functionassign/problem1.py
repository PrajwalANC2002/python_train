#P1. Define an animal class with name and define a say_hello method. It should say "Hello, My name is {name}

class Animal:
    #constructor
    def __init__(self,name):
        self.name = name


    def say_hello(self):
        print(f"Hello, My name is {self.name}")


#P1.1. Create two animals with different names and call the say_hello method on them
animal1 = Animal("Tommy")
animal2 = Animal("Jerry")

animal1.say_hello()
animal2.say_hello()
