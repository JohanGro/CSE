import Special_Random


class WaterGun(object):  # What The Water Gun Has
    def __init__(self, capacity, distance=30, stock=False):
        # These are things that a water gun has
        # all of these should be relevant to our program
        self.capacity = capacity
        self.range = distance
        self.trigger = True
        self.stock = stock
        self.duration_of_pressure = capacity

    def shoot(self, time):  # What The Water Gun Can Do
        if self.trigger:
            if self.duration_of_pressure <= 0:
                print("There's no pressure")
            elif self .duration_of_pressure < time:
                print("You ran out of pressure after firing for %s seconds" % self.duration_of_pressure)
                self.duration_of_pressure = 0
            else:
                print("you shoot for %s seconds" % time)
                self.duration_of_pressure -= time
        else:
            print("There's no trigger!")

    def pump_it_up(self):
        self.duration_of_pressure = 5
        print("You pump the tank back to full pressure!")
# Initialize the objects


My_Water_Gun = WaterGun(5, 40, True)
Your_Water_Gun = WaterGun(1.0, 1, False)
Weibe_Water_Gun = WaterGun(999999, 99999999999999, True)
A_Water_Gun = WaterGun(0.1)


# do stuff with water gun
My_Water_Gun.shoot(5)
My_Water_Gun.pump_it_up()
My_Water_Gun.shoot(1)
Your_Water_Gun.shoot(5)
Weibe_Water_Gun.shoot(999999)

print(Special_Random.RandomWeibe.special_random())

