# -----------------------------------------------------------------------------
#
#  Copyright (c) 2009, Enthought, Inc.
#  All rights reserved.
#
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#
#  Author: Evan Patterson
#  Date:   06/19/2009
#
# -----------------------------------------------------------------------------

# Standard library imports
from optparse import OptionParser
import os


def main():
    # Do relative imports here to benefit from __package__ if set below
    from .rest_editor_view import ReSTHTMLEditorView

    app = ReSTHTMLEditorView()

    usage = 'usage: rsted [options] file ...'
    parser = OptionParser(usage=usage)
    options, args = parser.parse_args()
    for path in args:
        if os.path.isdir(path):
            app.selected_file = path
        elif os.path.isfile(path):
            app.open(path)
        else:
            if not os.path.splitext(path)[1]:
                path += '.rst'
            app.new(path)

    app.configure_traits()


if __name__ == '__main__':
    if __package__ is None:
        __package__ = "rested.app"
    main()
