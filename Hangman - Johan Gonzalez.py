import random
word_bank = ["Treble Clef", "Music Theory", "Cow", "Dog", "Animal", "Computer", "Mouse", "Crackers",
             "Grappling Hook", "Stringed Instruments", "Drought", "Red", "Drag", "Dripping",
             "Scary", "Ground", "Electricity", "Internet", "Living Room", "Blue", "Cyan", "Tyrannosaurus Rex"
             "Ripping", "Pig", "Chicken", "Frog", "Water", "Wandering", "Training", "Reading Is Good",
             "playing games", "reading books", "potato", "tomato", "turkey", "potted plant", "corn", "town", "mayor",
             "painting", "switch", "cpu", "internet browser", "starry sky", "flag", "train", "cruel", "tree", "earthy",
             "serious", "answer", "kick", "oceanic", "beautiful", "tiger", "history", "plasma", "gateway", "forty",
             "llama", "cactus", "camel", "chocolate", "harmony", "world", "coral reef"]
guessed = []
random_word = random.choice(word_bank)
word = list(random_word)
true = list(word)
answer = "".join(word)
line = ""
space = " "
question_mark = "?"
for character in word:
    if character is question_mark:
        line = line + "?"
    if character is space:
        line = line + " "
    else:
        line = line + "-"
        answer = answer.replace(answer, line)
correct = 7
while correct > 0:
    print(answer)
    answer = list(answer)
    if true == answer:
        answer = "".join(answer)
        print("congratulations! the word was %s" % answer)
        exit()
    guessed = "".join(guessed)
    print("letters you've guessed - %s" % guessed)
    guessed = list(guessed)
    guess = input("insert guess")
    guessed.append(guess)
    if guess in answer:
        print("you already guessed this")
        answer = "".join(answer)
    if guess.swapcase() in word:
        guess = guess.swapcase()
    while guess in word:
        answer = list(answer)
        current_index = word.index(guess)
        word.pop(current_index)
        word.insert(current_index, "-")
        answer.pop(current_index)
        answer.insert(current_index, guess)
        answer = "".join(answer)
        if guess.swapcase() in word:
            guess = guess.swapcase()
    if guess not in word and guess not in answer:
        answer = "".join(answer)
        print("nope")
        correct = correct - 1
true = "".join(true)
print("the word was %s" % true)
print("you could'nt guess it :/")
