#Inheritance
class Car:
    
    def __init__(self, model, make, year):
        
        self.model = model
        self.make = make
        self.year = year
        #Setting a Default Value for an Attribute
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.model} {self.make} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        #print a statement showing the car's mileage
        print(f"This car has {self.odometer_reading} miles on it.")
    
    #modifying an attribute's value through a method
    def update_odometer(self, mileage):
        self.odometer_reading = mileage


class EletricCar(Car):
    def __init__(self, model, make, year):
        #"Initialize attributes of the parent class.
        super().__init__(model, make, year)
        self.battery_size = 75
    
    def describe_battery(self):
        #Printing a statement describing the battery
        print(f"This car has a {self.battery_size}-KWh battery")

my_tesla = EletricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()