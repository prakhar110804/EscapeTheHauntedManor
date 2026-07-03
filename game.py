from player import Player


class Game:
    def __init__(self):
        self.player = None

    def start(self):
        self.show_intro()

        name = input("\nEnter your name: ")
        self.player = Player(name)

        print(f"\nWelcome, {self.player.name}!")
        print("Your adventure begins now...")

        self.player.show_stats()

    def show_intro(self):
        print("=" * 50)
        print("      ESCAPE THE HAUNTED MANOR")
        print("=" * 50)
        print("Year: 1998")
        print("Location: Blackwood Forest")
        print()
        print("Your car breaks down during a thunderstorm.")
        print("You enter an abandoned manor looking for help.")
        print("The door slams shut behind you.")
        print()
        print('"No one leaves until the Manor chooses."')
        print("=" * 50)