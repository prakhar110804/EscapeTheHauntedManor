from game import Game


def show_menu():
    while True:
        print("\n" + "=" * 55)
        print("         ESCAPE THE HAUNTED MANOR")
        print("=" * 55)
        print("1. Start Game")
        print("2. About")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            game = Game()
            game.start()
            break

        elif choice == "2":
            print("\nEscape The Haunted Manor is a text-based adventure game.")
            print("Explore the haunted mansion, collect important items,")
            print("and escape before it's too late!")

        elif choice == "3":
            print("\nThanks for playing!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    show_menu()