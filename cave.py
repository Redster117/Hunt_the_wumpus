"""Cave class for HUnt the Wumpus."""
class Cave:
    """Defines attributes and methods for cave objects."""
    def __init__(self, cave_name):
        """Sets class attributes."""
        self.name = cave_name
        self.description = None
        self.linked_caves = {}

    def set_name(self, cave_name):
        """Sets the cave name"""
        self.name = cave_name

    def get_name(self):
        """Gets the cave name"""
        return self.name

    def set_description(self, cave_description):
        """Sets the cave description."""
        self.description = cave_description

    def get_description(self):
        """Gets the cave description."""
        return self.description

    def describe(self):
        """Sets the cave description."""
        print(self.description)

    def link_caves(self, cave_to_link, direction):
        """Links this cave to another cave in a specified direction."""
        self.linked_caves[direction] = cave_to_link
        #print(self.name + " linked caves:" + repr(self.linked_caves))

    def get_details(self):
        """Sets the cave details including name, description, and linked caves."""
        print("\n" + self.name)
        print("--------")
        print(self.description)
        for direction, cave in self.linked_caves.items():
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        """Moves to a linked cave in the specified direction."""
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You shall not pass here.")
            return self
