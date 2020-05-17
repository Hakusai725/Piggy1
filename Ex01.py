L = ['Bart', 'Lisa', 'Adam']

# Solution 1
n = 0
while n < 3:
    print('Hello, %s!' % L[n])
    n = n + 1

print('''\n''')

# Solution 2
for name in L:
    print('Hello, ' + name + '!')
