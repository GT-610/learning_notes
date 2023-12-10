class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name

    def update_odometer(self,mileage):
        if(mileage<=self.odometer_reading):
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading=mileage

    def increment_odometer(self,miles):
        if(miles>=0):
            self.odometer_reading+=miles
        else:
            printf("You can't roll back an odometer!")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

class Battery:
    def __init__(self,battery_size=40):
        self.battery_size=battery_size

    def upgrade_battery(self):
        if(self.battery_size!=65):
            self.battery_size=65

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

    def describe_battery(self):
        print(f"This car has a {self.battery.battery_size}-kWh battery.")