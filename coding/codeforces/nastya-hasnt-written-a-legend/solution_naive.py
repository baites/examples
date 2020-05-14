# python3


def Add(a, k, i, x):
    a[i] += x
    while i < len(a)-1 and a[i] + k[i] > a[i+1]:
        a[i+1] = a[i] + k[i]
        i += 1

def GetSum(a, l, r):
    return sum(a[l:r])

def main():

    n = int(input().strip())
    a = input().strip().split()
    a = [int(a[i]) for i in range(n)]
    k = input().strip().split()
    k = [int(k[i]) for i in range(n-1)]
    q = int(input().strip())

    for j in range(q):
        #print(a)
        line = input().split()
        if line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            #print('s {} {}'.format(l, r))
            print(GetSum(a, l-1, r))
        elif line[0] == '+':
            i = int(line[1])
            x = int(line[2])
            #print('+ {} {}'.format(i, x))
            Add(a, k, i-1, x)
        else:
            print('unknown ops')

    #print(a)

if __name__ == "__main__":
    main()
