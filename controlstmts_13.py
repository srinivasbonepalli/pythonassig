a = int(input('enter a number :'))
b = int(input('enter a number :'))


def sum_double(c, d):
    if c != d :
        return c+d
    else:
        return 2*(c+d)


print('sum is :', sum_double(a, b))