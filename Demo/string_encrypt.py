word = input()
for letter in word:
    if word.count(letter) == 1:
        print(letter, end="")
    else:
        print(f"{letter}{word.count(letter)}", end="")
