rested
======

OS X Install*
============
Installing QT and PyQT is a pain on OS X. I am not an expert in either
one. The correct steps are left as an exercise to the reader.
       *DO NOT CONTACT ME ABOUT PROBLEMS INSTALLING QT/PYQT.*

Requirements:
1. Qt 4 and PyQt
```bash
# cmake is needed for PySide
brew install cmake pyqt
```
2. PySide
Download and run the binary installer from [PySide Binaries for Mac OS X](http://qt-project.org/wiki/PySide_Binaries_MacOSX).
The one labelled [PySide 1.1.0 for Python 2.7](http://pyside.markus-ullmann.de/pyside-1.1.0-qt47-py27apple.pkg) worked well for me
on OS X 10.8 with Python 2.7.
3. Rested code + libs
The PyQt and PySide libraries will be installed in the global python context
and will not be present in a virtualenv unless you specifically ask them to
be.
```bash
# inherit the system python packages to get PyQt and PySide in the virtualenv
mkvirtualenv --system-site-packages rested

# grab the source and go into dir
git clone https://github.com/carschar/rested.git
cd rested

# install dependencies
pip install -r requirements.txt
```

Running It
==========
```python rested/app.py```
