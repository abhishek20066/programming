file = open("playlist.txt", "r")

file.readline()
file.readline()

song = file.readline()

print(song.strip())

file.close()