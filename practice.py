word = ["animals"]
list1 = "".join(word[0])
list1 = list(list1)
guesses_left = 2
while guesses_left > 0:
    guess = input("insert a guess")
    for character in list1:
        if character == guess:
            # replace with a *
            current_index = list1.index(character)
            list1.pop(current_index)
            list1.insert(current_index, "*")
    print(list1)