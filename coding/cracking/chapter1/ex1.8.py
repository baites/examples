
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return
    length = len(s1)
    s = ''
    for j in range(length):
        for i in range(length):
            s = s + s1[(i+j)%length]
    return s2 in s

s1 = "erbottlewat"
s2 = "waterbottle"

print(is_rotation(s1, s2))
