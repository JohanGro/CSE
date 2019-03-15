import Items
import random


class Room(object):
    def __init__(self, name, description="",  north=None, east=None, south=None, west=None, up=None, down=None,
                 characters=None):
        self.name = name
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.characters = characters


class Character(object):
    def __init__(self, inventory, name, health, weapon, armor, accuracy):
        self.inventory = inventory
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.accuracy = accuracy

    def take_damage(self, attack):
        self.health -= attack
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def pickup(self, item):
        self.inventory.append(item.name)
        print("%s picked up some %s" % (self.name, item.name))

    def throw(self, target, item):
        if item.name in self.inventory:
            self.inventory.remove(item.name)
            print(self.inventory)
            print("%s threw some dirt" % self.name)
            print("%s's accuracy was lowered" % target.name)
            target.accuracy -= 1

    def attack(self, target):
        e = random.randint(0, 10)
        r = random.randint(0, 10)
        print(r)
        if self.accuracy is 10:
            if e is 0:
                print("%s attacks %s for %d damage, critical hit" % (self.name, target.name, self.weapon.attack * 2))
                target.take_damage(self.weapon.attack * 2)
            if e in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.attack))
                target.take_damage(self.weapon.attack)
        if self.accuracy in (8, 9):
            if r in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                if e is 0:
                    print("%s attacks %s for %d damage, critical hit" % (self.name, target.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if e in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if r in (9, 10):
                print("they missed the attack.")
        if self.accuracy in (4, 5, 6, 7):
            if r in (0, 1, 2, 3, 4, 5):
                if e is 0:
                    print("%s attacks %s for %d damage, critical hit" % (self.name, target.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if e in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if r in (6, 7, 8, 9, 10):
                print("they missed the attack.")
        if self.accuracy in (0, 1, 2, 3):
            if r in (1, 2):
                if e is 0:
                    print("%s attacks %s for %d damage, critical hit" % (self.name, target.name, self.weapon.attack * 2))
                    target.take_damage(self.weapon.attack * 2)
                if e in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            else:
                print("They missed the attack")


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.damage = 10
        self.inventory = []
        self.money = 0

    def pickup(self, item):
        self.inventory.append(item.name)
        print("you picked up a %s" % item.name)

    def move(self, new_location):
        """This method moves a character to a new location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


Ominous_Room = Room("Ominous room", "It's a room with light blue walls. a large gate blocks the north exit.")
Forest_Entrance = Room("Forest Entrance", "light glimmers through the treetops.", None, None, Ominous_Room)
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
                          " empty.", Mountains)
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

sword = Items.Weapons("Sword", "a normal sword to use, used highly by knights in the royal guard.", 20, None)
woodBat = Items.Weapons("Wood Bat", "A bat commonly used by big enemies.", 5, 5)


class Dirt(Items.Item):
    def __init__(self, name, description, price):
        super(Dirt, self).__init__(name, description, price)


Person = Player(Ominous_Room)
dirt = Dirt("dirt", "just some normal dirt from the ground..", 0)
c1 = Character([], "c1", 100, sword, None, 10)
c2 = Character([], "c2", 500, woodBat, None, 10)
c1.attack(c2)
c1.pickup(dirt)
c1.throw(c2, dirt)
c1.pickup(dirt)
c1.throw(c2, dirt)
c2.attack(c1)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
while playing:
    print(Person.current_location.name)
    print(Person.current_location.description)
    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    if command.lower() in ('inv', 'inventory', 'i'):
        print(Person.inventory)
    if command.lower() in ("p", 'pickup'):
        a = input("what would you like to pick up?")
        items = [dirt.name]
        if a.lower() in items:
            i = items.index(a)
            o = items.
            print(i)
            Person.pickup(dirt)
    elif command.lower() in directions:
        try:
            # command = north
            room_object = getattr(Person.current_location, command)
            if room_object is None:
                raise AttributeError
            Person.move(room_object)
        except AttributeError:
            print("I can not go that way")