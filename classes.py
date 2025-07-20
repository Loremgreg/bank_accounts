class Vehicle:
    def __init__(self, make, model):
        self.make = make 
        self.model = model

    def moves(self):
        print("Moves along")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along")
    
    def get_make_model(self):
        super().get_make_model()
        print(f"FAA ID: {self.faa_id}")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along")

class GolfCart(Vehicle):
    pass

my_vehicle = Vehicle("Toyota", "Camry")
my_vehicle.get_make_model()
my_vehicle.moves()

my_plane = Airplane("Boing", "747", "id-666")
my_plane.get_make_model()
my_plane.moves()

my_truck = Truck("Scania", "007")
my_truck.get_make_model()
my_truck.moves()

golfcart = GolfCart("Yamaha", "R2D2")
golfcart.get_make_model()
golfcart.moves()

vehicles = [my_vehicle, my_plane, my_truck, golfcart]
for v in vehicles:
    print("*********************")
    v.get_make_model()
    v.moves()
