import random
word_bank = ["treble clef", "music theory", "cow", "dog", "animal", "computer", "mouse", "crackers",
             "grappling hook", "stringed instruments", "drought", "red", "drag", "dripping",
             "scary", "ground", "electricity", "internet", "living room", "blue", "cyan", "tyrannosaurus rex"
             "ripping", "pig", "chicken", "frog", "water", "wandering", "training", "reading is good",
             "how are you doing?", "hows the weather?", "playing games", "reading books", "squashing the bugs",
             "cleaning the code", "potato", "tomato", "turkey", "potted plant", "corn", "town", "mayor",
             "painting", "switch", "cpu", "internet browser", "starry sky", "flag", "train", "cruel", "tree",
             "earthy", "serious", "answer", "kick", "oceanic", "beautiful", "tiger", "history", "plasma",
             "gateway", "forty", "llama", "cactus", "camel", "chocolate", "harmony", "world", "coral reef"]
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
win = False
while correct > 0 and win is False:
    print(answer)
    answer = list(answer)
    if true == answer:
        win = True
        answer = "".join(answer)
        print("congratulations! the word was %s" % answer)
        exit()
    guessed = "".join(guessed)
    print("letters you've guessed - %s" % guessed)
    guessed = list(guessed)
    guess = input("insert guess")
    guessed.append(guess)
    guess = guess.lower()
    if guess in answer:
        print("you already guessed this")
        answer = "".join(answer)
    while guess in word:
        answer = list(answer)
        current_index = word.index(guess)
        word.pop(current_index)
        word.insert(current_index, "-")
        answer.pop(current_index)
        answer.insert(current_index, guess)
        answer = "".join(answer)
    if guess not in word and guess not in answer:
        answer = "".join(answer)
        print("nope")
        correct = correct - 1
true = "".join(true)
print("the word was %s" % true)
print("you could'nt guess it :/")
