import subprocess
class StockFishEng:
    def __init__(self):
        """
        Create a connection to the
        stockfish engine ready to process commands
        """
        print "Stockfish Engine Init"
		#Pi path for stockfish /usr/games/stockfish
        self.engine = subprocess.Popen("/usr/games/stockfish",universal_newlines=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,)
        print "Connected to stockfish as subprocess"

    def get(self):
        self.engine.stdin.write('isready\n')
        #Wait for reply
        waiting = True
        while waiting:
            stdText = self.engine.stdout.readline().strip()
            if stdText == 'readyok':
                waiting = False #Exit while
            
            #Any other text just echo to console
            if stdText != '':
                dummy = stdText #Just do something maybe able to remove 
                #print "Stockfish:" + stdText
                #waiting = False - Dont think I need to exit loop until readyok
                
        return stdText        
    def sget(self):
        self.engine.stdin.write('isready\n')
        #Wait for reply
        waiting = True
        while waiting:
            stdText = self.engine.stdout.readline().strip()
            #Any other text just echo to console
            if stdText != '':
                #Maybe able to remove these dummy lines
                #Just used to get output to console
                dummy = stdText
                #print "Stockfish:" + stdText
                #waiting = False - Dont think I need to exit loop until readyok
            if stdText[0:8] == 'bestmove':
                waiting = False    
        return stdText        
                
    def put(self,command):
        #print('\nyou:\n\t'+command)
        self.engine.stdin.write(command+'\n')
        
    def setUpForNewGame(self, skillLevel):
        self.get ()
        self.put('uci')
        self.get ()
        self.put('setoption name Skill Level value ' + skillLevel)
        self.get ()
        self.put('setoption name Hash value 128')
        self.get()
        self.put('setoption name Best Book Move value true')
        self.get()
        self.put('setoption name OwnBook value true')
        self.get()
        self.put('uci')
        self.get ()
        self.put('ucinewgame')
        self.get ()
    def sendMoves(self, theMoves, moveTime,startPos):
        """
        send moves as a string list to engine
        """
        print "Thinking..."
        cmdMoves = "position " + startPos + " moves" + theMoves
        #Send full list of moves to engine
        self.put(cmdMoves)
        self.put("go movetime " + moveTime)
        engBestMove = self.sget()
        return engBestMove      
        
