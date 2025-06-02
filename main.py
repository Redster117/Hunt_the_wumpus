"""Info about the cave system."""
from cave import Cave

cavern = Cave("Cavern")
cavern.set_description("A dark and damp cavern with stalactites hanging from the ceiling.")
grotto = Cave("Grotto")
grotto.set_description("A small grotto with a serene pool of water.")
dungeon = Cave("Dungeon")
dungeon.set_description("A foreboding dungeon with stone walls.")

cavern.link_caves(dungeon, "South")
dungeon.link_caves(cavern, "North")
dungeon.link_caves(grotto, "West")
grotto.link_caves(dungeon, "East")

cavern.get_details()
dungeon.get_details()
grotto.get_details()

cavern.describe()
grotto.describe()
dungeon.describe()
