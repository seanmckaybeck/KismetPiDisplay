KismetPiDisplay
=============

These scripts display information from a Kismet XML log file during a wardrive on the Adafruit LCD for the Raspberry Pi. The more mobile your wardriving setup the better, so why not use a Pi? Carrying around a monitor with your Pi is not ideal so we can use an LCD to display information about gathered networks during the wardrive.

The script will start by displaying the total number of networks discovered thus far. By pressing the `UP` or `DOWN` buttons you can cycle between the other screens. The `LEFT` and `RIGHT` buttons scroll the text on the screen left or right. The other information that is displayed is the total number of networks using `WPA`, `WEP`, or no encryption. 

Eventually this script will also display information on discovered networks using `WPS`. This requires using the development version of Kismet. 

## Installation

This code requires that Adafruit's [Raspberry Pi Python Code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code) be installed in your home directory on the Raspberry Pi.

You should be using Python 2.7+ since the code uses the `argparse` module. It also requires `lxml` be installed. You can install that via pip. 

### Complete Guide

For those who are new to this, here is how to set everything up on your Pi. This requires a wireless card that supports monitor mode. I use the Alfa `AWUS036H`. This also assumes you are using `Raspbian` as your OS. 

Use the following commands to install the necessities. 

```
sudo apt-get update
sudo apt-get install libssl-dev
wget http://download.aircrack-ng.org/aircrack-ng-1.2-beta1.tar.gz
tar -zxvf aircrack-ng-1.2-beta1.tar.gz
cd aircrack-ng-1.2-beta1
make && sudo make install
sudo airodump-ng-oui-update
sudo apt-get -y install iw kismet python-dev python-smbus libxml2-dev libxslt-dev
curl -O http://python-distribute.org/distribute_setup.py
sudo python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
sudo python get-pip.py
sudo pip install lxml
```

After running these commands one-at-a-time you can then put your wireless card into monitor mode using `airmon-ng start wlan0` assuming your wireless card's interface is `wlan0`. This will create an interface called `mon0` which you will give to Kismet. Note that installing these will be SLOW on the Pi. Have patience. 

You will also need to edit the Kismet configuration file. `sudo vi /etc/kismet/kismet.conf` and change the `source` line to `source=rt8180,wlan0,ALFA`. 

Finally you also will need to enable I2c. You can use [Adafruit's guide](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) to get that set up.

## Usage

This script should be run after starting Kismet. You provide it with the XML log file and it will parse it every 5 seconds. Since Kismet is run with `sudo` this needs to be run with `sudo` as well.

> sudo python pi_kismet.py -f /path/to/logfile.netxml

The logfile will most likely be in `/var/log/kismet`.

To stop the script hold the `SELECT` key on the LCD plate for 3 seconds and the script will stop parsing and displaying information. 

## Licensing

This project uses some code from Adafruit's [PiMiner](https://github.com/adafruit/PiMiner) and as such this project is licensed under GPLv3 like PiMiner. 
