def char_count_dict(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

text = input("Enter a string: ")

result = char_count_dict(text)

for char in sorted(result):
    print(char, ":", result[char])