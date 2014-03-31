from lxml import etree

class KismetInfo:
    screen1 = ['no data', 'no data'] # total networks
    screen2 = ['no data', 'no data'] # wpa total
    screen3 = ['no data', 'no data'] # wep total
    screen4 = ['no data', 'no data'] # no encryption total
    screen5 = ['no-data', 'no data'] # total wps
    doc = None
    total_networks = 0
    total_wpa = 0
    total_wep = 0
    total_none = 0
    total_wps = 0
    root = None
    filename = ''
    last_index = 0

    def __init__(self, filename):
        self.filename = filename
        self.refresh()
        self.parse_xml()

    def parse_xml(self):
        self.doc = etree.parse(self.filename)
        self.root = doc.getroot()
        self.total_networks = len(root) - 1 # all children are networks except first one which is card info
        nodes = doc.findall('wireless-network/SSID/encryption') #TODO how to ignore multiple children?
        # for i in range(self.last_index, len(
        none = wep = wpa = wps = 0
        # TODO add in checking for WPS. need to do test run with kismet development version
        for node in nodes:
            if 'None' in node.text:
                none += 1
            elif 'WPA' in node.text:
                wpa += 1
            elif 'WEP' in node.text:
                wep += 1
        self.total_wep = wep
        self.total_wpa = wpa
        self.total_none = none
    def refresh(self):
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
