def summa(*args):
    print(args)

summa(1, 3, 5, 4, 7)

def brand(**kwargs):
    for x, y in kwargs.items():
        print(x, ': ', y)

brand(a='APPLE', s='Samsung')