import math

def get_prime_numbers(n):
    ls = []
    is_prime = True
    for i in range(2,n):
        for j in range(2,i):
            if (i%j == 0 and i!=j):

                is_prime = False
        if(is_prime==True):
            ls.append(i)

        is_prime = True
    return ls

tmpl=[]
tmpl=get_prime_numbers(20)
print tmpl
