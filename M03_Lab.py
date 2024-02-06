class Vehicle:
    def __init__(self):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__()
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


vehicleType = input('Enter the type of vehicle: ')
Vehicle.type = vehicleType

vehicleYear = input('Enter the year of the vehicle: ')
Vehicle.year = vehicleYear

vehicleMake = input('Enter the make of the vehicle: ')
Vehicle.make = vehicleMake

vehicleModel = input('Enter the model of the vehicle: ')
Vehicle.model = vehicleModel

vehicleDoors = input('Does the vehicle have 2 or 4 doors? ')
Vehicle.doors = vehicleDoors

vehicleRoof = input('Does the vehicle have a solid or sun roof? ')
Vehicle.roof = vehicleRoof

print(f'Vehicle Type: {Vehicle.type}\nYear: {Vehicle.year}\nMake: {Vehicle.make}\nModel: {Vehicle.model}\n'
      f'Number of doors: {Vehicle.doors}\nType of roof: {Vehicle.roof} ')
