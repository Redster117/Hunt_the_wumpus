"""This module defines a class Cave."""
class Cave:
    """Defines the self name."""
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}

    def set_name(self, cave_name):
        """Defines the set name"""
        self.name = cave_name

    def get_name(self):
        """Defines the get name"""
        return self.name

    def set_description(self, cave_description):
        """Defines the set description"""
        self.description = cave_description

    def get_description(self):
        """Defines the get description"""
        return self.description

    def describe(self):
        """Prints the description of the cave."""
        print(self.description)

    def link_caves(self, cave_to_link, direction):
        """Links this cave to another cave in a specified direction."""
        self.linked_caves[direction] = cave_to_link
        print(self.name + " linked caves:" + repr(self.linked_caves))

    def get_details(self):
        """Return the details of the cave."""
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)
