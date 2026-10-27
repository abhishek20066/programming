def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    playlists.setdefault(user, {})
    playlists[user].setdefault(playlist_name, [])

    song = {"title": song_title, "artist": artist}
    playlists[user][playlist_name].append(song)


playlists = {}

add_song_to_playlist(playlists, "Rahul", "Favourites", "Perfect", "Ed Sheeran")
add_song_to_playlist(playlists, "Rahul", "Favourites", "Believer", "Imagine Dragons")
add_song_to_playlist(playlists, "Amit", "Chill", "Kesariya", "Arijit Singh")

print(playlists)