#! /usr/bin/env python

import json
import urllib.request
from pprint import pprint

with urllib.request.urlopen(
    'http://bseanalytics/collectordb/TestNodeStats'
) as response:
    pprint(json.load(response))
