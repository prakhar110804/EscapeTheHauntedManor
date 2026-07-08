class Room:
    def __init__(
        self,
        name,
        description,
        exits,
        item=None,
        enemy=None,
        puzzle=None,
    ):
        self.name = name
        self.description = description
        self.exits = exits
        self.item = item
        self.enemy = enemy
        self.puzzle = puzzle
        self.item_taken = False

    def display(self):
        print("\n" + "=" * 55)
        print(self.name.upper())
        print("=" * 55)
        print(self.description)

        print("\nAvailable Paths:")
        for option, room in self.exits.items():
            print(f"{option}. {room}")


def create_rooms():

    rooms = {

        "Entrance Hall": Room(
            "Entrance Hall",
            "A dusty entrance hall with broken furniture. Two large doors stand before you.",
            {
                "1": "Library",
                "2": "Dining Hall"
            }
        ),

        "Library": Room(
            "Library",
            "Rows of ancient books line the walls. Something shines beneath a bookshelf.",
            {
                "1": "Entrance Hall",
                "2": "Basement"
            },
            item="Flashlight"
        ),

        "Dining Hall": Room(
            "Dining Hall",
            "A massive dining table is covered with rotten food. You hear strange footsteps.",
            {
                "1": "Entrance Hall",
                "2": "Basement"
            },
            enemy="Zombie Butler"
        ),

        "Basement": Room(
            "Basement",
            "Cold air fills the room. Strange symbols cover the walls.",
            {
                "1": "Library",
                "2": "Dining Hall",
                "3": "Hidden Chamber"
            },
            puzzle="Ancient Riddle"
        ),

        "Hidden Chamber": Room(
            "Hidden Chamber",
            "A mysterious chamber glows with blue light.",
            {
                "1": "Basement",
                "2": "Exit Gate"
            },
            item="Ancient Amulet",
            enemy="Shadow Monster"
        ),

        "Exit Gate": Room(
            "Exit Gate",
            "A giant iron gate blocks your escape.",
            {
                "1": "Hidden Chamber"
            },
            enemy="Final Demon"
        )

    }

    return rooms