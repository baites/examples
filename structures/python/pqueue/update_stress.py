
from pqueue import PQueue
import random
import sys
import uuid

Q = PQueue()

while 1:
    inputs = []
    for i in range(10):
        key = random.randint(1,1000)
        inputs.append(key)
        Q.push(key, str(uuid.uuid4()))

    test = Q._heap[random.randint(0,len(Q._heap)-1)]
    Q.push(0, test.value)

    key, value = Q.pop()
    if test.value != value:
        print('Error')
        print(inputs)
        print(test.value)
        sys.exit(1)

    print('OK')
