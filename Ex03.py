m = ''
for n in range(10):
    m += ' '
print(m + '*')

l = ' '
for n in range(9):
    m = ''
    for k in range(9-n):
        m += ' '
    print(m + '*' + l + '*')
    l += '  '

m = '*'
for n in range(10):
    m += ' *'
print(m)


# Solution 2
a = '*'
for i in range(10):
    b = ''
    for j in range(9-i):
        b += ' '
    print(b + a)
    a += '**'
