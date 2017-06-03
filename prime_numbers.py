def Prime(n):
    if n == 2 or n == 3:
        return True
    Prime = True
    x = 2
    while x <= n**0.5:
        if n%x == 0:
            Prime = False
        x += 1

    return Prime

def get_prime_numbers(n):
    if n < 1:
        return
    primes = []

    return [number for number in range(2,n+1) if Prime(number)]
