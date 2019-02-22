class Food(object):
    def __init__(self, name="", description="", fact="", calories=0, protein=0):
        self.name = name
        self.description = description
        self.fact = fact
        self.calories = calories
        self.protein = protein

    def check(self):
        print("~<>~" * 20)
        print("Health: %s" % self.name)
        print("Description: %s" % self.description)
        print("Fun Fact: %s" % self.fact)
        print("Calories: %s" % self.calories)
        print("Protein: %s" % self.protein)

    def cook(self):
        print("~<>~" * 10)
        if self is apple:
            print("you baked an apple pie!")
        if self is banana:
            print("pancakes with bananas on top! yum!")
        if self is strawberry:
            print("you made a berry pie!")
        if self is grape:
            print("what can you make with grapes? just eat them!")


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