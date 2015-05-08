Simple image editor.
Right now only B&W and sepia filters implemented.

The editor also allows editing and reloading the filter code (i.e. the actual pixel manipulation code) without restarting the application. 

---------------------------------------------------

This code has been tested on Mac OS 10.10 and Raspbian 3.18.

---------------------------------------------------

Prerequisites: wxPython

On Mac OS, download wxPython3.0-osx-cocoa-py2.7 from http://www.wxpython.org/download.php and install it. 
Note: wxPython cannot be installed in virtualenv.

On Raspbian,  install wxPython using:
sudo apt-get install python-wxgtk2.8

---------------------------------------------------

To start the application:
python runapp.py