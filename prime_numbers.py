#Sieve of Eratosthenes
from math import sqrt


def get_prime_numbers(n):
    allnums = range(2, n+1)
    num = 2
    j = 1
    while num <= int(sqrt(n)+1) and j < len(allnums):
        allnums = [i for i in allnums if i%num != 0 or i == num]
        num = allnums[j]
        j += 1
    return allnums
