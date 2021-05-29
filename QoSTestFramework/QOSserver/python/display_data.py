# Copyright (C) <2019> Intel Corporation
#
#SPDX-License-Identifier: Apache-2.0



import os
from itertools import islice
import sys
import getopt
import time
import subprocess
import re
import os
import os.path
'''
this python scripts is used for load existing result and show the final result in html page 
'''
try:
    opts, args = getopt.getopt(sys.argv[1:], "h:c:if:", ["help", "folder=", "file=", "install"])
except getopt.GetoptError:
    print('error : run.py -c <folder> -f <file>')
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print('display_data.py -c <folder> -f <file> \n')
    elif opt == '-c':
        folder = arg
    elif opt == '-f':
        file = arg
    else:
        assert False, "unhandled option"

compareFolder = folder.split(',')
lines = []
if len(compareFolder) > 1:
    for item in compareFolder:
        f = open(item+'/'+file)
        lines.extend(f.readlines())
        f.close
        lines.append('#')
    print(lines)
else:
    f = open(os.path.join(folder,file))
    lines = f.readlines()
    f.close()
    list_line = []
    print(lines)
