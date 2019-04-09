# this was moved from my world map oop so some variables do not work as of now
class Store(object):
    def __init__(self, selling, location):
        self.selling = selling
        self.location = location

    def buy(self):
        if Person.current_location == self.location:
            print("your money: %s" % Person.money)
            ab = 0
            for z in self.selling:
                thing = self.selling[ab]
                print("%s: price - %s" % (thing.name, thing.price))
                ab += 1
            buying = input("what would you like to buy?")
            b = 0
            for y in self.selling:
                if buying.lower() == self.selling[b].name:
                    if Person.money >= self.selling[b].price:
                        Person.money -= self.selling[b].price
                        print("you brought a %s for %s dollars." % (self.selling[b].name, self.selling[b].price))
                        Person.inventory.append(self.selling[b])
                    else:
                        print("you do not have enough money for this item.")
                b += 1

    def sell(self):
        if Person.current_location == self.location:
            print(Person.money)
            selling = input("what would you like to sell")
            r = 0
            for x in Person.inventory:
                if selling.lower() == Person.inventory[r].name:
                    try:
                        sellprice = Person.inventory[r].price / 2
                        print("you sold a %s for %s dollars" % (Person.inventory[r].name, sellprice))
                        Person.money += sellprice
                        Person.inventory.remove(Person.inventory[r])
                        print("your money is now at %s" % Person.money)
                    except TypeError:
                        print("this item can not be sold, if you do not want it try dropping it")
                r += 1


# Items
class Item(object):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class Key(Item):
    def __init__(self, name, description, price):
        super(Key, self).__init__(name, description, price)


class WellKey(Key):
    def __init__(self, name, description, price):
        super(WellKey, self).__init__(name, description, price)

    def use(self):
        if self.name in Person.inventory:
            if Person.current_location == Below_The_Well:
                sealing_room = Room("The Sealing Room", "A place heavily used to make the troublesome people disappear"
                                                        "a sword lies in the center of the room.", None, None,
                                    Below_The_Well)
                villagetreasure = Room("The Village Treasury", "a place holding the treasures of the village.")
                Below_The_Well.north = sealing_room
                Below_The_Well.west = villagetreasure
                sealing_room.south = Below_The_Well
                villagetreasure.east = Below_The_Well
                print("The doors to the north and west have opened up.")
                Below_The_Well.description = "Under the well of the village. the passages continue to the north and" \
                                             " west"
                Person.inventory.remove(WellKey)
                print("you dropped the key.")
            else:
                print("you are not in the right location to use this item")
        else:
            print("you do not own this item...")


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

    @staticmethod
    def change():
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

    @staticmethod
    def stab():
        print("the enemy you were fighting was stabbed by your sword.")


class EnhancedSword(Weapons):
    def __init__(self, name, description, power, price):
        super(EnhancedSword, self).__init__(name, description, power, price)


class Axe(Weapons):
    def __init__(self, name, description, power, price):
        super(Axe, self).__init__(name, description, power, price)

    @staticmethod
    def hit():
        print("you hit the enemy with the bottom of the axe.")

    @staticmethod
    def cutdown():
        if Person.current_location == Forest:
            if wood in Forest.items:
                print("you cut down some trees in the nearby area.")
                Forest.items.append(wood)
            else:
                print("wood is already in the area")


class Fancy(Armor):
    def __init__(self, name, description, protect, price):
        super(Fancy, self).__init__(name, description, protect, price)

    def block(self):
        print("You shouldn't get your suit ruined.")


class Food(Consumables):
    def __init__(self, name, description, health, price):
        super(Food, self).__init__(name, description, health, price)


class Bombs(Weapons):
    def __init__(self, name, description, power, price):
        super(Bombs, self).__init__(name, description, power, price)

    @staticmethod
    def use():
        c = input("use what?")
        if c.lower() in ("bombs", "bomb"):
            print("you blew up whatever was in the room.")


class Wild(Item):
    def __init__(self, name, description, price, location):
        super(Wild, self).__init__(name, description, price)
        self.location = location


class Dirt(Item):
    def __init__(self, name, description, price):
        super(Dirt, self).__init__(name, description, price)

    def pickup(self, opposite):
        print("you throw dirt at %s" % opposite.name)
        opposite.accuracy -= 1
        print("%s's accuracy was ")


class Bandana(Armor):
    def __init__(self, name, description, protect, price):
        super(Bandana, self).__init__(name, description, protect, price)

    @staticmethod
    def equip():
        print("now you can traverse through the desert. the hot air wont bother you as much.")
        Desert.description = "with your bandanna you can continue through."
        Desert.north = oasis
        Desert.east = desert_temple
        desert_temple.north = town
        oasis.west = town

    @staticmethod
    def unequip():
        Desert.description = "The hot air would be too hot to travel any further."
        print("the desert is now too harsh to traverse")
        Desert.north = None
        Desert.east = None
        if Person.current_location == oasis:
            Person.current_location = Desert
        if Person.current_location == desert_temple:
            Person.current_location = Desert
        if Person.current_location == town:
            Person.current_location = Desert