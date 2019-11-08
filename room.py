import os

class room:

    def __init__(self, name, description, commands):
        self.name = name
        self.description = description
        self.commands = commands

    def __repr__(self):
        print(self.name)
        return self.description["Default"]

    def choose_description(self, command, description):
        if command in description and type(description[command] == dict):
            return self.choose_description(None, description[command])
        else:
            return description

    def command_rules(self, current_room):
        player_input = input("> ")

        for command in self.commands:
          if player_input.lower().capitalize() in self.commands and player_input.lower() == command.lower() and (player_input.lower() == "north" or player_input.lower() == "south" or player_input.lower() == "east" or player_input.lower() == "west" or player_input.lower() == "up" or player_input.lower() == "down"):
            os.system("clear")
            return self.commands[command], None
          elif player_input.lower() == command.lower() and player_input.lower() != "Default":
            os.system("clear")
            self.description = self.choose_description(command, self.description)
            print(self)
            if type(self.commands[command]) == dict:
              self.commands = self.commands[command]
              return current_room, self.commands["Default"]
            return current_room, self.commands[command]

        os.system("clear")
        print(self)
        return current_room, "You can't do that."
