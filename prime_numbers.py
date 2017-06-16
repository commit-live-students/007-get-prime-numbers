def isprime(num):
    flag = True
    for i in range(2,num/2+1):
        if(num%i==0):
            flag=False
            break
    return flag
def get_prime_numbers(number):
    ans=[]
    for i in range(2,number):
        if(isprime(i)):
            ans.append(i)
    return ans
print(get_prime_numbers(20))
