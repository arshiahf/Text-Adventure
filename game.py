class game:

    def __init__(self, rooms, first_room):
        self.rooms = rooms
        self.player_inventory = list()
        self.current_room = first_room

    def __repr__(self):
        return self.rooms[self.current_room]
