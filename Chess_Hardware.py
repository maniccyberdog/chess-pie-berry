
#Used to test Hardware and movment
#Hardware Test Program
import McpBoard
from time import sleep

#Init the hardware
theBoard = McpBoard.McpChessBoard()
theBoard.ledAllOff()


def boardMove(aPlayer):
  """
  Board movement and logic 
  aPlayer - Computer or Player
  returns the location of the move
  """
  #Start with waiting for remove
  movementState = 'r'
  
  while movementState != 'e':
    #Store the current board posistions
    theBoard.storeMCPBoard()
    if movementState == 'r':
      print aPlayer + " to move..."
    else:
      print aPlayer + " to place"
    status = ['nom']
    #wait for a move
    while status[0] == 'nom':
      currentList = theBoard.scanMCPBoard()
      status = theBoard.compareMCPBoard(currentList)
      sleep(0.25) #scan every 0.5 second
    #print the move
    #print status[1]
    if status[0] == 'rem':
      if movementState == 'r':
        if len(status[1]) == 1: #only one piece moved
          #removed and in correct state
          theBoard.ledMCPBoardMove(status[1][0]) #flash led
          fromMove = status[1][0] # store the move
          #Set to next state for movement
          movementState = 'p' #place
        else:
          print "more than one piece moved"
      else:
        print "moved - not in correct state"
    if status[0] == 'add':
      if movementState == 'p':
        if len(status[1]) == 1: #only one piece moved
          #added and in correct state
          theBoard.ledMCPBoardMove(status[1][0]) #flash led
          toMove = status[1][0] #store the move
          #set to next state
          movementState = 'e'
        else:
          print "more than one piece added"
      else:
        print "placed - not in correct state"
  return (fromMove,toMove)


#Main program
while True:
  print boardMove('Player')
  print boardMove('Pi')
