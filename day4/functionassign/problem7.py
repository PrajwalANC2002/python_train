#P7. Change print_info method to a name "__str__". What happens when you print an object of that class? This is the Pythonic way of printing info about an object and what happens when you do print on a list or a dictionary


class Person:
    # Constructor - the first argument is always self
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Define a print_info method that prints the name and age of the person
    def __str__(self):
        return(f"Name: {self.name}, Age: {self.age}")

obj = Person("Prajwal","22")
print(obj)

list_person = Person(["person1","person2","person3"],[22,24,25])
print(list_person)

dict_person = Person({"person1","person2","person3"},{22,23,25})
print(dict_person)
