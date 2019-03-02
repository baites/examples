
def unique_char(string):
    char_bits = 0
    for c in string:
        index = ord(c)
        if (char_bits >> index) & 1:
            return False
        char_bits = char_bits | 1 << index
    return True

print(unique_char('hola'))
print(unique_char('hola como va'))

