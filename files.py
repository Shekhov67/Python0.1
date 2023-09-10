'''file = open('1.txt', 'w')
file.write('Hello my Bro!')
file.close()

file = open('1.txt', 'r')
print(file.read())
file.close()

with open('1.txt', 'a') as f:
    f.write('Sucker!')
print(f)'''

try:
    a = int(input('a: '))
    b = int(input('b: '))
    print(a/b)
except ZeroDivisionError:
    print('Divizion is ZERO!!!!WTF?Bro!')