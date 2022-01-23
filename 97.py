intro = input("Enter String: ")
char = 0
word = 1
for i in intro:
    char += 1
    if(i == ' '):
        word += 1
print("number of characters: ", char)
print("number of words: ", word)