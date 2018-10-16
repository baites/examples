
def unique_char(string):
    char_set = [False]*256
    for c in string:
        index = ord(c)
        if char_set[index]:
            return False
        char_set[index] = True
    return True

print(unique_char('hola'))
print(unique_char('hola como va'))

