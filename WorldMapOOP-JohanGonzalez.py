import random


objective = []
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
        self.battle = True


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
        if self in Person.inventory:
            if Person.current_location == Below_The_Well:
                villagetreasure = Room("The Village Treasury", "a place holding the treasures of the village.")
                Below_The_Well.north = sealing_room
                Below_The_Well.west = villagetreasure
                sealing_room.south = Below_The_Well
                villagetreasure.east = Below_The_Well
                print("The doors to the north and west have opened up.")
                Below_The_Well.description = "Under the well of the village. the passages continue to the north and" \
                                             " west"
                sealing_room.items = [ghostsword]
                Person.inventory.remove(KeyforWell)
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
    def cutdown():
        if Person.current_location == Forest:
            if wood not in Forest.items:
                print("you cut down some trees in the nearby area.")
                Forest.items.append(wood)
            else:
                print("wood is already in the area")


class Flippers(Armor):
    def __init__(self, name, description, protect, price):
        super(Flippers, self).__init__(name, description, protect, price)

    @staticmethod
    def equip():
        Ocean_Bay.description = "you feel like you can swim forever"
        Ocean = Room("Ocean", "The wide ocean. you see a small island up ahead.", Ocean_Bay)
        Deep_Ocean = Room("Deep Ocean", "Fish swim by you. if you had something to breath maybe you could"
                                        "explore the bottom")
        Ocean_Bay.south = Ocean
        
        print("you can swim in water")

    def unequip(self):
        print("you can no longer swim in the water.")


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

    @staticmethod
    def pickup(opposite):
        print("you throw dirt at %s" % opposite.name)
        opposite.accuracy -= 1
        print("%s's accuracy was ")


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
    def __init__(self, name, health, weapon, armor, accuracy, money, inithealth):
        self.inventory = []
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.accuracy = accuracy
        self.money = money
        self.inithealth = inithealth

    def take_damage(self, attack):
        self.health -= attack
        if self.health < 0:
            self.health = 0
        print("%s has %d health left." % (self.name, self.health))

    def pickup(self, d):
        self.inventory.append(d)
        print("%s picked up some %s" % (self.name, d.name))

    def throw(self, target, v):
        if v.name in self.inventory:
            self.inventory.remove(v.name)
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
    def __init__(self, text, name, inventory, health, weapon, armor, accuracy, money, inithealth):
        super(Npc, self).__init__(name, health, weapon, armor, accuracy, money, inithealth)
        self.text = text
        self.inventory = inventory


class Knight(Npc):
    def __init__(self, text, name, inventory, health, weapon, armor, accuracy, money, inithealth):
        super(Knight, self).__init__(text, name, inventory, health, weapon, armor, accuracy, money, inithealth)

    @staticmethod
    def quest():
        print("ah welcome to the village, uh if you have the time, will you please listen to our problem?")
        input("next >>")
        print("well you see, recently there has been lots of trouble, coming from one specific place.")
        input("next >>")
        print("the well in this place. its been causing trouble recently.")
        input("next >>")
        print("there is something in there... and all i can ask is you come to help.")
        print("please accept to help us.")
        input("you accepted the quest")
        print("~~New Objective~~")
        print("type objectives to check out your current ones.")
        objective.append("Main Quest: The Bottom of the Well.")
        print(objective[objective.index("Main Quest: The Bottom of the Well.")])
        input("next >>")
        print("your going to need this if you are going down there.")
        print("next >>")
        print("good luck, my friend.")
        Person.inventory.append(KeyforWell)
        print("you obtained the %s" % KeyforWell.name)


class Lumberjack(Npc):
    def __init__(self, text, name, inventory, health, weapon, armor, accuracy, money, inithealth):
        super(Lumberjack, self).__init__(text, name, inventory, health, weapon, armor, accuracy, money, inithealth)
        self.woodleft = 5

    @staticmethod
    def quest():
        print("oh talking about that axe, how about you go help me get some wood")
        input("Next >>")
        print("how about if you get some wood, come back to me")
        input("Next >>")
        print("once i have 5 wood from you ill give you something!")
        input("Next >>")
        print("~~New Objective~~")
        objective.append("Side Quest: Wood Collector")
        print(objective[objective.index("Side Quest: Wood Collector")])

    def woodcollector(self):
        if wood in Person.inventory:
            print("this wood is for me?")
            print("why thank you! you wont regret this!")
            self.woodleft -= 1
            print("i only need %s more wood!" % self.woodleft)
            Person.inventory.remove(wood)
        if self.woodleft is 0:
            print("wow, you really got me all the wood i needed!")
            input("Next >>")
            print("well thank you so much")
            input("Next >>")
            print("here take this cake my wife made, its not much but i hope it helps you!")
            print("~~Objective Complete~~")
            Person.inventory.append(Cake)
            objective.remove("Side Quest: Wood Collector")


