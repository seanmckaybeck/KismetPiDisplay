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
        self.total_networks = len(doc.xpath('//wireless-network/SSID'))
        nodes = doc.xpath('//wireless-network/SSID/encryption[1]/text()')
        none = wep = wpa = wps = 0
        # TODO add in checking for WPS. need to do test run with kismet development version
        for text in nodes:
            if 'None' in text:
                none += 1
            elif 'WPA' in text:
                wpa += 1
            elif 'WEP' in text:
                wep += 1
        self.total_wep = wep
        self.total_wpa = wpa
        self.total_none = none
    def refresh(self):
        self.parse_xml()
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
