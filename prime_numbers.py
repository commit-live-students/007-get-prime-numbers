import math
def is_prime(n):
  if n==1:
    return False
  val=math.floor(math.sqrt(n))
  for i in range(2,val+1):
    if n%i==0:
      return False
  
  return True


def get_prime_numbers(n):
  lst=[]
  for i in range(1,n+1):
    if is_prime(i):
      lst.append(i)
  return lst


# print(get_prime_numbers(10))
