from room import Room
from player import Player
from item import Item

# Declare all the rooms

items = {
    'burger': Item('Burger', "It's a burger."),

    'sandwich': Item('Sandwich', 'Probably has some cheese on it.'),

    'tuna': Item('Tuna', "It's a fish."),

    'apple': Item('Apple', "Fruit one of two."),

    'banana': Item('Banana', "Fruit two of two."),
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['burger']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['banana']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['tuna']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['sandwich']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['apple']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Indaina", room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

movement = ''



# while not movement == "quit":
#     print(f"You are at location {player.room.name}: {player.room.description}")
#     movement = str(input("Choose a direction "))
#     if movement == 'north':
#         player.room = player.room.n_to
#     elif movement == 'east':
#         player.room = player.room.e_to
#     elif movement == 'south':
#         player.room = player.room.s_to
#     elif movement == 'west':
#         player.room = player.room.w_to
#     elif movement == 'quit':
#         exit()
#     else:
#         print("Please enter a direction")


directions = {'n': 'n_to', 'e': 'e_to', 's': 's_to', 'w': 'w_to',}

while True:
    print(player.room.name)
    print(player.room.description)

    if len(player.room.items) > 0:
        print(player.room.listo())

    choice = input(f"What will you do, {player.name}?\n put a direction: n, e, s, w, or you can take/drop items.  ").lower()

    print(choice.split()[1])

    if 'take' in choice:
        player.take(items[choice.split(' ')[1]])

    if 'drop' in choice:
        player.drop(items[choice.split(' ')[1]])

    if choice in directions:
        direction = directions[choice]

        if hasattr(player.room, f'{direction}'):

            player.room = getattr(player.room, f'{direction}')
        else:
            print("Sorry, you can't go that way.")

    