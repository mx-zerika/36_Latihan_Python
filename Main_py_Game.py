import time

# =====================
# Player Data
# =====================

player = {
    "name": "",
    "sanity": 100,
    "inventory": [],
    "clues": []
}


# =====================
# Basic Function
# =====================

def slow_print(text):
    for char in text:
        print( char, end="", flush=True)
        time.sleep(0.02)
    print()

def divider():
    print("\n" + "=" * 50 + "\n")

def show_status():
    divider()

    print(f"Name   : {player['name']}")
    print(f"Sanity: {player['sanity']}/100")

    print("\ninventory:")      

    if player["inventory"]:
        for item in player ["inventory"]:
            print(f"- {item}")
    else:
        print("- Empty")

    print("\nClues:")

    if player["clues"]:
        for clue in player["clues"]:
            print(f"- {clue}")
    else:
        print("- None")

    divider()


def add_item(item):
    if item not in player["inventory"]:
        player["inventory"].append(item)
        print(f"\nYou obtained: {item}")


def add_clue(clue):
    if clue not in player["clues"]:
        player["clues"].append(clue)
        print(f"\nCLUE FOUND: {clue}")


def change_sanity(amount):
    player["sanity"] += amount

    if player["sanity"] > 100:
        player["sanity"] = 100

    if player["sanity"] < 0:
        player["sanity"] = 0

    if player["sanity"] ==0:
        game_over()

def game_over():
    divider()

    print("YOUR SANITY HAS REACHED ZERO!")
    print()
    print("The Hallway dissapears..")
    print("You can no longer tell what is real..")

    divider()

    print("GAME OVER")

# =========================
# INTRO
# =========================
def main_menu():
    while True:
        divider()

        print("THE EMPTY FLOOR")
        print()
        print("[1] Start Game")
        print("[2] Quit")
        print("[3] About")

        choice  = input("\n> ")

        if choice == "1":
            intro()
            break

        elif choice == "2":
            print("\nGoodbye.")
            break

        elif choice == "3":
            print()
            print("THE EMPTY FLOOR")
            print("A psychological mystery text adventure.")
            print()
            print("Created by: Mx. Z")
            print()
            input("Press ENTER to return...")

        else:
            print("\nInvalid choice")

def intro():
    divider()

    slow_print("THE EMPTY FLOOR")

    divider()

    player["name"] = input("Enter your name: ")

    print()

    slow_print(
        f"It is almost midnight, {player['name']}."
    )

    slow_print(
        "You are walking home when the rain suddenly becomes heavier."
    )

    slow_print(
        "You notice an old building standing across the street."
    )

    slow_print(
        "The building looks abandoned."
    )

    slow_print(
        "But one light is still on."
    )

    input("\nPress ENTER to continue...")

    divider()

    slow_print(
        "You enter the building to escape the rain."
    )

    slow_print(
        "There is an elevator directly in front of you."
    )

    slow_print(
        "You press the button."
    )

    slow_print(
        "DING."
    )

    slow_print(
        "The elevator doors open."
    )

    slow_print(
        "You step inside."
    )

    input("\nPress ENTER to continue...")

    divider()

    slow_print(
        "The elevator begins moving."
    )

    slow_print(
        "6..."
    )

    slow_print(
        "5..."
    )

    slow_print(
        "4..."
    )

    slow_print(
        "3..."
    )

    slow_print(
        "2..."
    )

    slow_print(
        "1..."
    )

    slow_print(
        "..."
    )

    slow_print(
        "The elevator stops."
    )

    slow_print(
        "The display changes."
    )

    slow_print(
        "7"
    )

    slow_print(
        "You stare at the number."
    )

    slow_print(
        "This building only has six floors."
    )

    input("\nPress ENTER to continue...")

    floor_seven()


# =========================
# FLOOR 7
# =========================

def floor_seven():

    divider()

    slow_print(
        "The elevator doors slowly open."
    )

    slow_print(
        "A long hallway stretches before you."
    )

    slow_print(
        "There are three doors."
    )

    print("""
    [1] Room 701
    [2] Room 702
    [3] Room 703
    [4] Check status
    """)

    choice = input("> ")

    if choice == "1":
        room_701()

    elif choice == "2":
        room_702()

    elif choice == "3":
        room_703()

    elif choice == "4":
        show_status()
        floor_seven()

    else:
        print("\nInvalid choice.")
        floor_seven()


# =========================
# ROOM 701
# =========================

def room_701():

    divider()

    slow_print(
        "ROOM 701"
    )

    slow_print(
        "The room is completely empty."
    )

    slow_print(
        "There is only a chair beside the window."
    )

    print("""
    [1] Inspect the chair
    [2] Look outside
    [3] Leave
    """)

    choice = input("> ")

    if choice == "1":

        slow_print(
            "\nYou inspect the chair."
        )

        slow_print(
            "There is a name carved underneath it."
        )

        slow_print(
            f"The name is: {player['name']}"
        )

        change_sanity(-10)

        add_clue(
            "Your name is carved underneath the chair."
        )

        input("\nPress ENTER to continue...")
        room_701()

    elif choice == "2":

        slow_print(
            "\nYou look through the window."
        )

        slow_print(
            "You can see the street below."
        )

        slow_print(
            "There is someone standing outside."
        )

        slow_print(
            "They are looking directly at you."
        )

        change_sanity(-10)

        input("\nPress ENTER to continue...")
        room_701()

    elif choice == "3":
        floor_seven()

    else:
        print("\nInvalid choice.")
        room_701()


