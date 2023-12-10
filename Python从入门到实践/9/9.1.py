from restaurant import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=["sh*t","concrete No.42","Han Xin's 13 spears"]

    def show_flavors(self):
        print(f"We have {self.flavors} ice cream.")

firststand=IceCreamStand("SmallStand","Ice cream")
firststand.show_flavors()