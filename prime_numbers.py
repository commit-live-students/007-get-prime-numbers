n=20
def get_prime_numbers(n):
    l = []
    for i in range(2,n):
        p=0
        for j in range(2,i):
            if i % j == 0 :
                p = 1
        if p == 0 :
            l.append(i)


    return l


print get_prime_numbers(n)
