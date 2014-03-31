KismetPiDisplay
=============

These scripts display information from a Kismet XML log file during a wardrive on the Adafruit LCD for the Raspberry Pi. The more mobile your wardriving setup the better, so why not use a Pi? Carrying around a monitor with your Pi is not ideal so we can use an LCD to display information about gathered networks during the wardrive.

The script will start by displaying the total number of networks discovered thus far. By pressing the `UP` or `DOWN` buttons you can cycle between the other screens. The `LEFT` and `RIGHT` buttons scroll the text on the screen left or right. The other information that is displayed is the total number of networks using `WPA`, `WEP`, or no encryption. 

Eventually this script will also display information on discovered networks using `WPS`. This requires using the development version of Kismet. 

## Installation

This code requires that Adafruit's [Raspberry Pi Python Code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code) be installed in your home directory on the Raspberry Pi. It really only needs the `Adafruit_CharLCDPlate` directory so you can get rid of the rest of the subdirectories if you want. 

You should be using Python 2.7+ since the code uses the `argparse` module. It also requires `lxml` be installed. You can install that via pip. 

## Usage

This script should be run after starting Kismet. You provide it with the XML log file and it will parse it every 5 seconds. 

> python pi_kismet.py -f /path/to/logfile.netxml

To stop the script hold the `SELECT` key on the LCD plate for 3 seconds and the script will stop parsing and displaying information. 

## Licensing

This project uses some code from Adafruit's [PiMiner](https://github.com/adafruit/PiMiner) and as such this project is licensed under GPLv3 like PiMiner. 
