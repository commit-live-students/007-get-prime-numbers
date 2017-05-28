def is_Prime(n):
    for i in range(2, n+1):
        if n%i==0:
          return i
    return dict


def get_prime_numbers(n):
   dect = []
   for i in range(2,n+1):
      #print is_Prime(i)
      if is_Prime(i)==i:
         #print i," is prime"
         dect.append(i)
   return dect


print get_prime_numbers(100)
#print is_Prime(11)
