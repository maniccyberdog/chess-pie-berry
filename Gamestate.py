from ChessBoard import ChessBoard

class GameState:
    def __init__(self,aSkillLevel,aMoveTime):
        """
        Create an object to hold the game state
        Use Chessboard library for logic
        """
        print "Game State Initilized"
        self.chessGame = ChessBoard()
        self.chessGame.resetBoard()
        self.chessGame.printBoard()
        self.moveTime = aMoveTime #Used to store movetime
        self.skillLevel = aSkillLevel #Used to store skill level
        self.gameMoves = [] #Used to store all moves in game
        self.saveFileExt = ".txt"
        self.saveFilePath = ""
        self.startPos = "startpos" #Used to store the start position or fen string

    def loadGameState(self,aFileName):
        """
        Load from file, game should be reset first
        """
        if len(self.gameMoves) == 0:
            #Game moves must be empty to load game
            try:
                aFile = open(self.saveFilePath + aFileName + self.saveFileExt,'r')
                for aLine in aFile:
                    if aLine[0] != '#':
                        self.gameMoves.append(aLine[0:4])
                        self.chessGame.addTextMove(aLine)
                aFile.close()
                #Show moves
                self.chessGame.printBoard()
            except IOError:
                print "File Error"
        else:
            #Game moves not empty
            print "Can't load game, has it been reset?"

    def loadFen(self,aFileName):
        """
        Load from file, game should be reset first
        """
        if len(self.gameMoves) == 0:
            #Game moves must be empty to load game
            try:
                fenInstruc = ""
                aFile = open(self.saveFilePath + aFileName + self.saveFileExt,'r')
                for aLine in aFile:
                    if aLine[0] == '$':
                        removeChar = aLine.strip('$') #remove the first char
                        removeChar = removeChar.strip('\n')
                        fenInstruc = fenInstruc + removeChar + " " #build any instructions for game
                    if aLine[0] == '!':
                        fenLine = aLine #found line with fen code
                        fenLine = fenLine.strip('!')
                        
                aFile.close()
                #Load fen line on to game board
                self.chessGame.setFEN(fenLine)
                print fenInstruc
                self.chessGame.printBoard()
                self.startPos = "fen " + fenLine #set startpos to fen line
            except IOError:
                print "File Error"
        else:
            #Game moves not empty
            print "Can't load FEN file, has it been reset?"

    def saveGameState(self,aFileName):
        """
        Save game moves to file
        """
        print "Saving game state"
        if len(self.gameMoves) > 0:
            #Have a game to save
            aFile = open(self.saveFilePath + aFileName + self.saveFileExt,'w')
            for aMove in self.gameMoves:
                aFile.write(aMove + "\n")
            aFile.close()
        else:
            #No moves stored, nothing to save
            print "No game to save"

    def getSkillLevel(self):
        """
        Return game state skill level as a string
        """
        return str(self.skillLevel)

    def getMoveTime(self):
        """
        Return movetime as a string
        """
        return str(self.moveTime)
    def getMoveList(self):
        """
        Return moves in list as a string 
        """
        moveString = ""
        for aMove in self.gameMoves:
            moveString = moveString + " " + aMove
        return moveString

    def addMove(self,chessMove):
        """
        Add chess move to game state 
        """
        theMove = chessMove.lower()
        if self.chessGame.addTextMove(theMove) == False:
            #Invalid move
            errorText = "Error in GameState:" + str(self.chessGame.getReason()) + " " + theMove
            print errorText
            self.chessGame.printBoard()
            theMove = "xxxx" #return something to catch if the move had an error
        else:
            #Move OK
            self.chessGame.printBoard()
            #Add the move to the list of moves for this game
            self.gameMoves.append(theMove)
        return theMove    
    def undoMove(self):
        """
        Undo the last move.  Will need to undo last two moves
        as the last move will be the engine's and then the players
        """
        if len(self.gameMoves) > 1:
            self.gameMoves.pop()
            self.gameMoves.pop()
            self.chessGame.undo()
            self.chessGame.undo()
            self.chessGame.printBoard()
            print "Last move undo"
        else:
            print "No moves to undo!"
    def getStartPos(self):
        """
        Return the current start positionof the game
        this will be 'startpos' or fen <some fen string>
        """
        return self.startPos
    def findLocation(self,aPiece):
        """
        Find the location of a Piece orPieces
        """
        pieceList = []
        rowNumber = 8
        theBoard = self.chessGame.getBoard()
        for eachRow in theBoard:
            columnNumber = 1
            for piece in eachRow:
                if piece == aPiece:
                    value = self.colToLetter(columnNumber) + str(rowNumber)
                    pieceList.append(value)
                columnNumber = columnNumber + 1
            rowNumber = rowNumber - 1 #rows inverted to match a chess board
        print pieceList
    def colToLetter(self,aNumber):
        """
        Convert column number to a letter
        """
        letter =""
        if aNumber == 1: letter = 'A'
        elif aNumber == 2: letter = 'B'
        elif aNumber == 3: letter = 'C'
        elif aNumber == 4: letter = 'D'
        elif aNumber == 5: letter = 'E'
        elif aNumber == 6: letter = 'F'
        elif aNumber == 7: letter = 'G'
        elif aNumber == 8: letter = 'H'
        return letter