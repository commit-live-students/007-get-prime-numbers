#n = input("Enter a number: ")
n=10
array = []

def get_prime_numbers(n):
    for k in range(2,n+1):
        if all(k%i!=0 for i in range(2,k)):
            array.append(k)
    return array

if n>1:
    output=get_prime_numbers(n)
    print output
