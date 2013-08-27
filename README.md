rested
======
Rested is a reStructuredText editor written in Python with the QT framework. It is sole copyright of [Enthought](https://enthought.com/). 

Resources:
* Blog post about features added in 2010: [A Renewed ReStructuredText Editor!](http://blog.enthought.com/enthought-tool-suite/a-renewed-restructured-text-editor/)
* Original code resides in [enthought/rested](https://github.com/enthought/rested) repository.

# Debian/Ubuntu Install
Instructions from [Issue 5 in enthought repo](https://github.com/enthought/rested/issues/5)
```bash
sudo apt-get install build-essential python-pip python-dev
sudo pip install numpy configobj pygments docutils sphinx rst2pdf

# grab the source
git clone https://github.com/enthought/rested
cd rested

sudo python setup.py install
```


#OS X Install*

Installing QT and PyQT is a pain on OS X. I am not an expert in either
one. The correct steps are left as an exercise to the reader.
       *DO NOT CONTACT ME ABOUT PROBLEMS INSTALLING QT/PYQT.*

##Requirements:
1. Qt 4 and PyQt

```brew install cmake pyqt```

2. PySide

Download and run the binary installer from [PySide Binaries for Mac OS X](http://qt-project.org/wiki/PySide_Binaries_MacOSX).
The one labelled [PySide 1.1.0 for Python 2.7](http://pyside.markus-ullmann.de/pyside-1.1.0-qt47-py27apple.pkg) worked well for me
on OS X 10.8 with Python 2.7.

3. Rested code + libs

The PyQt and PySide libraries will be installed in the global python context
and will not be present in a virtualenv unless you specifically ask them to
be. 

```bash
# grab the source
git clone https://github.com/carschar/rested.git
cd rested

python setup.py install
```


# Running It (applies to Linux/OS X)
Create a small helper script to execute the app:
```
#!/bin/bash
# Run Enthought's rested ReStructuredText editor.
python -c "from rested import app; app.main()" "$@" 2&>1 &
```

Or you can run it directly from the git repo:
```python rested/app.py```
