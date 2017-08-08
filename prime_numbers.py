import math


def get_prime_numbers(n):
    primes = range(2, n + 1)
    for i in range(2, n + 1):
        i_sqrt = int(math.sqrt(i)) + 1
        for j in range(2, i_sqrt):
            if i % j == 0:
                primes.remove(i)
                break

    return primes
