def get_prime_numbers(n):
    array=[]
    if n<=1:
        print "The number is less than one"
    else:
        if n > 1:
            for i in range(2,n):
                for j in range(2,i):
                    if (i%j==0):
                        break
                else:
                    array.append(i)

    return array
