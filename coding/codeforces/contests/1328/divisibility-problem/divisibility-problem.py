import sys

def main():
    next(sys.stdin)
    for line in sys.stdin:
        a, b = tuple(map(lambda x: int(x), line.split()))
        if a % b == 0:
            print(0)
        else:
            m = a//b
            print((m+1)*b-a)
            
main()
