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
            "WEST": "Forest"
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
    },
    "Foothills": {
        "NAME": "Foothills",
        "DESCRIPTION": "The small hills are surrounded around a volcano and mountains."
                       " The path towards the volcano has been blocked by tons of rocks.",
        "PATHS": {
            "WEST": "Hilltop_Mansion",
            "EAST": "Shop"
        }
    },
    "Hilltop_Mansion": {
        "NAME": "Hilltop Mansion",
        "DESCRIPTION": "The door seems to be shut. you hear random noises coming from the inside."
                       " there two trees on either side of the mansion.",
        "PATHS": {
            "SOUTH": "Highlands",
            "EAST": "Foothills"
        }
    },
    "Highlands": {
        "NAME": "Highlands",
        "DESCRIPTION": "You can see almost everything from up here.",
        "PATHS": {
            "SOUTH": "Mountains",
            "NORTH": "Hilltop_Mansion"
        }
    },
    "Mountains": {
        "NAME": "Mountains",
        "DESCRIPTION": "There are a lot of wild animals roaming around."
                       " there is something floating to the west. you seem to barely be able to get onto it.",
        "PATHS": {
            "WEST": "Floating_Shop",
            "SOUTH": "Village",
            "NORTH": "Highlands"
        }
    },
    "Floating_Shop": {
        "NAME": "Floating Shop",
        "DESCRIPTION": "Hello! How did you manage to get up here? No Matters! Browse my selection of items:"
                       " Glider: 100 coins, Food: 5 coins",
        "PATHS": {
            "EAST": "Mountains"
        }
    },
    "Village": {
        "NAME": "Village",
        "DESCRIPTION": "The village is painted bright colors. It is full of life, everyone seems happy."
                       " the well at the center of the village is empty.",
        "PATHS": {
            "NORTH": "Mountains",
            "DOWN": "???",
            "EAST": "Forest"
        }
    },
    "???": {
        "NAME": "???",
        "DESCRIPTION": "You are under the well. You hear faint whispering.",
        "PATHS": {
            "NORTH": "Dream_Room",
            "WEST": "Treasure_Room",
            "UP": "Village"
        }
    },
    "Dream_Room": {
        "NAME": "Dream Room",
        "DESCRIPTION": "This room is said to be used to put nightmares into thieves that would not"
                       "confess to their crimes. a man sits in the middle of the room asking to set him free.",
        "PATHS": {
            "SOUTH": "???"
        }
    },
    "Treasure_Room": {
        "NAME": "Treasure Room",
        "DESCRIPTION": "The chest is locked.",
        "PATHS": {
            "EAST": "???"
        }
    },
    "Forest": {
        "NAME": "Forest",
        "DESCRIPTION": "The forest is filled with thick trees. you may be able to chop them down for wood.",
        "PATHS": {
            "WEST": "Village",
            "EAST": "Forest_Entrance"
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
