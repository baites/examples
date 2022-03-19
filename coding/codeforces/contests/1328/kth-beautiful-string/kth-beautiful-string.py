import sys

# The solution is based on mapping different
# string combinations as indices of a off-diagonal
# lower triangular part of a matrix.
#           j
#       1  2  3  4  5
#   1 | x
#   2 | 1  x
# i 3 | 2  3  x
#   4 | 4  5  6  x
#   5 | 7  8  9 10  x
#
# So for example the 8th string of size 5 is located
# in i=5, j=2, so the string is
# baaba
# ^  ^j=2
# i=5


def search_indexes(n, k):
    min_index = 2
    max_index = n+1

    while 1:
        index = (min_index + max_index) // 2
        temp = (index-1)*(index-2)//2
        a = temp + 1
        b = temp + index - 1
        if k < a:
            max_index = index
        elif k > b:
            min_index = index
        else:
            break

    return index, k-a + 1


def print_string(n, i, j):
    string = ''
    for index in range(n):
        if n-index in (i, j):
            string += 'b'
        else:
            string += 'a'
    print(string)


def main():

    next(sys.stdin)
    for line in sys.stdin:
        n, k = tuple(map(lambda x: int(x), line.split()))
        i, j = search_indexes(n, k)
        print_string(n, i, j)

main()
