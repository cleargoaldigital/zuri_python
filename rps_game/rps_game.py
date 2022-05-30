# Rock-Paper_Scissors Game
# A simple 2-player game.
# Rock beat Scissors
# Scissors beats Paper
# paper beats Rock

# If players chose the same object at the same time, they tie.

R = "rock"
P = "Paper"
S = "Scissors"

# is_running = True

# while is_running:
options = ["R", "P", "S"]

playerSelect = input("Enter any of R/P/S...").upper()

ComputerSelect = random.choice(options)


if PlayerSelect == ComputerSelect:
   print("The game is a tie!")

elif
   playerSelect == "P" && ComputerSelect == "R":
   print("Congratulations. You have won the game!")

elif
   playerSelect == "R" && ComputerSelect == "P":
   print("Oh Sorry! Computer has won this game!")

elif
   playerSelect == "S" && ComputerSelect == "R":
   print("Oh Sorry! Computer has won this game!")

elif
   playerSelect == "S" && ComputerSelect == "P":
   print("Congratulations. You have won the game!")

elif
   playerSelect == "P" && ComputerSelect == "S":
   print("Oh Sorry! Computer has won this game!")

elif
   playerSelect == "R" && ComputerSelect == "S":
   print("Congratulations. You have won the game!")