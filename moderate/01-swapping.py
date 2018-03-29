def swapping(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return print("{} {}".format(a, b))

swapping(2, 3)
