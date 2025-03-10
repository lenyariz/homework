songs_list = input("Песни: ").split(", ")
authors_list = input("Исполнители: ").split(", ")
dict_songs = {}
counter = 1

print("Плейлист:")
for song, author in list(zip(songs_list, authors_list)):
    print(f"{counter}. {song} - {author}")
    counter += 1
    if author not in dict_songs:
        dict_songs[author] = [song]
    else:
        dict_songs[author].append(song)

print("Группировка по исполнителям:\n", dict_songs)