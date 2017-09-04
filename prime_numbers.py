def get_prime_numbers(n):
    p=[]
    for num in range(2,n):
        prime = True
        for i in range(2,num):
            if(num%i == 0):
                prime = False
        if prime:
                p.append(num)
    return p

print get_prime_numbers(27)
