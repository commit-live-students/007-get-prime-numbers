import math


def is_prime(n):
    n_sqrt = int(math.sqrt(n)) + 1
    prime_factors = filter(lambda i: n % i == 0, range(2, n_sqrt))
    return False if prime_factors else True


def get_prime_numbers(n):
    return filter(is_prime, range(2, n + 1))


print get_prime_numbers(50)
