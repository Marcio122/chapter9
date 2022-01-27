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


my_new_car = Car("a4", "audi", 2019)
print(my_new_car.get_descriptive_name())

# Modifying an Attribute’s Value Directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(30)
my_new_car.read_odometer()