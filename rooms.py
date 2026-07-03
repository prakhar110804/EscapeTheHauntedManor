class Room:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits

    def display(self):
        print("\n" + "=" * 50)
        print(self.name.upper())
        print("=" * 50)
        print(self.description)

        print("\nAvailable Paths:")

        for option, room in self.exits.items():
            print(f"{option}. {room}")