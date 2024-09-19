#P3. Define a Cat class that inherits from Animal and redefine the say_hello method. It should say "Hello, My name is {name} and I am a cat"

class Animal:
    #constructor
    def __init__(self,name):
        self.name = name


    def say_hello(self):
        print(f"Hello, My name is {self.name}")

class Cat(Animal):
    #constructor
    def __init__(self,name):
        #call the parent constructor
        super().__init__(name)
    
    def say_hello(self):
        print(f"Hello, My name is {self.name} and I am a cat")

#P3.1. Create two cats with different names and call the say_hello method on them

Cat1 = Cat("kitty")
Cat2 = Cat("charlie")

Cat1.say_hello()
Cat2.say_hello()

