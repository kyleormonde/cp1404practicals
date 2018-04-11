word_list = []
repeated_words = []
word = input("Enter a string: ")
while word != "":
    if word in word_list:
        repeated_words.append(word)
    else:
        word_list.append(word)
    word = input("Enter a string: ")
if repeated_words:
    for i in range(len(repeated_words)):
        print(repeated_words[i], end=", ")
    print()
    # print([repeated_words[i] for i in range(len(repeated_words))])
else:
    print("No repeated strings entered.")
# for i in word:

