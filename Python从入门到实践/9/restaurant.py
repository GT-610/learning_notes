class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"Its name is {self.restaurant_name}. Its cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open!")

    def set_number_served(self,number_served):
        self.number_served=number_served

    def increment_served(self,add):
        self.number_served+=add