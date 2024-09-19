#P2. Define a Dog class that inherits from Animal and redefine the say_hello method. It should say "Hello, My name is {name} and I am a dog"

class Animal:
    #constructor
    def __init__(self,name):
        self.name = name


    def say_hello(self):
        print(f"Hello, My name is {self.name}")

class Dog(Animal):
    #constructor
    def __init__(self,name):
        #call the parent constructor
        super().__init__(name)
    
    def say_hello(self):
        print(f"Hello, My name is {self.name} and I am a Dog")

#P2.1. Create two dogs with different names and call the say_hello method on them

Dog1 = Dog("Tom")
Dog2 = Dog("Leo")

Dog1.say_hello()
Dog2.say_hello()

