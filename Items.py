inventory = []

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print("you picked up %s" % self.name)
        inventory.append(self)


class Weapons(Item):
    def __init__(self, name, description, power):
        super(Weapons, self).__init__(name, description)
        self.attack = power

    def swing(self):
        print("you swing and do %s damage!" % self.attack)


class Armor(Item):
    def __init__(self, name, description, protect):
        super(Armor, self).__init__(name, description)
        self.protection = protect

    def shield(self):
        if self.protection <= 30:
            self.protection = self.protection * 2
            print("Your defense went up")
        else:
            print("Your defense has reached the max.")

    def change(self):
        input("change to what?")


class Consumables(Item):
    def __init__(self, name, description, health):
        super(Consumables, self).__init__(name, description)
        self.health = health

    def eat(self):
        print("you ate %s and gained %s health" % (self.name, self.health))


class WoodSword(Weapons):
    def __init__(self, name, description, power):
        super(WoodSword, self).__init__(name, description, power)


class Poison(Consumables):
    def __init__(self, name, description, health):
        super(Poison, self).__init__(name, description, health)

    def eat(self):
        print("you ate %s and your health was drained." % self.name)


class Glider(Armor):
    def __init__(self):
        super(Glider, self).__init__(name="Glider", description="it can help you glide to places that you couldn't"
                                                                " normally reach", protect=0)


class IronSword(Weapons):
    def __init__(self, name, description, power):
        super(IronSword, self).__init__(name, description, power)

    def stab(self):
        print("the enemy you were fighting was stabbed by your sword.")


class EnhancedSword(Weapons):
    def __init__(self, name, description, power):
        super(EnhancedSword, self).__init__(name, description, power)


class Axe(Weapons):
    def __init__(self, name, description, power):
        super(Axe, self).__init__(name, description, power)

    def hit(self):
        print("you hit the enemy with the bottom of the axe.")

    def cutdown(self):
        print("you cut down some trees in the nearby area.")


class Fancy(Armor):
    def __init__(self, name, description, protect):
        super(Fancy, self).__init__(name, description, protect)

    def shield(self):
        print("You shouldn't get our suit ruined.")


class Medicine(Consumables):
    def __init__(self, name, description, health):
        super(Medicine, self).__init__(name, description, health)


class Bombs(Weapons):
    def __init__(self, name, description, power):
        super(Bombs, self).__init__(name, description, power)

    def use(self):
        print("you blew up whatever was in the room.")


Bomb = Bombs("Bombs", "something used to blow up areas or things.", 10)
Bombs.pickup()
print(inventory)