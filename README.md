ems-flasher-gui for OSX
=====

This is just a GUI for OSX made in Python 2.7 for the [ems-flasher CLI application](https://github.com/mikeryan/ems-flasher).
It uses wxPython to display the Graphical User Interface and subprocess to call ems-flasher from shell.

### Dependencies
First of all, an EMS 64M USB Cart and a USB cable are required (duh).
You can't believe it but the cart needs to be connected to the computer via USB cable.
A compiled version of [ems-flasher](https://github.com/mikeryan/ems-flasher) is required in order for the GUI to make the necessary read/write functions to the cart.

It also uses the Python package installed with Xcode.
So, before running all the packages installation, you need to have Xcode and the CLI Tools installed.

### Installation
- Install [Homebrew](http://brew.sh/) and write this in Terminal:

 ```bash
 brew install wxpython
 ```
 It will install the wxWidgets libraries and wxPython.
- Download the repository by launching the git command:

 ```bash
 git clone git@github.com:zeroerrequattro/ems-flasher-gui.git
 ```
- Move inside the GUI folder in the terminal

 ```bash
 cd ems-flasher-gui
 ```
- Move the compiled ems-flasher in the same folder of the GUI
- Launch the GUI by writing this:

 ```bash
 python ems-flasher-gui
 ```

### Usage
Using this GUI is quite easy (well, the meaning of making a GUI is to make things easy).
Just push the buttons to read/write ROMs and .sav files into the cart.

You can also drag and drop the files to automatically set the .gb/.sav file in order to be written.

### Known Issues
This GUI is meant to save/write one ROM from/to bank.
It seems the GUI doesn't show all the output ems-flasher throws.

### To Do
Priorities are:
- Making ems-flasher outputs visible on the GUI
- Add multiple ROM writing on single bank.

The main goal is to make this GUI a standalone app, without all the Xcode/Homebrew/python/wxPython installation crap.
Maybe someday I'll get rid of ems-flasher too, having all included in a single software.

But not today.