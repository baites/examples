def reverse_bytearray(a):
    tmp = ''
    size = len(a) - 1
    for i in range(size//2):
        tmp = a[i]
        a[i] = a[size-1-i]
        a[size-1-i] = tmp

a = bytearray(b'hola\n')

reverse_bytearray(a)

print(a)
