
s = 'abcd'

def get_perms(index=0):
    if index == len(s):
        return ['']
    char = s[index]
    subperms = get_perms(index+1)
    newperms = []
    for perm in subperms:
        size = len(perm) + 1
        for i in range(size):
            newperms.append(
                perm[:i] + char + perm[i:]
            )
    return newperms

print(get_perms())
