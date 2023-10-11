# shop keeper has a buff you upgrade. Each upgrade makes your efficency +1.
# Efficency is equal to times the collect_resources goes off.

# Okay, so there needs to be a value that associates with the shop buff upgrades and the counter in the
# first line of the collect_resource function.

# naming the buff to store its value


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
