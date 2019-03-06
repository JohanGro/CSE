import random


class Food(object):
    def __init__(self, name="", description="", fact="", calories=0, protein=0):
        self.name = name
        self.description = description
        self.fact = fact
        self.calories = calories
        self.protein = protein

    def check(self):
        print("~<>~" * 20)
        print("Name: %s" % self.name)
        print("Description: %s" % self.description)
        print("Fun Fact: %s" % self.fact)
        print("Calories: %s" % self.calories)
        print("Protein: %s" % self.protein)

    def cook(self):
        rand = random.randint(0, 10)
        print("~<>~" * 10)
        if self is apple:
            if rand is 0 or rand is 1:
                print("you baked an apple pie!")
            if rand is 2 or rand is 3:
                print("You Burnt A Apple... how do you even do that")
            if rand is 4 or rand is 5:
                print("Caramel Apple!")
            if rand is 6 or rand is 7:
                print("WOW! you blew up the oven. how are you going to pay for that?")
            if rand is 8 or rand is 9:
                print("You didn't bake anything at all. You just ate the apple.")
            if rand is 10:
                print("You chopped up some apples. what a cook.")
        if self is banana:
            if rand is 0 or rand is 1:
                print("banana pie...")
            if rand is 2 or rand is 3:
                print("You Fried a banana, great!")
            if rand is 4 or rand is 5:
                print("You made a banana... you made no difference")
            if rand is 6 or rand is 7:
                print("Ring Ring Ring! Banana Phone!")
            if rand is 8 or rand is 9:
                print("You made pancakes, with bananas! At least you cooked.")
            if rand is 10:
                print("You ran away from the kitchen.")
        if self is strawberry:
            if rand is 0 or rand is 1:
                print("you baked an Berry pie!")
            if rand is 2 or rand is 3:
                print("You threw the strawberry away. how dare you!")
            if rand is 4 or rand is 5:
                print("Chocolate covered!")
            if rand is 6 or rand is 7:
                print("WOW! you blew up the oven. With a berry?")
            if rand is 8 or rand is 9:
                print("You ate the strawberry whole.")
            if rand is 10:
                print("The strawberry scared you away...")
        if self is grape:
            if rand is 0 or rand is 1:
                print("you baked an Grape pie???")
            if rand is 2 or rand is 3:
                print("The grape blew up... how do you manage that.")
            if rand is 4 or rand is 5:
                print("You made the grapes into raisins! Why would you do that!")
            if rand is 6 or rand is 7:
                print("Stop Crying! The grape is not scary!")
            if rand is 8 or rand is 9:
                print("You didn't bake anything at all. You just ate the grape.")
            if rand is 10:
                print("Great work on your first day of cooking! You are not a good cook. so please, save the work and "
                      "do not cook ever again, please, your making everybody get food poisoning.")


apple = Food("Apple", "a red fruit that tastes delicious!", "Apples are 25% air, that is why they float!", 95, .5)
banana = Food("Banana", "A yellow fruit", "banana's are actually berries.", 105, 1.3)
strawberry = Food("Strawberry", "a small red berry", "there are 200 seeds on a single strawberry!", 4, .1)
grape = Food("Grape", "a tiny little purple fruit.", "The fruit was introduced over 300 years ago by spanish explorers.", 62, .6)
apple.check()
banana.check()
strawberry.check()
grape.check()
apple.cook()
banana.cook()
strawberry.cook()
grape.cook()