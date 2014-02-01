import wiringpi2 as wiringpi
from time import sleep


class McpChessBoard:
   """
   Main Class for control of hardware chessboard
   using the Microchip MCP23017 chip
   and wiringpi2 plus some gpios on the raspi
   """
  def __init__(self):
    """
    Setup ports and pin names
    """
    self.wiringpi = wiringpi
    self.pinBase = 65
    self.i2cAddr = 0x20
    #Constants to make code less brain acre
    self.HIGH = 1
    self.LOW = 0
    self.OUT = 1
    self.IN = 0
    self.LED1 = self.pinBase
    self.LED2 = self.pinBase + 1
    self.LED3 = self.pinBase + 2
    self.LED4 = self.pinBase + 3
    self.LED5 = self.pinBase + 4
    self.LED6 = self.pinBase + 5
    self.LED7 = self.pinBase + 6
    self.LED8 = self.pinBase + 7
    #leds = [LED1,LED2,LED3,LED4,LED5,LED6,LED7,LED8]
    self.leds = [self.LED1,self.LED2,self.LED3]
    self.IN1 = self.pinBase + 8
    self.IN2 = self.pinBase + 9
    self.IN3 = self.pinBase + 10
    self.IN4 = self.pinBase + 11
    self.IN5 = self.pinBase + 12
    self.IN6 = self.pinBase + 13
    self.IN7 = self.pinBase + 14
    self.IN8 = self.pinBase + 15
    #ins = [IN1,IN2,IN3,IN3,IN4,IN5,IN6,IN7,IN8]
    self.ins = [self.IN1,self.IN2,self.IN3]
    self.ROW1 = 0
    self.ROW2 = 1
    self.ROW3 = 2
    self.ROW4 = 3
    self.ROW5 = 4
    self.ROW6 = 5
    self.ROW7 = 6
    self.ROW8 = 7
    #rows = [ROW1,ROW2,ROW3,ROW4,ROW5,ROW6,ROW7,ROW8]
    self.rows = [self.ROW1,self.ROW2,self.ROW3]
    self.wiringpi.wiringPiSetup()
    self.wiringpi.mcp23017Setup(self.pinBase,self.i2cAddr)
    #Setup pin mode for LEDs AS OUTPUTS
    self.wiringpi.pinMode(self.LED1,self.OUT)
    self.wiringpi.pinMode(self.LED2,self.OUT)
    self.wiringpi.pinMode(self.LED3,self.OUT)
    self.wiringpi.pinMode(self.LED4,self.OUT)
    self.wiringpi.pinMode(self.LED5,self.OUT)
    self.wiringpi.pinMode(self.LED6,self.OUT)
    self.wiringpi.pinMode(self.LED7,self.OUT)
    self.wiringpi.pinMode(self.LED8,self.OUT)
    #pull ups
    self.wiringpi.pullUpDnControl(self.IN1,2)
    self.wiringpi.pullUpDnControl(self.IN2,2)
    self.wiringpi.pullUpDnControl(self.IN3,2)
    self.wiringpi.pullUpDnControl(self.IN4,2)
    self.wiringpi.pullUpDnControl(self.IN5,2)
    self.wiringpi.pullUpDnControl(self.IN6,2)
    self.wiringpi.pullUpDnControl(self.IN7,2)
    self.wiringpi.pullUpDnControl(self.IN8,2)
    #Set pin mode for ROWs as OUTPUT
    self.wiringpi.pinMode(self.ROW1,self.OUT)
    self.wiringpi.pinMode(self.ROW2,self.OUT)
    self.wiringpi.pinMode(self.ROW3,self.OUT)
    self.wiringpi.pinMode(self.ROW4,self.OUT)
    self.wiringpi.pinMode(self.ROW5,self.OUT)
    self.wiringpi.pinMode(self.ROW6,self.OUT)
    self.wiringpi.pinMode(self.ROW7,self.OUT)
    self.wiringpi.pinMode(self.ROW8,self.OUT)

    #Set pin mode for INPUT Reeds
    self.wiringpi.pinMode(self.IN1,self.IN)
    self.wiringpi.pinMode(self.IN2,self.IN)
    self.wiringpi.pinMode(self.IN3,self.IN)
    self.wiringpi.pinMode(self.IN4,self.IN)
    self.wiringpi.pinMode(self.IN5,self.IN)
    self.wiringpi.pinMode(self.IN6,self.IN)
    self.wiringpi.pinMode(self.IN7,self.IN)
    self.wiringpi.pinMode(self.IN8,self.IN)
    self.storedPositions = []
    print "MCP Board Initilized..."
  def ledAllOff(self):
    """
    Turn all LEDs off
    """
    for pin in range(self.pinBase,self.pinBase + 7):
      self.wiringpi.digitalWrite(pin,self.HIGH)
    for pin in range(0,7):
      self.wiringpi.digitalWrite(pin,self.LOW)

  def led(self,pos,flash,quick):
    """
    Get a board position and convert
    to a LED
    example input a2,True,True  = flash a2 quick
    """
    self.ledAllOff()
    #Get row
    aRow = pos[1]
    #Get column
    aCol = pos[0]
    #Set col to LOW
    if aCol == 'a':
      theLed = self.LED1
    if aCol == 'b':
      theLed = self.LED2
    if aCol == 'c':
      theLed = self.LED3
    if aCol == 'd':
      theLed = self.LED4
    if aCol == 'e':
      theLed = self.LED5
    if aCol == 'f':
      theLed = self.LED6
    if aCol == 'g':
      theLed = self.LED7
    if aCol == 'h':
      theLed = self.LED8

    #Set row to HIGH
    if aRow == '1':
      theRow = self.ROW1
    if aRow == '2':
      theRow = self.ROW2
    if aRow == '3':
      theRow = self.ROW3
    if aRow == '4':
      theRow = self.ROW4
    if aRow == '5':
      theRow = self.ROW5
    if aRow == '6':
      theRow = self.ROW6
    if aRow == '7':
      theRow = self.ROW7
    if aRow == '8':
      theRow = self.ROW8
    self.wiringpi.digitalWrite(theRow,self.HIGH)
    self.wiringpi.digitalWrite(theLed,self.LOW)
    if quick == True:
      flashTime = 0.2
    else:
      flashTime = 0.5
    if flash == True:
      sleep(flashTime)
      self.wiringpi.digitalWrite(theLed,self.HIGH)
      sleep(flashTime)
      self.wiringpi.digitalWrite(theLed,self.LOW)
      sleep(flashTime)
      self.wiringpi.digitalWrite(theLed,self.HIGH)
       
  def scanBoard(self):
    """
    Scan the matrix and return position
    """
    activePos = []
    #Put all rows HIGH
    for row in self.rows:
      self.wiringpi.digitalWrite(row,self.HIGH)
    #Loop each row
    for row in self.rows:
      self.wiringpi.digitalWrite(row,self.LOW)
      for swIn in self.ins:
        if not wiringpi.digitalRead(swIn):
          if row == self.ROW1:
            theRow = '1'
          if row == self.ROW2:
            theRow = '2'
          if row == self.ROW3:
            theRow = '3'
          if row == self.ROW4:
            theRow = '4'
          if row == self.ROW5:
            theRow = '5'
          if row == self.ROW6:
            theRow = '6'
          if row == self.ROW7:
            theRow = '7'
          if row == self.ROW8:
            theRow = '8'
          if swIn == self.IN1:
            theCol = 'a'
          if swIn == self.IN2:
            theCol = 'b'
          if swIn == self.IN3:
            theCol = 'c'
          if swIn == self.IN4:
            theCol = 'd'
          if swIn == self.IN5:
            theCol = 'e'
          if swIn == self.IN6:
            theCol = 'f'
          if swIn == self.IN7:
            theCol = 'g'
          if swIn == self.IN8:
            theCol = 'h'
          activePos.append(theCol+theRow)
          #led(theCol+theRow,True)
      self.wiringpi.digitalWrite(row,self.HIGH)
    
    return activePos


  def scanMCPBoard(self):
    """
    scan and return a list of activated reeds switches
    """
    return self.scanBoard()
  def ledMCPBoardMove(self,theLed):
    """
    Quick flash the LED toshow movement
    """
    self.led(theLed, True, True)

  def ledMCPBoard(self,theLed, flash, quick):
    """
    set theLed to on
    set flash to true or false to flash LED
    """
    self.led(theLed, flash, quick)
  
  def storeMCPBoard(self):
    """
    Store the current on reed switches
    """
    self.storedPositions = self.scanBoard()
    
  def compareMCPBoard(self,theList):
    """
    Compare the stored positions with theList
    and return the status of the compare
    add - piece added will show positions
    rem - piece removed will show position
    err - an error will report the error
    nom - no movement
    """
    sizeOfStored = len(self.storedPositions)
    sizeOfTheList = len(theList)
    changesToBoard = []
    returnedValue = []
    #If stored larger piece removed
    if sizeOfStored > sizeOfTheList:
      returnedValue.append('rem')
      for item in self.storedPositions:
        if item not in theList:
          changesToBoard.append(item)
    #If stored smaller piece added
    if sizeOfTheList > sizeOfStored:
      returnedValue.append('add')
      for item in theList:
        if item not in self.storedPositions:
          changesToBoard.append(item)
    #If the same size make sure positions have not changed
    if sizeOfTheList == sizeOfStored:
      for item in self.storedPositions:
        if item not in theList:
          changesToBoard.append(item)
      for item in theList:
        if item not in self.storedPositions:
          changesToBoard.append(item)
      if changesToBoard != []:
        #list size the same but we have changes - ERROR
        returnedValue.append('err')
        returnedValue.append('Looks like an error - McpBoard.py - list size same, but has movment')
      else:
        #lists the same zize and no movment
        returnedValue.append('nom')

    if changesToBoard != []:
      #Append the movment list
      returnedValue.append(changesToBoard)
    #Return list with status as first element and movment as second
    return returnedValue
