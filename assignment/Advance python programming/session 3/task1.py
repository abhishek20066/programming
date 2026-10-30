song_durations = {
    "Kesariya": 4.28,
    "Perfect": 4.23,
    "Believer": 3.24
}

def get_song_duration(song):
    try:
        return song_durations[song]
    except KeyError:
        print("Song not found on Spotify!")

print(get_song_duration("Kesariya"))
get_song_duration("Shape of You")