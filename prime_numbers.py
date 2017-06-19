def get_prime_numbers(n):
    isPrime=[[True]] * (n+1)
    isPrime[0]=isPrime[1]=0
    ret=[]
    for i in range(2,n+1):
        if(isPrime[i]):
            ret.append(i)
            for j in range(i*2,n+1,i):
                isPrime[j]=False
    return ret

print(get_prime_numbers(11))

#implemented using sieve of Eratosthenes
