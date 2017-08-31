#! /usr/bin/env python

import json
import urllib.request
from pprint import pprint

with urllib.request.urlopen(
    'http://google.com'
) as response:
    pprint(response.read())
