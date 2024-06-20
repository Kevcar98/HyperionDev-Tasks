class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name=album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"The album called {self.album_name} made by {self.album_artist} has {self.number_of_songs} songs."
    

albums1=[["Cocktails Reflections", "Paval Teja Tittensor", 19],
         ["Bouncy Forest", "Iason Marcelino Gibson", 17],
         ["Calm rest", "Taisa Orla Quigley", 11],
         ["Riotous new world", "Conley Lovrenc Gosselin", 8],
         ["Social light", "Zhanna Fausta Butcher", 14]
         ]

albums2=[["Wonderful Troubles", "Julie Mara Causer", 12],
         ["Urban Nightmare", "Sappheire Albertus Mihailović", 15],
         ["Need Swamp", "Shiv Nadezhda Price", 13],
         ["Restful darkness", "Viktor Valeriu Schenk", 8],
         ["Gleeful dreams", "Romana Cemal Aliev", 16]
         ]

new_albums = [["Dark Side of the Moon", "Pink Floyd", 9],
            ["Oops!... I Did It Again", "Britney Spears", 16]
            ]

def sort_album(list, pos):
    # Sorts the list by the value in the "pos" position of each row in the list from low to high
    if pos == 0:
        return sorted(list, key=lambda x: str(x[pos]))
    else:
        return sorted(list, key=lambda x: int(x[pos]))


def swap_elements(list, num1, num2):
    # Swaps the elements of postion num1 and num2 in the list
    list[num1], list[num2] = list[num2], list[num1]
    return list

def print_list(list):
    # Prints all the elements in the list
    for element in list:
        print(element)
    print()

def insert_list(list, list_to_add):
    # Adds elements of the list "list_to_add" to the list "list"
    return list.extend(list_to_add)

print("Album 1:")
print_list(albums1)
print()


print("Album 1 sorted in Alphabetical Order:")
albums1 = sort_album(albums1, 2)
print_list(albums1)
print()

print("Album 1 swapped element postions at 1 & 2:")
albums1 = swap_elements(albums1, 1, 2)
print_list(albums1)
print()

print("Album 2:")
print_list(albums2)
print()


insert_list(albums2, albums1)
insert_list(albums2, new_albums)
albums2 = sort_album(albums2, 0)
print_list(albums2)
print()

for index, sublist in enumerate(albums2):
    if sublist[0] == "Dark Side of the Moon":
        print("Index of 'Dark Side of the Moon':", index)
        break


