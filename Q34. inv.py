# Initialize the inventory dictionary
inventory = {}

# Function to add an item to the inventory
def add_item(item_name, quantity):
    """
    Adds an item to the inventory or updates its quantity.
    """
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"Added {quantity} of {item_name} to the inventory.")

# Function to remove an item from the inventory
def remove_item(item_name, quantity):
    """
    Removes a certain quantity of an item from the inventory.
    """
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            if inventory[item_name] == 0:
                del inventory[item_name]
            print(f"Removed {quantity} of {item_name} from the inventory.")
        else:
            print(f"Not enough {item_name} in the inventory to remove {quantity}.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to display the current inventory
def display_inventory():
    """
    Displays all items in the inventory with their quantities.
    """
    if inventory:
        print("\nCurrent Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("\nThe inventory is empty.")

# Example Usage
if __name__ == "__main__":
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Display Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter the item name: ")
            qty = int(input(f"Enter the quantity of {item}: "))
            add_item(item, qty)
        elif choice == "2":
            item = input
