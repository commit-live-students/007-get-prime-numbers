def get_prime_numbers(n):
    isPrime=[[True]] * n
    isPrime[0]=isPrime[1]=0
    ret=[]
    for i in range(2,n):
        if(isPrime[i]):
            ret.append(i)
            for j in range(i*2,n,i):
                isPrime[j]=False
    return ret

print(get_prime_numbers(10000))

#implemented using sieve of Eratosthenes
