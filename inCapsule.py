def massage(x):
    def print_massage(y):
        return x, y

    return print_massage

d = massage(4)
print(d(5))
print(d(9))