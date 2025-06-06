# Base Class
class Vehicle:
    def move(self):
        print("Vehicle is moving...")


# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water ")


# Test
def main():
    vehicles = [Car(), Plane(), Boat()]

    for v in vehicles:
        v.move()

if __name__ == "__main__":
    main()
