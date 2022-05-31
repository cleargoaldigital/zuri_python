Pseudocode for Rock Paper Scissors Game Brief about the game: A player is set up against the computer. Each (computer and player) has three weapons: rock, paper, and scissors. The following analysis holds true for the weapons:

Paper has a higher value than rock - Paper can cover rock.

Rock has higher value than Scissors - Rock can crush Scissors.

Scissors has a higher value than paper - Scissors can cut paper.

playerChoice == computerChoice : Tie

playerChoice: rock - computerChoice : scissors == player wins

playerChoice: paper - computerChoice : rock == player wins

playerChoice: scissors - computerChoice : paper == player wins

playerChoice: paper - computerChoice : scissors == computer wins

playerChoice: scissors - computerChoice : rock == computer wins