import wiringpi2 as wiringpi
from time import sleep

pinBase = 65
i2cAddr = 0x20
#Constants to make code less brain acre
HIGH = 1
LOW = 0
OUT = 1
IN = 0
LED1 = pinBase
LED2 = pinBase + 1
LED3 = pinBase + 2
LED4 = pinBase + 3
LED5 = pinBase + 4
LED6 = pinBase + 5
LED7 = pinBase + 6
LED8 = pinBase + 7
#leds = [LED1,LED2,LED3,LED4,LED5,LED6,LED7,LED8]
leds = [LED1,LED2,LED3]
IN1 = pinBase + 8
IN2 = pinBase + 9
IN3 = pinBase + 10
IN4 = pinBase + 11
IN5 = pinBase + 12
IN6 = pinBase + 13
IN7 = pinBase + 14
IN8 = pinBase + 15
#ins = [IN1,IN2,IN3,IN3,IN4,IN5,IN6,IN7,IN8]
ins = [IN1,IN2,IN3]
ROW1 = 0
ROW2 = 1
ROW3 = 2
ROW4 = 3
ROW5 = 4
ROW6 = 5
ROW7 = 6
ROW8 = 7
#rows = [ROW1,ROW2,ROW3,ROW4,ROW5,ROW6,ROW7,ROW8]
rows = [ROW1,ROW2,ROW3]
wiringpi.wiringPiSetup()
wiringpi.mcp23017Setup(pinBase,i2cAddr)
#Setup pin mode for LEDs AS OUTPUTS
wiringpi.pinMode(LED1,OUT)
wiringpi.pinMode(LED2,OUT)
wiringpi.pinMode(LED3,OUT)
wiringpi.pinMode(LED4,OUT)
wiringpi.pinMode(LED5,OUT)
wiringpi.pinMode(LED6,OUT)
wiringpi.pinMode(LED7,OUT)
wiringpi.pinMode(LED8,OUT)
#pull ups
wiringpi.pullUpDnControl(IN1,2)
wiringpi.pullUpDnControl(IN2,2)
wiringpi.pullUpDnControl(IN3,2)
wiringpi.pullUpDnControl(IN4,2)
wiringpi.pullUpDnControl(IN5,2)
wiringpi.pullUpDnControl(IN6,2)
wiringpi.pullUpDnControl(IN7,2)
wiringpi.pullUpDnControl(IN8,2)
#Set pin mode for ROWs as OUTPUT
wiringpi.pinMode(ROW1,OUT)
wiringpi.pinMode(ROW2,OUT)
wiringpi.pinMode(ROW3,OUT)
wiringpi.pinMode(ROW4,OUT)
wiringpi.pinMode(ROW5,OUT)
wiringpi.pinMode(ROW6,OUT)
wiringpi.pinMode(ROW7,OUT)
wiringpi.pinMode(ROW8,OUT)

#Set pin mode for INPUT Reeds
wiringpi.pinMode(IN1,IN)
wiringpi.pinMode(IN2,IN)
wiringpi.pinMode(IN3,IN)
wiringpi.pinMode(IN4,IN)
wiringpi.pinMode(IN5,IN)
wiringpi.pinMode(IN6,IN)
wiringpi.pinMode(IN7,IN)
wiringpi.pinMode(IN8,IN)

def ledAllOff():
  for pin in range(pinBase,pinBase + 7):
    wiringpi.digitalWrite(pin,HIGH)
  for pin in range(0,7):
    wiringpi.digitalWrite(pin,LOW)

def led(pos,flash):
  #Get a board position and convert
  #to a LED
  #example input a2
  #All off
  ledAllOff()
  #Get row
  aRow = pos[1]
  #Get column
  aCol = pos[0]
  #Set col to LOW
  if aCol == 'a':
    theLed = LED1
  if aCol == 'b':
    theLed = LED2
  if aCol == 'c':
    theLed = LED3
  if aCol == 'd':
    theLed = LED4
  if aCol == 'e':
    theLed = LED5
  if aCol == 'f':
    theLed = LED6
  if aCol == 'g':
    theLed = LED7
  if aCol == 'h':
    theLed = LED8

  #Set row to HIGH
  if aRow == '1':
    theRow = ROW1
  if aRow == '2':
    theRow = ROW2
  if aRow == '3':
    theRow = ROW3
  if aRow == '4':
    theRow = ROW4
  if aRow == '5':
    theRow = ROW5
  if aRow == '6':
    theRow = ROW6
  if aRow == '7':
    theRow = ROW7
  if aRow == '8':
    theRow = ROW8
  wiringpi.digitalWrite(theRow,HIGH)
  wiringpi.digitalWrite(theLed,LOW)
  if flash == True:
    sleep(0.5)
    wiringpi.digitalWrite(theLed,HIGH)
    sleep(0.5)
    wiringpi.digitalWrite(theLed,LOW)
    sleep(0.5)
    wiringpi.digitalWrite(theLed,HIGH)
       
def scanBoard():
  activePos = []
  #Put all rows HIGH
  for row in rows:
    wiringpi.digitalWrite(row,HIGH)
  #Loop each row
  for row in rows:
    wiringpi.digitalWrite(row,LOW)
    for swIn in ins:
      if not wiringpi.digitalRead(swIn):
        if row == ROW1:
          theRow = '1'
        if row == ROW2:
          theRow = '2'
        if row == ROW3:
          theRow = '3'
        if row == ROW4:
          theRow = '4'
        if row == ROW5:
          theRow = '5'
        if row == ROW6:
          theRow = '6'
        if row == ROW7:
          theRow = '7'
        if row == ROW8:
          theRow = '8'
        if swIn == IN1:
          theCol = 'a'
        if swIn == IN2:
          theCol = 'b'
        if swIn == IN3:
          theCol = 'c'
        if swIn == IN4:
          theCol = 'd'
        if swIn == IN5:
          theCol = 'e'
        if swIn == IN6:
          theCol = 'f'
        if swIn == IN7:
          theCol = 'g'
        if swIn == IN8:
          theCol = 'h'
        activePos.append(theCol+theRow)
        #led(theCol+theRow,True)
    wiringpi.digitalWrite(row,HIGH)
    
  return activePos
  
ledAllOff()
while True:
  ledToLight = scanBoard()
  for theLed in ledToLight:
    led(theLed,True)
  sleep(2)
