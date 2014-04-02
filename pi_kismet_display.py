from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
# from pi_kismet_info import KismetInfo

class KismetDisplay:
    lcd = Adafruit_CharLCDPlate()
    mode = 0
    screen = []
    col = []
    prevCol = 0
    offset = 0
    maxOffset = 0
    # info = None
    screen1 = ['no data', 'no data']
    screen2 = ['no data', 'no data']
    screen3 = ['no data', 'no data']
    screen4 = ['no data', 'no data']
    screen5 = ['no data', 'no data']

    def __init__(self):
        self.lcd.clear()
        self.col = (self.lcd.ON,   self.lcd.OFF, self.lcd.YELLOW, self.lcd.OFF,
                    self.lcd.GREEN, self.lcd.OFF, self.lcd.TEAL,   self.lcd.OFF,
                    self.lcd.BLUE,  self.lcd.OFF, self.lcd.VIOLET, self.lcd.OFF,
                    self.lcd.RED,    self.lcd.OFF)
        self.lcd.backlight(self.col[self.prevCol])

    def display_screen(self, new_screen):
        """
        A general function for displaying a specified screen

        new_screen is a list with two elements to be displayed
        """
        self.screen = new_screen
        try:
            self.maxOffset = max((len(self.screen[0]) - 16), (len(self.screen[1]) - 16))
            self.lcd.clear()
            s = self.screen[0] + '\n' + self.screen[1]
            self.lcd.message(s)
        except TypeError:
            self.lcd.clear()
            self.lcd.message('error\ndisplaying details ...')

    def update_screens(self, wpa, wep, wps, none, total):
        self.screen1[0] = 'Total Networks: '
        self.screen1[1] = '%d' % total
        self.screen2[0] = 'Total WPA: '
        self.screen2[1] = '%d' % wpa
        self.screen3[0] = 'Total WEP: '
        self.screen3[1] = '%d' % wep
        self.screen4[0] = 'Total with none: '
        self.screen4[1] = '%d' % none
        self.screen5[0] = 'Total WPS: '
        self.screen5[1] = '%d' % wps

    # def init_info(self):
    #     """
    #     Initializes the KismetInfo member variable

    #     filename is the log file from Kismet that will be parsed for data
    #     """
    #     self.info = KismetInfo()
    #     self.display_total()

    def display_total(self):
        """
        Displays the total number of networks discovered
        """
        self.display_screen(self.screen1)

    def display_wpa(self):
        """
        Displays the total number of networks using WPA
        """
        self.display_screen(self.screen2)

    def display_wep(self):
        """
        Displays the total number of networks using WEP
        """
        self.display_screen(self.screen3)

    def display_none(self):
        """
        Displays the total number of networks with no encryption
        """
        self.display_screen(self.screen4)

    def display_wps(self):
        """
        Displays the total number of networks using WPS
        """
        self.display_screen(self.screen5)
        
    # the code below this line is taken directly from PiMinerDisplay
    # except for the changes made to update()

    def backlightStep(self):
        """
        Cycles the backlight color on/off
        """
        if self.prevCol is (len(self.col) -1): self.prevCol = -1
        newCol = self.prevCol + 1
        self.lcd.backlight(self.col[newCol])
        self.prevCol = newCol
    
    def scrollLeft(self):
        """
        Offsets the text to the right
        """
        if self.offset >= self.maxOffset: return
        self.lcd.scrollDisplayLeft()
        self.offset += 1
    
    def scrollRight(self):
        """
        Offsets the text to the left
        """
        if self.offset <= 0: return
        self.lcd.scrollDisplayRight()
        self.offset -= 1
    
    def modeUp(self):
        """
        Displays the next info screen on up button push
        """
        self.mode += 1
        if self.mode > 4: self.mode = 0
        self.update()
    
    def modeDown(self):
        """
        Displays the prior info screen on down button push
        """
        self.mode -= 1
        if self.mode < 0: self.mode = 4
        self.update()
    
    def update(self):
        """
        Updates the display based on the mode
        """
        # self.info.refresh()
        if self.mode == 0: self.display_total()
        elif self.mode == 1: self.display_wpa()
        elif self.mode == 2: self.display_wep()
        elif self.mode == 3: self.display_none()
        elif self.mode == 4: self.display_wps()
