from kismetclient import Client
from kismetclient import handlers

class KismetInfo:
    screen1 = ['no data', 'no data'] # total networks
    screen2 = ['no data', 'no data'] # wpa total
    screen3 = ['no data', 'no data'] # wep total
    screen4 = ['no data', 'no data'] # no encryption total
    screen5 = ['no-data', 'no data'] # total wps
    total_networks = 0
    total_wpa = 0
    total_wep = 0
    total_none = 0
    total_wps = 0
    k = Client()
    aps = []

    def __init__(self, handler):
        k.register_handler(handler)
        self.refresh()

    def refresh(self):
        """
        Reparses the XML logfile and updates possible screens
        """
        self.screen1[0] = 'Total Networks: '
        self.screen1[1] = '%d' % self.total_networks
        self.screen2[0] = 'Total WPA: '
        self.screen2[1] = '%d' % self.total_wpa
        self.screen3[0] = 'Total WEP: '
        self.screen3[1] = '%d' % self.total_wep
        self.screen4[0] = 'Total with none: '
        self.screen4[1] = '%d' % self.total_none
        self.screen5[0] = 'Total WPS: '
        self.screen5[1] = '%d' % self.total_wps
