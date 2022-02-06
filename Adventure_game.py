import time
import random


def print_pause(message):
    time.sleep(2)
    print(message)


def validate_input(prompt, option1, option2):
    while True:
        print_pause(prompt)
        answer = input().lower()
        if answer == option1:
            print("")
            return option1
        elif answer == option2:
            print("")
            return option2


def intro():
    print_pause("You are standing in an open field with green pastures and \
small bushes.")
    print_pause("Rumor has it that a monster is roaming the area and harasing \
the nearby population.")


def field(items):
    print_pause("In front of you is a tower.")
    print_pause("To your left is a door on the ground around some building \
ruins.")
    if "Woodcutter's axe" in items:
        print_pause("In your hand you hold your woodcutter's axe.\n")
    elif "Legendary silver axe of Spamalot" in items:
        print_pause("The feeling of the axe of Spamalot in your hand \
makes you hungry.")
        print_pause("You wonder when was the last time you had breakfast")
    print_pause("Where would you like to go?")
    print_pause("Enter 1 to go up the tower.")
    print_pause("Enter 2 to go down into the dungeon.")
    field_choice = validate_input("Please enter 1 or 2.", "1", "2")
    if field_choice == "1":
        tower(items)
    elif field_choice == "2":
        dungeon(items)


def tower(items):
    print_pause("You approach the entrance of the tower.")
    print_pause("You are about to enter the tower and out steps a monster.")
    print_pause("Oh no! This is the monster's lair!")
    print_pause("The monster attacks you!")
    if "Woodcutter's axe" in items:
        print_pause("You are a bit unprepared for a battle with only a \
woodcutter's axe.")
    tower_choice = validate_input("Would you like to (1) fight or (2) run\
 away?", "1", "2")
    if tower_choice == "1":
        combat(items)
    if tower_choice == "2":
        run_away(items)


def combat(items):
    if "Woodcutter's axe" in items:
        print_pause("You do your best...")
        luck = random.randint(1, 5)
        if luck == 5:
            print_pause("The battle is fierce.")
            print_pause("You lose a lot of blood after an attack.")
            print_pause("You swing your axe downwards with all your might.")
            print_pause("Out of luck you are able to slice the head off of the\
 monster.")
            victory(items)
        else:
            print_pause("But your woodcutter's axe is not enough to beat the\
 monster.")
            print_pause("You lost!")
            play_again()
    elif "Legendary silver axe of Spamalot" in items:
        print_pause("As the monster moves in your direction you raise the \
Legendary silver axe of Spamalot!")
        print_pause("Suddenly a bright flash emerges from the tip of the axe.")
        print_pause("Ghosts of vikings appear behind the monster.")
        print_pause("They start singing in thundrous voices a song that \
went like this:")
        print_pause("SPAM! SPAM! SPAM! SPAM! SPAM! SPAM!")
        print_pause("LOVELY SPAM! WONDERFUL SPAM!")
        print_pause("You notice one of the ghosts holding a can of SPAM!")
        print_pause("The monster yells 'I DON'T LIKE SPAM!' and flees!")
        print_pause("The ghost vikings give you a can of Spam and vanish.")
        victory(items)


def run_away(items):
    print_pause("You run as fast as you can, trying to avoid the monster.")
    luck = random.randint(1, 5)
    if luck != 1:
        print_pause("You are able to escape and find yourself standing\
 back in the field.\n")
        field(items)
    elif luck == 1:
        print_pause("But the monster catches you and you lose.\n")
        play_again()


def dungeon(items):
    if "Woodcutter's axe" in items:
        print_pause("You venture slowly into the dungeon")
        print_pause("It happens to be only a small cellar from the ruins of a \
tavern.")
        print_pause("You see some molded cheese and barrels of wine")
        print_pause("Laying on the corner, near some old barrels, you find a \
wooden stick with a shiny tip.")
        print_pause("You have found the legendary Spamalot silver axe!")
        print_pause("You leave your woodcutter's axe behind and take the \
legendary weapon with you.")
        items.remove("Woodcutter's axe")
        items.append("Legendary silver axe of Spamalot")
        print_pause("You walk back to the field.\n")
        field(items)
    elif "Menu badge" in items:
        print_pause("Once again you go inside the old cellar.")
        print_pause("There are empty cans laying on the corners of the room.")
        print_pause("You feel your stomach rumble.")
        print_pause("You return to the field.\n")
        field(items)
    elif "Green Midget badge" in items:
        print_pause("You venture back in the cellar.")
        print_pause("You notice a wodden board with some writings on it.")
        print_pause("You can figure out the following items:")
        print_pause("- Egg and bacon")
        print_pause("- Egg, sausage and bacon")
        print_pause("- Egg and SP...(unreadable)")
        print_pause("You can't figure out anything else.")
        print_pause("You go back to the field.\n")
        items.append("Menu badge")
        field(items)
    elif "Legendary silver axe of Spamalot" in items:
        print_pause("You wander back in the cellar.")
        print_pause("You notice an old dust covered sign")
        print_pause("It has the drawing of a Green Midget holding a cup of\
 coffe.")
        print_pause("Nothing else catches your eye.")
        print_pause("You go back to the field\n")
        items.append("Green Midget badge")
        field(items)


def victory(items):
    print_pause("Hurray, you have saved the people from the monster!")
    if "Woodcutter's axe" in items:
        print_pause("You are victoriuous and are able to save the people \
from the monster")
        play_again()
    elif "Legendary silver axe of Spamalot" in items:
        print_pause("You are victorious and are able to enjoy some delicious \
SPAM! for breakfast.")
        play_again()


def play_again():
    print("")
    end_game = validate_input("Would you like to play again? (y/n)", "y", "n")
    if end_game == "y":
        print_pause("Excellent! Restarting the game...")
        print_pause("")
        play_game()
    elif end_game == "n":
        print_pause("Thanks for playing! See you next time.")
        print_pause("")
        exit()


def play_game():
    items = ["Woodcutter's axe"]
    intro()
    field(items)


if __name__ == '__main__':
    play_game()