class Ghost(Character):
    def __init__(self, name, health, weapon, armor, accuracy, money, inithealth):
        super(Ghost, self).__init__(name, health, weapon, armor, accuracy, money, inithealth)

    @staticmethod
    def specialattack():
        print("unscramble the word to dodge the attack")
        words = ('owod', 'uragd', 'dgeod', 'gthif', 'tatack', 'pjum', 'tea', 'ovme', 'kalw', 'aptr', 'thosg')
        trueword = ('wood', 'guard', 'dodge', 'fight', 'attack', 'jump', 'eat', 'move', 'walk', 'trap', 'ghost')
        wordchoice = random.choice(words)
        print(wordchoice)
        solve = input("your guess?")
        if solve.lower() in trueword:
            toom = trueword.index(solve.lower())
            correct = words[toom]
            if correct == wordchoice:
                print("you got it correct!")
                print("you were able to dodge the attack")
        else:
            print("you were attacked.")
            print("you lost 30 health")
            Person.health -= 30

    def attack(self, target):
        spe = random.randint(0, 10)
        rand1 = random.randint(0, 10)
        rand2 = random.randint(0, 10)
        if self.accuracy is 10:
            if spe in (0, 1, 2, 3, 4, 5):
                self.specialattack()
            elif rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                target.take_damage(self.weapon.attack)
        if self.accuracy in (8, 9):
            if rand2 in (0, 1, 2, 3, 4, 5, 6, 7, 8):
                if spe in (0, 3, 7, 9, 10):
                    self.specialattack()
                elif rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if rand2 in (9, 10):
                print("they missed the attack.")
        if self.accuracy in (4, 5, 6, 7):
            if rand2 in (0, 1, 2, 3, 4, 5):
                if spe in (0, 1, 6, 9):
                    self.specialattack()
                elif rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            if rand2 in (6, 7, 8, 9, 10):
                print("they missed the attack.")
        if self.accuracy in (0, 1, 2, 3):
            if rand2 in (1, 2):
                if rand1 in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                    print("%s attacks for %d damage" % (self.name, self.weapon.attack))
                    target.take_damage(self.weapon.attack)
            else:
                print("They missed the attack")
        if self.health <= 0:
            print("~~Objective Complete!~~")
            print(objective[0])
            Gatekeeper.text = "Thank you so much, i see you have taken care of that monster. " \
                              "i hope you found something useful to help you," \
                              " i wish i could give you something for the help."


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
        self.clothing = None

    def take_damage(self, attack):
        self.health -= attack
        if self.health < 0:
            self.health = 0
        print("you have %d health left." % self.health)

    def clothingequip(self):
        try:
            o = 0
            for i in Person.inventory:
                print(Person.inventory[o].name)
                o += 1
            cloquip = input("what would you like to equip")
            q = 0
            for i in Person.inventory:
                if cloquip.lower() == Person.inventory[q].name:
                    if Person.clothing is None:
                        Person.clothing = Person.inventory[q]
                        Person.inventory.remove(Person.inventory[q])
                        Person.clothing.equip()
                    else:
                        Person.inventory.append(Person.clothing)
                        Person.clothing.unequip()
                        Person.clothing = Person.inventory[q]
                        print("the item in your clothing slot moved to your inventory")
                        Person.inventory.remove(Person.inventory[q])
                        Person.clothing.equip()
                q += 1
        except AttributeError:
            print("that item is not clothing.")
            Person.inventory.append(Person.clothing)
            Person.clothing = None


    @staticmethod
    def equip():
        equipness = input("equip what")
        f = 0
        for u in Person.inventory:
            if equipness.lower() == Person.inventory[f].name:
                try:
                    print("you equipped the %s" % Person.inventory[f].name)
                    print("%s: %s" % (Person.inventory[f].name, Person.inventory[f].description))
                    print("the item that was in your weapon slot had been transferred to your inventory")
                    Person.inventory.append(Person.weapon)
                    Person.weapon = Person.inventory[f]
                    Person.inventory.remove(Person.inventory[f])
                except AttributeError:
                    print("that item is not a weapon.")
            f += 1

    @staticmethod
    def drop(thing):
        print("you dropped the %s" % thing.name)
        Person.inventory.remove(thing)
        p = 0
        for t in Rooms:
            if Person.current_location == Rooms[p]:
                roomlocate = Rooms[p]
                roomlocate.items.append(thing)
            p += 1

    def attack(self, target):
        rand1 = random.randint(0, 10)
        rand2 = random.randint(0, 10)
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
                    print("you attack %s for %d damage, critical hit" % (target.name, self.weapon.attack * 2))
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
                for s in Person.inventory:
                    print(Person.inventory[w].name)
                    w += 1
                g = input("eat what")
                h = 0
                for r in Person.inventory:
                    if g.lower() == Person.inventory[h].name:
                        Person.eat(Person.inventory[h])
                    h += 1
                target.attack(Person)

            if action.lower() in ['run', 'r']:
                print("you ran away from further combat.")
                battle = False

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
                target.health = target.inithealth
                battle = False

    @staticmethod
    def talk(target):
        print("%s: %s" % (target.name, target.text))

    def pickup(self):
        resp = input("pickup what?")
        j = 0
        for q in self.current_location.items:
            if resp.lower() == self.current_location.items[j].name:
                if self.current_location in Rooms:
                    self.inventory.append(self.current_location.items[j])
                    print("you picked up a %s" % self.current_location.items[j].name)
                    self.current_location.items.remove(self.current_location.items[j])
            j += 1

    def eat(self, thing):
        try:
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
        except AttributeError:
            print("you can not eat that item")

    def move(self, new_location):
        """This method moves a character to a new location
        :param new_location: The variable containing a room object
        """
        self.current_location = new_location
        chance = random.randint(0, 5)
        n = 0
        if self.current_location.battle is True:
            if n in [0, 1]:
                if chance in [0, 1]:
                    Person.battle(weak_monster)
                    weak_monster.health = 20
                    n = 0
            if n in [2, 3]:
                if chance in [0, 1, 2]:
                    Person.battle(weak_monster)
                    weak_monster.health = 20
                    n = 0
            if n in [5]:
                Person.battle(weak_monster)
                weak_monster.health = 20
                n = 0
            n += 1
        if self.current_location.battle is False:
            print("This is a safe place")


