text = "this is a collection of words of nice words this is a fun thing it is"
# text = input("Enter a string of words: ")
WORDS = {}
for word in text.split():
    if word in WORDS:
        WORDS[word] += 1
    else:
        WORDS[word] = 1

ordered_words = []
for word in WORDS:
    ordered_words.append(word)

ordered_words.sort()


max_length = max((len(word) for word in ordered_words))


for word in ordered_words:
    print("{:{}} : {}".format(word, max_length, WORDS[word]))

