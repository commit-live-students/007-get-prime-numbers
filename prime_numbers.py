def get_prime_numbers(n):
    l = []
    for i in range(2,n):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            l.append(i)
    return l
