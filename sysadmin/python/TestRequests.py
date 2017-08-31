#! /usr/bin/env python

import requests
from pprint import pprint

r = requests.get('http://bseanalytics/collectordb/TestNodeStats')
r.raise_for_status()
pprint(r.json())
