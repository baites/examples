#! /usr/bin/env python

import random
import sys

def ToStr(text, func=str):
    return ''.join(map(func, text))

alphabet = [chr(inx) for inx in range(ord('A'),ord('Z')+1)]
alphabet.append(' ')
alphamap = { alphabet[inx]:inx for inx in range(len(alphabet)) }

plaintext = ' '.join(sys.argv[1:]).upper()

key = [random.randint(0,4) for inx in range(len(plaintext))]

ciphertext = []
for inx in range(len(plaintext)):
    ninx = (alphamap[plaintext[inx]] + key[inx]) % len(alphabet)
    ciphertext.append(alphabet[ninx])

print('Key: {}'.format(ToStr(key,
    lambda inx: str(alphabet[inx])
)))

print('Ciphertext: {}'.format(ToStr(ciphertext)))
