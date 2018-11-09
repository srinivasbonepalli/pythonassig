l = []
for x in range(10):
    l.append(int(input('enter a no:')))
not_prime = 0
prime = 0
for y in range(10):
    if l[y] > 1:
        for i in range(2, l[y]):
            if (l[y] % i) == 0:
                not_prime += 1
                break
        else:
            prime +=1
    else:
        print(l[y],'is niether prime nor composite')

print("no of prime's are", prime, "no of not prime's are", not_prime)
