from Adafruit_CharLCDPlate impoer Adafruit_CharLCDPlate
from pi_kismet_info import KismetInfo

class KismetDisplay:
    lcd = Adafruit_CharLCDPlate()
    mode = 1
    screen = []
    col = []
    prevCol = 0
    info = None

    def __init__(self):
        self.lcd.clear()
        self.col = (self.lcd.ON,   self.lcd.OFF, self.lcd.YELLOW, self.lcd.OFF,
                    self.lcd.GREEN, self.lcd.OFF, self.lcd.TEAL,   self.lcd.OFF,
                    self.lcd.BLUE,  self.lcd.OFF, self.lcd.VIOLET, self.lcd.OFF,
                    self.lcd.RED,    self.lcd.OFF)
        self.lcd.backlight(self.col[self.prevCol])
