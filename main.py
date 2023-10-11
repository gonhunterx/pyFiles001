# system where you go farm something either wood maybe fishing.
# you could have a stat that keeps track of how many you have compelted
# this could even be something like a skill in runescape
# also just create a 50/50 battle where you enter with coins and you can bet coins you
# have obtained by selling wood and fish
import sys


# Classes
class ShopKeeper:
    def __init__(self):
        self.shop_inventory = []
        # im not sure how this works but id assume the shop keepers gold does not matter.
        self.gold = 100000


class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Player:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.inventory = []

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Gold: {self.gold}")
        print("Inventory:")
        for i in self.inventory:
            print(f"{i.name}")


# List of Items (Unsure if these are necessary)
wood_log = Item("wood log", 4)
fish = Item("fish", 5)


# Functions
def intro_menu(player):
    print("1. Begin game")
    print("2. Exit game")
    intro_choice = input("Enter input: ")
    if intro_choice == "1":
        main_menu(player)


# the length of the main menu is nearing the point of making a seperate menu for just location options
def main_menu(player):
    print("==================")
    print("1. Go to the woods")
    print("2. Go to the pond")
    print("3. Go to the shop")
    print("4. Enter the arena")
    print("5. Display Stats/Inv")
    print("6. Exit Game")
    print("==================")
    choice = input("Enter input: ")
    if choice == "1":
        woods(player)
    elif choice == "2":
        pond(player)
    elif choice == "3":
        shop(player)
    elif choice == "4":
        arena(player)
    elif choice == "5":
        player.display_stats()
        continue_input = input("1. to continue...: ")
        if continue_input == "1":
            main_menu(player)
        else:
            main_menu(player)
    elif choice == "6":
        sys.exit()
    else:
        print("Invalid input.")


def woods(player):
    print("you enter the woods...")
    collect_resource(player, "wood log", 4)
    main_menu(player)


def pond(player):
    # do i want it so you immediatly fish or chop?
    print("you walk over to the pond...")
    collect_resource(player, "fish", 5)
    main_menu(player)


def shop(player):
    shop_keeper = ShopKeeper()
    print("you enter the shop...")
    # shop menu
    print("1. Buy")
    print("2. Sell")
    print
    # logic for buying and selling items.
    shop_choice = input("Input: ")
    if shop_choice == "1":
        print("What do you want to buy?")
        print(shop_keeper.shop_inventory)


def arena(player):
    print("you enter the arena...")


def collect_resource(player, resource_name, resource_value):
    print(f"You found {resource_name}! +1 {resource_name}")
    # append the item found to the player inventory
    player.inventory.append(Item(resource_name, resource_value))
    collect_more = input(f"Collect more {resource_name}? yes or no: ")
    if collect_more.lower() == "yes":
        collect_resource(player, resource_name, resource_value)
    elif collect_more == "no":
        main_menu(player)
    else:
        print("Invalid Entry.")
    # display stats
    # pretty much just want this as its own option on the main menu.
    # player.display_stats()


def main():
    print("Welcome to Honimata Sekai")
    player_name = input("What is your name?: ")
    player = Player(player_name)

    intro_menu(player)


if __name__ == "__main__":
    main()
