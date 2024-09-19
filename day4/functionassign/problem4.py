#P4. Add a food attribute to the Animal class and define a eat method that prints "I do not eat anything" if food is nil, else prints "I eat {food}". Initialise food to nil in the constructor

class Animal:
    #constructor
    def __init__(self,name):
        self.name = name
        self.food = None

    def say_hello(self):
        print(f"Hello, My name is {self.name}")

    def eat(self):
        if(self.food is None):
            print("I do not eat anything")
        else:
            print(f"I eat {self.food}")

animal1 = Animal("lion")
animal1.say_hello()
animal1.eat()  

animal1.food = "meat"
animal1.eat()  


