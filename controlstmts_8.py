a = int(input('enter a no:'))
b = int(input('enter a no:'))


def makes10(d, c):
    if d == 10 or c == 10 or c+d == 10:
        e = True
    else:
        e = False
    return e


print('none of them make 10 ', makes10(a, b))
