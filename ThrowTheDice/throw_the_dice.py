"""
Throw the Dice: throw_the_dice.py.

From the course: "Python programming for kids".
Written by Anatoly Nikiforov and his students, Kodium, 2020.
https://kodium.online/
"""
import random
import time

# Enter your name
NAME = input("What is your name?\n> ")
# Generate the cash for both PLAYers
STRANGER_GOLD = random.randint(5, 100)
MY_GOLD = random.randint(5, 100)

while STRANGER_GOLD > 0 and MY_GOLD > 0:
    print("Stranger:\n- Try your luck,", NAME, "\t\t\t\t\
          Your Gold:", MY_GOLD, "$")
    # You can't set the amount of the bet more than the cash you have
    BET_IS_OK = False

    while BET_IS_OK is False:
        print("Stranger invites you to play the dices")
        BET = int(input("Set the amount of your bet:\n>"))

        if BET > MY_GOLD:
            print("You can't bet more than you have!")
        elif BET > STRANGER_GOLD:
            print("Stranger doesn't have enough Gold")
        else:
            print("Okay, you can play!")
            BET_IS_OK = True

    print("Stranger's in...")
    STRANGER_SHOT1 = random.randint(1, 6)
    STRANGER_SHOT2 = random.randint(1, 6)
    time.sleep(3)
    print("On the table:", STRANGER_SHOT1, STRANGER_SHOT2)

    PLAY = input("Do you want to throw the dices? (yes/no)").lower()

    if PLAY == "yes":
        PLAYER_SHOT1 = random.randint(1, 6)
        PLAYER_SHOT2 = random.randint(1, 6)
        time.sleep(3)
        print("On the table:", PLAYER_SHOT1, PLAYER_SHOT2)
    elif PLAY == "no":
        MY_GOLD = MY_GOLD - BET
        print("You lost", "-", BET, "$")

    if PLAYER_SHOT1 + PLAYER_SHOT2 < STRANGER_SHOT1 + STRANGER_SHOT2:
        print("Stranger won")
        MY_GOLD -= BET
        STRANGER_GOLD += BET
    elif PLAYER_SHOT1 + PLAYER_SHOT2 > STRANGER_SHOT1 + STRANGER_SHOT2:
        print("You win!")
        STRANGER_GOLD = STRANGER_GOLD - BET
        MY_GOLD = MY_GOLD + BET
        print(BET, "Gold")
    else:
        print('No winner!')

if STRANGER_GOLD <= 0:
    print("Stranger has no more gold")
else:
    print("You have no more gold =(")
