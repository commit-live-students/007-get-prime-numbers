from math import *
from array import *
def get_prime_numbers(n):
    isPrime = True
    prime = array('i',[])
    if n>1:
        for i in range(2,n+1):
            isPrime = True
            for j in range(2,int(sqrt(n))+1):
                if i%j == 0 and i!=j :
                    isPrime = False
                    break
            if isPrime:
                prime.append(i)
    return prime
