import json
import room

rooms_file = open("rooms.json", "r")
rooms_json = json.load(rooms_file)

rooms = dict()

for current_room in rooms_json:
  container = rooms_json[current_room]
  descriptions = container["Description"]
  commands = container["Commands"]
  rooms[current_room] = room.room(current_room, descriptions, commands)

current = "Home"

print(rooms[current])
while True:
  current, command = rooms[current].command_rules(current)
  if command != None:
    print(command)
  else:
    print(rooms[current])
