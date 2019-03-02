def remove_dups(a):
    l = 0
    r = 0
    charbits = 0
    while r < len(a):
        index = a[r] - 97
        if (charbits >> index) & 1:
            r += 1
            continue
        a[l] = a[r]
        r += 1
        l += 1
        charbits = charbits | 1 << index
    return a[:l]

a = bytearray(b'ooooollaasss')

print(remove_dups(a))