# =========================
# ROOM 702
# =========================

def room_702():

    divider()

    slow_print(
        "ROOM 702"
    )

    slow_print(
        "The door is unlocked."
    )

    slow_print(
        "Inside, you find an old desk."
    )

    print("""
    [1] Search the desk
    [2] Read the note
    [3] Leave
    """)

    choice = input("> ")

    if choice == "1":

        slow_print(
            "\nYou search the desk."
        )

        slow_print(
            "You find an old brass key."
        )

        add_item("Brass Key")

        input("\nPress ENTER to continue...")
        room_702()

    elif choice == "2":

        slow_print(
            "\nThere is a piece of paper on the desk."
        )

        slow_print(
            "It contains only one sentence:"
        )

        print(
            '\n"DO NOT ENTER ROOM 703."'
        )

        add_clue(
            'A note warns you not to enter Room 703.'
        )

        input("\nPress ENTER to continue...")
        room_702()

    elif choice == "3":
        floor_seven()

    else:
        print("\nInvalid choice.")
        room_702()


# =========================
# ROOM 703
# =========================

def room_703():

    divider()

    slow_print(
        "ROOM 703"
    )

    slow_print(
        "The door is locked."
    )

    slow_print(
        "You hear knocking from the other side."
    )

    slow_print(
        "Knock."
    )

    slow_print(
        "Knock."
    )

    slow_print(
        "Knock."
    )

    print("""
    [1] Knock back
    [2] Use the Brass Key
    [3] Leave
    """)

    choice = input("> ")

    if choice == "1":

        slow_print(
            "\nYou knock three times."
        )

        slow_print(
            "..."
        )

        slow_print(
            "Something knocks back."
        )

        slow_print(
            "Four times."
        )

        change_sanity(-15)

        add_clue(
            "Something inside Room 703 responds to your knocks."
        )

        input("\nPress ENTER to continue...")
        room_703()

    elif choice == "2":

        if "Brass Key" in player["inventory"]:

            slow_print(
                "\nYou insert the brass key."
            )

            slow_print(
                "CLICK."
            )

            room_703_inside()

        else:

            slow_print(
                "\nYou don't have a key."
            )

            room_703()

    elif choice == "3":
        floor_seven()

    else:
        print("\nInvalid choice.")
        room_703()


# =========================
# ROOM 703 INSIDE
# =========================

def room_703_inside():

    divider()

    slow_print(
        "The door opens."
    )

    slow_print(
        "The room is dark."
    )

    slow_print(
        "You turn on your phone flashlight."
    )

    slow_print(
        "There is a large mirror on the wall."
    )

    slow_print(
        "You look at your reflection."
    )

    slow_print(
        "..."
    )

    slow_print(
        "Your reflection is not moving."
    )

    change_sanity(-25)

    add_clue(
        "Your reflection does not move with you."
    )

    print("""
    [1] Touch the mirror
    [2] Look away
    [3] Leave the room
    """)

    choice = input("> ")

    if choice == "1":

        slow_print(
            "\nYou touch the mirror."
        )

        slow_print(
            "Your reflection smiles."
        )

        slow_print(
            "You don't."
        )

        ending_truth()

    elif choice == "2":

        slow_print(
            "\nYou look away."
        )

        slow_print(
            "When you look back..."
        )

        slow_print(
            "The mirror is empty."
        )

        ending_loop()

    elif choice == "3":

        ending_escape()

    else:
        print("\nInvalid choice.")
        room_703_inside()


# =========================
# ENDINGS
# =========================

def ending_truth():

    divider()

    slow_print("ENDING: THE TRUTH")

    divider()

    slow_print(
        "You finally understand."
    )

    slow_print(
        "The seventh floor was never part of the building."
    )

    slow_print(
        "It was a place created from your memories."
    )

    slow_print(
        "And the person in the mirror..."
    )

    slow_print(
        "was the version of you that never left."
    )

    divider()

    print("GAME OVER")


def ending_loop():

    divider()

    slow_print("ENDING: THE LOOP")

    divider()

    slow_print(
        "You leave Room 703."
    )

    slow_print(
        "You enter the elevator."
    )

    slow_print(
        "The doors close."
    )

    slow_print(
        "DING."
    )

    slow_print(
        "The doors open."
    )

    slow_print(
        "You are standing in front of Room 701."
    )

    slow_print(
        "You look at the door."
    )

    slow_print(
        "Someone knocks from inside."
    )

    divider()

    print("GAME OVER")


def ending_escape():

    divider()

    slow_print("ENDING: ESCAPE")

    divider()

    slow_print(
        "You run back to the elevator."
    )

    slow_print(
        "The doors close."
    )

    slow_print(
        "The elevator descends."
    )

    slow_print(
        "6..."
    )

    slow_print(
        "5..."
    )

    slow_print(
        "4..."
    )

    slow_print(
        "3..."
    )

    slow_print(
        "2..."
    )

    slow_print(
        "1..."
    )

    slow_print(
        "The doors open."
    )

    slow_print(
        "You are outside."
    )

    slow_print(
        "The building behind you has six floors."
    )

    slow_print(
        "You look up."
    )

    slow_print(
        "There is someone standing on the seventh floor."
    )

    divider()

    print("GAME OVER")


# =========================
# START GAME
# =========================

main_menu()