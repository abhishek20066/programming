file = open("my_fav_songs.txt", "r")

songs = file.readlines()

for i in range(len(songs)):
    print(i + 1, songs[i].strip())

file.close()