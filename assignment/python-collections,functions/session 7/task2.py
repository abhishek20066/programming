review = """Zomato is good.
Zomato delivers food fast!"""

review = review.lower()

for mark in ".,!?":
    review = review.replace(mark, "")

words = review.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)