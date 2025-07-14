class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def moves(self):
        print("Moves....")

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color


my_car = Vehicle("VW", "Black")

print(my_car.get_name())


class Airplane(Vehicle):
    def __init__(self, name, color, wingspan):
        super().__init__(name, color)
        self.wingspan = wingspan

    def moves(self):

        print("Flies....")


class Truck(Vehicle):
    def __init__(self, name, color, load_capacity):
        super().__init__(name, color)
        self.load_capacity = load_capacity

    def moves(self):

        print("Runs....")


class Bike(Vehicle):
    def __init__(self, name, color, type):
        super().__init__(name, color)
        self.type = type

    def moves(self):

        print("Rides....")


jet = Airplane("Boeing", "White", 100)
print(jet.get_name())
jet.moves()

truck = Truck("Volvo", "Red", 1000)
print(truck.get_name())
truck.moves()

bike = Bike("Harley", "Black", "Cruiser")
print(bike.get_name())
bike.moves()

print("\n\nPolymorphismm")

for x in (my_car, jet, truck, bike):
    print(x.name)
    x.moves()
