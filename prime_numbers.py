def get_prime_numbers(n):
    prime_numbers = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    return(prime_numbers)





print get_prime_numbers(100)
