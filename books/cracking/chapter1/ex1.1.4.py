
def unique_char(string):
    sorted_string = sorted(list(string))
    oldc = None
    for c in sorted_string:
        if not oldc:
            oldc = c
            continue
        if c == oldc:
            return False
        oldc = c
    return True

print(unique_char('hola'))
print(unique_char('hola como va'))

