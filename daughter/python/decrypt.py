#! /usr/bin/env python

import random
import sys

def tostr(plaintext):
    return ''.join(map(str, plaintext))

alphabet = [chr(inx) for inx in range(ord('A'),ord('Z')+1)]
alphabet.append(' ')
alphabet.append('.')
alphamap = { alphabet[inx]:inx for inx in range(len(alphabet)) }

key = sys.argv[1]
key = [alphamap[value] for value in key]
ciphertext = ' '.join(sys.argv[2:]).upper()

if len(ciphertext) != len(key):
    print("Error ciphertext and key length do not match")

plaintext = []
for inx in range(len(ciphertext)):
    ninx = (alphamap[ciphertext[inx]] - key[inx]) % len(alphabet)
    plaintext.append(alphabet[ninx])
print('Plaintext: {}'.format(tostr(plaintext)))
