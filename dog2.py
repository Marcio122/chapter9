class Dog:
   
    species = "Canis Familiaris"
   
    def __init__(self, name, age, breed):
       
        self.name = name
        self.age = age
        self.breed = breed
           
        # Instance Method

    def description(self):
            return f"{self.name} is {self.age} years old."

        #Another Instance Method
    def speak(self, sound):
            return f"{self.name} says {sound}"
            
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshumund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

print(miles.description())
print(miles.speak("wow"))
print(buddy.speak("woof woof"))
print(jack.speak("yep yep"))
print(jim.speak("yep yep"))