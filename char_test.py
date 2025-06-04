"""Testing character module."""
from character import Enemy

blorpington = Enemy("Blorpington", "A Wumpus")
blorpington.describe()
blorpington.set_conversation("Greetings Nigga :)")
blorpington.talk()
blorpington.set_weakness("Mondragon Rifle")

fight_with = input("What do you want to fight with? ")
blorpington.fight(fight_with)
