import StockfishEng
import Gamestate


class MainGame:
	def __init__(self,aSkillLevel,aMoveTime):
		print "Game start"
		#Set skill level and move time to start up values
		self.skillLevel = aSkillLevel
		self.moveTime = aMoveTime
		self.chessEng = StockfishEng.StockFishEng()
		#Setup the game pass skill level and movetime
		self.theGame = Gamestate.GameState(self.skillLevel,self.moveTime)
		self.chessEng.setUpForNewGame(self.theGame.getSkillLevel())
		self.running = True
		
	def showHelp(self):
		"""
		Show current command list
		Used so that I don't forget what I've done while testing
		"""
		print "q - Quit the program"
		print "u - Undo last player move"
		print "txxxx - Change move time from 1000 ->"
		print "kxx - Change skill level 01 - 99 (must be two chars)"
		print "sxxxxxx - Save game where xxxxxx is the file name"
		print "lxxxxxx - Load game where xxxxxx is the file name"
		print "fxxxxxx - Load fen string where xxxxxx is the file name"
		print "h - show this help"
	def execCommand(self,theCommand):
		"""
		Execute a command.  First char is the command type followed
		by data for that command if needed.
		"""
		if theCommand[0] == 'q':
			#Quit Program
			self.running = False
		elif theCommand[0] == 'u':
			#Undo last player move
			self.theGame.undoMove()
		elif theCommand[0] == 'n':
			#Start new game
			self.resetGame()
		elif theCommand[0] == 'k':
			#Change skill level
			#next two chars will be skill level 01 - 99
			aSkillLevel = theCommand[1:3]
			self.changeSkill(aSkillLevel)
		elif theCommand[0] == 't':
			#Change move time
			#A normal value seems to be 6000
			aMoveTime = theCommand[1:6]
			self.changeMoveTime(aMoveTime)
		elif theCommand[0] == 'h':
			self.showHelp()
		elif theCommand[0] == 's':
			#File name length fixed for the moment to 6 chars
			aFileName = theCommand[1:8]
			self.saveGame(aFileName)
		elif theCommand[0] == 'l':
			aFileName = theCommand[1:8]
			self.loadGame(aFileName)
		elif theCommand[0] == 'f':
			aFileName = theCommand[1:8]
			self.loadFen(aFileName)
		elif theCommand[0] == 'p':
			self.findPiece(theCommand[1:3])
			
	def findPiece(self,thePiece):
		self.theGame.findLocation(thePiece)

	def changeMoveTime(self,aMoveTime):
		#don't work with any value less than 1000
		if aMoveTime < 1000:
			aMoveTime = 1000
		self.moveTime = aMoveTime
		#and reset the game
		self.resetGame()
		
	def changeSkill(self,aSkillLevel):
		#Test for a zero in first char
		if aSkillLevel[0] == '0':
			aSkillLevel = aSkillLevel[1]
		self.skillLevel = aSkillLevel
		#Now reset the game
		self.resetGame()
	def resetGame(self):
		"""
		Reset the game to start position
		"""
		print "Game Reset using skill level:" + str(self.skillLevel) + " and move time:" + str(self.moveTime)
		self.theGame = None
		self.theGame = Gamestate.GameState(self.skillLevel,self.moveTime)
		self.chessEng.setUpForNewGame(self.theGame.getSkillLevel())
		
	def loadGame(self,aFileName):
		"""
		Load Game from file, reset game first
		"""
		self.resetGame()
		self.theGame.loadGameState(aFileName)
		print "Game State Loaded"
		
	def loadFen(self,aFileName):
		"""
		Load fen from file
		"""
		self.resetGame()
		self.theGame.loadFen(aFileName)
	def saveGame(self,aFileName):
		"""
		Safe game to file using the filename given
		"""
		self.theGame.saveGameState(aFileName)
	def runGame(self):		
		while self.running:
			textInput = raw_input("\n Enter message: ")
			if len(textInput) != 4:
				#if input is not four chars it we be a command
				#program command
				self.execCommand(textInput)
			else:
				if self.theGame.addMove(textInput) != "xxxx":
					#Game move good
					print "Valid move"
					#print theGame.getMoveList()
					#Get move from engine
					engMove = self.chessEng.sendMoves(self.theGame.getMoveList(),self.theGame.getMoveTime(),self.theGame.getStartPos())
					#Will return a long string chop it down
					engHint = engMove[21:25] #get ponder, think this is a hint
					engMove = engMove[9:13] #get engines move
					#Add the engines move to the game
					if self.theGame.addMove(engMove) != "xxxx":
						#Should always be a valid move from the engine
						print "Pi move:" + engMove
					else:
					   #Engine has a problem
					   print "Error in move from engine:" + engMove
				else:
					#bad move
					print "You have given the game a bad move!"
					#Deal with this!
		
aGameOfChess = MainGame(1,6000)
aGameOfChess.runGame()	