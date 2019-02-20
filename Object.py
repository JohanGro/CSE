class Food(object):
    def __init__(self, health, fill, color, time,  plate=False):
        self.health = health
        self.fill = fill
        self.color = color
        self.plate = plate
        self.time_taken = time


health = 100
full = 20
print("letting health or fullness go down to 0 will result in death.")
apple = Food(10, 2, "red", 5, False)
fries = Food(-10, 5, "yellow", 10, True)
