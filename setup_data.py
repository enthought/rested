# Function to convert simple ETS project names and versions to a requirements
# spec that works for both development builds and stable builds.  Allows
# a caller to specify a max version, which is intended to work along with
# Enthought's standard versioning scheme -- see the following write up:
#    https://svn.enthought.com/enthought/wiki/EnthoughtVersionNumbers
def etsdep(p, min, max=None, literal=False):
    require = '%s >=%s.dev' % (p, min)
    if max is not None:
        if literal is False:
            require = '%s, <%s.a' % (require, max)
        else:
            require = '%s, <%s' % (require, max)
    return require


# Declare our ETS project dependencies. Versions BEFORE the namespace refactor.
ENTHOUGHTBASE = etsdep('EnthoughtBase', '3.0.5')
TRAITSBACKENDQT = etsdep('TraitsBackendQt', '3.4.0')
TRAITSGUI = etsdep('TraitsGUI', '3.4.0')
TRAITS_UI3 = etsdep('Traits[ui]', '3.4.0')

# Version after the refactor
# FIXME: What else is left to add?
TRAITS_UI4 = etsdep('traitsui', '4.0')


# A dictionary of the setup data information. 
INFO = {
    'extras_require' : {
        },
    # This is the list with packages BEFORE the ETS4 namespace refactor
    'install_requires3' : [
        ENTHOUGHTBASE,
        TRAITSBACKENDQT,
        TRAITSGUI,
        TRAITS_UI3,
        ],
    # This is the list with packages AFTER the ETS4 namespace refactor.
    # FIXME: What else is left to add?
    'install_requires4' : [
        TRAITS_UI4,
        ],
    'name': 'Rested',
    'version': '1.0.0',
    }

# Add multiprocessing (only used by enthought.rst) as an extra if Python
# version is less than 2.6.
import sys
if sys.hexversion < 0x020600F0:
    INFO['extras_require']['nonets'].append('multiprocessing')
