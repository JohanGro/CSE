import random
word_bank = ["animal"]
random_word = random.choice(word_bank)
word = list(random_word)
answer = "".join(word)
line = ""
for character in word:
    line = line + "-"
    answer = answer.replace(answer, line)
print(answer)
correct = 5
win = False
while correct > 0 and win is False:
    answer = list(answer)
    if word == answer:
        win = True
        answer = "".join(answer)
        print("congratulations! the word was %s" % answer)
        exit()
    guess = input("insert guess")
    if guess in answer:
        print("you already guessed this")
    if guess in word and guess not in answer:
        current_index = word.index(guess)
        answer.pop(current_index)
        answer.insert(current_index, guess)
        answer = "".join(answer)
        print(answer)
    if guess not in word:
        answer = "".join(answer)
        print("nope")
        correct = correct - 1
        print(answer)