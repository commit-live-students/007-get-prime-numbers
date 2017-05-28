def get_prime_numbers(n):
    a = []
    for i in range(2,n):
        flag = 0
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            a.append(i)
    return a
