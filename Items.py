class Player(object):
    def __init__(self):
        self.health = 100
        self.damage = 10
        self.inventory = []
        self.Money = 0


Person = Player()


class Item(object):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def pickup(self):
        print("you picked up %s" % self.name)
        Person.inventory.append(self.name.upper())


class ItemShop(Item):
    def __init__(self, name, description):
        super(ItemShop, self).__init__(name, description, price=0)
        self.selling = []

    def sell(self):
        p = input("sell what")
        if p.upper() in Person.inventory:
            Person.Money += self.price
            print(Person.Money)

    def check(self):
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
        if self.name.upper() in Person.inventory:
            Person.health += self.health
            print("you ate %s and gained %s health" % (self.name, self.health))
            print(Person.health)
        if self.name.upper() not in Person.inventory:
            print("You do not have a %s in your inventory." % self.name)


class WoodSword(Weapons):
    def __init__(self, name, description, power, price):
        super(WoodSword, self).__init__(name, description, power, price)


class Poison(Consumables):
    def __init__(self, name, description, health, price):
        super(Poison, self).__init__(name, description, health, price)

    def eat(self):
        if self.name.upper() in Person.inventory:
            Person.health -= self.health
            print("you ate %s and your health was drained." % self.name)
        if self.name.upper() not in Person.inventory:
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


class Bombs(Weapons):
    def __init__(self, name, description, power, price):
        super(Bombs, self).__init__(name, description, power, price)

    def use(self):
        print("you blew up whatever was in the room.")


Shop = ItemShop("Shop", "hello, here to sell or buy?")
Red_Mushroom = Poison("Red Mushroom", "a bright red mushroom found in the wild.", 20, 2)
Tonic = Medicine("Tonic", "A healing item to heal wounds.", 10, 15)
Bomb = Bombs("Bombs", "something used to blow up areas or things.", 10, 5)
Bomb.pickup()
Bomb.use()
Red_Mushroom.pickup()
print(Person.inventory)
print(Person.health)
Red_Mushroom.eat()
print(Person.health)
Tonic.eat()
print(Person.health)
print(Shop.selling)

