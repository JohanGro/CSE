class Room(object):
    def __init__(self, name, description="",  north=None, east=None, south=None, west=None):
        self.name = name
        self.description = description
        self.NORTH = north
        self.EAST = east
        self.SOUTH = south
        self.WEST = west


Ominous_Room = Room("Ominous room", "It's a room with light blue walls. a large gate blocks the north exit.")
Forest_Entrance = Room("Forest Entrance", "light glimmers through the treetops.", None, None, Ominous_Room)
Main_Road = Room("Main Road", "This road used to be highly traveled by. yet nobody can be seen.", None, None,
                 Forest_Entrance)
Town_Square = Room("Town Square", "The center of town. it used to be a place of happiness. seems that is no more.",
                   None, None, Main_Road)
Ominous_Room.NORTH = Forest_Entrance
Forest_Entrance.NORTH = Main_Road
Main_Road.NORTH = Town_Square
