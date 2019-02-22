class Room(object):
    def __init__(self, name, description="",  north=None, east=None, south=None, west=None, up=None):
        self.name = name
        self.description = description
        self.NORTH = north
        self.EAST = east
        self.SOUTH = south
        self.WEST = west
        self.up = up


Ominous_Room = Room("Ominous room", "It's a room with light blue walls. a large gate blocks the north exit.")
Forest_Entrance = Room("Forest Entrance", "light glimmers through the treetops.", None, None, Ominous_Room)
Main_Road = Room("Main Road", "This road used to be highly traveled by. yet nobody can be seen.", None, None,
                 Forest_Entrance)
Town_Square = Room("Town Square", "The center of town. it used to be a place of happiness. seems that is no more.",
                   None, None, Main_Road)
Shop = Room("Shop", "It's a place to buy a lots of helpful things!", None, None, Town_Square)
Desert = Room("Desert", "The hot air would be too hot to travel any further.", None, None, None, Shop)
Foothills = Room("Foothills", "The small hills surround the volcano and the mountains.", None, Shop)
Hilltop_Mansion = Room("Hilltop Mansion", "The doors are shut.", None, Foothills)
Highlands = Room("Highlands", "You can see everything from up here", Hilltop_Mansion)
Mountains = Room("Mountains", "this is where wild animals thrive. a shadow falls over you.", Highlands)
Village = Room("Village", "The village is painted many bright colors. It seems they have been in a drought, the well is"
                          " empty.", Mountains)
Floating_Shop = Room("Floating Shop", "The shop floats high over the world.", None, Mountains)
Ominous_Room.NORTH = Forest_Entrance
Forest_Entrance.NORTH = Main_Road
Main_Road.NORTH = Town_Square
Shop.EAST = Desert
Shop.WEST = Foothills
Foothills.WEST = Hilltop_Mansion
Highlands.SOUTH = Mountains
Mountains


