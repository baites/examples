"""Implementing pqueue stress test"""

from pqueue import PQueue
import random
import sys
import uuid

Q = PQueue()

while 1:
    inputs = []
    for i in range(100):
        key = random.randint(0,1000)
        inputs.append(key)
        Q.push(key, str(uuid.uuid4()))
    keys = []
    while not Q.empty():
        key, value = Q.pop()
        keys.append(key)
    for i in range(1,len(keys)):
        if keys[i] < keys[i-1]:
            print('ERROR')
            print(inputs)
            print(keys)
            sys.exit(1)
    print('OK')
    print(keys)
