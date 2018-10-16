
def unique_char(string):
    char_set = set()
    for c in string:
        if c in char_set:
            return False
        char_set.add(c)
    return True

print(unique_char('hola'))
print(unique_char('hola como va'))

