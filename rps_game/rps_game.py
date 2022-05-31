#import random module
import random

print("Welcome to Rock-Paper-Scissors Game")
print("General rules of the game: \n"
    +"Rock vs paper -> paper wins \n"
    + "Rock vs scissor -> Rock wins \n"
    +"paper vs scissor -> scissor wins \n")

while True:
    # take the input from user
    print("Select a weapon: \n R for Rock, \n P for Paper, and \n S for Scissors \n")

    # accept input from user
    playerChoice = input("Select your weapon: ").upper()

    while (playerChoice != "R" or playerChoice != "P" or playerChoice != "S"):
        print("Invalid input.")
        playerChoice = input("enter valid input. Enter a valid weapon: ").upper()
        if (playerChoice == "R" or playerChoice == "P" or playerChoice == "S"):
            break

    if playerChoice == "R":
        user_choice = "Rock"
    elif playerChoice == "P":
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    # print user's choice
    print("Player choice is: ", playerChoice, ":", user_choice)
    print("\nNow it's computer's turn....")

    # CPU selects weapon randomly
    options = ["R", "P", "S"]
    computerChoice = random.choice(options)

    if computerChoice == "R":
        auto_choice = "Rock"
    elif computerChoice == "P":
        auto_choice = "Paper"
    else:
        auto_choice = "Scissors"

    # print computer's choice
    print("Computer's choice is: ", computerChoice,":", auto_choice)

    # display players' choices
    print(user_choice + " VS " + auto_choice)

    # compare weapons and display results
    if playerChoice == computerChoice:
        print("The game is a tie!", end = "")

    elif playerChoice == "P" and computerChoice == "R":
        print("Congratulations. You have won the game!", end = "")

    elif playerChoice == "R" and computerChoice == "P":
        print("Oh Sorry! Computer has won this game!", end = "")

    elif playerChoice == "S" and computerChoice == "R":
        print("Oh Sorry! Computer has won this game!", end = "")

    elif playerChoice == "S" and computerChoice == "P":
        print("Congratulations. You have won the game!", end = "")

    elif playerChoice == "P" and computerChoice == "S":
        print("Oh Sorry! Computer has won this game!", end = "")

    elif playerChoice == "R" and computerChoice == "S":
        print("Congratulations. You have won the game!", end = "")

    # ask if user wants to exit or continue the game
    print("\nDo you want to play again? (Y/N)")
    user_response = input().lower()
  
    # user chooses n to exit the game
    if user_response == 'n':
        break
    # goodbye message after the game.
print("\nThanks you for taking time to play this incredible game.")