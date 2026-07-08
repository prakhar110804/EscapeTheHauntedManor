class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.lives = 3
        self.inventory = []

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)
            self.score += 10
            print(f"\n✅ You collected: {item}")
        else:
            print(f"\nYou already have {item}.")

    def has_item(self, item):
        return item in self.inventory

    def show_stats(self):
        print("\n========================================")
        print("PLAYER STATS")
        print("========================================")
        print(f"Name      : {self.name}")
        print(f"Health    : {self.health}")
        print(f"Score     : {self.score}")
        print(f"Lives     : {self.lives}")

        print("Inventory:")

        if self.inventory:
            for item in self.inventory:
                print(f"  • {item}")
        else:
            print("  Empty")

        print("========================================")