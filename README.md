# EMS Flasher GUI for OSX

Just a GUI for OSX made in Python 2.7 for the [ems-flasher CLI application](https://github.com/mikeryan/ems-flasher).

### Dependencies
First of all, an EMS 64M USB Cart and a USB cable are required (duh).<br />
You can't believe it but the cart needs to be connected to the computer via USB cable.<br />
A compiled version of [ems-flasher](https://github.com/mikeryan/ems-flasher) is required in order for the GUI to make the necessary read/write functions to the cart.

It also uses the Python package installed with Xcode.<br />
So, before running all the packages installations, you need to have Xcode and the CLI Tools installed.

This code uses wxPython to display the windows and the dialogs in this app.<br>
It uses py2app to create the application on OSX.

To make ems-flasher works, you need to have [libusb installed](http://libusb.info/).<br>
You can install it via [Homebrew](http://brew.sh/):
```bash
brew install libusb
```
For a precompiled libusb package, [you can get it there](http://www.ellert.se/twain-sane/).

### Download
If you just want to get the app, [Download it here](http://labs.biggiogero.net/ems/ems-flasher-gui.zip).<br>
It has also a compiled ems-flasher included.

### Installation & Build
- With Homewbrew installed, write this in Terminal:<br />
 ```bash
 brew install wxpython
 ```
 
 It will install the wxWidgets libraries and wxPython.
- Install [py2app](https://pythonhosted.org/py2app/).
- Download the repository by launching the git command:<br />
 ```bash
 git clone git@github.com:zeroerrequattro/ems-flasher-gui.git
 ```
 
- In the ems-flasher-gui folder, run the installation script:<br />
 ```bash
 python setup.py py2app
 ```
 
 In the `dist` folder you'll find the app.

### Usage
Before using this GUI you need to load the EMS Flasher. Click on the "Load EMS" button and you're good to go:)<br />
Using this GUI is quite easy (well, the meaning of making a GUI is to make things easy).<br />
Just push the buttons to read/write ROMs and .sav files into the cart.<br />
You can also drag and drop the files to automatically set the .gb/.sav file in order to be written.

### Known Issues
- On El Capitan (OSX 10.11.2), When you launch the py2app command it gives `error: [Errno 1] Operation not permitted`. To resolve it, [follow these steps](http://stackoverflow.com/questions/33197412/py2app-operation-not-permitted).
- The packaged App is awfully heavy (~70Mb) for what it does.
 to make it work without py2app, just launch the main script with Python:<br />
 ```bash
 python ems-flasher-gui.py
 ```
 
- The Packaged app in the download URL doesn't work on OSX versions prior to 10.11, it puts an error.
- After pressing one of the button, the app seems to be stuck and not responding. Have patience, the software is working.
- This GUI is meant to save/write one ROM from/to bank.

### To Do
- Add multiple ROM writing on single bank.
- Add the errors that ems-flasher throws.

Maybe someday I'll get rid of ems-flasher too, having all included in a single software.

But not today.