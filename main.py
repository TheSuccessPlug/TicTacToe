from helpers import print_board

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
while playing:
  print_board(spots)
  choice = input()
  if choice == 'q':
    playing = False

#Establish Player Moves
#Establish Win recognition
#Establish if spot is taken
#Establish turn switching between players
#Establish Tie Game