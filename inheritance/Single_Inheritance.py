class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"{self.brand} is my car.")

class Car(Vehicle):  
    def drive (self):
        print(f"I am driving my {self.brand}.")