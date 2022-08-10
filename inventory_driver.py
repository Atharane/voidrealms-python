import json
import os.path


# Inventory class
class VendingMachine:
    inventory = {}

    def __init__(self):
        self.load()

    def add(self, key, qty):
        self.inventory[key] = self.inventory.get(key, 0) + int(qty)  # modify existing value or add new key

        print(f'Added {qty} {key}s: total = {self.inventory[key]}')

    def remove(self, key, qty):
        if key in self.inventory:
            existing = self.inventory[key]
            if existing < int(qty):
                print(f"Only {existing} {key}s available")
                return

            new = existing - int(qty)
            self.inventory[key] = new
            print(f'Removed {qty} {key}: total = {self.inventory[key]}')

        else:
            print(f'{key} currently not available')
            return

    def display(self):
        for key, value in self.inventory.items():
            print(f'{key}: {value}')

    def save(self):
        print('Saving inventory...')
        with open('inventory.txt', 'w') as f:
            json.dump(self.inventory, f)
        print('Saved!')

    def load(self):
        print('Loading inventory...')
        if not os.path.exists('inventory.txt'):
            print('Skipping, nothing to load')
            return
        with open('inventory.txt', 'r') as f:
            self.inventory = json.load(f)
        print('Loaded!')


def main():
    inv = VendingMachine()

    while True:
        command = input("\nAction: ").split()

        if command[0] == 'exit':
            inv.save()
            break

        try:
            method = getattr(inv, command[0])
            method(*command[1:])  # execute method with arguments

        except AttributeError:
            print('Invalid command')


if __name__ == "__main__":
    main()
