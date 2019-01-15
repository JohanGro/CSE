import random
word_bank = ["dog"]
random_word = random.choice(word_bank)
word = list(random_word)
answer = "".join(word)
stars = ""
for character in word:
    stars = stars + "-"
    answer = answer.replace(answer, stars)
print(answer)
correct = 5
while correct > 0:
    guess = input("insert guess")
    answer = list(answer)
    if answer is word:
        print("congratulations!")
        exit(0)
    if guess in answer:
        print("you already guessed this")
    if guess in word:
        current_index = word.index(guess)
        answer.pop(current_index)
        answer.insert(current_index, guess)
        answer = "".join(answer)
        print(answer)
    else:
        answer = "".join(answer)
        print("nope")
        correct = correct - 1
        print(answer)
