def are_anagrams(a, b):
    if len(a) != len(b):
        return false

    char_counter_a = {}
    char_counter_b = {}

    for c in a:
        char_counter_a[c] = char_counter_a.setdefault(c,0) + 1
    for c in b:
        char_counter_b[c] = char_counter_b.setdefault(c,0) + 1

    for c in char_counter_a:
        if c not in char_counter_a:
            return False
        if char_counter_a[c] != char_counter_b[c]:
            return False

    return True

a = 'hola'
b = 'aloh'

print(are_anagrams(a,b))
