# Base Class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.strength_level = strength_level

    def display_info(self):
        print(f"{self.name} has the power of {self.power} and strength level {self.strength_level}.")

    def fight(self):
        print(f"{self.name} uses {self.power} to fight!")


# Subclass (Inheritance + Encapsulation)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"Flying at speed: {self.flight_speed} km/h!")

    def fight(self):
        super().fight()
        print("And attacks from the sky!")


# Test
def main():
    hero1 = Superhero("ShadowKnight", "Invisibility", 85)
    hero2 = FlyingSuperhero("SkyBlazer", "Fire Manipulation", 90, 300)

    hero1.display_info()
    hero1.fight()

    print()

    hero2.display_info()
    hero2.fight()
    hero2.fly()

if __name__ == "__main__":
    main()
