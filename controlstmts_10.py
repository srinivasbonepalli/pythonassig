a = int(input('enter the hour (0-23):'))
b = input('enter if parrot is talking "True" or "False":')

if b == 'True' or b=='true':
    b = True
elif b == 'False' or b=='false':
        b = False
else:
    print('invalid input')

print(b)

if 0 <= a <= 23 and b == True or b == False:
    def parrot_trouble(c,d):
        if d == True:
            if 7 <= c <= 20:
                return False
            else:
                return True
        else:
            return False
    print('getting trouble is ',parrot_trouble(a, b))
else:
    print('invalid input')

