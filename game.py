from rooms import Room
from player import Player


class Game:
    def __init__(self):
        self.player = None

        self.rooms = {
            "Entrance Hall": Room(
                "Entrance Hall",
                "A dusty entrance hall with two old wooden doors.",
                {
                    "1": "Library",
                    "2": "Dining Hall"
                }
            ),

            "Library": Room(
                "Library",
                "Tall bookshelves stretch to the ceiling. Something glows in the corner.",
                {
                    "1": "Entrance Hall"
                }
            ),

            "Dining Hall": Room(
                "Dining Hall",
                "A massive dining table is covered with rotten food.",
                {
                    "1": "Entrance Hall"
                }
            )
        }

        self.current_room = "Entrance Hall"

    def start(self):
        self.show_intro()

        name = input("\nEnter your name: ")
        self.player = Player(name)

        print(f"\nWelcome, {self.player.name}!")
        print("Your adventure begins now...")

        self.player.show_stats()

        self.game_loop()

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

    def game_loop(self):

        while True:

            room = self.rooms[self.current_room]

            room.display()

            print("\nActions:")
            print("3. Check Inventory")
            print("4. View Player Stats")
            print("5. Quit Game")

            choice = input("\nChoose an option: ").strip()

            if choice in room.exits:
                self.current_room = room.exits[choice]

            elif choice == "3":
                print("\n========== INVENTORY ==========")

                if self.player.inventory:
                    for item in self.player.inventory:
                        print(f"- {item}")
                else:
                    print("Your inventory is empty.")

            elif choice == "4":
                self.player.show_stats()

            elif choice == "5":
                print("\nYou leave the haunted manor...")
                print("Game Over!")
                break

            else:
                print("\n❌ Invalid choice. Please try again.")