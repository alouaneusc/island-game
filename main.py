class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []


class IslandExplorerGame:
    def __init__(self):
        self.player = None
        self.world = {
            "beach": {
                "description": "You find yourself on a sandy beach.",
                "exits": {"jungle": "Enter the dense jungle."},
                "items": ["shovel"]
            },
            "jungle": {
                "description": "You are in a dense jungle. It's dark and mysterious.",
                "exits": {"beach": "Go back to the beach."},
                "items": ["key"]
            }
        }

    def start(self):
        player_name = input("Welcome to Island Explorer! What's your name? ")
        self.player = Player(player_name)
        print(f"Hello, {self.player.name}! Let's begin your adventure.")
        self.current_location = "beach"
        self.play()

    def play(self):
        while True:
            location = self.world[self.current_location]
            print(location["description"])
            action = input("What do you want to do? ").lower()
            self.process_action(action)

    # Modify the process_action method

    def process_action(self, action):
        if action == "quit":
            print("Thanks for playing!")
            exit()

        location = self.world[self.current_location]
        if action in location["exits"]:
            self.current_location = action
        elif action == "inventory":
            print("Inventory:", ", ".join(self.player.inventory))
        elif action == "take":
            items_here = location["items"]
            if items_here:
                item_to_take = items_here[0]
                self.player.inventory.append(item_to_take)
                location["items"].remove(item_to_take)
                print(f"You picked up {item_to_take}.")
            else:
                print("There's nothing to take here.")
        else:
            print("Invalid action. Try again.")

        self.play()


if __name__ == "__main__":
    game = IslandExplorerGame()
    game.start()
