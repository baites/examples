#! /usr/bin/env python

import bisect
from pprint import pprint
from datetime import datetime

records = []

def ParseLine(line):
    """Parse one access line."""
    fields = line.split()
    ip = fields[0]
    datestr = ' '.join(fields[3:5])[1:-1]
    timestamp = datetime.strptime(
        datestr, '%d/%b/%Y:%H:%M:%S %z'
    ).timestamp()
    command = fields[5][1:]
    uri = fields[6]
    protocol = fields[7][:-1]
    status = int(fields[8])
    size = int(fields[9])
    meta = [var.strip('"') for var in fields[11:-1]]
    return {
        'timestamp': timestamp,
        'ip': ip,
        'command': command,
        'uri': uri,
        'protocol': protocol,
        'status': status,
        'size': size,
        'meta': meta
    }

with open('api-access.log') as handler:
    line = handler.readline()
    while line:
        record = ParseLine(line)
        records.append(record)
        line = handler.readline()

records.sort(key = lambda x: x['timestamp'])
timestamps = [record['timestamp'] for record in records]

start = bisect.bisect_left(timestamps, 1498068495)
end = bisect.bisect_left(timestamps, 1498068496)
pprint(records[start:end])