class Darksword(Weapons):
    def __init__(self, name, description, power, price):
        super(Darksword, self).__init__(name, description, power, price)

    @staticmethod
    def pickup():
        print("the ground shakes.")
        print("")
        print("a figure appears in front of you")
        print("the figure awaits you to do something")
        print("will you attack it?")
        ghostfight = input("yes or no?")
        if ghostfight.lower() in ('yes', 'y'):
            currentweapon = Person.weapon
            Person.weapon = ghostsword
            Person.battle(ghost)
            Person.weapon = currentweapon
            if ghost.health is 0:
                print("you won the battle and got the flippers, now you can swim in shallow water")
                print("the ghost swirled around, holding on to its final hope, it ran away.")
                sealing_room.description = "a place to make troublesome people disappear. it feels less scary than" \
                                           "how it was when you first entered."
            else:
                print("you ran away")
        else:
            print("you retreated before anything happened")
            Person.current_location = Below_The_Well


sword = Weapons("Sword", "a normal sword to use, used highly by knights in the royal guard.", 20, None)
ghostsword = Darksword("ghost sword", "the figures sword from when they lived.", 20, 0)
carrots = Consumables("carrot", "a hearty vegetable used in cooking.", 10, 5)
Knightarmor = Armor("Knights armor", "Made of Iron, sturdy", 30, 50)
Broadsword = Weapons("Broadsword", "A double handed sword.", 40, 50)
woodBat = Weapons("Wood Bat", "A bat commonly used by big enemies.", 5, 5)
KeyforWell = WellKey("Well Key", "A rusted key passed down from generations before. it grants access to the Well.",
                     None)
Tiller = Weapons("Tiller", "A tool used by farmers to till the soil.", 3, 5)
seeds = Consumables("seeds", "Would be better to plant them...", 5, 5)
watermelon = Consumables("watermelon", "A big fruit that came from small seeds", 30, 20)
acorn = Consumables("acorn", "a squirrel would enjoy this.", 5, 3)
apple = Consumables("apple", "a small red fruit", 10, 10)
axe = Axe("axe", "a huge axe, can be used to chop down trees in certain areas.", 10, None)
wood = Item("wood", "some wood that can be used to light a fire.", 5)
woodsword = Weapons("wood sword", "a fairly common weapon", 5, None)
Cake = Consumables("cake", "a huge cake", 50, 40)
glider = Glider()
bandanna = Bandana("bandanna", "this will help you traverse the desert", 0, 50)
weak_monster = Character("monster", 20, woodBat, None, 10, 5, 20)
cactus_fruit = Consumables("cactus fruit", "a fruit grown in the desert oasis", 20, 30)
potion = Consumables("potion", "This potion will heal fully!", 100, 50)
pie = Consumables("pie", "a slice of apple pie", 40, 30)
starfruit = Consumables("starfruit", "Fruit shaped like a star!", 60, 40)
peanuts = Consumables("peanuts", "some peanuts", 10, 5)
wheat = Consumables("wheat", "wheat from the highlands", 15, 10)
flippers = Flippers("flippers", "some rubber flippers to help you swim.", 5, None)

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
sealing_room = Room("The Sealing Room", "A place heavily used to make the troublesome people disappear"
                                        ", a sword lies in the center of the room.", None, None, Below_The_Well)
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
CentralStore = Store([carrots, watermelon, Cake, potion, starfruit], Shop)
Ominous_Room.battle = False
Village.battle = False
Floating_Shop.battle = False
Shop.battle = False
town.battle = False
oasis.east = town
Highlands.items = [wheat]
Rain_Forest.items = [starfruit, watermelon]
oasis.items = [cactus_fruit]

