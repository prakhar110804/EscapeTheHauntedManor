from player import Player
from rooms import create_rooms


class Game:
    def __init__(self):
        self.player = None
        self.rooms = create_rooms()
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
        print("=" * 55)
        print("         ESCAPE THE HAUNTED MANOR")
        print("=" * 55)
        print("Year: 1998")
        print("Location: Blackwood Forest")
        print()
        print("Your car breaks down during a thunderstorm.")
        print("You enter an abandoned manor looking for help.")
        print("The door slams shut behind you.")
        print()
        print('"No one leaves until the Manor chooses."')
        print("=" * 55)

    def game_loop(self):

        while True:

            room = self.rooms[self.current_room]

            room.display()

            # ------------------ BASEMENT PUZZLE ------------------
            if room.name == "Basement" and not room.item_taken:

                print("\n🧩 A mysterious voice echoes through the basement...")
                print("\nRIDDLE")
                print('"I speak without a mouth and hear without ears."')
                print("What am I?")

                answer = input("\nYour answer: ").strip().lower()

                if answer == "echo":
                    print("\n✅ Correct!")
                    self.player.add_item(room.item)
                    room.item_taken = True
                else:
                    print("\n❌ Wrong answer.")
                    print("The amulet remains protected.")
                    continue

            # ---------------- ITEM COLLECTION ----------------
            elif room.item and not room.item_taken:

                print(f"\n✨ You found: {room.item}")

                take = input("Do you want to take it? (y/n): ").strip().lower()

                if take == "y":
                    self.player.add_item(room.item)
                    room.item_taken = True
                else:
                    print("You leave it where it is.")

            # ---------------- EXIT CHECK ----------------
            if room.name == "Exit Gate":

                required_items = [
                    "Flashlight",
                    "Rusty Key",
                    "Ancient Amulet"
                ]

                if all(self.player.has_item(item) for item in required_items):

                    print("\n🎉 CONGRATULATIONS!")
                    print("You unlocked the gate.")
                    print("You escaped the Haunted Manor!")
                    print("\n★★★★★ GOOD ENDING ★★★★★")

                else:

                    print("\n❌ BAD ENDING")
                    print("The gate remains locked.")
                    print("You are missing important items.")

                break

            print("\nActions")
            print("1. Move to another room")
            print("3. Check Inventory")
            print("4. View Player Stats")
            print("5. Quit Game")

            choice = input("\nChoose an option: ").strip()

            if choice in room.exits:
                self.current_room = room.exits[choice]

            elif choice == "3":
                self.show_inventory()

            elif choice == "4":
                self.player.show_stats()

            elif choice == "5":
                print("\nYou gave up and left the adventure.")
                break

            else:
                print("\nInvalid choice.")

    def show_inventory(self):

        print("\n========== INVENTORY ==========")

        if self.player.inventory:
            for item in self.player.inventory:
                print(f"• {item}")
        else:
            print("Your inventory is empty.")