a = int(input("enter a no:"))


def diff21(c):
    if c < 21:
        s=21-c
        print (s, 'is the absolute difference')
    else:
        s=2*(c-21)
        print (s, 'is the difference')


diff21(a)
