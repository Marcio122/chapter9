class Dog:
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attribute"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
    
    def eat(self, food):
        print(f"{self.name} loves to eat {food}")

pet = Dog("Leao", 8)
#calling methods
pet.sit()
pet.roll_over()
pet.eat("Meat")