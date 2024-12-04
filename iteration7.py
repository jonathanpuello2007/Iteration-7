import random


runner = True
games_played = 0
games_won = 0
games_lost = 0
ties = 0

print("Let's play rock, paper, scissors")


def get_user_choice():
  while True:
    try:
      choice = input("Choose rock, paper, or scissors: ")
      if choice not in ["rock", "paper", "scissors"]:
       raise ValueError
    except ValueError:
      print("Please enter 'rock', 'paper', 'scissors'.")
    else:
      return choice

def get_computer_choice():
  choices = ["rock", "paper", "scissors"]
  cpu_choice = random.choice(choices)
  return cpu_choice

def determine_winner(user_choice, computer_choice, games_won, games_lost, ties):
  if user_choice == computer_choice:
    print("IT'S A TIE!")
    ties += 1

  elif (user_choice == "scissors" and computer_choice == "paper") or \
  (user_choice == "paper" and computer_choice == "rock") or \
  (user_choice =="rock" and computer_choice=="scissors"):
    print("You won")
    games_won +=1

  else:
    print("THE COMPUTER WINS")
    games_lost += 1

  return games_won, games_lost, ties


def scoreboard(games_played, games_won, games_lost, ties):
  print("==SCOREBOARD==")
  print(f"Games played : {games_played}")
  print(f"Games won: {games_won}")
  print(f"Games lost: {games_lost}")
  print(f"Tie games: {ties}")


def play_game(games_played, games_won, games_lost, ties):
  while True:
    user_choice = get_user_choice()
    games_played += 1
    computer_choice = get_computer_choice()
    print(f"The computer chose: {computer_choice}")
    games_won, games_lost, ties = determine_winner(user_choice, computer_choice, games_won, games_lost, ties)
    scoreboard(games_played, games_won, games_lost, ties)
    choice = input("Do you want to play again (y/n)?: ")
    if choice == "y":

        continue
    if user_choice == "n":

        print("Invalid input. Please check what is wrong.")

    else:
        break



play_game(games_played, games_won, games_lost, ties)

 
