from copy import deepcopy

def recursion(s,l,c=[]):
    if len(s) == 0:
        if len(c) == 4:
            l.append(c)
            return True
        return False
    for n in range(1,4):
        p = deepcopy(c)
        v = s[0:n]
        if (v.startswith('0') and len(v) > 1) or int(v) > 255:
            continue
        p.append(v)
        if recursion(s[n:], l, p):
            break

def initiator(s):
    l = []
    recursion(s,l)
    return ['.'.join(p) for p in l]

ip = "255255255255"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "25525511255"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "25551125"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "2552"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "0255255255"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "0000"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "001100"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "001900"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "001994482909400"
print('{} -> {}'.format(ip, initiator(ip)))
ip = "011"
print('{} -> {}'.format(ip, initiator(ip)))
