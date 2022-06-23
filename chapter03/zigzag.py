#!/usr/bin/env python

import time, sys

indent = 0
indentIncreasing = True
try:
    while True:
        print(' '*indent, '********', sep='')
        time.sleep(0.01)

        if indentIncreasing:
            indent += 1
        else:
            indent -= 1

        match indent:
            case 20:
                indentIncreasing = False
            case 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

