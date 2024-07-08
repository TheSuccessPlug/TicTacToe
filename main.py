from helpers import print_board, check_turn, check_win
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
complete = False
turn = 0
while playing:
  os.system('cls' if os.name == 'nt' else 'clear')
  print_board(spots)
  if turn % 2 == 0:
    choice = input("Player 1: Which Spot?")
  else:
    choice = input("Player 2: Which Spot?")
  if choice == 'q':
    playing = False
  elif str.isdigit(choice) and int(choice) in spots:
    if not spots[int(choice)] in {"X", "O"}:
      turn += 1
      spots[int(choice)] = check_turn(turn)
    if check_win(spots): playing, complete = False, True 
    if turn > 8: playing = False
os.system('cls' if os.name == 'nt' else 'clear')
print_board(spots)

if complete:
  if check_turn(turn) == 'X': print("Player 1 Wins!")
  else: print("Player 2 Wins!")
else:
  print("No Winner")
  
  
    





#Establish Win recognition
#Establish if spot is taken
#Establish turn switching between players
#Establish Tie Game
