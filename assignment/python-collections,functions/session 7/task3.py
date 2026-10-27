def word_freq_dict(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        word = word.strip(",.")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

print(word_freq_dict(text))