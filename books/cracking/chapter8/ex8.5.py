
def print_par(count):

    result = [None]*(2*count)
    print(result)

    def print_par_itr(l, r, index):
        if l < 0 or r < 0:
            return
        if l == 0 and r == 0:
            print(''.join(result))
            return
        if l > 0:
            result[index] = '('
            print_par_itr(l-1, r, index+1)
        if r > l:
            result[index] = ')'
            print_par_itr(l, r-1, index+1)

    print_par_itr(count, count, 0)

print_par(5)
