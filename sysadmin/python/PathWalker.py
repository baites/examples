#! /usr/bin/env python

import os
from os.path import join, getsize
for root, dirs, files in os.walk('./'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
