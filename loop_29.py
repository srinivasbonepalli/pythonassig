no = int(input('enter a four digit number:'))
l = []
no_re = 0
no1 = no
for x in range(4):
    l.append(int(no1 % 10))
    no1 = (no1 - (no1 % 10))/10
l.reverse()
for y in range(4):
    no_re = no_re+(l[y]*(10**y))
print(no_re)

