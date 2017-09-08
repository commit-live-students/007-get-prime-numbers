import math
def get_prime_numbers (n):
    if n <= 1:
        print "Give a number greater than one"
        return []
    else:
        primes = []
        nums = range (2,n+1)
        while nums:
            prime = nums[0]
            primes.append (prime)
            nums2 = nums[:]
            for x in nums2:
                if x % prime == 0:
                    nums.remove(x)
        return primes

if __name__ == "__main__":
    print get_prime_numbers (1)
    print get_prime_numbers (2)
    print get_prime_numbers (3)
    print get_prime_numbers (4)
    print get_prime_numbers (10)
    print get_prime_numbers (100)
