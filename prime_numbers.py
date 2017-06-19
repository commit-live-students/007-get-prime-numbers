from array import array
l = []

def get_prime_numbers(n):
    if n <= 1:
        print "Number should be greater then 1"

    for x in range(2,n):
        prime = True
        for num in range(2,x):
            if(x%num == 0):
                prime = False
        if prime:
            l.append(x)
    arr = l
    return arr

print get_prime_numbers(20)
