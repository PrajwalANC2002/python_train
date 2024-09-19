#P5. Set the food to "bones" in the Dog class constructor and to "mice" in the Cat class constructor

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

class Cat(Animal):
    #constructor
    def __init__(self,name):
        #call the parent constructor
        super().__init__(name)
        self.food = "bones"
    
    def say_hello(self):
        print(f"Hello, My name is {self.name} and I am a cat")

class Dog(Animal):

    def __init__(self,name):
        super().__init__(name)
        self.food = "mice"

    def say_hello(self):
        print(f"Hello, My name is {self.name} and I am a dog")

#P6. Call the eat method on both the dogs and cats
cat1 = Cat("Whiskers")
cat1.say_hello()
cat1.eat()

dog1 = Dog("Buddy")
dog1.say_hello()
dog1.eat()


