a = int(input('enter a no:'))
b = int(input('enter a no:'))
c = input('enter "True" or "False":')


def pos_neg(d, e, f):
    if d < 0 or e < 0:
        return True
    elif d < 0 and e < 0 and f == True:
        return True
    else:
        return False


if c == 'True':
    c = True
    print(pos_neg(a, b, c))
elif c == 'False':
        c = False
        print(pos_neg(a, b, c))
else:
    print('invalid input')






