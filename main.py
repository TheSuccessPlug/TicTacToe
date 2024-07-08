from helpers import print_board
import os

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
while playing:
  os.system('cls' if os.name == 'nt' else 'clear')
  print_board(spots)
  choice = input("Player 1: Which Spot?")
  if choice == 'q':
    playing = False
  elif choice == '1':
    spots[1] = 'X'
  elif choice == '2' :
    spots[2] = 'X'
  elif ask_player == '3':
    spots[3] = 'X'
  elif ask_player == '4':
    spots[4] = 'X'
  elif ask_player == '5':
    spots[5] = 'X'
  elif ask_player == '6':
    spots[6] = 'X'
  elif ask_player == '7':
    spots[7] = 'X'
  elif ask_player == '8':
    spots[8] = 'X'
  elif ask_player == '9':
    spots[9] = 'X'
  
    





#Establish Win recognition
#Establish if spot is taken
#Establish turn switching between players
#Establish Tie Game
