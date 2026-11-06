class Car:
    showroom = "NewAge"

    def __init__(self, make, model, year, color, started=False, speed=0, max_speed=200):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = started
        self.speed = speed
        self.max_speed = max_speed

    @classmethod
    def change_showroom(cls, new_showroom):
        cls.showroom = new_showroom

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @staticmethod
    def show_intro_message():
        print("This class is used to model and manage real-world car objects and their attributes.")


# Create instances
toyota_camry = Car(make="Toyota", model="Camry", year="2022", color="Red")
ford_mustang = Car(make="Ford", model="Mustang", year=2022, color="Black")

# Explicitly print outputs
print(toyota_camry.make)
print(ford_mustang.__dict__)
print(str(toyota_camry))
Car.show_intro_message()