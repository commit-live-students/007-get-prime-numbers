def checkprime(n):
    result = True
    if n == 2:
        return result
    else:
        for i in range(2, n):
            if n%i == 0:
                result = False
    return result


def get_prime_numbers(n):
    primecount = []
    for i in range(2,n+1):
        if checkprime(i) is True:
            primecount.append(i)
    return primecount
