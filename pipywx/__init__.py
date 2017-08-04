"""
pipywx: Some random tools for wx in py on pi
============================================
"""

from __future__ import print_function

# Detect if we're being called as part of Py-ART's setup procedure
try:
    __pipywx_SETUP__
except NameError:
    __pipywx_SETUP__ = False

if __pypiwx_SETUP__:
    import sys as _sys
    _sys.stderr.write("Running from pipwx source directory.\n")
    del _sys
else:
    from . import sensors
