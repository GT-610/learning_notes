from car import ElectricCar,Car

my_electric_car=ElectricCar("Tesla","CyberTruck",2023)
print(my_electric_car.get_descriptive_name())
my_electric_car.describe_battery()

my_electric_car.battery.upgrade_battery()

my_electric_car.describe_battery()

my_fuel_car=Car("Ford","F150",2019)
print(my_fuel_car.get_descriptive_name())
my_fuel_car.get_descriptive_name()