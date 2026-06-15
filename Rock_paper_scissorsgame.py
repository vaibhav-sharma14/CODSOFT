import random

while True:

    print("\n------ WELCOME TO ROCK PAPER SCISSORS GAME ------\n")

    print("Choices: Rock, Paper, Scissors")

    game = input("\nEnter your choice: ").capitalize()

    computerchoice = ["Rock", "Paper", "Scissors"]

    print("\nYour Choice is:", game)

    computer_move = random.choice(computerchoice)

    if game == "Rock" and computer_move == "Paper":
        print("\nComputer Choice is:", computer_move)
        print("\nSorry! You Lost. Better Luck Next Time.")

    elif game == "Paper" and computer_move == "Scissors":
        print("\nComputer Choice is:", computer_move)
        print("\nSorry! You Lost. Better Luck Next Time.")

    elif game == "Scissors" and computer_move == "Rock":
        print("\nComputer Choice is:", computer_move)
        print("\nSorry! You Lost. Better Luck Next Time.")

    elif game == "Rock" and computer_move == "Scissors":
        print("\nComputer Choice is:", computer_move)
        print("\nCongratulations! You Won.")

    elif game == "Paper" and computer_move == "Rock":
        print("\nComputer Choice is:", computer_move)
        print("\nCongratulations! You Won.")

    elif game == "Scissors" and computer_move == "Paper":
        print("\nComputer Choice is:", computer_move)
        print("\nCongratulations! You Won.")

    elif game == "Rock" and computer_move == "Rock":
        print("\nComputer Choice is:", computer_move)
        print("\nIt's a Tie.")

    elif game == "Paper" and computer_move == "Paper":
        print("\nComputer Choice is:", computer_move)
        print("\nIt's a Tie.")

    elif game == "Scissors" and computer_move == "Scissors":
        print("\nComputer Choice is:", computer_move)
        print("\nIt's a Tie.")

    else:
        print("\nInvalid Choice. Please Enter Rock, Paper or Scissors.")

    user = input("\nDo You Want To Play Again? (Yes/No): ")

    if user.lower() == "yes":
        print("\nGame Restarting...\n")

    else:
        print("\nGame Ended.")
        print("Thank You For Playing.")
        break