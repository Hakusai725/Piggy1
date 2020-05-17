def fx1(L):
    s = ''
    for i in L:
        s += i + '\n'
    f1 = open('test1.txt', 'w')
    f1.write(s[:-1])
    f1.close()
#    return f1


if __name__ == '__main__':
    l = 'HengJiHengJi'
    fx1(l)
