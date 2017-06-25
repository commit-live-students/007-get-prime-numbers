def get_prime_numbers(n):
    prime=[]
    if n > 1:
        for i in range(2,n):
            for j in range(2,i):
                if (i%j==0):
                        break
            else:
                prime.append(i)
    else:
        if n<=1:
            print "Number is less than one"

    return prime

# get_prime_numbers(20)
# Output : [2, 3, 5, 7, 11, 13, 17, 19]
