def get_prime_numbers(n):
    prime=[]
    for num in range(1,n + 1):
   # prime numbers are greater than 1
     if (num > 1):
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           prime.append(num)
    return prime
print get_prime_numbers(20)
