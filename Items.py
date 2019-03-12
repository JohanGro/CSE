import WMOOPJG


class Item(object):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def pickup(self):
        print("you picked up %s" % self.name)
        WMOOPJG.Person.inventory.append(self.name.upper())


class ItemShop(Item):
    def __init__(self, name, description, selling, location):
        super(ItemShop, self).__init__(name, description, price=0)
        self.selling = selling
        self.location = location

    def sell(self):
        p = input("sell what")
        if p.upper() in WMOOPJG.Person.inventory:
            print(WMOOPJG.Person.Money)

    def buy(self):
        p = input("buy what?")
        if p in self.selling:
            p = input("are you sure you want to buy?")
            if p.lower() in ("yes", "y"):

                print("Yoi brought something from the shop. look in your inventory for more information.")
            if p.lower() in ("no", "n"):
                print("you decided not to buy anything.")
        else:
            print("this person does not sell that.")

    def check(self):
        print(self.description)
        print(self.selling)


class Weapons(Item):
    def __init__(self, name, description, power, price):
        super(Weapons, self).__init__(name, description, price)
        self.attack = power

    def swing(self):
        print("you swing and do %s damage!" % self.attack)


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

    def eat(self):
        if self.name.upper() in WMOOPJG.Person.inventory:
            WMOOPJG.Person.health += self.health
            print("you ate %s and gained %s health" % (self.name, self.health))
            print(WMOOPJG.Person.health)
        if self.name.upper() not in WMOOPJG.Person.inventory:
            print("You do not have a %s in your inventory." % self.name)


class WoodSword(Weapons):
    def __init__(self, name, description, power, price):
        super(WoodSword, self).__init__(name, description, power, price)


class Poison(Consumables):
    def __init__(self, name, description, health, price, location):
        super(Poison, self).__init__(name, description, health, price)
        self.location = location

    def eat(self):
        if self.name.upper() in WMOOPJG.Person.inventory:
            WMOOPJG.Person.health -= self.health
            print("you ate %s and your health was drained." % self.name)
            print(WMOOPJG.Person.health)
        if self.name.upper() not in WMOOPJG.Person.inventory:
            print("you do not have %s in your inventory" % self.name)


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
        print("You shouldn't get our suit ruined.")


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
        print("you blew up whatever was in the room.")


class Wild(Consumables):
    def __init__(self, name, description, health, price, location):
        super(Wild, self).__init__(name, description, health, price)
        self.location = location


red_mushroom = Poison("Red Mushroom", "a bright red mushroom found in the wild.", 20, 2, WMOOPJG.Forest)
purple_mushroom = Wild("Purple Mushroom", "a purple mushroom", 30, 20, None)
Tonic = Medicine("Tonic", "A healing item to heal wounds.", 10, 15)
Bomb = Bombs("Bombs", "something used to blow up areas or things.", 10, 20)
Shop = ItemShop("Shop", "hello, here to sell or buy?", (Tonic.name, Bomb.name), WMOOPJG.Shop)

AllItems = ["red mushroom", "purple mushroom"]
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
while playing:
    print(WMOOPJG.Person.current_location.name)
    print(WMOOPJG.Person.current_location.description)
    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    if command.lower() in ('pickup', 'pick up', 'p'):
        a = input("pickup what?")
        if a.lower() in ("red mushroom", "rm"):
            if WMOOPJG.Person.current_location == red_mushroom.location:
                Poison.pickup(red_mushroom)
            else:
                print("there is nothing called %s around here." % a)
    if command.lower() in ("eat", "e"):
        a = input("eat what?")
        if a.lower() in ("rm", "red mushroom"):
            Poison.eat(red_mushroom)

    if command.lower() in ("shop", "s"):
        if WMOOPJG.Person.current_location == Shop.location:
            a = input("Buying or selling, or looking around?")
            if a.lower() in ("buy", "buying"):
                Shop.buy()
            if a.lower() in "check":
                print(Shop.selling)

    if command.lower() in ('inv', 'inventory', 'i'):
        print(WMOOPJG.Person.inventory)

    elif command.lower() in directions:
        try:
            # command = north
            room_object = getattr(WMOOPJG.Person.current_location, command)
            if room_object is None:
                raise AttributeError
            WMOOPJG.Person.move(room_object)
        except AttributeError:
            print("I can not go that way")