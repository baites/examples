# python3


def Add(a, i, x):
    i -= 1
    a[i] += x
    while i < len(a)-1 and a[i] > a[i+1]:
        a[i+1] = a[i]
        i += 1

def GetSum(a, l, r):
    l -= 1
    return sum(a[l:r])

def main():

    n = int(input().strip())
    a = input().strip().split()
    a = [int(a[i]) for i in range(n)]
    #k = input().strip().split()
    #k = [int(k[i]) for i in range(n-1)]
    q = int(input().strip())

    for j in range(q):
        #print(j, a)
        line = input().split()
        if line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            #print('s {} {}'.format(l, r))
            print(GetSum(a, l, r))
        elif line[0] == '+':
            i = int(line[1])
            x = int(line[2])
            #print('+ {} {}'.format(i, x))
            Add(a, i, x)
        else:
            print('unknown ops')

    #print(j, a)

if __name__ == "__main__":
    main()
