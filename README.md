KismetPiDisplay
=============

These scripts display information from a Kismet XML log file during a wardrive on the Adafruit LCD for the Raspberry Pi. The more mobile your wardriving setup the better, so why not use a Pi? Carrying around a monitor with your Pi is not ideal so we can use an LCD to display information about gathered networks during the wardrive.

The script will start by displaying the total number of networks discovered thus far. By pressing the `UP` or `DOWN` buttons you can cycle between the other screens. The `LEFT` and `RIGHT` buttons scroll the text on the screen left or right. The other information that is displayed is the total number of networks using `WPA`, `WEP`, or no encryption. 

## Installation

This code requires that Adafruit's [Raspberry Pi Python Code](https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code) be installed in your home directory on the Raspberry Pi. It also requires you have Paul McMillan's [kismetclient](https://github.com/PaulMcMillan/kismetclient) installed in your home directory. Note that the script assumes your username is `pi`. If your username isn't `pi` go into `pi_kismet.py` and on lines 2 and 3 change the `pi` in the strings to your username.

You will also need the development version of Kismet. 

Complete steps for setting up your RPi follow. 

### Complete Guide

For those who are new to this, here is how to set everything up on your Pi. This requires a wireless card that supports monitor mode. I use the Alfa `AWUS036H`. This also assumes you are using `Raspbian` as your OS. 

Use the following commands to install the dependencies. 

```
sudo apt-get update
sudo apt-get -y install iw kismet python-dev python-smbus python-rpi.gpio libssl-dev libpcap-dev libnl-dev
```

Next you will need to enable I2c. You can use [Adafruit's guide](http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c) to get that set up. Follow it exactly please.

Next you will need to install the libraries the code depends on. Run the following commands. 

```
cd
git clone https://www.kismetwireless.net/kismet.git
git clone https://github.com/PaulMcMillan/kismetclient.git
git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
cd kismet
./configure
make && sudo make install
```

Please note that compiling and installing Kismet takes a long time. Have patience. 

You will now need to edit the Kismet configuration file. `sudo vi /usr/local/etc/kismet.conf` and add in the line `ncsource=wlan0:name=RTL8187`. You will see a section of lines that say `ncsource` near the beginning of the config file. 

## Usage

This script should be run after starting Kismet. It should be run with `sudo` so you can access the smbus. 

You will need two terminals for this so everything can run. 

```
sudo apt-get install tmux
tmux
sudo kismet_server
Ctrl-B c
cd KismetPiDisplay
sudo python pi_kismet.py
```

To stop the script hold the `SELECT` key on the LCD plate for 3 seconds and the script will stop displaying information. 

If you want to use GPS with Kismet then you can fire up `gpsd` BEFORE you run `kismet_server`. There are plenty of tutorials on that you can find on Google.

### Possible errors

Sometimes when you run kismet it will give a bunch of errors about your wireless card and how it can't set to a different channel. You will notice this in the output in the console window your kismet_server is runnning in (press `Ctrl-B 0` to go back to it if you followed this guide). To fix this open a new tmux window (`Ctrl-B c`) and run `ps aux | grep wpa` and `ps aux | grep ifplugd`. Any of the processes that show up that are associated with your wireless interface `wlan0` need to be killed. To kill them run `sudo kill -9` followed by the process number.

## Licensing

This project uses some code from Adafruit's [PiMiner](https://github.com/adafruit/PiMiner) and as such this project is licensed under GPLv3 like PiMiner. 
