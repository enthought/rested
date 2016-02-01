#!/usr/bin/env python
#
# Copyright by Enthought, Inc.
# All rights reserved.

from os.path import join

from setuptools import setup, find_packages


info = {}
exec (compile(open(join('rested', '__init__.py')).read(),
              join('rested', '__init__.py'), 'exec'), info)


setup(
    name = 'rested',
    version = info['__version__'],
    author = 'Enthought, Inc.',
    author_email = 'info@enthought.com',
    classifiers = [c.strip() for c in """\
        Development Status :: 5 - Production/Stable
        Intended Audience :: Developers
        Intended Audience :: Science/Research
        License :: OSI Approved :: BSD License
        Operating System :: MacOS
        Operating System :: Microsoft :: Windows
        Operating System :: OS Independent
        Operating System :: POSIX
        Operating System :: Unix
        Programming Language :: Python
        Topic :: Scientific/Engineering
        Topic :: Software Development
        Topic :: Software Development :: Libraries
        """.splitlines() if len(c.strip()) > 0],
    description = 'rested: ReST Editor',
    entry_points = {
        'gui_scripts': [
            'rested = rested.app:main',
            ],
        },
    install_requires = info['__requires__'],
    license = 'BSD',
    #long_description = open('README.rst').read(),
    maintainer = 'ETS Developers',
    maintainer_email = 'enthought-dev@enthought.com',
    package_data = dict(rested=['images/*', 'sphinx_default/*']),
    packages = find_packages(),
    platforms = ["Windows", "Linux", "Mac OS-X", "Unix", "Solaris"],
    zip_safe = False,
)
