import random


# Room


class Room(object):
    def __init__(self, name, description="", north=None, east=None, south=None, west=None, up=None, down=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.characters = []
        self.items = []

    def look(self):
        print("~-~" * 20)
        print("%s: %s" % (self.name, self.description))
        print("Items: %s" % self.items)


class store(object):
    def __init__(self, selling, location):
        self.selling = selling
        self.location = location

    def buy(self):
        if Person.current_location == self.location:
            print("your money: %s" % Person.money)
            e = 0
            for i in self.selling:
                thing = self.selling[e]
                print("%s: price - %s" % (thing.name, thing.price))
                e += 1
            buying = input("what would you like to buy?")
            w = 0
            for i in self.selling:
                if buying.lower() == self.selling[w].name:
                    if Person.money >= self.selling[w].price:
                        Person.money -= self.selling[w].price
                        print("you brought a %s for %s dollars." % (self.selling[w].name, self.selling[w].price))
                        Person.inventory.append(self.selling[w])
                    else:
                        print("you do not have enough money for this item.")
                w += 1

    def sell(self):
        if Person.current_location == self.location:
            print(Person.money)
            selling = input("what would you like to sell")
            r = 0
            for i in Person.inventory:
                if selling.lower() == Person.inventory[r].name:
                    sellprice = Person.inventory[r].price / 2
                    print("you sold a %s for %s dollars" % (Person.inventory[r].name, sellprice))
                    Person.money += sellprice
                    Person.inventory.remove(Person.inventory[r])
                    print("your money is now at %s" % Person.money)
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
        o = input("use what?")
        if o.lower() in ("bombs", "bomb"):
            print("you blew up whatever was in the room.")


class Wild(Item):
    def __init__(self, name, description, price, location):
        super(Wild, self).__init__(name, description, price)
        self.location = location


class Dirt(Item):
    def __init__(self, name, description, price):
        super(Dirt, self).__init__(name, description, price)


class Bandana(Armor):
    def __init__(self, name, description, protect,  price):
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


# Characters


class Character(object):
    def __init__(self, name, health, weapon, armor, accuracy, money):
        self.inventory = []
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.accuracy = accuracy
        self.money = money

    def take_damage(self, attack):
        self.health -= attack
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def pickup(self, item):
        self.inventory.append(item)
        print("%s picked up some %s" % (self.name, item.name))

    def throw(self, target, item):
        if item.name in self.inventory:
            self.inventory.remove(item.name)
            print(self.inventory)
            print("%s threw some dirt" % self.name)
            print("%s's accuracy was lowered" % target.name)
            target.accuracy -= 1

    def attack(self, target):
        rand1 = random.randint(0, 10)
        rand2 = random.randint(0, 10)
        print(rand2)
        if self.accuracy is 10:
            if rand1 is 0:
                print("%s attacks for %d damage, critical hit" % (self.name, self.weapon.attack * 2))
                target.take_damage(self.weapon.attack * 2)
            if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                target.take_damage(self.weapon.attack)
        if self.accuracy in (8, 9):
            if rand2 in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                if rand1 is 0:
                    print("%s attacks for %d damage, critical hit" % (self.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if rand2 in (9, 10):
                print("they missed the attack.")
        if self.accuracy in (4, 5, 6, 7):
            if rand2 in (0, 1, 2, 3, 4, 5):
                if rand1 is 0:
                    print("%s attacks for %d damage, critical hit" % (self.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if rand2 in (6, 7, 8, 9, 10):
                print("they missed the attack.")
        if self.accuracy in (0, 1, 2, 3):
            if rand2 in (1, 2):
                if rand1 is 0:
                    print("%s attacks for %d damage, critical hit" % (self.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            else:
                print("They missed the attack")


class Npc(Character):
    def __init__(self, text, name, inventory, health, weapon, armor, accuracy, money):
        super(Npc, self).__init__(name, health, weapon, armor, accuracy, money)
        self.text = text
        self.inventory = inventory


# Player


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.damage = 10
        self.inventory = []
        self.money = 0
        self.accuracy = 10
        self.weapon = woodsword

    def take_damage(self, attack):
        self.health -= attack
        if self.health < 0:
            self.health = 0
        print("you have %d health left." % self.health)

    @staticmethod
    def equip():
        equipness = input("equip what")
        o = 0
        for i in Person.inventory:
            if equipness.lower() == Person.inventory[o].name:
                try:
                    print("you equipped the %s" % Person.inventory[o].name)
                    print("%s: %s" % (Person.inventory[o].name, Person.inventory[o].description))
                    print("the item that was in your weapon slot had been transferred to your inventory")
                    Person.inventory.append(Person.weapon)
                    Person.weapon = Person.inventory[o]
                    Person.inventory.remove(Person.inventory[o])
                except AttributeError:
                    print("that item is not a weapon.")
            o += 1

    @staticmethod
    def drop(thing):
        print("you dropped the %s" % thing.name)
        Person.inventory.remove(thing)
        p = 0
        for i in Rooms:
            if Person.current_location == Rooms[p]:
                roomlocate = Rooms[p]
                roomlocate.items.append(thing)
            p += 1

    def attack(self, target):
        rand1 = random.randint(0, 10)
        rand2 = random.randint(0, 10)
        print(rand2)
        if self.accuracy is 10:
            if rand1 is 0:
                print("you attack %s for %d damage, critical hit" % (target.name, self.weapon.attack * 2))
                target.take_damage(self.weapon.attack * 2)
            if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                print("you attack %s for %d damage" % (target.name, self.weapon.attack))
                target.take_damage(self.weapon.attack)
        if self.accuracy in (8, 9):
            if rand2 in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                if rand1 is 0:
                    print("you attack %s for %d damage, critical hit" % (target.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("you attack %s for %d damage" % (target.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if rand2 in (9, 10):
                print("you missed the attack.")
        if self.accuracy in (4, 5, 6, 7):
            if rand2 in (0, 1, 2, 3, 4, 5):
                if rand1 is 0:
                    print("you attack %s for %d damage, critical hit" % (target.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("you attack %s for %d damage" % (target.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if rand2 in (6, 7, 8, 9, 10):
                print("you missed the attack.")
        if self.accuracy in (0, 1, 2, 3):
            if rand2 in (1, 2):
                if rand1 is 0:
                    print("you attack %s for %d damage, critical hit" % (target.name,self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("you attack %s for %d damage" % (target.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            else:
                print("you missed the attack")

    def battle(self, target):
        battle = True
        while battle is True:
            print("%s:" % target.name)
            print("%s's health: %s" % (target.name, target.health))
            print("~-~" * 20)
            print("your health: %s" % self.health)
            action = None
            while action is None:
                action = input("what would you like to do? attack, bag, run")
            if action.lower() in ['attack', 'a']:
                Person.attack(target)
                target.attack(Person)
            if action.lower() in ['item', 'bag']:
                w = 0
                for i in Person.inventory:
                    print(Person.inventory[w].name)
                    w += 1
                e = input("eat what")
                num = 0
                for i in Person.inventory:
                    if e.lower() == Person.inventory[num].name:
                        Person.eat(Person.inventory[num])
                    num += 1
                target.attack(Person)

            if action.lower() in ['run', 'r']:
                ran = random.randint(0, 10)
                if ran in [10, 7, 5]:
                    print("you ran away from further combat.")
                    battle = False
                else:
                    print("you could not get away")
                    target.attack(Person)

            if target.health <= 0:
                print("The %s was taken down." % target.name)
                print("you got %s coins. they can be spent at shops." % target.money)
                Person.money += target.money
                print("gasp...")
                battle = False

            if Person.health <= 0:
                print("you lost the battle")
                print("you dropped 20 coins.")
                Person.money -= 20
                if Person.money <= 0:
                    Person.money = 0
                Person.current_location = Village
                print("Nurse: someone brought you in, i hope your feeling better.")
                print("your health went up to 100")
                Person.health = 100
                target.health = 100
                battle = False

    def talk(self, target):
        print("%s: %s" % (target.name, target.text))

    def pickup(self):
        resp = input("pickup what?")
        k = 0
        for i in self.current_location.items:
            if resp.lower() == self.current_location.items[k].name:
                if self.current_location in Rooms:
                    self.inventory.append(self.current_location.items[k])
                    print("you picked up a %s" % self.current_location.items[k].name)
                    self.current_location.items.remove(self.current_location.items[k])
            k += 1

    def eat(self, thing):
        if self.health >= 100:
            q = input("you will not gain anything from eating this item, would you still like to eat it?")
            if q.lower() in ("yes", "y"):
                print("you ate %s and did not gain anything." % thing.name)
                self.inventory.remove(thing)
            else:
                print("you did not eat the %s" % thing.name)
        else:
            print("current health: %s " % self.health)
            self.health += thing.health
            if self.health >= 100:
                nf = self.health - 100  # Nf for Not Finished calculations
                nf -= thing.health
                final = nf - nf - nf
                self.health = 100
                print("you ate the %s and gained %s health!" % (thing.name, final))
                print("your health is at %s" % self.health)
                self.inventory.remove(thing)
            else:
                print("you ate the %s and gained %s health!" % (thing.name, thing.health))
                print("your health is at %s" % self.health)
                self.inventory.remove(thing)

    def move(self, new_location):
        """This method moves a character to a new location
        :param new_location: The variable containing a room object
        """
        self.current_location = new_location
        chance = random.randint(0, 5)
        randbattle = 0
        if randbattle in [0, 1]:
            if chance in [0, 1]:
                Person.battle(weak_monster)
                weak_monster.health = 20
                randbattle = 0
        if randbattle in [2, 3]:
            if chance in [0, 1, 2, 3, 4, 5, 6]:
                Person.battle(weak_monster)
                weak_monster.health = 20
                randbattle = 0
        if randbattle in [4, 5]:
            Person.battle(weak_monster)
            weak_monster.health = 20
            randbattle = 0
        randbattle += 1


sword = Weapons("Sword", "a normal sword to use, used highly by knights in the royal guard.", 20, None)
carrots = Consumables("carrot", "a hearty vegetable used in cooking.", 20, 30)
Knightarmor = Armor("Knights armor", "Made of Iron, sturdy", 30, 50)
Broadsword = Weapons("Broadsword", "A double handed sword.", 40, 50)
woodBat = Weapons("Wood Bat", "A bat commonly used by big enemies.", 5, 5)
KeyforWell = WellKey("Well Key", "A rusted key passed down from generations before. it grants access to the Well.", None)
Tiller = Weapons("Tiller", "A tool used by farmers to till the soil.", 3, 5)
seeds = Consumables("seeds", "Would be better to plant them...", 5, 5)
watermelon = Consumables("watermelon", "A big fruit that came from small seeds", 30, 20)
acorn = Consumables("acorn", "a squirrel would enjoy this.", 5, 3)
apple = Consumables("apple", "a small red fruit", 10, 10)
axe = Axe("axe", "a huge axe, can be used to chop down trees in certain areas.", 10, None)
wood = Item("wood", "some wood that can be used to light a fire.", 5)
woodsword = Weapons("wood sword", "a fairly common weapon", 5, None)
Cake = Consumables("Cake", "a huge cake", 50, 40)
glider = Glider()
bandana = Bandana("bandana", "this will help you traverse the desert", 0, 50)
weak_monster = Character("monster", 20, woodBat, None, 10, 5)

Ominous_Room = Room("Ominous room", "It's a room with light blue walls. a large gate blocks the north exit.")
Forest_Entrance = Room("Forest Entrance", "a couple of apple trees grow here. acorns scatter the floor",
                       None, None, Ominous_Room)
Main_Road = Room("Main Road", "This road used to be highly traveled by. yet nobody can be seen.", None, None,
                 Forest_Entrance)
Town_Square = Room("Town Square", "The center of town. it used to be a place of happiness.",
                   None, None, Main_Road)
Shop = Room("Shop", "It's a place to buy a lots of helpful things!", None, None, Town_Square)
Desert = Room("Desert", "The hot air would be too hot to travel any further.", None, None, None, Shop)
Foothills = Room("Foothills", "The small hills surround the volcano and the mountains.", None, Shop)
Hilltop_Mansion = Room("Hilltop Mansion", "The doors are shut.", None, Foothills)
Highlands = Room("Highlands", "You can see everything from up here", Hilltop_Mansion)
Mountains = Room("Mountains", "this is where wild animals thrive. a shadow falls over you.", Highlands)
Village = Room("Village", "The village is painted many bright colors. It seems they have been in a drought, the well is"
                          " empty. the friendly gate keeper allows you in.", Mountains)
Floating_Shop = Room("Floating Shop", "The shop floats high over the world.", None, Mountains)
Below_The_Well = Room("Below The Well", "There are doors inside here. they are locked. maybe someone can open "
                                        "it for you.", None, None, None, None, Village)
Forest = Room("Forest", "The Forest filled with trees and wildlife.", None, Forest_Entrance, None, Village)
Rain_Forest = Room("Rain Forest", "The forest had large trees. its a perfect place for crocodiles and other animals "
                                  "alike.", None, None, None, Forest_Entrance)
Beach = Room("Beach", "The beach allows you to see into the vast ocean.", None, None, None, Rain_Forest)
Beach_Village = Room("Beach Village", "The people of the village tell you they would be delighted for you to stay.",
                     None, None, Beach)
Ocean_Bay = Room("Ocean Bay", "The ocean seems endless. It would be dangerous to swim any further.", Beach)
oasis = Room("Oasis", "a much better and cooler place than the desert.", None, None, Desert)
desert_temple = Room("desert temple", "The door to the temple is closed.", None, None, None, Desert)
town = Room("desert town", "the brightly colored town, you wonder how people can live in such hard conditions",
            None, None, desert_temple, oasis)
Ominous_Room.north = Forest_Entrance
Forest_Entrance.north = Main_Road
Forest_Entrance.west = Forest
Forest.west = Village
Main_Road.north = Town_Square
Town_Square.north = Shop
Shop.east = Desert
Shop.west = Foothills
Foothills.west = Hilltop_Mansion
Highlands.south = Mountains
Mountains.south = Village
Mountains.up = Floating_Shop
Village.down = Below_The_Well
Village.east = Forest
Floating_Shop.down = Mountains
Rain_Forest.east = Beach
Forest_Entrance.east = Rain_Forest
Beach.north = Beach_Village
Beach.south = Ocean_Bay
Hilltop_Mansion.south = Mountains
CentralStore = store([carrots, watermelon], Shop)

Rooms = [Ominous_Room, Forest_Entrance, Forest, Main_Road, Town_Square, Shop, Foothills, Highlands, Mountains, Village,
         Floating_Shop, Rain_Forest, Beach, Beach_Village, Below_The_Well]

Village.items = [carrots]
Forest_Entrance.items = [acorn, apple]
Ominous_Room.items = [apple]
Forest.items = [axe, wood]
Person = Player(Ominous_Room)
Gatekeeper = Npc("Ah, welcome to the village, im the gatekeeper, please do not cause any harm to"
                 "the people living here, i hope you enjoy your stay.", "gatekeeper", [KeyforWell], 100,
                 Broadsword, Knightarmor, 10 , 50)
Villagefarmer = Npc("oh, hello! have you said hello to the Gatekeeper yet?", 'farmer',
                    [seeds, watermelon], 100, Tiller, None, 10, 10)
VillageLumberjack = Npc("why hello there! thanks for talking to me but i better get back to work,"
                        " if you would like to help, grab the axe on the floor over there, and chop down"
                        " some trees. the wood could be very helpful!", "lumberjack", [apple], 100, axe, None, 10, 20)
Forest.characters = [VillageLumberjack]
Village.characters = [Gatekeeper, Villagefarmer]
Person.money = 0
Person.inventory.append(bandana)
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
while playing:
    print(Person.current_location.name)
    print(Person.current_location.description)
    command = input(">_")
    if command.lower() in ('equip', 'e'):
        Person.equip()
    if command.lower() in ('drop', 'd'):
        o = 0
        for i in Person.inventory:
            print(Person.inventory[o].name)
            o += 1
        dropping = input("drop what?")
        o = 0
        for i in Person.inventory:
            if dropping.lower() in Person.inventory[o].name:
                Person.drop(Person.inventory[o])
            o += 1
    if command.lower() in ('shop', 'buy', 'purchase'):
            CentralStore.buy()
    if command.lower() in ('sell', 'trade'):
            print("items:")
            add = 0
            for item in Person.inventory:
                print(Person.inventory[add].name)
                add += 1
            CentralStore.sell()
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    if command.lower() in ('inv', 'inventory', 'i'):
        print("items:")
        add = 0
        for item in Person.inventory:
            print(Person.inventory[add].name)
            add += 1
    if command.lower() in ('talk', 'speak', 't'):
        tar = 0
        for i in Person.current_location.characters:
            print(Person.current_location.characters[tar].name)
            tar += 1
        a = input("talk to who?")
        e = 0
        for i in Person.current_location.characters:
            if a.lower() == Person.current_location.characters[e].name:
                Person.talk(Person.current_location.characters[e])
            e += 1

    if command.lower() in ('eat', 'e'):
        e = input("eat what")
        num = 0
        for i in Person.inventory:
            if e.lower() == Person.inventory[num].name:
                Person.eat(Person.inventory[num])
            num += 1

    if command.lower() in ('battle', 'fight'):
        e = 0
        for i in Person.current_location.characters:
            print(Person.current_location.characters[e].name)
            e += 1
        commence = input("fight who?")
        k = 0
        for i in Person.current_location.characters:
            if commence.lower() == Person.current_location.characters[k].name:
                Person.battle(Person.current_location.characters[k])
            k += 1

    if command.lower() in ('cut', 'c'):
        s = input('use what to cut')
        if s.lower() in ['axe', 'a']:
            num = 0
            for i in Person.inventory:
                if s.lower() == Person.inventory[num].name:
                    Person.inventory[num].cutdown()
                num += 1
        else:
            print("you can not cut anything with this item.")

    if command.lower() in ('p', 'pickup'):
        print("items in the area:")
        l = 0
        for i in Person.current_location.items:
            print(Person.current_location.items[l].name)
            l += 1
        Person.pickup()

    elif command.lower() in directions:
        try:
            randbattle = 0
            # command = north
            room_object = getattr(Person.current_location, command)
            if room_object is None:
                raise AttributeError
            Person.move(room_object)
            randbattle += 1
        except AttributeError:
            print("I can not go that way")
