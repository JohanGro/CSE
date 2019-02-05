world_map = {
    "Ominous_Room": {
        "NAME": "Ominous Room",
        "DESCRIPTION": "Its a room with glowing blue walls. There is a crate that is filled with goods."
                       " A large gate blocks the north exit.",
        "PATHS": {
            "NORTH": "Forest_Entrance"
        }
    },
    "Forest_Entrance": {
        "NAME": "Forest Entrance",
        "DESCRIPTION": "an entrance to a forest that has light shining through the trees."
                       " to the North is the Main Road.",
        "PATHS": {
            "SOUTH": "Ominous_Room",
            "NORTH": "Main_Road",
        }
    },
    "Main_Road": {
        "NAME": "Main Road",
        "DESCRIPTION": "You are on the road that to the west leads to a small town.",
        "PATHS": {
            "SOUTH": "Forest_Entrance",
            "NORTH": "Center"
        }
    },
    "Center": {
        "NAME": "Center",
        "DESCRIPTION": "The center of the whole map. many people would not be able to visit"
                       " this place. there is a giant statue that doesnt seem to be able to be nudged."
                       "there is a merchants shop to the north",
        "PATHS": {
            "SOUTH": "Main_Road",
            "NORTH": "Shop"
        }
    },
    "Shop": {
        "NAME": "Shop",
        "DESCRIPTION": "Welcome to my shop! not many people these days are passing by here,"
                       " so i'll sell to you for cheap! Here's what i have:"
                       " Wooden Sword: 10 coins, Bomb Sack: 40 coins, Food: 5 coins",
        "PATHS": {
            "SOUTH": "Center",
            "WEST": "Foothills",
            "EAST": "Desert"
        }
    },
    "Desert": {
        "NAME": "Desert",
        "DESCRIPTION": "The air is too hot to travel any further",
        "PATHS": {
            "WEST": "Shop"
        }
    }
}

# Other Variables
current_node = world_map["Ominous_Room"]
print(current_node['NAME'])
print("-" * 20)
print(current_node["DESCRIPTION"])
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# controller
while playing:
    command = input(">_")
    if command.lower() in ('q', 'quit', 'exit'):
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
            print(current_node['NAME'])
            print('-' * 20)
            print(current_node['DESCRIPTION'])
        except KeyError:
            print("I cant go that way")