Rooms = [Ominous_Room, Forest_Entrance, Forest, Main_Road, Town_Square, Shop, Foothills, Highlands, Mountains, Village,
         Floating_Shop, Rain_Forest, Beach, Beach_Village, Below_The_Well, oasis, town, desert_temple, sealing_room]

Village.items = [carrots]
Forest_Entrance.items = [acorn]
Ominous_Room.items = [apple]
Forest.items = [axe, wood]
Person = Player(Ominous_Room)
Gatekeeper = Knight("Ah, welcome to the village, im the gatekeeper, please do not cause any harm to the people living"
                    " here, i hope you enjoy your stay.", "gatekeeper", [KeyforWell], 100, Broadsword, Knightarmor, 10,
                    50, 100)
Villagefarmer = Npc("oh, hello! have you said hello to the Gatekeeper yet?", 'farmer',
                    [seeds, watermelon], 100, Tiller, None, 10, 10, 100)
VillageLumberjack = Lumberjack("why hello there! thanks for talking to me but i better get back to work, if you would"
                               " like to help, grab the axe on the floor over there, and chop down some trees. the wood"
                               " could be very helpful!", "lumberjack", [apple], 100, axe, None, 10, 20, 100)
Forest.characters = [VillageLumberjack]
Village.characters = [Gatekeeper, Villagefarmer]
ghost = Ghost("Ghost", 200, ghostsword, None, 10, 0, 200)
Person.money = 0
playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
firstGate = True
firstwood = True
Person.inventory.append(bandanna)
Person.inventory.append(flippers)
Person.clothingequip()
while playing:
    print(Person.current_location.name)
    print(Person.current_location.description)
    command = input(">_")
    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]
    if command.lower() in ('help', 'tutorial'):
        print("The commands are:")
        print("check, equip, unequip, drop, pickup, shop, sell, quit, inventory,")
        print("use, talk, eat, battle, cut")

    if command.lower() in ('objectives', 'obj', 'objective'):
        print(objective)

    if command.lower() in ("heal", "nurse"):
        if Person.current_location == Village:
            print("your wounds were healed!")
            Person.health = 100
        else:
            print("your not in the right location for this")

    if Person.current_location is sealing_room:
        if command.lower() in ('pickup', 'p'):
            ghostsword.pickup()

    if command.lower() in ('check', 'self'):
        print("Current Health:")
        print(Person.health)
    if command.lower() in ('equip', 'e'):
        what = input("weapon or clothing")
        if what.lower() == 'clothing':
            Person.clothingequip()
        if what.lower() == 'weapon':
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
    if command.lower() in ('clothing', 'ci'):
        try:
            print(Person.clothing.name)
        except AttributeError:
            print("you have nothing in your clothing slot")
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
    if command.lower() in ('use', 'try'):
        KeyforWell.use()
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
                if a.lower() == Gatekeeper.name:
                    if firstGate is True:
                        Gatekeeper.quest()
                        firstGate = False
                if a.lower() == VillageLumberjack.name:
                    if firstwood is True:
                        VillageLumberjack.quest()
                        firstwood = False
                    if wood in Person.inventory:
                        VillageLumberjack.woodcollector()

            e += 1

    if command.lower() in ('eat', 'eating'):
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
        m = 0
        for i in Person.current_location.items:
            print(Person.current_location.items[m].name)
            m += 1
        Person.pickup()

    elif command.lower() in directions:
        try:
            randbattle = 0
            # command = north
            room_object = getattr(Person.current_location, command)
            if room_object is None:
                raise AttributeError
            Person.move(room_object)
        except AttributeError:
            print("I can not go that way")
