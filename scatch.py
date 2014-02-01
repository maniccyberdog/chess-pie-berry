def saveGameState(self,aFileName):
		"""
		Save game moves to file
		"""
		print "Saving game state"
		if len(self.gameMoves) > 0:
			#Have a game to save
			aFile = open(aFileName,'w')
			for aMove in self.gameMoves:
				aFile.write(aMove + "\n")
			aFile.Close()
		else:
			#No moves stored, nothing to save
			print "No game to save"
			