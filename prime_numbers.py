from math import sqrt


def get_prime_numbers(n):
    return [2] if n == 2 else [x for x in range(2, n + 1) if all([x % y for y in range(2, int(sqrt(x) + 1))])]


print get_prime_numbers(50)
