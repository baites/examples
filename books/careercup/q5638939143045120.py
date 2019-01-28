
def coins(coinset, maxvalue):
    sum = {0}
    for value in range(1, maxvalue):
        for coin in coinset:
            if (value - coin) in sum:
                print(value)
                sum.add(value)
                break

coinset = {10, 15, 55}
maxvalue = 1000

coins(coinset, maxvalue)
