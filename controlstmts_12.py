m1 = input('enter monkey_a is smiling "True" or "False":')
m2 = input('enter monkey_b is smiling "True" or "False":')

if m1 == 'True' or m1 == 'true':
    m1 = True
elif m1 == 'False' or m1 == 'false':
    m1 = False
else:
    print('invalid input')

if m2 == 'True' or m2 == 'true':
    m2 = True
elif m2 == 'False' or m2 == 'false':
    m2 = False
else:
    print('invalid input')


def monkey_trouble(a, b):

        if a == True and b == True:
                return True
        elif a == False and b == False:
                return True
        else:
                return False


print('we are having trouble:', monkey_trouble(m1, m2))



