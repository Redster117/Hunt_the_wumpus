"""Info about the cave system."""
from cave import Cave
from character import Enemy

cavern = Cave("Cavern")
cavern.set_description("A dark and damp cavern with stalactites hanging from the ceiling.")
grotto = Cave("Grotto")
grotto.set_description("A small grotto with a serene pool of water.")
dungeon = Cave("Dungeon")
dungeon.set_description("A foreboding dungeon with stone walls.")

blorpington = Enemy("Blorpington", "A Wumpus")
blorpington.describe()
blorpington.set_conversation("Greetings :)")
blorpington.talk()
blorpington.set_weakness("Mondragon Rifle")
dungeon.set_character(blorpington)

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

cavern.get_details()
dungeon.get_details()
grotto.get_details()

current_cave = cavern
dead = False
while dead is False:
    print("\n")
    current_cave.get_details()
    inhabitated = current_cave.get_character()
    if inhabitated is not None:
        inhabitated.describe()
    command = input("> ")
    if command in ["North", "East", "South", "West"]:
        current_cave = current_cave.move(command)
    elif command == "Talk":
        if inhabitated is not None:
            inhabitated.talk()
    elif command == "Fight":
        if inhabitated is not None and isinstance(inhabitated, Enemy):
            fight_with = input("What do you want to fight with? ")
            if inhabitated.fight(fight_with) is True:
                print("Bravo, you win.")
                current_cave.set_character(None)
            else:
                print("Fuck off. U lost the fight weak ass bitch. ")
                dead = True
        else:
            print("There is no one here to fight with.")
