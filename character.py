"""Character class for Hunt the Wunpus"""
class Character:
    """Defines attributes and methods for cave objects."""
    def __init__(self, char_name, char_description):
        """Sets character attributes."""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Sets the character description."""
        print(self.name + " is here!" )
        print(self.description)

    def set_conversation(self, conversation):
        """Sets what the character can say."""
        self.conversation = conversation

    def talk(self):
        """Prints the character's conversation."""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " has nothing to say to you.")

    def fight(self):
        """Declines to fight."""
        print(self.name + "does not want to fight a retard like you.")
        return True
