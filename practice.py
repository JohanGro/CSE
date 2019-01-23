word = ["animals"]
answer = "".join(word[0])
list1 = "".join(word[0])
guesses_left = 2
line = ""
space = " "
for character in list1:
    if character is space:
        line = line + " "
    else:
        line = line + "-"
        list1 = list1.replace(list1, line)
print(list1)
while guesses_left > 0:
    ans
    list1 = list(list1)
    guess = input("insert a guess")
    for character in list1:
        if character == guess:
            current_index = answer.index(character)
            list1.pop(current_index)
            list1.insert(current_index, guess)
    print(list1)