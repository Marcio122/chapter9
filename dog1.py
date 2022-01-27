class Dog:
    species = "Canis Familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(f"My dog's name is {buddy.name} he is {buddy.age}")
print(buddy.age)
print(buddy.species)
print(miles.species)
buddy.name = "Bino"
print(buddy.name)