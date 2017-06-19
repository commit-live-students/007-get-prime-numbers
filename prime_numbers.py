from math import sqrt


def get_prime_numbers(n):
    result = range(2, n+1)
    num = 2
    j = 1
    while num <= int(sqrt(n)+1) and j < len(result):
        result = [i for i in result if i%num != 0 or i == num]
        num = result[j]
        j += 1
    return result
get_prime_numbers(20)
