class Vehicle(object):
    def __init__(self, name, engine):
        self.name = name
        self.engine_type = engine


class Car(Vehicle):
    def __init__(self, name, engine_type, body_type):
        super(Car, self).__init__(name, engine_type)
        self.body_type = body_type
        self.steering_wheel = True
        self.engine_status = False  # Because the engine is off.
        self.fuel = 100

    def start_engine(self):
        self.engine_status = True
        print("You turn the key and the car turns on")
        print(self.fuel)

    def move_forward(self):
        if self.engine_status is True:
            if self.fuel >= 0:
                self.fuel -= 1
                print("You move forward")
                print(self.fuel)
            else:
                print("You do not have any gas")

    def turn_left(self):
        self.fuel -= 1
        print("You turn left")
        print(self.fuel)

    def turn_right(self):
        self.fuel -= 1
        print("You turn right")
        print(self.fuel)

    def turn_off(self):
        self.engine_status = False
        print("You turn the engine off")
        print("You have %s fuel left" % self.fuel)


class Corvette(Car):
    def __init__(self):
        super(Corvette, self).__init__("Corvette", "Gas", "Slim")


Car = Corvette()
Car.start_engine()
while Car.fuel >= 0:
    Car.move_forward()
