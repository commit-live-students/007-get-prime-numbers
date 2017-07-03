
def get_prime_numbers(num):
    if num <= 1:
        return
    primes = []
    for x in range(2, num+1):
        # if x is divisible by any of primes found till now, then it is not prime
        isPrime = True
        for prime in primes:
            if x%prime == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(x)
    return primes
