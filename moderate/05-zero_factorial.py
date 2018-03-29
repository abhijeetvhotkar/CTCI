def zeroFact(n):
    zeroCount = 0
    fivePow = 5
    while fivePow <= n:
        zeroCount += n//fivePow
        fivePow *= 5
    return print(zeroCount)

zeroFact(10)
