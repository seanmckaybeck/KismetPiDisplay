from Adafruit_CharLCDPlate impoer Adafruit_CharLCDPlate
from pi_kismet_info import KismetInfo

class KismetDisplay:
    lcd = Adafruit_CharLCDPlate()
    mode = 1
    screen = []
    col = []
    prevCol = 0
    offset = 0
    maxOffset = 0
    info = None

    def __init__(self):
        self.lcd.clear()
        self.col = (self.lcd.ON,   self.lcd.OFF, self.lcd.YELLOW, self.lcd.OFF,
                    self.lcd.GREEN, self.lcd.OFF, self.lcd.TEAL,   self.lcd.OFF,
                    self.lcd.BLUE,  self.lcd.OFF, self.lcd.VIOLET, self.lcd.OFF,
                    self.lcd.RED,    self.lcd.OFF)
        self.lcd.backlight(self.col[self.prevCol])

    def display_screen(self, new_screen):
        self.screen = new_screen
        try:
            self.maxOffset = max((len(self.screen[0]) - 16), (len(self.screen[1]) - 16))
            self.lcd.clear()
            s = self.screen[0] + '\n' + self.screen[1]
            self.lcd.message(s)
        except TypeError:
            self.lcd.clear()
            self.lcd.message('error\ndisplaying details ...')


    def init_info(self, filename):
        self.info = KismetInfo(filename)
        self.display_total()

    def display_total(self):
        self.display_screen(self.info.screen1)

    def display_wpa(self):
        self.display_screen(self.info.screen2)

    def display_wep(self):
        self.display_screen(self.info.screen3)

    def display_none(self):
        self.display_screen(self.info.screen4)

    def display_wps(self):
        self.display_screen(self.info.screen5)
        
    # the code below this line is taken directly from PiMinerDisplay
    # except for the changes made to update()

    #Cycle Backlight Color / On/Off
    def backlightStep(self):
        if self.prevCol is (len(self.col) -1): self.prevCol = -1
        newCol = self.prevCol + 1
        self.lcd.backlight(self.col[newCol])
        self.prevCol = newCol
    
    #Offset text to the right
    def scrollLeft(self):
        if self.offset >= self.maxOffset: return
        self.lcd.scrollDisplayLeft()
        self.offset += 1
    
    #Offset text to the left
    def scrollRight(self):
        if self.offset <= 0: return
        self.lcd.scrollDisplayRight()
        self.offset -= 1
    
    #Display next info screen
    def modeUp(self):
        self.mode += 1
        if self.mode > 4: self.mode = 0
        self.update()
    
    #Display previous info screen
    def modeDown(self):
        self.mode -= 1
        if self.mode < 0: self.mode = 4
        self.update()
    
    #Update display
    def update(self):
        self.info.refresh()
        if self.mode == 0: self.display_total()
        elif self.mode == 1: self.display_wpa()
        elif self.mode == 2: self.display_wep()
        elif self.mode == 3: self.display_none()
        elif self.mode == 4: self.display_wps()
