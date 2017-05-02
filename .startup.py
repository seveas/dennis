from __future__ import division, print_function, unicode_literals, absolute_import
import atexit
import readline
import datetime, os, sys, re, time, socket
from pprint import pprint
try:
    from whelk import shell
except ImportError:
    pass

sys.displayhook = pprint

histfile = os.path.join(os.environ["HOME"], ".python_history")
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)
del histfile, atexit, readline
