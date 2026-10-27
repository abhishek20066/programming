text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

words = text.lower().split()
word_count = {}

for word in words:
    word = word.strip(",.")
    if word not in stopwords:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

print(word_count)
