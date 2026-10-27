file = open("my_fav_songs.txt", "r")

songs = file.readlines()

print("Total songs:", len(songs))

file.close()