
import sys


def compose_solution(n, x):
    flag = False
    a_string = ''
    b_string = ''
    for c in x:
        if not flag and c == '2':
            a_digit = 1
            b_digit = 1
        elif not flag and c == '1':
            a_digit = 1
            b_digit = 0
            flag = True
        else:
            a_digit = 0
            b_digit = int(c)
        a_string += str(a_digit)
        b_string += str(b_digit)
    return a_string, b_string

def main():

    next(sys.stdin)
    for line in sys.stdin:
        n = int(line)
        x = next(sys.stdin).strip()
        a_string, b_string = compose_solution(n, x)
        print(a_string)
        print(b_string)
main()
