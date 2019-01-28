#! /usr/bin/env python

class Vault:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


vault = Vault([c for c in 'Mutable'])
print(vault.value)
value = vault.value
value += [' ', 'n', 'o', '?']
print(vault.value)
