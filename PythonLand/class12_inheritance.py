#Inheritance

class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed

    def start(self):
        self.started = True
        print("Started, let's ride!")

    def stop(self):
        self.speed = 0
    
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vroom!")
        else:
            print("You need to start me first")

class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

class Motorcycle(Vehicle):
    def __init__(self, center_stand_out=False, started=False, speed=0):
        self.center_stand_out = center_stand_out
        super().__init__()
    
    def start(self):
        print("Sorry, out of fuel")