'''s = [x*2 for x in range(1, 10) if x % 3 == 0]
print(s)

s1 = [(i, j) for i in range(1, 21) for j in range(1, 51)]
print(s1)

s2 = [i**2 if i > 0 else i**3 for i in range(-10, 11) if i % 2 == 0]
print(s2)
 Сначала идет цикл перебираня(for i in range(-10, 11)), затем фильтр (if i % 2 == 0)
и только после идет условие (i**2 if i > 0 else i**3 ). 
Такой же принцип для генератора множеств(не хранит дубликат), кортежей, словарей'''

s3 = [2, 2, 8, 8, 10, 10]
s4 = {i for i in s3}
print(s4)
s5 = {i: i **10 for i in s3}
print(s5)