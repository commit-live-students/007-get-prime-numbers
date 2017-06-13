lis = []

def get_prime_numbers(num):
  for n in range(2,num):
   if n > 1:
       for i in range(2,n):
           if (n % i == 0):
               break
       else:
           lis.append(n)
  return lis


get_prime_numbers(20)
print lis
