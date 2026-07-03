class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.score = 0
        self.lives = 3
        self.inventory = []

    def show_stats(self):
        print("\n" + "=" * 40)
        print("PLAYER STATS")
        print("=" * 40)
        print(f"Name      : {self.name}")
        print(f"Health    : {self.health}")
        print(f"Score     : {self.score}")
        print(f"Lives     : {self.lives}")
        print(f"Inventory : {self.inventory}")
        print("=" * 40)