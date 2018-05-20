der tog far Python
==================

der tog far Python is a Jewish Calendar program running under the
Python 3 interpreter.
It has a graphical user interface based on the Tkinter library.


Getting started
---------------

Before starting the program, make sure that the following
external Python Libraries required by der tog far Python
are installed:

  - Pmw Python megawidgets
  - Pillow

To check if they are installed, enter

  pip list

If a line containing the string "Pillow" or "Pmw" is displayed, the respective
library is already installed.
You can install them e.g. with the commands

  pip install Pillow
  pip install Pmw

der tog far Python can be started by entering

  python cal.pyw


Configuring the program
-----------------------

First, the configuration should be checked and adapted.
In the menu "Calendar", the following configuration can be changed:

  - "Preferences..."
      Setting Diaspora or Israel custom for readings/holidays,
      the time format (12 hour with AM/PM or 24 hour) and
      location for times calculation

  - "Candle Lighting/Havdalah..."
      Configuring calculation methods for candle lighting and
      havdalah for Shabbat

  - "DST Settings..."
      Configuring rule for considering Daylight Savings Time

  - "Zmanim..."
      Configuring calculation methods for Zmanim


Operating the program
---------------------

With the left and right arrow keys, the previous or next
month is viewed.

By clicking on a day, that day is selected for viewing its
Zmanim.


Adapting the displayed strings in the month calendar view
---------------------------------------------------------

The file customnames.py contains the names of the weekdays,
months, torah sections as well as a method for retrieving
the string for the omer count.
The file holidays.py contains the strings of the holidays.
These strings can be adapted by the user by editing them.

Hint: If saving the Python source file in the UTF-8 charset
and adding the line

# -*- coding: utf-8 -*-

at the top of the file, any letters in the Unicode charset
can be used, e.g. Hebrew.


Customizing the font sizes of the displayed strings in the
month calendar view
----------------------------------------------------------

The file customfonts.py contains the names and sizes of
the fonts for the various elements of the month calendar
view.
For changing the font size, you can either change the
value of the "size=" attribute or adjust the value in "addsize".
The value in "addsize" is added to the default values so
that all fonts are made larger in the same way automatically.
The if-statement distinguishes between Windows ("nt") or
Unix ("posix") systems.


Contact
-------

David and Ulrich Greve
E-Mail: ulrichgreve@tichnut.de
Website: http://www.tichnut.de/jewish


License agreement
-----------------

The delivered software is protected by copyright laws and is freeware.

The authors are not liable for consequential, incidential or
indirect damages of any kind which arise out of the use of
the software.
