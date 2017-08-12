
def get_prime_numbers(n):
    l = []
    for i in range(2,n):
        prime = 0
        for j in range(2,i):
            if i % j == 0:
                prime = 1
        if prime == 0:
            l.append(i)
    return l

n = 20
print get_prime_numbers(n)

#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
