#! /usr/bin/env python

class Vault:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

vault = Vault('Inmutable')
print(vault.value)
value = vault.value
value += ' not so much!'
print(vault.value)
