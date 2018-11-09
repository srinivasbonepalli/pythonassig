l = []
for x in range(10):
    l.append(int(input('enter a no:')))
pos = 0
neg = 0

for y in range(10):
    if l[y] > 0:
        pos += 1
    else:
        neg += 1

print("in the entered no's", "\nno of negative's are", neg, "\nno of positive are", pos)