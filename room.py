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
