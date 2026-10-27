file = open("lyrics.txt", "r")

print("Before reading:", file.tell())

data = file.read(10)
print(data)

print("After reading:", file.tell())

file.close()