import argparse, sys, time
sys.path.append("/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from pi_kismet_display import KismetDisplay

HOLD_TIME = 3.0
REFRESH_TIME = 5.0
display = KismetDisplay()
lcd = display.lcd
prevCol = -1
prev = -1
lastTime = time.time()

parser = argparse.ArgumentParser(prog='KismetDisplay', version='1.0')
parser.add_argument('-f', '--filename', type=str, help='The XML log file from Kismet')
args = parser.parse_args()
if not args.filename:
    print 'Error: no file specified'
    exit(1)

display.init_info(args.filename)

def shutdown():
    lcd.clear()
    exit(0)

# Listen for button presses
while True:
    b = lcd.buttons()
    if b is not prev:
        if lcd.buttonPressed(lcd.SELECT):
            tt = time.time() # Start time of button press
            while lcd.buttonPressed(lcd.SELECT): # Wait for button release
                if (time.time() - tt) >= HOLD_TIME: # Extended hold?
                    shutdown() # We're outta here
            display.backlightStep()
        elif lcd.buttonPressed(lcd.LEFT):
                display.scrollRight()
        elif lcd.buttonPressed(lcd.RIGHT):
                display.scrollLeft()
        elif lcd.buttonPressed(lcd.UP):
                display.modeUp()
        elif lcd.buttonPressed(lcd.DOWN):
                display.modeDown()
        prev = b
        lastTime = time.time()
    else:
        now = time.time()
        since = now - lastTime
        if since > REFRESH_TIME or since < 0.0:
            display.update()
            lastTime = now
