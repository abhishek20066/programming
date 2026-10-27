def extract_artist(song_title):
    dash = song_title.index("-")
    artist = song_title[dash + 2:]
    return artist


print(extract_artist("Song Name - Artist Name"))