class Item(object):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Weapons(Item):
    def __init__(self, name, description, power, price):
        super(Weapons, self).__init__(name, description, price)
        self.attack = power


class Armor(Item):
    def __init__(self, name, description, protect, price):
        super(Armor, self).__init__(name, description, price)
        self.protection = protect

    def block(self):
        if self.protection <= 30:
            self.protection = self.protection * 2
            print("Your defense went up")
        else:
            print("Your defense has reached the max.")

    def change(self):
        input("change to what?")


class Consumables(Item):
    def __init__(self, name, description, health, price):
        super(Consumables, self).__init__(name, description, price)
        self.health = health


class WoodSword(Weapons):
    def __init__(self, name, description, power, price):
        super(WoodSword, self).__init__(name, description, power, price)


class Poison(Consumables):
    def __init__(self, name, description, health, price):
        super(Poison, self).__init__(name, description, health, price)


class Glider(Armor):
    def __init__(self):
        super(Glider, self).__init__(name="Glider", description="it can help you glide to places that you couldn't"
                                                                " normally reach", protect=0, price=0)


class IronSword(Weapons):
    def __init__(self, name, description, power, price):
        super(IronSword, self).__init__(name, description, power, price)

    def stab(self):
        print("the enemy you were fighting was stabbed by your sword.")


class EnhancedSword(Weapons):
    def __init__(self, name, description, power, price):
        super(EnhancedSword, self).__init__(name, description, power, price)


class Axe(Weapons):
    def __init__(self, name, description, power, price):
        super(Axe, self).__init__(name, description, power, price)

    def hit(self):
        print("you hit the enemy with the bottom of the axe.")

    def cutdown(self):
        print("you cut down some trees in the nearby area.")


class Fancy(Armor):
    def __init__(self, name, description, protect, price):
        super(Fancy, self).__init__(name, description, protect, price)

    def block(self):
        print("You shouldn't get your suit ruined.")


class Medicine(Consumables):
    def __init__(self, name, description, health, price):
        super(Medicine, self).__init__(name, description, health, price)


class Food(Consumables):
    def __init__(self, name, description, health, price):
        super(Food, self).__init__(name, description, health, price)


class Bombs(Weapons):
    def __init__(self, name, description, power, price):
        super(Bombs, self).__init__(name, description, power, price)

    def use(self):
        a = input("use what?")
        if a.lower() in ("bombs", "bomb"):
            print("you blew up whatever was in the room.")


class Wild(Item):
    def __init__(self, name, description, price):
        super(Wild, self).__init__(name, description, price)


red_mushroom = Poison("Red Mushroom", "a bright red mushroom found in the wild.", 20, 2)
purple_mushroom = Food("Purple Mushroom", "a purple mushroom", 30, 20)
Tonic = Medicine("Tonic", "A healing item to heal wounds.", 10, 15)
Bomb = Bombs("Bombs", "something used to blow up areas or things.", 10, 20)