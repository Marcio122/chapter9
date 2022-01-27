class Restaurant:

    def __init__(self, name, coisine_type):
       
        self.name = name
        self.coisine_type = coisine_type
    
    def describe_restaurant(self):
        print(f"My restaurant's name is {self.name}, come to eat in our {self.coisine_type} food restaurant.")
    
    def open_restaurant(self, opened):
        print(f"The restaurant is now {opened}")

my_food = Restaurant("KingsFood", "modern")

my_food.describe_restaurant()
my_food.open_restaurant("opened")